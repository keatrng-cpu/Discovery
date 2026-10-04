---
name: education-explain
description: Use when a learner asks to be taught one concept with an example. Quiet when the ask covers several concepts, a whole course, or a graded quiz.
---
## Trigger
A learner names one concept and wants it explained. Quiet when two or more concepts are named, or when the ask is to mark, drill, or plan a course.
## Done-when
check: count
Before writing, save the one concept's neighbouring terms to neighbours.txt (model-authored today; a concept-graph or glossary service is absent, so the term search is only as strong as that list). The reply is exactly three non-empty lines, one each starting "Concept:", "Example:", "Question:" (count 1/1/1), with no body text, and the last starts with "Question:" and ends with "?". leaks = (non-empty lines outside those three) + (neighbours.txt terms found anywhere in the reply other than the Concept line). leaks must be 0. "Concept not stated" is a valid result.
## Rung
rung: L1
One fast-model pass writes the reply; a line count and a term search check it. Escalate only if leaks stays above 0 twice.
## Forbidden move
Leaking a second concept: naming, defining, or previewing a neighbouring idea in the Example, the Question, or any extra line. Drop it.
## Tool
tool: none
scope: none
