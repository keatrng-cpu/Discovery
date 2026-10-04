#!/usr/bin/env python3
"""Hook tests: feed real hook JSON to the real hook scripts and assert exit codes.

usage: test_hooks.py [stop|deny|trace|route|all]      exit 0 only if every case behaves as written.
Traces from tests go to a temp DESK_TRACE_ROOT so the evidence trace is never polluted.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

ROOT =os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
H = os.path.join(ROOT, ".claude", "hooks")
PY = sys.executable
TMP = tempfile.mkdtemp(prefix="hooks-")
ENV = dict(os.environ, DESK_TRACE_ROOT=os.path.join(TMP, "traceroot"))
FAILS = []
N = [0]
TRACE_REL = os.path.join("trace", "trace.jsonl")


def run(script, payload, env=ENV, raw=None):
    r = subprocess.run([PY, os.path.join(H, script)], input=raw if raw is not None else json.dumps(payload), capture_output=True, text=True, env=env, timeout=240)
    run.stdout = r.stdout
    return r.returncode, r.stderr


def expect(name, want, got, note=""):
    ok = want == got
    print(f"{'PASS' if ok else 'FAIL'} {name}: got {got!r} (want {want!r}) {note if not ok else ''}".rstrip())
    if not ok:
        FAILS.append(name)


def pre(name, tool, tin, want):
    rc, err = run("pretooluse_gate_deny.py", {"hook_event_name": "PreToolUse", "tool_name": tool, "tool_input": tin})
    expect(name, want, rc, err.strip()[:120])


def copy(src):
    N[0] += 1
    dst = os.path.join(TMP, f"proj{N[0]}")
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__", "state.json"))
    return dst


def stop():
    base = os.path.join(ROOT, "fixtures", "sw-verify", "tune")
    stop_in = lambda cwd: run("stop_contract_gate.py", {"hook_event_name": "Stop", "cwd": cwd})
    rc, err = stop_in(copy(os.path.join(base, "broken")))
    expect("stop_red: a verify task with a failing test is blocked", 2, rc, err.strip()[:160])
    rc, _ = stop_in(copy(os.path.join(base, "fixed")))
    expect("stop_green: a clean verify is released", 0, rc)
    rc, _ = stop_in(tempfile.mkdtemp(dir=TMP))
    expect("stop_no_contract: a missing contract.md is blocked", 2, rc)
    red = copy(os.path.join(base, "broken"))
    codes = [stop_in(red)[0] for _ in range(4)]
    expect("stop_cap: blocked 3 times, then forced on the 4th", [2, 2, 2, 0], codes)
    tp = os.path.join(ENV["DESK_TRACE_ROOT"], TRACE_REL)
    expect("stop_cap: the forced stop is written to the trace", True, os.path.exists(tp) and "STOP-FORCED" in open(tp).read())


def deny():
    pre("deny_send: Gmail send_message", "mcp__Gmail__send_message", {"to": "a@b.c"}, 2)
    pre("deny_order: broker place_order", "mcp__broker__place_order", {"symbol": "X", "qty": 1}, 2)
    pre("deny_pay: Vercel buy_domain", "mcp__Vercel__buy_domain", {}, 2)
    pre("deny_act_unadded: github merge_pull_request", "mcp__github__merge_pull_request", {}, 2)
    pre("deny_unregistered: unknown MCP tool", "mcp__Unknown__list_things", {}, 2)
    pre("deny_sendmail: Bash sendmail", "Bash", {"command": "echo hi | sendmail -t a@b.c"}, 2)
    pre("deny_sendmail_wrapped: Bash sudo mail", "Bash", {"command": "cd /tmp && sudo mail -s x a@b.c"}, 2)
    pre("allow_read: github get_file_contents", "mcp__github__get_file_contents", {}, 0)
    pre("allow_draft: Gmail create_draft", "mcp__Gmail__create_draft", {}, 0)
    pre("allow_human_added_act: github create_pull_request", "mcp__github__create_pull_request", {}, 0)
    pre("allow_heredoc_words: a data heredoc that says send, order, pay, sign", "Bash", {"command": "cat > f.md <<'EOT'\nsend the order and pay then sign\nEOT"}, 0)
    pre("allow_builtin_read", "Read", {"file_path": "/etc/hostname"}, 0)
    pre("deny_trace_write_tool: Write to the trace", "Write", {"file_path": os.path.join(ROOT, TRACE_REL), "content": ""}, 2)
    pre("deny_trace_rm: Bash rm of the trace", "Bash", {"command": "rm -f " + TRACE_REL}, 2)
    pre("deny_trace_truncate: Bash redirect over the trace", "Bash", {"command": ": > " + TRACE_REL}, 2)
    pre("deny_trace_sed: Bash sed -i on the trace", "Bash", {"command": "sed -i '1d' " + TRACE_REL}, 2)
    pre("allow_trace_read: Bash cat | tail", "Bash", {"command": "cat " + TRACE_REL + " | tail -3"}, 0)
    pre("allow_trace_verify: Bash verify-trace", "Bash", {"command": "python3 desk/desk.py verify-trace"}, 0)


def tr():
    d = os.path.join(TMP, "tr")
    env = dict(ENV, DESK_TRACE_ROOT=d)
    for i in range(3):
        rc, _ = run("posttooluse_trace.py", {"tool_name": f"Tool{i}", "tool_input": {"i": i}, "tool_response": {}, "session_id": "s"}, env)
        expect(f"trace_append_{i}", 0, rc)
    sys.path.insert(0, os.path.join(ROOT, "desk"))
    import trace
    ok, msg = trace.verify(d)
    expect("trace_verify_clean", True, ok, msg)
    p = os.path.join(d, TRACE_REL)
    lines = open(p).read().splitlines()
    open(p, "w").write("\n".join([lines[0], lines[1].replace("Tool1", "ToolX"), lines[2]]) + "\n")
    expect("trace_tamper_edit_fails", False, trace.verify(d)[0])
    open(p, "w").write("\n".join([lines[0], lines[2]]) + "\n")
    expect("trace_tamper_delete_fails", False, trace.verify(d)[0])
    open(p, "w").write("\n".join([lines[1], lines[0], lines[2]]) + "\n")
    expect("trace_tamper_reorder_fails", False, trace.verify(d)[0])


def route():
    sys.path.insert(0, os.path.join(ROOT, "desk"))
    import caps
    cmap = caps.load_caps(ROOT)
    never = {t for c in cmap["capabilities"] for t in c.get("never_auto", [])}

    def ups(prompt, env=ENV, raw=None):
        t0 = time.time()
        rc, _ = run("userpromptsubmit_route.py", {"hook_event_name": "UserPromptSubmit", "session_id": "t", "prompt": prompt}, env, raw)
        return rc, run.stdout, time.time() - t0

    rc, out, secs = ups("pull keyword volume and difficulty for junk removal grand forks")
    j = json.loads(out) if out.strip() else {}
    ctx = j.get("hookSpecificOutput", {}).get("additionalContext", "")
    expect("route_match_exit0", 0, rc)
    expect("route_match_event_name", "UserPromptSubmit", j.get("hookSpecificOutput", {}).get("hookEventName"))
    expect("route_match_names_the_exact_load_call", True, "select:mcp__Semrush__keyword_research" in ctx)
    expect("route_match_leaks_no_act_tool", False, any(t in ctx for t in never))
    expect("route_match_states_the_gate", True, "stay gated" in ctx or "prepare the details and stop" in ctx)
    expect("route_match_is_fast", True, secs < 3, f"{secs:.2f}s")
    expect("route_match_under_hook_cap", True, len(ctx) < 10000, str(len(ctx)))
    rc, out, _ = ups("thanks, that makes sense")
    expect("route_chitchat_silent", (0, ""), (rc, out.strip()))
    rc, out, _ = ups("", raw="{not json")
    expect("route_bad_stdin_fail_open", (0, ""), (rc, out.strip()))
    rc, out, _ = ups("")
    expect("route_empty_prompt_silent", (0, ""), (rc, out.strip()))
    rc, out, _ = ups("what's our revenue this month, but do it without using any connectors")
    expect("route_off_switch_silent", (0, ""), (rc, out.strip()))
    rc, out, _ = ups("send the invoice to the landlord and show revenue this month")
    gv = json.loads(out)["hookSpecificOutput"]["additionalContext"] if out.strip() else ""
    expect("route_gate_verb_called_out", True, "Gate verbs in this prompt (send)" in gv)
    log = os.path.join(ENV["DESK_TRACE_ROOT"], "trace", "route_log.jsonl")
    lines = open(log).read().splitlines() if os.path.exists(log) else []
    expect("route_log_ids_only_no_prompt_text", True, bool(lines) and all("prompt" not in json.loads(x) for x in lines))
    rc, out, _ = ups("a" * 20000)
    expect("route_long_junk_prompt_fast_and_silent", (0, ""), (rc, out.strip()))
    # session start index
    rc, _ = run("sessionstart_index.py", {"hook_event_name": "SessionStart", "source": "startup"})
    j = json.loads(run.stdout)
    expect("sessionstart_exit0", 0, rc)
    expect("sessionstart_event_name", "SessionStart", j["hookSpecificOutput"]["hookEventName"])
    expect("sessionstart_is_the_generated_index", True, open(os.path.join(ROOT, caps.INDEX_REL)).read() == j["hookSpecificOutput"]["additionalContext"])
    expect("sessionstart_under_hook_cap", True, len(j["hookSpecificOutput"]["additionalContext"]) <= 10000)


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("route", "all"):
        route()
    if which in ("stop", "all"):
        stop()
    if which in ("deny", "all"):
        deny()
    if which in ("trace", "all"):
        tr()
    shutil.rmtree(TMP, ignore_errors=True)
    print("ALL PASS" if not FAILS else f"{len(FAILS)} FAILED: {FAILS}")
    sys.exit(1 if FAILS else 0)
