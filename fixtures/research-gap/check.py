#!/usr/bin/env python3
"""Held-out check for research-gap: list claims, search only the first unsupported, stop when filled or open."""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
STOP = set("the a an of to in and or for on at by with was were is are be been it its as that this from per".split())


def toks(s):
    return {t for t in re.findall(r"[a-z0-9]+", s.lower()) if t not in STOP}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fixture", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--searchlog", required=True)
    a = ap.parse_args()
    base = os.path.join(HERE, a.fixture)
    exp = json.load(open(os.path.join(base, "expected.json")))["expected"]
    claims = {}
    for line in open(os.path.join(base, "draft.md"), encoding="utf-8"):
        m = re.match(r"^(C\d+)\.\s+(.*?)(?:\s+\[src:(\S+)\])?\s*$", line)
        if m:
            claims[m.group(1)] = m.group(2)
    order = list(claims)
    errs = []
    try:
        out = json.load(open(a.out))
    except Exception as e:
        print(f"FAIL: cannot read {a.out}: {e}")
        return 1
    rows = out.get("claims") if isinstance(out, dict) else None
    if not isinstance(rows, list) or [r.get("id") for r in rows] != order:
        print(f"FAIL: claims ids must be exactly {order} in order")
        return 1
    corpus = os.path.join(base, "corpus")
    for r in rows:
        cid = r["id"]
        if set(r) != {"id", "text", "status", "evidence", "searched", "resolution"}:
            errs.append(f"{cid}: keys {sorted(r)}")
            continue
        want = exp[cid]
        for k in ("status", "searched", "resolution"):
            if r[k] != want[k]:
                errs.append(f"{cid}: {k} is {r[k]!r}, expected {want[k]!r}")
        if r["text"].strip() != claims[cid].strip():
            errs.append(f"{cid}: text is not the draft's claim verbatim")
        ev = r["evidence"]
        if want["status"] == "supported":
            if not isinstance(ev, dict) or set(ev) != {"doc", "quote"}:
                errs.append(f"{cid}: supported claim needs evidence {{doc, quote}}")
                continue
            p = os.path.join(corpus, os.path.basename(str(ev["doc"])))
            if not os.path.isfile(p):
                errs.append(f"{cid}: evidence doc {ev['doc']!r} does not exist")
                continue
            lines = open(p, encoding="utf-8").read().splitlines()
            if not any(ev["quote"].strip() and ev["quote"].strip() in l for l in lines):
                errs.append(f"{cid}: quote is not verbatim in {ev['doc']}")
            ct, qt = toks(claims[cid]), toks(ev["quote"])
            digits = {t for t in ct if t.isdigit()}
            if not digits <= qt or len(ct & qt) * 2 < len(ct):
                errs.append(f"{cid}: quote does not carry the claim's numbers and half its terms")
        elif ev is not None:
            errs.append(f"{cid}: unsupported claim must have evidence null")
    # exactly the expected number of searches, aimed at the first unsupported claim only
    n_expected = sum(1 for v in exp.values() if v["searched"])
    try:
        log = [json.loads(l) for l in open(a.searchlog) if l.strip()]
    except FileNotFoundError:
        log = []
    if len(log) != n_expected:
        errs.append(f"search log has {len(log)} queries; expected exactly {n_expected}")
    elif log:
        first = next(cid for cid in order if exp[cid]["searched"])
        i = order.index(first)
        first_t = toks(claims[first])
        later_only = set()
        for cid in order[i + 1:]:
            later_only |= toks(claims[cid])
        later_only -= first_t
        q = toks(log[0]["query"])
        if not (q & first_t):
            errs.append(f"query {log[0]['query']!r} shares no term with the first unsupported claim {first}")
        if q & later_only:
            errs.append(f"query reaches into later claims via {sorted(q & later_only)}")
    for e in errs:
        print("FAIL:", e)
    print("OK" if not errs else f"{len(errs)} assertion(s) failed")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
