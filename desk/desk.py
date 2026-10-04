#!/usr/bin/env python3
"""Capability Desk: deterministic core. Stdlib only. Code computes, the model narrates.

  route <task>            classify shelf, directive, stakes, novelty; emit a contract
  route-eval <tasks.json> route every task, lint each contract, compare to expected
  contract-lint <file>    validate a per-task contract
  contract-check [file]   run every Done-when check command; exit 0 only if all exit 0
  lint [--shelf S]        validate registry, skills, tools, gates (errors fail; warnings print)
  claims [--shelf S]      write artifacts/claims/<shelf>.json from the registry (what verifiers read)
  verdicts                per-shelf verified counts from the verdict files
  merge-registry          rebuild registry/shelves.json from registry/shelf/*.json
  merge-shelves           merge desk/<shelf>-rN worker branches after a path-scope check
  invent-check <file>     validate an invention result: 3 candidates, exactly 1 kill, real tools
  promote-gate <json>     promote only if held-out passes and cost or time drops
  verify-trace            verify the hash chain of trace/trace.jsonl
  tokens --main <jsonl> --workflow-dir <dir>   sum real usage from transcripts into artifacts/tokens.json
  seed-attempts --workflow-dir <dir>   checker runs per seed agent, from transcripts
  tokens-check <file>     validate artifacts/tokens.json
  report                  print the deterministic part of the final report
  report-check <plan.md>  require the report headings and a written body
"""
import argparse
import glob
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gate  # noqa: E402
import trace  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

SHELF_ORDER = [
    "software", "research", "scientific", "lab-protocols", "data", "markets", "legal",
    "design-systems", "motion-games-3d", "audio", "writing", "sales", "support", "recruiting",
    "education", "personal-admin", "computer-use", "strategy", "clinical-notes",
    "security-review", "harness", "reverse-engineering",
]
SEEDS = {
    "software": "verify", "research": "gap", "markets": "print", "reverse-engineering": "triage",
}
TOKEN_CAPS = {"L0": 0, "L1": 20000, "L2": 60000, "L3": 40000, "L4": 90000}
RUNGS = list(TOKEN_CAPS)
STAKES = ["low", "med", "high"]
CHECK_KINDS = ["exit-code", "quote", "schema", "state-diff", "signature", "count", "human-only"]
STATUSES = ["reliable", "assisted", "weak", "gated"]
SCOPES = ["read", "draft", "act", "none"]
SKILL_SECTIONS = ["Trigger", "Done-when", "Rung", "Forbidden move", "Tool"]
AND_OK = set()  # no directive may carry an 'and'; the owner's 'Book and pay' is split into book + pay
CONTRACT_KEYS = ["task", "shelf", "directive", "stakes", "novelty", "check", "gate", "rung",
                 "token cap", "verifier", "skill", "files", "status"]


# ---------------------------------------------------------------- loading
def read_json(p):
    with open(p) as f:
        return json.load(f)


def load_shelves():
    out = {}
    for s in SHELF_ORDER:
        p = ROOT / "registry" / "shelf" / f"{s}.json"
        if p.exists():
            out[s] = read_json(p)
    return out


def load_tools():
    return read_json(ROOT / "registry" / "tools.json")


def build_registry():
    return {"generated": "from registry/shelf/*.json by desk.py merge-registry; do not edit",
            "shelves": load_shelves()}


def skill_path(shelf, directive):
    return ROOT / ".claude" / "skills" / f"{shelf}-{directive}" / "SKILL.md"


def _final_vote_files(shelf):
    out = {"a": [], "b": []}
    for f in glob.glob(str(ROOT / "artifacts" / "verdicts" / f"{shelf}.final.*.json")):
        m = re.search(r"\.final\.([ab])\.(\d+)\.json$", f)
        if m:
            try:
                out[m.group(1)].append({v["directive"]: bool(v.get("pass")) for v in read_json(f)["verdicts"]})
            except Exception:
                pass
    return out


def final_verdicts(shelf):
    """directive -> bool. Preferred: <shelf>.final.<lens>.<k>.json, a majority of the votes per lens, both lenses must pass
    (at least 2 votes per lens). Fallback: the latest single-vote round that has BOTH lenses on disk."""
    votes = _final_vote_files(shelf)
    if votes["a"] or votes["b"]:
        dirs = set()
        for lens in votes.values():
            for v in lens:
                dirs |= set(v)
        res = {}
        for d in dirs:
            ok = True
            for lens in ("a", "b"):
                vs = [v[d] for v in votes[lens] if d in v]
                if len(vs) < 2 or sum(vs) * 2 <= len(vs):
                    ok = False
            res[d] = ok
        return res
    rounds = {}
    for f in glob.glob(str(ROOT / "artifacts" / "verdicts" / f"{shelf}.r*.*.json")):
        m = re.search(r"\.r(\d+)\.([ab])\.json$", f)
        if m:
            rounds.setdefault(int(m.group(1)), {})[m.group(2)] = f
    for k in sorted(rounds, reverse=True):
        lens = rounds[k]
        if "a" in lens and "b" in lens:
            res = {}
            try:
                a = {v["directive"]: bool(v.get("pass")) for v in read_json(lens["a"])["verdicts"]}
                b = {v["directive"]: bool(v.get("pass")) for v in read_json(lens["b"])["verdicts"]}
            except Exception:
                continue
            for d in set(a) | set(b):
                res[d] = a.get(d, False) and b.get(d, False)
            return res
    return {}


def skill_state(shelf, directive):
    if not skill_path(shelf, directive).exists():
        return "none"
    return "verified" if final_verdicts(shelf).get(directive) else "unverified"


# ---------------------------------------------------------------- router
def _hits(text, kws):
    out = []
    for kw in kws:
        k = (kw or "").lower().strip()
        if k and re.search(r"(?<![a-z0-9])" + re.escape(k) + r"(?![a-z0-9])", text):
            out.append(k)
    return out


