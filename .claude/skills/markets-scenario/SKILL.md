---
name: markets-scenario
description: Use when a thesis must be shown under a move in exactly one variable with every other input pinned. Quiet for multi-variable what-ifs, orders, or position sizing.
---
## Trigger
A baseline input set and a named variable to move. Quiet when two variables are named, or when the ask is to place risk.
## Done-when
check: state-diff
A diff of baseline inputs versus scenario inputs shows exactly one changed key; all other keys are byte-equal. The output shows the thesis under that move and stops. A move that leaves the thesis unchanged is a valid result.
## Rung
rung: L1
Code diffs the input sets; one fast-model pass writes the thesis under the move. Escalate only if the diff shows more than one changed key.
## Forbidden move
Moving two variables, or continuing past the one requested variable. No order, no size.
## Tool
tool: Bash:python3
scope: read
