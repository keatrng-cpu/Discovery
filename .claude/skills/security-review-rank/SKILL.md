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
Check: one command with one exit code per row, `python3 -c "import sys;f,n,q,c,k,r=sys.argv[1:7];L=open(f).read().splitlines()[int(n)-1];R=[[x.strip() for x in l.split('|')] for l in open(r) if l.count('|')==2];sys.exit(0 if q in L and any(a==c and b in q and z==k for a,b,z in R) else 1)" <file> <line> "<quote>" <clause> <rank> <rubric-file>`. Inputs are the source file, line number, quote, cited clause, row rank, and rubric file.
Assertions: the quote is a substring of line <line> of <file>; the cited clause exists in the rubric with its pattern inside the quote; the rubric rank equals the row's rank.
Exit 0 keeps the row. Non-zero removes it as dropped. State rows in = rows out + dropped. This command is not a repo program yet, so the desk would run it as written; it is not claimed runnable.
## Rung
rung: L0
A program alone: the rubric maps clause to rank, so the python3 run assigns and checks the rank. No model pass. Escalate only if the command errors.
## Forbidden move
Ranking unquoted code: assigning a severity to a file, function, or pattern that no quoted line supports.
## Tool
tool: Bash:python3
scope: read