# Stakes inference from task prose uses the owner's gate list only. The wider synonym set in gate.DENY_VERBS is for
# tool names, where being strict is right; in prose it turns nouns ("checkout service", "reply rate") into false alarms.
TASK_GATE_VERBS = ("order", "send", "pay", "hire", "sign", "diagnose", "exploit", "payload", "bypass", "decrypt")


def _gate_verbs_in(task):
    t = re.sub(r"\b(in order to|in order|order by|sort order|order of)\b", " ", task.lower())
    found = {v for v in TASK_GATE_VERBS if re.search(rf"(?<![a-z0-9]){v}(?![a-z0-9])", t)}
    if re.search(r"hardware[- ]start", t):
        found.add("hardware-start")
    return sorted(found)


def _dkw(name, entry):
    base = [name, name.replace("-", " ")]
    return base + list((entry or {}).get("keywords", []))


def route(task, shelves=None):
    shelves = shelves if shelves is not None else load_shelves()
    text = task.lower()
    scored = []
    for sname, sh in shelves.items():
        s_hits = _hits(text, sh.get("keywords", []))
        d_scores = {}
        for d, entry in sh.get("directives", {}).items():
            d_scores[d] = len(set(_hits(text, _dkw(d, entry))))
        best = max(d_scores.values()) if d_scores else 0
        scored.append((len(s_hits) + best, len(s_hits), sname, d_scores))
    scored.sort(key=lambda r: (-r[0], r[2]))
    base = {"task": " ".join(task.split())}
    if not scored or scored[0][1] == 0:
        # no shelf-level evidence at all: unsupported (a valid result, not smoothed)
        return dict(base, status="unsupported", shelf="none", directive="none", stakes="low",
                    novelty="high", candidates=[], contracts=[])
    top = [r for r in scored if r[0] == scored[0][0]]
    if len(top) > 1:
        return dict(base, status="ambiguous", shelf="none", directive="none", stakes="low",
                    novelty="high", candidates=[r[2] for r in top], contracts=[])
    _, _, sname, d_scores = scored[0]
    sh = shelves[sname]
    best = max(d_scores.values())
    if best == 0:
        return dict(base, status="ambiguous", shelf=sname, directive="none", stakes=sh.get("stakes", "low"),
                    novelty="high", candidates=[f"{sname}/{d}" for d in sh["directives"]], contracts=[])
    order = list(sh["directives"])
    winners = [d for d in order if d_scores[d] == best]
    if len(winners) > 1 and best < 2:
        return dict(base, status="ambiguous", shelf=sname, directive="none", stakes=sh.get("stakes", "low"),
                    novelty="high", candidates=[f"{sname}/{d}" for d in winners], contracts=[])
    chosen = [d for d in order if d_scores[d] >= 2 and d_scores[d] * 2 >= best]
    if not chosen:
        chosen = winners[:1]
    verbs = _gate_verbs_in(task)
    contracts = [_contract(base["task"], sname, sh, d, verbs) for d in chosen]
    status = "split" if len(contracts) > 1 else "ready"
    return dict(base, status=status, shelf=sname, directive=chosen[0], stakes=contracts[0]["stakes"],
                novelty=contracts[0]["novelty"], candidates=[], contracts=contracts)


def _contract(task, sname, sh, d, verbs):
    entry = sh["directives"].get(d)
    state = skill_state(sname, d)
    stakes = sh.get("stakes", "low")
    if verbs:
        stakes = "high"
    novelty = "low" if state == "verified" else "high"
    rung = entry["rung"] if (state == "verified" and entry) else "L3"
    if novelty == "high" and stakes == "high":
        rung = "L4"
    if entry and entry.get("gated") and sh.get("gates"):
        gate_s = "ABSENT: " + ", ".join(sh["gates"])
    elif verbs:
        gate_s = "ABSENT: " + ", ".join(verbs) + " (prepare and stop)"
    else:
        gate_s = "none"
    check = f"{entry['checkKind']}: {entry['doneWhen']}" if entry else "none authored: write the check before any edit"
    verifier = {"low": "check program only",
                "med": "check program + draft-blind verifier on the claims table",
                "high": "check program + two-lens draft-blind verifier + human gate"}[stakes]
    return {
        "task": task, "shelf": sname, "directive": d, "stakes": stakes, "novelty": novelty,
        "check": " ".join(check.split()), "gate": gate_s, "rung": rung, "token cap": str(TOKEN_CAPS[rung]),
        "verifier": verifier,
        "skill": str(skill_path(sname, d).relative_to(ROOT)) if state == "verified" else f"none ({state})",
        "files": f"plan.md state.json artifacts/{sname}/{d}.out",
        "status": "ready",
    }


def render_contract(c):
    return "# contract (task)\n" + "".join(f"{k}: {c[k]}\n" for k in CONTRACT_KEYS)


def render_result(res):
    if res["status"] in ("ready", "split"):
        parts = []
        for i, c in enumerate(res["contracts"]):
            c = dict(c, status="split" if res["status"] == "split" else "ready")
            parts.append(render_contract(c))
        return "\n---\n".join(parts)
    cand = ", ".join(res["candidates"]) or "none"
    c = {"task": res["task"], "shelf": res["shelf"], "directive": res["directive"], "stakes": res["stakes"],
         "novelty": res["novelty"], "check": f"none: {res['status']}; candidates: {cand}",
         "gate": "none", "rung": "L0", "token cap": "0", "verifier": "none",
         "skill": "none", "files": "state.json", "status": res["status"]}
    return render_contract(c)


def parse_contract(text):
    d = {}
    for line in text.splitlines():
        m = re.match(r"^([a-z ]+): (.*)$", line)
        if m:
            d[m.group(1)] = m.group(2)
    return d


