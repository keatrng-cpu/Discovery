#!/usr/bin/env python3
"""PreToolUse: exit 2 blocks. Gates are missing tools; this hook is the backstop, not the gate."""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "desk"))
import gate  # noqa: E402

try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
try:
    reg = gate.load_registry(ROOT)
except Exception:
    reg = {}  # fail closed for MCP tools: an empty registry denies every unregistered mcp__ tool
ok, why = gate.decide(d.get("tool_name", ""), d.get("tool_input", {}), reg)
if not ok:
    print(why, file=sys.stderr)
    sys.exit(2)
sys.exit(0)
