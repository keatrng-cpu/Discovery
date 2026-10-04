---
name: harness-evolve
description: Use when proposing one change to a harness piece and deciding whether it earns promotion on a held-out task with a token count. Quiet for authoring a first skill or hook.
---
## Trigger
A single harness piece (skill, hook, memory, CLAUDE.md line) was changed and a baseline exists. Quiet when nothing was changed. If two pieces changed, it is two evolve runs: split it and run one change per json.
## Done-when
check: exit-code
`python3 desk/desk.py promote-gate <json>` exits 0 printing "PROMOTE" only if candidate.heldout_pass and candidate.tune_pass are true and candidate.tokens is less than baseline.tokens, both counts present in the json and published with the result. A json lacking either token count is unsupported, not PROMOTE. HOLD (exit 1) is valid. A person promotes.
## Rung
rung: L0
A program alone reads the result JSON. Producing heldout_pass needs a held-out runner with a token meter, which is absent; a person supplies that result.
## Forbidden move
Promoting on a gain seen only on the tuning set, or the agent promoting its own change.
## Tool
tool: none
scope: none
gate: ABSENT promote (prepare the change, held-out result and token count, stop; a person promotes)
