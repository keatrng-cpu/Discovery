---
name: harness-trace
description: Use when an agent action log must be append-only and a tamper attempt must fail. Quiet for memory notes, skill text, hook wiring, or promotion.
---
## Trigger
A log of agent actions is kept as a record of what happened. Quiet when the ask is memory or a summary: a trace is not a note.
## Done-when
check: exit-code
`python3 desk/desk.py verify-trace` exits 0 and prints "chain intact". After a tamper of a record with a successor it exits 1 and names the line. No trace file is a valid result ("0 records"). Tail edit and truncation are not caught by the chain; they are denied by the absent write and delete path below, not checked.
## Rung
rung: L0
A program alone verifies the hash chain. The model never writes the file.
## Forbidden move
Giving the agent a write or delete path to its own trace, or trusting the agent's report that the log is intact.
## Tool
tool: none
scope: none
gate: ABSENT write, delete (the agent holds no write or delete path to its own trace; a person or an external sink owns the file)