def lint_contract(d):
    errs = [f"missing key: {k}" for k in CONTRACT_KEYS if not d.get(k)]
    if errs:
        return errs
    if d["status"] in ("ready", "split"):
        if d["shelf"] not in SHELF_ORDER:
            errs.append(f"unknown shelf {d['shelf']}")
        if d["rung"] not in RUNGS:
            errs.append(f"bad rung {d['rung']}")
        if d["stakes"] not in STAKES:
            errs.append("bad stakes")
        if d["novelty"] not in ("low", "high"):
            errs.append("bad novelty")
        if not d["token cap"].isdigit():
            errs.append("token cap not an integer")
        elif int(d["token cap"]) != TOKEN_CAPS.get(d["rung"], -1):
            errs.append("token cap does not match rung")
        if d["check"].startswith("none"):
            errs.append("ready contract with no check")
        if d["gate"] == "":
            errs.append("empty gate")
    elif d["status"] not in ("ambiguous", "unsupported"):
        errs.append(f"bad status {d['status']}")
    return errs


def cmd_route(a):
    res = route(a.task)
    if a.json:
        print(json.dumps(res, indent=1))
    else:
        out = render_result(res)
        if a.out:
            Path(a.out).parent.mkdir(parents=True, exist_ok=True)
            Path(a.out).write_text(out)
        print(out)
    return 0


def cmd_route_eval(a):
    tasks = read_json(a.tasks)
    bad = 0
    for t in tasks:
        res = route(t["task"])
        text = render_result(res)
        outp = ROOT / "artifacts" / "router" / f"{t['id']}.contract.md"
        outp.parent.mkdir(parents=True, exist_ok=True)
        outp.write_text(text)
        errs = []
        for block in text.split("\n---\n"):
            errs += lint_contract(parse_contract(block))
        for k, want in t.get("expect", {}).items():
            got = res.get(k)
            if got != want:
                errs.append(f"{k}: expected {want!r}, got {got!r}")
        print(f"{'PASS' if not errs else 'FAIL'} {t['id']}: {res['status']} {res['shelf']}/{res['directive']} "
              f"stakes={res['stakes']} novelty={res['novelty']}" + ("" if not errs else "  <- " + "; ".join(errs)))
        bad += bool(errs)
    print(f"{len(tasks) - bad}/{len(tasks)} contracts emitted, valid, and matching")
    return 1 if bad else 0


def cmd_contract_lint(a):
    errs = []
    for block in Path(a.file).read_text().split("\n---\n"):
        errs += lint_contract(parse_contract(block))
    for e in errs:
        print("ERROR", e)
    return 1 if errs else 0


# ---------------------------------------------------------------- contract-check
def cmd_contract_check(a):
    cpath = Path(a.file).resolve()
    cwd = cpath.parent
    text = cpath.read_text()
    m = re.search(r"^## Done-when\s*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    rows = []
    if m:
        for line in m.group(1).splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if line.strip().startswith("|") and len(cells) >= 3 and cells[0] not in ("id", "") and not set(cells[0]) <= set("-: "):
                cmd = re.search(r"`([^`]+)`", cells[2])
                rows.append((cells[0], cells[1], cmd.group(1) if cmd else None))
    if not rows:
        print("FAIL: no Done-when rows with a check command")
        return 1
    bad = []
    for rid, label, cmd in rows:
        if not cmd:
            print(f"FAIL {rid}: no check command in row ({label})")
            bad.append(rid)
            continue
        try:
            r = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True, timeout=a.timeout)
            rc, tail = r.returncode, (r.stdout + r.stderr).strip().splitlines()[-4:]
        except subprocess.TimeoutExpired:
            rc, tail = 124, ["timeout"]
        if rc == 0:
            print(f"PASS {rid}: {label}")
        else:
            print(f"FAIL {rid}: {label} (exit {rc})")
            for t in tail:
                print("      " + t[:200])
            bad.append(rid)
    status = "GREEN" if not bad else "RED"
    if a.write:
        new = re.sub(r"^STATUS: .*$", f"STATUS: {status}", text, count=1, flags=re.M)
        cpath.write_text(new)
        sp = cwd / "state.json"
        st = read_json(sp) if sp.exists() else {}
        st.update(contract_status=status, failing=bad)
        sp.write_text(json.dumps(st, indent=1) + "\n")
    print(f"{status}: {len(rows) - len(bad)}/{len(rows)} rows pass")
    return 0 if not bad else 1


# ---------------------------------------------------------------- lint
def parse_skill(path):
    text = Path(path).read_text()
    lines = text.splitlines()
    fm = {}
    body_start = 0
    if lines and lines[0] == "---":
        for i, ln in enumerate(lines[1:], 1):
            if ln == "---":
                body_start = i + 1
                break
            m = re.match(r"^([A-Za-z_-]+):\s*(.*)$", ln)
            if m:
                fm[m.group(1)] = m.group(2).strip()
    sections, cur = {}, None
    order = []
    for ln in lines[body_start:]:
        m = re.match(r"^## (.+?)\s*$", ln)
        if m:
            cur = m.group(1)
            sections[cur] = []
            order.append(cur)
        elif cur is not None:
            sections[cur].append(ln)
    return {"fm": fm, "sections": {k: "\n".join(v).strip() for k, v in sections.items()},
            "order": order, "nlines": len(lines)}


def _kv(block, key):
    m = re.search(rf"^{key}:\s*(.+)$", block, re.M)
    return m.group(1).strip() if m else None


