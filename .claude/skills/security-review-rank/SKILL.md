---
name: security-review-rank
description: Use when quoted security findings need ordering by a written rubric. Quiet when no rubric or no quoted lines exist, and for exploit work.
---
## Trigger
A list of quoted findings (scanner lines or diff items with file:line) and a written rubric are both present. Quiet when either is missing, or when the ask is to rank code nobody quoted.
## Done-when
check: quote
Every ranked row carries the rubric clause it applies, by id or quoted text, and the quoted source line with `file:line`. A row with no quote is removed, not ranked. If the rubric is absent, the result is "rank: unsupported (no rubric)". An empty input list gives "rank: 0 rows". Row count in equals row count out plus dropped, both stated.
## Rung
rung: L1
One fast-model pass applies the rubric; a program checks that each row's quote is a substring of the input. Escalate only on a failed substring check.
## Forbidden move
Ranking unquoted code: assigning a severity to a file, function, or pattern that no quoted line supports.
## Tool
tool: none
scope: none
