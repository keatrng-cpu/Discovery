---
name: sales-test
description: Use when a sales frame needs the smallest spend or send test and the result that kills it written out. Stops before any send or spend.
---
## Trigger
A frame and a stated budget or audience are present and the ask is to plan a test. Quiet when the ask is to run it: the run is a person's action.
## Done-when
check: schema
Write test.json with {frame, smallest_action, cap, kill_result, gate}. `jq -e '(.smallest_action|length>0) and (.cap|length>0) and (.kill_result|length>0) and (.gate|length>0)' test.json` exits 0. Nothing is sent or spent; the plan stops at the gate.
## Rung
rung: L1
One fast-model pass drafts the plan; jq checks the fields. Whether the kill result is sound needs a person.
## Forbidden move
Opening the gate: sending a message, launching a campaign, or committing spend because the plan is ready.
## Tool
tool: none
scope: none
gate: ABSENT send, pay (prepare the test sheet with smallest spend and kill result, stop; a person sends or spends)
