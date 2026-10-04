---
name: security-review-rank
description: Use when quoted security findings need ordering by a written rubric. Quiet when no rubric or no quoted lines exist, and for exploit work.
---
## Trigger
A list of quoted findings (scanner lines or diff items with file:line) and a written rubric are both present. Quiet when either is missing, or when the ask is to rank code nobody quoted.
## Done-when
check: quote
Precondition, before any row: no written rubric gives "rank: unsupported"; empty input gives "rank: 0 rows".
Check: per row run `python3 -c "import sys;f,n,q=sys.argv[1:4];sys.exit(0 if q in open(f).read().splitlines()[int(n)-1] else 1)" <file> <line> "<quote>"`. Exit 0 keeps the row; non-zero removes it as dropped. Each kept row also names its rubric clause. State rows in = rows out + dropped.
## Rung
rung: L1
One fast-model pass applies the rubric; the python3 substring run is the check. Escalate only if a kept row fails the run.
## Forbidden move
Ranking unquoted code: assigning a severity to a file, function, or pattern that no quoted line supports.
## Tool
tool: Bash:python3
scope: read
