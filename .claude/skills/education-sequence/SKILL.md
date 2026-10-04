---
name: education-sequence
description: Use when a learner asks what to learn next and the answer must be the smallest gap plus one next step. Quiet for full course plans.
---
## Trigger
A learner's current state is given (a quiz result, a stated stuck point) and the ask is what comes next. Quiet when the ask is for the whole path or an order of topics.
## Done-when
check: count
One command, python3 desk/check_sequence.py state.txt reply.txt, gives one exit code and does not exist yet. It asserts the reply is exactly two non-empty lines, one starting 'gap:' and one starting 'next:' (count 1/1), each at most 160 characters. It asserts the gap line names exactly one item that appears verbatim in state.txt as a miss or stuck point and has no ';' or list marker, and the 'next:' line has no ';', no numeral-with-period or bullet marker, and none of 'then', 'after that', 'finally', 'step 2'. 'gap: none found' with 'next: none' passes only when state.txt records no miss; an absent state.txt requires 'gap: unsupported'. That the gap is the smallest is not verified by the program (no prerequisite graph) and stays a model judgment.
## Rung
rung: L1
One fast-model pass names the gap; a line and pattern count checks it. Escalate only if the count fails twice.
## Forbidden move
Laying out the whole course: any list of steps, in list or prose form, beyond the single next one.
## Tool
tool: none
scope: none
