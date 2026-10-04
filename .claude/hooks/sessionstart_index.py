#!/usr/bin/env python3
"""SessionStart: hand the model the capability index once per session (startup, resume, clear, compact).

The index is generated from registry/capabilities.json by `desk.py caps-index --write` and checked for freshness by `desk.py lint`.
Fail-open: a missing or oversized file says nothing rather than blocking the session. No model call.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CAP = 10000  # documented hook cap on additionalContext


def main():
    try:
        sys.stdin.read()
        text = open(os.path.join(ROOT, "registry", "capabilities.index.md")).read()
    except Exception:
        return 0
    if not text.strip() or len(text) > CAP:
        return 0
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": text}}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
