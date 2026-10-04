---
name: harness-evolve
description: Use when proposing one change to a harness piece and deciding whether it earns promotion on a held-out task with a token count. Quiet for authoring a first skill or hook.
---
## Trigger
A single harness piece (skill, hook, memory, CLAUDE.md line) was changed and a baseline exists. Quiet when nothing was changed or when two pieces changed at once: split it.
## Done-when
check: exit-code
`python3 desk/desk.py promote-gate <json>` prints "PROMOTE" and exits 0 only when heldout_pass is true, tune_pass is true, and tokens or seconds dropped. No held-out result prints "HOLD" and exits 1; HOLD is a valid result. The output is a recommendation; a person promotes.
## Rung
rung: L0
A program alone reads the result JSON. Publish the token count with it.
## Forbidden move
Promoting on a gain seen only on the tuning set, or the agent promoting its own change.
## Tool
tool: none
scope: none
gate: ABSENT promote (prepare the change, held-out result and token count, stop; a person promotes)
