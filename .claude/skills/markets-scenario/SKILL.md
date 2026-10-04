---
name: markets-scenario
description: Use when a thesis must be shown under a move in exactly one variable with every other input pinned. Quiet for multi-variable what-ifs, orders, or position sizing.
---
## Trigger
A baseline input set and a named variable to move. Quiet when two variables are named, or when the ask is to place risk.
## Done-when
check: state-diff
One command, one exit code: `python3 desk/scenario_check.py <baseline.json> <scenario.json> <out.md> <variable>` (a program the desk would run; it does not exist in the repo yet). Each assertion is one clause:
- Move one: the diff of baseline versus scenario shows exactly one changed key, the named variable.
- Hold fixed: every other key is byte-equal.
- Show thesis: out.md holds one line starting "THESIS under <variable>:" that states the thesis under that move.
- Stop: out.md holds no second thesis line and names no other variable as moved.
A thesis line that says the thesis is unchanged is a valid result.
## Rung
rung: L1
Code diffs the input sets; one fast-model pass writes the thesis under the move. Escalate only if the diff shows more than one changed key.
## Forbidden move
Moving two variables, or continuing past the one requested variable. No order, no size.
## Tool
tool: none
scope: none
gate: ABSENT broker, order (show the thesis under one move, stop; a person places any order or size)
