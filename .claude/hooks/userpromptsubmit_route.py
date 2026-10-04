#!/usr/bin/env python3
"""UserPromptSubmit: tell the model which connectors, plugins and skills fit this prompt, with the exact tool-load call.

Advisory and fail-open: it never blocks a prompt, never calls a model, and says nothing when nothing matches. The gate stays
the PreToolUse hook; this only decides what to put in front of the model. One code path with `python3 desk/desk.py caps "<prompt>"`.
Routing is logged as ids and a character count only (no prompt text) to trace/route_log.jsonl, which is gitignored.
"""
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "desk"))


def main():
    try:
        d = json.load(sys.stdin)
        import desk  # noqa: E402
        text, res, router = desk.auto_context(d.get("prompt") or "")
    except Exception:
        return 0
    if not text:
        return 0
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": text}}))
    try:
        base = os.environ.get("DESK_TRACE_ROOT", ROOT)
        os.makedirs(os.path.join(base, "trace"), exist_ok=True)
        with open(os.path.join(base, "trace", "route_log.jsonl"), "a") as f:
            f.write(json.dumps({"ts": int(time.time()), "session": d.get("session_id"), "ids": [m["id"] for m in res["matched"]],
                                "router": bool(router), "chars": len(text)}) + "\n")
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
