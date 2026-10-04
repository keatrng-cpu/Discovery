---
name: sales-question
description: Use when a gap in sales results or cluster evidence needs falsifiable questions about what would explain it. Quiet for answering, researching, or testing them.
---
## Trigger
A gap is stated (low conversion, a silent segment, a split in quotes) and the ask is to generate explanatory questions. Quiet when the ask is to answer them, run an interview, or plan a test.
## Done-when
check: schema
Write questions.json as a list of {question, refuted_if}. `jq -e 'all(.[]; (.question|endswith("?")) and (.refuted_if|length>0) and (has("answer")|not))' questions.json` exits 0. An empty list is valid when no gap is stated.
## Rung
rung: L1
One fast-model pass writes questions; jq enforces the shape. The no-answer rule is the block that holds.
## Forbidden move
Answering the question in the same directive, in an "answer", "likely", or "because" field or in prose beside it.
## Tool
tool: Bash:jq
scope: read
