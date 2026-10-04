---
name: education-sequence
description: Use when a learner asks what to learn next and the answer must be the smallest gap plus one next step. Quiet for full course plans.
---
## Trigger
A learner's current state is given (a quiz result, a stated stuck point) and the ask is what comes next. Quiet when the ask is for the whole path or an order of topics.
## Done-when
check: count
The reply has exactly one line starting "gap:" and exactly one line starting "next:" (count 1/1), and no numbered or bulleted list of further steps. "gap: none found" with "next: none" is a valid result when the evidence shows no gap. No stated state means "gap: unsupported".
## Rung
rung: L1
One fast-model pass names the gap; a line count checks it. Escalate only if the count fails twice.
## Forbidden move
Laying out the whole course: any list of steps beyond the single next one.
## Tool
tool: none
scope: none
