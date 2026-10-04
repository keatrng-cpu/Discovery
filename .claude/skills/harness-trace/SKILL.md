---
name: harness-trace
description: Use when an agent action log must be append-only and a tamper attempt must fail. Quiet for memory notes, skill text, hook wiring, or promotion.
---
## Trigger
A log of agent actions is kept as a record of what happened. Quiet when the ask is memory or a summary: a trace is not a note.
## Done-when
check: exit-code
`python3 .claude/hooks/test_hooks.py deny` exits 0. It runs desk/gate.py through the PreToolUse hook: a Write to the trace file, a Bash rm, a truncating redirect and a sed -i on it each exit 2, while cat, tail and `python3 desk/desk.py verify-trace` exit 0. The agent's tamper and delete attempts fail. Separate detector: verify-trace exits 1 naming the line after a mid-file edit. Not covered: tail edit, truncation, and a write by a route the patterns miss; those need chattr +a or a remote write-once sink, both absent.
## Rung
rung: L0
A program alone: hook exit codes, then the hash chain. The model never writes the file.
## Forbidden move
Giving the agent a write or delete path to its own trace, or trusting the agent's report that the log is intact.
## Tool
tool: none
scope: none
gate: ABSENT write, delete (the agent holds no write or delete path to its own trace: the PreToolUse hook denies them; a person or an external sink owns the file)
