---
name: markets-scenario
description: Use when a thesis must be shown under a move in exactly one variable with every other input pinned. Quiet for multi-variable what-ifs, orders, or position sizing.
---
## Trigger
A baseline input set and a named variable to move. Quiet when two variables are named, or when the ask is to place risk.
## Done-when
check: state-diff
A diff of baseline inputs versus scenario inputs shows exactly one changed key, the named variable; all other keys are byte-equal. Two or more changed keys fails.
Not part of the check, but required of the output: the thesis shown under that move, then stop. A move that leaves the thesis unchanged is a valid result.
## Rung
rung: L1
Code diffs the input sets; one fast-model pass writes the thesis under the move. Escalate only if the diff shows more than one changed key.
## Forbidden move
Moving two variables, or continuing past the one requested variable. No order, no size.
## Tool
tool: none
scope: none
gate: ABSENT broker, order (show the thesis under one move, stop; a person places any order or size)
