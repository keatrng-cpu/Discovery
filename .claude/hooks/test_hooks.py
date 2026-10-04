#!/usr/bin/env python3
"""Hook tests: feed real hook JSON to the real hook scripts and assert exit codes.

usage: test_hooks.py [stop|deny|trace|all]      exit 0 only if every case behaves as written.
Traces from tests go to a temp DESK_TRACE_ROOT so the evidence trace is never polluted.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
H = os.path.join(ROOT, ".claude", "hooks")
PY = sys.executable
TMP = tempfile.mkdtemp(prefix="hooks-")
ENV = dict(os.environ, DESK_TRACE_ROOT=os.path.join(TMP, "traceroot"))
FAILS = []
N = [0]
TRACE_REL = os.path.join("trace", "trace.jsonl")


def run(script, payload, env=ENV):
    r = subprocess.run([PY, os.path.join(H, script)], input=json.dumps(payload), capture_output=True, text=True, env=env, timeout=240)
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


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("stop", "all"):
        stop()
    if which in ("deny", "all"):
        deny()
    if which in ("trace", "all"):
        tr()
    shutil.rmtree(TMP, ignore_errors=True)
    print("ALL PASS" if not FAILS else f"{len(FAILS)} FAILED: {FAILS}")
    sys.exit(1 if FAILS else 0)