def lint_directive_entry(shelf, d, e, tools, errs, warns, only_when_skill=True):
    where = f"{shelf}/{d}"
    for k in ("trigger", "doneWhen", "checkKind", "rung", "forbidden", "tool", "toolScope", "gated", "status", "keywords", "checkRunnable"):
        if k not in e:
            errs.append(f"{where}: missing field {k}")
            return
    if e["checkKind"] not in CHECK_KINDS:
        errs.append(f"{where}: checkKind {e['checkKind']!r}")
    if e["rung"] not in RUNGS:
        errs.append(f"{where}: rung {e['rung']!r}")
    if e["status"] not in STATUSES:
        errs.append(f"{where}: status {e['status']!r}")
    if e["toolScope"] not in SCOPES:
        errs.append(f"{where}: toolScope {e['toolScope']!r}")
    if not str(e["doneWhen"]).strip():
        errs.append(f"{where}: empty doneWhen")
    if not isinstance(e["checkRunnable"], bool):
        errs.append(f"{where}: checkRunnable must be true or false")
    elif e["checkRunnable"]:
        if e["checkKind"] == "human-only":
            errs.append(f"{where}: a human-only check cannot be checkRunnable")
        if e["tool"] == "none" and not re.search(r"\b(desk|fixtures)/\S+", str(e["doneWhen"])):
            errs.append(f"{where}: checkRunnable true needs a registered tool or a repo program path in doneWhen")
    if e["checkKind"] == "human-only" and e["status"] == "reliable":
        errs.append(f"{where}: human-only check cannot be 'reliable'")
    kws = e["keywords"]
    if not (isinstance(kws, list) and len(kws) >= 3 and all(isinstance(k, str) and len(k.strip()) >= 3 and k == k.lower() for k in kws)):
        errs.append(f"{where}: keywords must be >=3 lowercase strings of >=3 chars")
    if e["gated"] and not str(e.get("gate", "")).strip():
        errs.append(f"{where}: gated directive needs a 'gate' field naming the absent tool or verb")
    # tool
    names = {t["name"]: t for t in tools["tools"]}
    if e["tool"] == "none":
        if e["toolScope"] != "none":
            errs.append(f"{where}: tool none but scope {e['toolScope']}")
    else:
        t = names.get(e["tool"])
        if t is None:
            errs.append(f"{where}: tool {e['tool']!r} is not in registry/tools.json")
        else:
            if t["scope"] != e["toolScope"]:
                errs.append(f"{where}: toolScope {e['toolScope']} != registry scope {t['scope']}")
            if t["scope"] == "act" and not t.get("human_added"):
                errs.append(f"{where}: relies on act tool {e['tool']} without a human add")
        if gate.verb_hit(e["tool"]):
            errs.append(f"{where}: gate verb in tool name {e['tool']}")
    if e["gated"] and e["toolScope"] == "act":
        errs.append(f"{where}: gated directive cannot hold an act tool")
    if re.search(r"(^|-)and(-|$)", d) and d not in AND_OK:
        errs.append(f"{where}: directive name contains 'and'; split it")
    if e["rung"] in ("L3", "L4") and e["checkKind"] in ("exit-code", "schema", "count", "state-diff") and e["tool"] != "none":
        warns.append(f"{where}: rung {e['rung']} for a tool-checkable directive; cheaper rung expected")


def lint_skill(shelf, d, e, errs, warns, seed_contracts):
    p = skill_path(shelf, d)
    where = f"{shelf}/{d}"
    if not p.exists():
        return
    sk = parse_skill(p)
    if sk["nlines"] > 60:
        errs.append(f"{where}: SKILL.md has {sk['nlines']} lines (>60)")
    if sk["fm"].get("name") != f"{shelf}-{d}":
        errs.append(f"{where}: frontmatter name {sk['fm'].get('name')!r} != {shelf}-{d}")
    desc = sk["fm"].get("description", "")
    if not desc or len(desc) > 200:
        errs.append(f"{where}: description missing or >200 chars")
    is_seed = SEEDS.get(shelf) == d
    expect = SKILL_SECTIONS + (["Held-out check"] if is_seed else [])
    if sk["order"] != expect:
        errs.append(f"{where}: sections {sk['order']} != {expect}")
        return
    s = sk["sections"]
    if e:
        if _kv(s["Done-when"], "check") != e.get("checkKind"):
            errs.append(f"{where}: skill 'check:' != registry checkKind")
        if _kv(s["Rung"], "rung") != e.get("rung"):
            errs.append(f"{where}: skill 'rung:' != registry rung")
        if _kv(s["Tool"], "tool") != e.get("tool"):
            errs.append(f"{where}: skill 'tool:' != registry tool")
        if _kv(s["Tool"], "scope") != e.get("toolScope"):
            errs.append(f"{where}: skill 'scope:' != registry toolScope")
        if e.get("gated") and not _kv(s["Tool"], "gate"):
            errs.append(f"{where}: gated but skill Tool section has no 'gate:' line")
    sc = seed_contracts.get(f"{shelf}-{d}")
    if sc:
        if sc["command"] not in (e or {}).get("doneWhen", ""):
            errs.append(f"{where}: seed doneWhen must contain the contract command {sc['command']!r}")
        if sc["command"] not in s["Done-when"]:
            errs.append(f"{where}: seed skill Done-when must contain {sc['command']!r}")
        if "heldout" in "\n".join(v for k, v in s.items() if k != "Held-out check"):
            errs.append(f"{where}: seed skill leaks the held-out fixture outside its Held-out check section")
        if "tune" not in s["Held-out check"] and "tune" not in "\n".join(s.values()):
            warns.append(f"{where}: seed skill never points at its tune fixture")


