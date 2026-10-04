---
name: education-sequence
description: Use when a learner asks what to learn next and the answer must be the smallest gap plus one next step. Quiet for full course plans.
---
## Trigger
A learner's current state is given (a quiz result, a stated stuck point) and the ask is what comes next. Quiet when the ask is for the whole path or an order of topics.
## Done-when
check: count
The whole reply is exactly two non-empty lines: one starting "gap:" and one starting "next:" (count 1/1, total non-empty lines 2), each at most 160 characters, and the "next:" line contains no ";", no numeral-with-period or bullet marker, and none of "then", "after that", "finally", "step 2" (so a prose course dump fails). "gap: none found" with "next: none" is valid when evidence shows no gap. No stated state means "gap: unsupported".
## Rung
rung: L1
One fast-model pass names the gap; a line and pattern count checks it. Escalate only if the count fails twice.
## Forbidden move
Laying out the whole course: any list of steps, in list or prose form, beyond the single next one.
## Tool
tool: none
scope: none
