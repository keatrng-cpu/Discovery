#!/usr/bin/env python3
"""Stop: block 'done' unless every Done-when check in contract.md exits 0 (exit 2 blocks).

The hook re-runs the checks; it never trusts the STATUS line. A failure counter in state.json caps the
block at 3 per red streak so a stuck session cannot loop forever; a forced stop is written to the trace.
"""
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "desk"))
import trace  # noqa: E402

CAP = 3
TRACE_ROOT = os.environ.get("DESK_TRACE_ROOT", ROOT)
try:
    d = json.load(sys.stdin)
except Exception:
    d = {}
cwd = d.get("cwd") or os.getcwd()
contract = os.path.join(cwd, "contract.md")
sp = os.path.join(cwd, "state.json")


def state():
    try:
        with open(sp) as f:
            return json.load(f)
    except Exception:
        return {}


def save(st):
    with open(sp, "w") as f:
        json.dump(st, f, indent=1)
        f.write("\n")


if not os.path.exists(contract):
    print("contract.md is missing: write the contract (shelf, directive, check, gate, rung, token cap) before done.", file=sys.stderr)
    sys.exit(2)
r = subprocess.run([sys.executable, os.path.join(ROOT, "desk", "desk.py"), "contract-check", contract],
                   capture_output=True, text=True, cwd=cwd)
st = state()
if r.returncode == 0:
    if st.get("stop_blocks"):
        st["stop_blocks"] = 0
        save(st)
    sys.exit(0)
n = int(st.get("stop_blocks", 0))
if n >= CAP:
    try:
        trace.append(TRACE_ROOT, {"ts": "", "tool": "STOP-FORCED", "in": "", "err": True, "session": str(d.get("session_id", ""))[:12]})
    except Exception:
        pass
    print(f"contract.md is still RED after {CAP} blocks; allowing stop. This is recorded in the trace as STOP-FORCED.", file=sys.stderr)
    sys.exit(0)
st["stop_blocks"] = n + 1
save(st)
print(f"BLOCKED ({n + 1}/{CAP}): contract.md is not green.\n" + r.stdout[-1500:], file=sys.stderr)
sys.exit(2)