def cmd_lint(a):
    errs, warns = [], []
    tools = load_tools()
    seed_contracts = {}
    for p in glob.glob(str(ROOT / "registry" / "seed" / "*.json")):
        seed_contracts[Path(p).stem] = read_json(p)
    # tools registry
    names = [t["name"] for t in tools["tools"]]
    if len(names) != len(set(names)):
        errs.append("tools.json: duplicate tool names")
    for t in tools["tools"]:
        if t.get("scope") not in ("read", "draft", "act"):
            errs.append(f"tools.json: {t.get('name')} bad scope")
        if t.get("scope") == "act" and "human_added" not in t:
            errs.append(f"tools.json: act tool {t['name']} needs an explicit human_added")
        if t.get("path") and not (ROOT / t["path"]).exists():
            errs.append(f"tools.json: {t['name']} points at {t['path']} which does not exist")
        if t.get("kind") == "local" and not shutil.which(t["cmd"].split()[0]):
            errs.append(f"tools.json: local tool {t['name']} is registered but {t['cmd'].split()[0]} is absent")
        if gate.verb_hit(t["name"]) and t.get("scope") != "act":
            errs.append(f"tools.json: {t['name']} carries a gate verb but is not scope act")
    for t in tools.get("proposed", []):
        if not t.get("human_add_required"):
            errs.append(f"tools.json: proposed {t.get('name')} must have human_add_required true")
    shelves = load_shelves()
    if not a.shelf:
        missing = [s for s in SHELF_ORDER if s not in shelves]
        if missing:
            errs.append(f"missing shelf files: {missing}")
        gen = ROOT / "registry" / "shelves.json"
        if gen.exists() and read_json(gen) != build_registry():
            errs.append("registry/shelves.json is stale: run merge-registry")
    for sname, sh in shelves.items():
        if a.shelf and sname != a.shelf:
            continue
        for k in ("shelf", "now", "stakes", "gates", "keywords", "directives"):
            if k not in sh:
                errs.append(f"{sname}: missing shelf field {k}")
        if sh.get("stakes") not in STAKES:
            errs.append(f"{sname}: bad stakes")
        brief = (ROOT / "registry" / "brief" / f"{sname}.md")
        btxt = brief.read_text() if brief.exists() else ""
        if not brief.exists():
            errs.append(f"{sname}: brief missing")
        for d, e in sh["directives"].items():
            spaced = d.replace("-", " ")
            if btxt and not re.search(rf"(?im)^({re.escape(spaced)}|{re.escape(d)})\b", btxt) and d not in ("book", "pay"):
                warns.append(f"{sname}/{d}: no line in the brief starts with this directive name")
            if e is None:
                warns.append(f"{sname}/{d}: not authored")
                continue
            lint_directive_entry(sname, d, e, tools, errs, warns)
            lint_skill(sname, d, e, errs, warns, seed_contracts)
            if skill_path(sname, d).exists() and skill_state(sname, d) != "verified":
                warns.append(f"{sname}/{d}: skill exists but is not verified (router treats it as novelty high)")
        for d in sh["directives"]:
            if sh["directives"][d] is None and skill_path(sname, d).exists():
                errs.append(f"{sname}/{d}: SKILL.md exists but the registry entry is null")
    for s in SEEDS.items():
        key = f"{s[0]}-{s[1]}"
        if key not in seed_contracts:
            errs.append(f"seed contract missing: registry/seed/{key}.json")
    for w in warns:
        print("WARN ", w)
    for e in errs:
        print("ERROR", e)
    print(f"lint: {len(errs)} error(s), {len(warns)} warning(s)")
    return 1 if errs else 0


CLAIM_FIELDS = ("trigger", "doneWhen", "checkKind", "rung", "forbidden", "tool", "toolScope", "gated", "gate", "status",
                "checkRunnable", "keywords", "absentTools")


def cmd_claims(a):
    """Deterministic claims table per shelf: exactly the registry entries, no SKILL.md text. Verifiers read these."""
    n = 0
    for sname, sh in load_shelves().items():
        if a.shelf and sname != a.shelf:
            continue
        rows = []
        for d, e in sh["directives"].items():
            if e:
                rows.append(dict({"directive": d}, **{k: e.get(k) for k in CLAIM_FIELDS}))
        p = ROOT / "artifacts" / "claims" / f"{sname}.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps({"shelf": sname, "directives": rows}, indent=1) + "\n")
        n += len(rows)
    print(f"wrote claims for {n} directives")
    return 0


def cmd_verdicts(a):
    tot = ok = 0
    for sname, sh in load_shelves().items():
        fv = final_verdicts(sname)
        names = [d for d, e in sh["directives"].items() if e]
        v = [d for d in names if fv.get(d)]
        tot += len(names)
        ok += len(v)
        un = [d for d in names if not fv.get(d)]
        print(f"{sname:20} {len(v):>2}/{len(names):<2} verified" + (f"   voted down: {', '.join(un)}" if un else ""))
    print(f"TOTAL {ok}/{tot} verified")
    return 0


def cmd_merge_registry(a):
    (ROOT / "registry" / "shelves.json").write_text(json.dumps(build_registry(), indent=1, sort_keys=False) + "\n")
    print("wrote registry/shelves.json")
    return 0


# ---------------------------------------------------------------- merge-shelves
def _git(*args, check=False):
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, check=check)


def cmd_merge_shelves(a):
    refs = _git("for-each-ref", "--format=%(refname:short)", "refs/heads/desk/").stdout.split()
    by_shelf = {}
    for r in refs:
        m = re.match(r"^desk/(.+)-r(\d+)$", r)
        if m:
            by_shelf.setdefault(m.group(1), []).append((int(m.group(2)), r))
    bad = 0
    for s in SHELF_ORDER:
        if s not in by_shelf:
            print(f"MISSING {s}: no desk/{s}-rN branch")
            bad += 1
            continue
        _, br = max(by_shelf[s])
        if _git("merge-base", "--is-ancestor", br, "HEAD").returncode == 0:
            print(f"SKIP    {s}: {br} already merged")
            continue
        base = _git("merge-base", "HEAD", br).stdout.strip()
        files = _git("diff", "--name-only", base, br).stdout.split()
        ok_prefix = (f".claude/skills/{s}-", f"registry/shelf/{s}.json")
        out_of_scope = [f for f in files if not f.startswith(ok_prefix)]
        if not files:
            print(f"SKIP    {s}: {br} changes nothing (empty commit)")
            continue
        if out_of_scope:
            print(f"REJECT  {s}: {br} touches out-of-scope paths {out_of_scope[:5]}")
            bad += 1
            continue
        r = _git("merge", "--no-ff", "-m", f"Merge shelf {s} ({br}) after path-scope check", br)
        if r.returncode != 0:
            _git("merge", "--abort")
            print(f"REJECT  {s}: merge failed: {(r.stdout + r.stderr).strip()[:200]}")
            bad += 1
            continue
        print(f"MERGED  {s}: {br} ({len(files)} files, scope ok)")
    return 1 if bad else 0


