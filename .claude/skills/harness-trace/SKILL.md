---
name: harness-trace
description: Use when an agent action log must be append-only and a tamper attempt must fail. Quiet for memory notes, skill text, hook wiring, or promotion.
---
## Trigger
A log of agent actions is kept as a record of what happened. Quiet when the ask is memory or a summary: a trace is not a note.
## Done-when
check: exit-code
`python3 desk/desk.py trace-tamper-check --anchor <anchor.json>` exits 0 only if: the PreToolUse hook (desk/gate.py) exits 2 on a Write to the trace file, a Bash rm, a truncating redirect and a sed -i, and exits 0 on cat and tail (the agent holds no write or delete on its own record); the hash chain verifies; the record count and last-record hash equal the anchor a person holds outside the agent's reach, so a mid-file edit, a tail edit and a truncation each exit 1. A missing anchor is unsupported, not a pass. The subcommand does not exist yet, so the check is not runnable today; test_hooks.py deny and verify-trace cover only the hook and chain parts.
## Rung
rung: L0
A program alone: hook exit codes, then the hash chain. The model never writes the file.
## Forbidden move
Giving the agent a write or delete path to its own trace, or trusting the agent's report that the log is intact.
## Tool
tool: none
scope: none
gate: ABSENT write-once log sink, chattr +a (the agent holds Bash, so the hook is only a pattern deny and not an absent tool; prepare the log, chain and anchor, stop; a person sets the attribute or sink)
