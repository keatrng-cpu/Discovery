---
name: education-explain
description: Use when a learner asks to be taught one concept with an example. Quiet when the ask covers several concepts, a whole course, or a graded quiz.
---
## Trigger
A learner names one concept and wants it explained. Quiet when two or more concepts are named, or when the ask is to mark, drill, or plan a course.
## Done-when
check: count
The reply carries exactly one line each starting "Concept:", "Example:", "Question:" (count 1/1/1), and the last non-empty line starts with "Question:" and ends with "?". Any other "Concept:" line, or a second "Example:" line, fails the count. A reply that says "concept not stated" instead of inventing one is a valid result.
## Rung
rung: L1
One fast-model pass writes the reply; a line count checks it. Escalate only if the count fails twice.
## Forbidden move
Leaking a second concept: naming, defining, or previewing a neighbouring idea inside the explanation. Park it in one line "later: <name>" outside the count, or drop it.
## Tool
tool: none
scope: none