# ---------------------------------------------------------------- invention + promotion
def cmd_invent_check(a):
    inv = read_json(a.file)
    tools = load_tools()
    callable_ = {t["name"]: t for t in tools["tools"]}
    proposed = {t["name"]: t for t in tools.get("proposed", [])}
    shelves = load_shelves()
    errs = []
    cands = inv.get("candidates", [])
    if len(cands) != 3:
        errs.append(f"need exactly 3 candidates, got {len(cands)}")
    if sum(1 for c in cands if c.get("kill")) != 1:
        errs.append("exactly one candidate must be a kill")
    for i, c in enumerate(cands):
        w = f"candidate {i + 1}"
        for k in ("shelf", "directive", "tool", "toolScope", "doneWhen", "shadowRun", "reason", "kill"):
            if k not in c or c[k] in ("", None):
                errs.append(f"{w}: missing {k}")
        if errs and any(e.startswith(w) for e in errs):
            continue
        sh = shelves.get(c["shelf"], {}).get("directives", {})
        if c["directive"] not in sh:
            errs.append(f"{w}: {c['shelf']}/{c['directive']} is not a registered directive")
        elif sh[c["directive"]] and sh[c["directive"]]["status"] == "reliable" and not c["kill"]:
            errs.append(f"{w}: crossing a 'reliable' directive; invention targets weak or assisted ones")
        if c["toolScope"] not in ("read", "draft"):
            errs.append(f"{w}: scope {c['toolScope']} (invention never invents act)")
        if gate.verb_hit(c["tool"]):
            errs.append(f"{w}: gate verb in tool {c['tool']}")
        t = callable_.get(c["tool"]) or proposed.get(c["tool"])
        if not t:
            errs.append(f"{w}: tool {c['tool']!r} is in neither tools nor proposed")
        elif c["tool"] in proposed and not c.get("needsHumanAdd"):
            errs.append(f"{w}: proposed tool {c['tool']} needs needsHumanAdd true")
        elif t.get("scope") != c["toolScope"]:
            errs.append(f"{w}: scope {c['toolScope']} != registry {t.get('scope')}")
    for e in errs:
        print("ERROR", e)
    print(f"invent-check: {len(errs)} error(s)")
    return 1 if errs else 0


def cmd_promote_gate(a):
    d = read_json(a.file)
    b, c = d["baseline"], d["candidate"]
    reasons = []
    if "heldout_pass" not in c:
        reasons.append("no held-out result: a tuning-set win does not promote")
    elif not c["heldout_pass"]:
        reasons.append("held-out check failed")
    if not c.get("tune_pass", False):
        reasons.append("tune check failed")
    cheaper = c.get("tokens", 10**18) < b.get("tokens", -1)
    faster = c.get("seconds", 10**18) < b.get("seconds", -1)
    if not (cheaper or faster):
        reasons.append("neither tokens nor wall time dropped")
    if c.get("heldout_pass") and b.get("heldout_pass") is False:
        pass
    print("PROMOTE" if not reasons else "HOLD: " + "; ".join(reasons))
    return 0 if not reasons else 1


# ---------------------------------------------------------------- trace + tokens
def cmd_verify_trace(a):
    ok, msg = trace.verify(str(ROOT))
    print(("OK " if ok else "TAMPER ") + msg)
    return 0 if ok else 1


def _usage_by_model(jsonl):
    """Sum usage from one transcript. Each API message is counted once (the record with the largest output_tokens for its id)."""
    ids, last_ts = {}, ""
    with open(jsonl) as f:
        for line in f:
            try:
                r = json.loads(line)
            except Exception:
                continue
            last_ts = max(last_ts, r.get("timestamp") or "")
            if r.get("type") != "assistant":
                continue
            m = r.get("message") or {}
            k, u = m.get("id"), m.get("usage") or {}
            if k and (k not in ids or u.get("output_tokens", 0) >= ids[k][1].get("output_tokens", 0)):
                ids[k] = (m.get("model") or "unknown", u)
    by = {}
    for mod, u in ids.values():
        b = by.setdefault(mod, {"uncached_input": 0, "cache_creation": 0, "cache_read": 0, "output_tokens": 0, "api_messages": 0})
        b["uncached_input"] += u.get("input_tokens", 0)
        b["cache_creation"] += u.get("cache_creation_input_tokens", 0)
        b["cache_read"] += u.get("cache_read_input_tokens", 0)
        b["output_tokens"] += u.get("output_tokens", 0)
        b["api_messages"] += 1
    return by, last_ts


def _fold(by):
    tot = {"uncached_input": 0, "cache_creation": 0, "cache_read": 0, "output_tokens": 0, "api_messages": 0}
    for b in by.values():
        for k in tot:
            tot[k] += b[k]
    tot["input_tokens"] = tot["uncached_input"] + tot["cache_creation"] + tot["cache_read"]
    return tot


