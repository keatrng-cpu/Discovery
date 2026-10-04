#!/usr/bin/env python3
"""PostToolUse: append one hash-chained record to trace/trace.jsonl. Append only; nothing here deletes."""
import hashlib
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "desk"))
import trace  # noqa: E402

try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
resp = d.get("tool_response")
err = bool(isinstance(resp, dict) and (resp.get("is_error") or resp.get("error")))
rec = {
    "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "tool": d.get("tool_name", ""),
    "in": hashlib.sha256(json.dumps(d.get("tool_input", {}), sort_keys=True).encode()).hexdigest()[:16],
    "err": err,
    "session": str(d.get("session_id", ""))[:12],
}
try:
    trace.append(os.environ.get("DESK_TRACE_ROOT", ROOT), rec)
except Exception as e:  # a trace failure must be visible, not silent
    print(f"trace append failed: {e}", file=sys.stderr)
sys.exit(0)
