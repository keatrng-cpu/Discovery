---
name: security-review-rank
description: Use when quoted security findings need ordering by a written rubric. Quiet when no rubric or no quoted lines exist, and for exploit work.
---
## Trigger
A list of quoted findings (scanner lines or diff items with file:line) and a written rubric are both present. Quiet when either is missing, or when the ask is to rank code nobody quoted.
## Done-when
check: quote
Precondition, before any row: no written rubric gives "rank: unsupported"; empty input gives "rank: 0 rows".
Rubric file lines are `clause | pattern | rank`. Each row cites a clause and a rank.
Check: per row run one program `python3 -c "import sys;f,n,q,c,k,r=sys.argv[1:7];L=open(f).read().splitlines()[int(n)-1];R=[[x.strip() for x in l.split('|')] for l in open(r) if l.count('|')==2];sys.exit(0 if q in L and any(a==c and b in q and z==k for a,b,z in R) else 1)" <file> <line> "<quote>" <clause> <rank> <rubric-file>`.
Exit 0 means the quote is in the line and the row's rank equals the cited clause's rank. Non-zero removes the row as dropped, including a rank that ignores or contradicts its clause. State rows in = rows out + dropped.
## Rung
rung: L1
One fast-model pass applies the rubric and cites clauses; the python3 run is the check. Escalate only if a kept row fails the run.
## Forbidden move
Ranking unquoted code: assigning a severity to a file, function, or pattern that no quoted line supports.
## Tool
tool: Bash:python3
scope: read
