---
name: scientific-hypothesis
description: Use when a research idea must become a hypothesis record naming a measurement, a direction of change, and a control. Quiet for experiment steps or for analyzing results.
---
## Trigger
A research question or literature gap is stated and a hypothesis is wanted. Quiet when steps, reagents, or a protocol are the ask (that is design), and quiet when a result file is the input (that is update).
## Done-when
check: schema
`jq -e` over the hypothesis record passes: non-empty fields measurement, direction (increase, decrease, or no-change), and control. Otherwise the record must carry status "rejected-not-runnable" with a reason string; that is a valid result and exits 0. A record with a field missing and no rejection status fails.
## Rung
rung: L1
One fast-model pass drafts the record; jq checks the fields. Escalate only on a schema failure, not on doubt about novelty.
## Forbidden move
Keeping a hypothesis that cannot be run: a vague measurement ("improves outcomes"), no direction, or no control, passed off as runnable instead of rejected.
## Tool
tool: Bash:jq
scope: read
