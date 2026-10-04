---
name: strategy-frame
description: Use when a problem needs two competing problem statements that each imply a different action. Quiet for restating the problem or for picking a winner.
---
## Trigger
A problem is given and the ask is to frame it. Quiet when the ask is to rank options, summarise, or pick one statement.
## Done-when
check: count
`python3` over the output prints "statements: 2" and "actions: 2 distinct": exactly two lines starting "P:" each followed by one line starting "Action:". After lowercasing and removing stop words, the two Action lines must have different leading verbs and a content-word overlap (Jaccard) of at most 0.34, and the two P: lines must also overlap at most 0.6; otherwise it prints "restatement" and exits 1. Exit 0 only then. A source with only one framing is a valid result: print "statements: 1" and exit 1 rather than pad a restatement. The program only rejects near-restatements; whether the actions differ in practice stays a person review.
## Rung
rung: L1
A fast model drafts the two statements; code counts them and rejects near-restatements by verb and content-word overlap. The substance of "different action" remains a person judgment the program only approximates.
## Forbidden move
Writing a restatement: a second statement whose Action line matches the first in substance. Drop it.
## Tool
tool: Bash:python3
scope: read