def _first_call_prompt(jsonl):
    """Prompt tokens of the agent's first API call: the inherited static prefix every subagent pays before doing any work."""
    with open(jsonl) as f:
        for line in f:
            try:
                r = json.loads(line)
            except Exception:
                continue
            u = (r.get("message") or {}).get("usage") if r.get("type") == "assistant" else None
            if u:
                return u.get("input_tokens", 0) + u.get("cache_creation_input_tokens", 0) + u.get("cache_read_input_tokens", 0)
    return 0


def _prefix_stats(rows):
    vals = sorted(r["first_call_prompt_tokens"] for r in rows if r.get("first_call_prompt_tokens"))
    if not vals:
        return None
    return {"agents": len(vals), "min": vals[0], "median": vals[len(vals) // 2], "max": vals[-1],
            "meaning": "prompt tokens of each agent's first API call, before any work: the harness's inherited system prompt, tool list and skill listing"}


def cmd_tokens(a):
    rows = []
    for wd in a.workflow_dir:
        for meta in sorted(glob.glob(os.path.join(wd, "agent-*.meta.json"))):
            jl = meta.replace(".meta.json", ".jsonl")
            if not os.path.exists(jl):
                continue
            m = read_json(meta)
            by, ts = _usage_by_model(jl)
            row = {"label": m.get("description", ""), "phase": m.get("workflowPhase", ""), "model": m.get("model", ""),
                   "source": jl, "last_ts": ts, "by_model": by, "first_call_prompt_tokens": _first_call_prompt(jl)}
            row.update(_fold(by))
            rows.append(row)
    main_by, main_ts = _usage_by_model(a.main)
    lead = {"source": a.main, "as_of": main_ts, "by_model": main_by}
    lead.update(_fold(main_by))
    authors = sorted((r for r in rows if r["label"].startswith("author:")), key=lambda r: (r["output_tokens"], r["label"]))
    rep = authors[(len(authors) - 1) // 2] if authors else None
    out = {"unit": "tokens as reported in each transcript's message.usage; input_tokens = uncached + cache_creation + cache_read",
           "lead_pass": lead,
           "worker_pass": dict(rep, note="the median author agent by output tokens; every agent starts with the harness's inherited prefix, so input is dominated by cache reads") if rep else None,
           "worker_pass_range": ({"authors": len(authors), "output_min": authors[0]["output_tokens"], "output_max": authors[-1]["output_tokens"]} if authors else None),
           "inherited_prefix": _prefix_stats(rows),
           "totals_by_label_prefix": {}, "per_agent": [{k: v for k, v in r.items() if k != "by_model"} for r in rows]}
    for r in rows:
        pre = r["label"].split(":")[0] or "unlabelled"
        t = out["totals_by_label_prefix"].setdefault(pre, {"agents": 0, "input_tokens": 0, "output_tokens": 0})
        t["agents"] += 1
        t["input_tokens"] += r["input_tokens"]
        t["output_tokens"] += r["output_tokens"]
    meters = {}
    for kv in a.meter:
        k, _, v = kv.partition("=")
        meters[k] = int(v)
    out["harness_meter"] = {"unit": "output tokens as metered by the harness (budget.spent deltas), per workflow, reasoning included", **meters}
    out["measurement_notes"] = [
        "input_tokens is exact as reported at each API call (uncached + cache write + cache read). It sums over repeated calls, so cache reads re-count the same prefix on every call; it is processed input, not distinct text.",
        "output_tokens in subagent transcripts is a streaming snapshot taken near the start of each message, so it is a LOWER BOUND (an author's recorded 93 against roughly 950 tokens of visible content). Do not read it as a total.",
        "harness_meter is the better output measure but exists only per workflow, never per agent. A per-agent output figure is not available; the mean per agent for a workflow is meter / agents.",
        "The lead's recorded output exceeds its visible characters / 4 because reasoning tokens count as output and are not visible text; they are not separately measurable here.",
        "The harness's own subagent_tokens totals use a definition that does not reconcile with the transcript sums, so they are quoted from the workflow results, not derived.",
    ]
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=1) + "\n")
    print(f"wrote {a.out}: lead output {lead['output_tokens']}, {len(rows)} agents, "
          f"worker pass {rep['label'] if rep else 'none'} output {rep['output_tokens'] if rep else 'n/a'}")
    for k, v in out["totals_by_label_prefix"].items():
        print(f"  {k}: {v['agents']} agents, input {v['input_tokens']}, output {v['output_tokens']}")
    return 0


def _result_text(block):
    cont = block.get("content")
    return cont if isinstance(cont, str) else " ".join(x.get("text", "") for x in cont if isinstance(x, dict))


def cmd_seed_attempts(a):
    """How many times each seed agent ran its checker and what each run said, read from the agent transcripts.
    OK = the checker printed OK; FAIL = it printed 'assertion(s) failed'; OTHER = anything else (usage error, missing file)."""
    out = []
    for wd in a.workflow_dir:
        for meta in sorted(glob.glob(os.path.join(wd, "agent-*.meta.json"))):
            label = read_json(meta).get("description", "")
            if not label.startswith("seed:"):
                continue
            pend, runs = {}, []
            with open(meta.replace(".meta.json", ".jsonl")) as f:
                for line in f:
                    try:
                        r = json.loads(line)
                    except Exception:
                        continue
                    c = (r.get("message") or {}).get("content")
                    if not isinstance(c, list):
                        continue
                    for b in c:
                        if b.get("type") == "tool_use" and b.get("name") == "Bash" and "check.py" in json.dumps(b.get("input", {})):
                            pend[b["id"]] = b["input"].get("command", "")
                        if b.get("type") == "tool_result" and b.get("tool_use_id") in pend:
                            t = _result_text(b).strip()
                            verdict = ("FAIL" if "assertion(s) failed" in t else "OK" if re.search(r"(^|\n)OK(\n|$)", t) else "OTHER")
                            runs.append({"result": verdict, "first_line": (t.splitlines() or [""])[0][:160]})
            out.append({"label": label, "checker_runs": len(runs), "runs": runs})
    out = [o for o in out if o["checker_runs"]]
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=1) + "\n")
    for o in out:
        print(f"{o['label']:44} checker runs={o['checker_runs']}  {[r['result'] for r in o['runs']]}")
    return 0


