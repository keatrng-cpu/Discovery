---
name: scientific-update
description: Use when an assay result forces a revision of an existing hypothesis: cite the result, drop the failed branch, keep the rest, propose one next measurement.
---
## Trigger
An old hypothesis record and a result file are both present. Quiet when there is no result file yet (nothing forces a change) or when a new hypothesis from scratch is wanted.
## Done-when
check: quote
Each cited result is quoted verbatim from the result file with a file and line locator, and a program confirms the quote at that locator. The updated record lists the dropped branch and the kept branches. It proposes exactly one next measurement. A result file that does not contain the claimed line fails; "no change forced" is a valid result.
## Rung
rung: L1
One fast-model pass rewrites the record; a program resolves each quote locator. Escalate only on a failed quote.
## Forbidden move
Keeping a dead branch in the hypothesis because it was the old one, or citing a result that is not in the file, or proposing more than the next measurement.
## Tool
tool: Bash:python3
scope: read
