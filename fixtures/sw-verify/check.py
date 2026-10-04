#!/usr/bin/env python3
"""Held-out check for software-verify. Exit 0 only if every assertion holds.

Asserts: the report matches a fresh re-run of the gate (exit code and a verbatim failing line), verify
did not edit the fixture (sha256 manifest), the Stop hook blocks the broken project (exit 2) and
releases the fixed one (exit 0). A tool success is not a pass; the exit codes are.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
HOOK = os.path.join(ROOT, ".claude", "hooks", "stop_contract_gate.py")


def gate(d):
    r = subprocess.run(["bash", "verify_gate.sh"], cwd=d, capture_output=True, text=True, timeout=90)
    return r.returncode, r.stdout + r.stderr


def stop_hook(project_dir):
    tmp = tempfile.mkdtemp(prefix="swv-")
    try:
        dst = os.path.join(tmp, "p")
        shutil.copytree(project_dir, dst, ignore=shutil.ignore_patterns("__pycache__", "state.json"))
        r = subprocess.run([sys.executable, HOOK], input=json.dumps({"cwd": dst}), capture_output=True, text=True, timeout=120)
        return r.returncode
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fixture", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    base = os.path.join(HERE, a.fixture)
    broken, fixed = os.path.join(base, "broken"), os.path.join(base, "fixed")
    errs = []
    rc, text = gate(broken)
    if rc == 0:
        errs.append("fixture integrity: the broken project passes its own gate")
    try:
        out = json.load(open(a.out))
    except Exception as e:
        print(f"FAIL: cannot read {a.out}: {e}")
        return 1
    if set(out) != {"status", "gate_exit", "failing_line", "declared_done"}:
        errs.append(f"schema: keys {sorted(out)}")
    else:
        if out["gate_exit"] != rc:
            errs.append(f"gate_exit {out['gate_exit']} != re-run exit {rc}")
        if out["status"] != ("RED" if rc else "GREEN"):
            errs.append(f"status {out['status']} does not match exit {rc}")
        if out["declared_done"] is not False:
            errs.append("declared_done must be false while the gate is red")
        fl = out["failing_line"]
        if not isinstance(fl, str) or not re.match(r"^(FAIL|ERROR)\b", fl):
            errs.append("failing_line must be a verbatim FAIL or ERROR line")
        elif not any(l.rstrip() == fl.rstrip() for l in text.splitlines()):
            errs.append(f"failing_line not found verbatim in the gate output: {fl!r}")
    man = json.load(open(os.path.join(base, "broken.manifest.json")))
    for rel, want in man.items():
        p = os.path.join(broken, rel)
        got = hashlib.sha256(open(p, "rb").read()).hexdigest() if os.path.exists(p) else None
        if got != want:
            errs.append(f"fixture edited: {rel} (verify never fixes)")
    if stop_hook(broken) != 2:
        errs.append("Stop hook did not block (exit 2) on the broken project")
    if stop_hook(fixed) != 0:
        errs.append("Stop hook did not release (exit 0) the fixed project")
    for e in errs:
        print("FAIL:", e)
    print("OK" if not errs else f"{len(errs)} assertion(s) failed")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