def cmd_tokens_check(a):
    d = read_json(a.file)
    errs = []
    for k in ("lead_pass", "worker_pass"):
        v = d.get(k)
        if not isinstance(v, dict) or not isinstance(v.get("output_tokens"), int) or not isinstance(v.get("input_tokens"), int):
            errs.append(f"{k}: needs integer input_tokens and output_tokens")
        elif not v.get("source"):
            errs.append(f"{k}: needs a source (the transcript file the numbers were summed from)")
    for e in errs:
        print("ERROR", e)
    print(f"tokens-check: {len(errs)} error(s)")
    return 1 if errs else 0


# ---------------------------------------------------------------- report
def cmd_report_check(a):
    txt = Path(a.file).read_text()
    need = ["## Report", "### Files created", "### Checks run", "### Not built: tool absent"]
    missing = [h for h in need if h not in txt]
    for h in missing:
        print("ERROR missing heading:", h)
    body = txt.split("## Report", 1)[-1]
    if "Filled after the run." in body:
        print("ERROR: the report has not been written")
        missing.append("body")
    print(f"report-check: {len(missing)} problem(s)")
    return 1 if missing else 0


def cmd_report(a):
    shelves = load_shelves()
    tools = load_tools()
    rows, absent = [], set()
    tot = {"reliable": 0, "assisted": 0, "weak": 0, "gated": 0, "unauthored": 0}
    unverified, gated, runnable = [], [], 0
    for s, sh in shelves.items():
        c = {"reliable": 0, "assisted": 0, "weak": 0, "gated": 0, "unauthored": 0}
        for d, e in sh["directives"].items():
            if e is None:
                c["unauthored"] += 1
                continue
            c[e["status"]] += 1
            runnable += bool(e.get("checkRunnable"))
            for t in e.get("absentTools", []):
                absent.add(t)
            if e["gated"]:
                gated.append(f"{s}/{d}")
            if skill_state(s, d) != "verified":
                unverified.append(f"{s}/{d} ({skill_state(s, d)})")
        for k in c:
            tot[k] += c[k]
        rows.append((s, c))
    print("| shelf | reliable | assisted | weak | gated | unauthored |\n|---|---|---|---|---|---|")
    for s, c in rows:
        print(f"| {s} | {c['reliable']} | {c['assisted']} | {c['weak']} | {c['gated']} | {c['unauthored']} |")
    print(f"| **total** | {tot['reliable']} | {tot['assisted']} | {tot['weak']} | {tot['gated']} | {tot['unauthored']} |")
    print(f"\ncheck runnable today (a registered tool or repo program produces the check): {runnable} of {sum(1 for sh in shelves.values() for e in sh['directives'].values() if e)} authored directives")
    print(f"\ngated directives ({len(gated)}): " + ", ".join(gated))
    print(f"\nnot verified ({len(unverified)}): " + (", ".join(unverified) or "none"))
    print("\nabsent tools registered: " + ", ".join(t["name"] for t in tools.get("absent", [])))
    print("absent tools named by directives: " + (", ".join(sorted(absent)) or "none"))
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(prog="desk")
    sp = p.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("route"); s.add_argument("task"); s.add_argument("--out"); s.add_argument("--json", action="store_true"); s.set_defaults(f=cmd_route)
    s = sp.add_parser("route-eval"); s.add_argument("tasks"); s.set_defaults(f=cmd_route_eval)
    s = sp.add_parser("contract-lint"); s.add_argument("file"); s.set_defaults(f=cmd_contract_lint)
    s = sp.add_parser("contract-check"); s.add_argument("file", nargs="?", default="contract.md"); s.add_argument("--write", action="store_true"); s.add_argument("--timeout", type=int, default=180); s.set_defaults(f=cmd_contract_check)
    s = sp.add_parser("lint"); s.add_argument("--shelf"); s.set_defaults(f=cmd_lint)
    s = sp.add_parser("claims"); s.add_argument("--shelf"); s.set_defaults(f=cmd_claims)
    s = sp.add_parser("verdicts"); s.set_defaults(f=cmd_verdicts)
    s = sp.add_parser("merge-registry"); s.set_defaults(f=cmd_merge_registry)
    s = sp.add_parser("merge-shelves"); s.set_defaults(f=cmd_merge_shelves)
    s = sp.add_parser("invent-check"); s.add_argument("file"); s.set_defaults(f=cmd_invent_check)
    s = sp.add_parser("promote-gate"); s.add_argument("file"); s.set_defaults(f=cmd_promote_gate)
    s = sp.add_parser("verify-trace"); s.set_defaults(f=cmd_verify_trace)
    s = sp.add_parser("tokens"); s.add_argument("--workflow-dir", action="append", default=[]); s.add_argument("--main", required=True); s.add_argument("--meter", action="append", default=[]); s.add_argument("--out", default="artifacts/tokens.json"); s.set_defaults(f=cmd_tokens)
    s = sp.add_parser("seed-attempts"); s.add_argument("--workflow-dir", action="append", default=[]); s.add_argument("--out", default="artifacts/seeds/attempts.json"); s.set_defaults(f=cmd_seed_attempts)
    s = sp.add_parser("tokens-check"); s.add_argument("file"); s.set_defaults(f=cmd_tokens_check)
    s = sp.add_parser("report"); s.set_defaults(f=cmd_report)
    s = sp.add_parser("report-check"); s.add_argument("file"); s.set_defaults(f=cmd_report_check)
    a = p.parse_args(argv)
    return a.f(a)


if __name__ == "__main__":
    sys.exit(main())
