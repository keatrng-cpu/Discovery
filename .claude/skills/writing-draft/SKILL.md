---
name: writing-draft
description: Use when an outline and a voice file are both present and prose is wanted. Quiet when either is missing or the ask is to shorten.
---
## Trigger
An outline file and a voice file are both present. Quiet when only one exists, or when the ask is cutting, channel change, or fact-checking.
## Done-when
check: count
`python3` over the draft and outline exits 0 and prints "paragraphs: N/N mapped": each paragraph carries one outline claim id, every id appears once, and no paragraph is unmapped. An unmapped paragraph is a new claim and fails. The check is the claim mapping only; banned-default scanning is a separate check.
## Rung
rung: L1
One fast-model pass writes the paragraphs under the voice file; a program counts the mapping. Escalate only if the mapping fails twice.
## Forbidden move
Adding a claim that is not in the outline, to fill a paragraph or smooth a transition.
## Tool
tool: Bash:python3
scope: read
