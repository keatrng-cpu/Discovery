---
name: strategy-frame
description: Use when a problem needs two competing problem statements that each imply a different action. Quiet for restating the problem or for picking a winner.
---
## Trigger
A problem is given and the ask is to frame it. Quiet when the ask is to rank options, summarise, or pick one statement.
## Done-when
check: count
`python3` over the output prints "statements: 2" and "actions: 2 distinct": exactly two lines starting "P:" each followed by one line starting "Action:", and the two Action lines are not equal after lowercasing and stripping stop words. Exit 0 only then. A source with only one framing is a valid result: print "statements: 1" and exit 1 rather than pad a restatement.
## Rung
rung: L1
A fast model drafts the two statements; code counts them and compares the Action lines. Whether the actions truly differ in practice is a person judgment the string compare only approximates.
## Forbidden move
Writing a restatement: a second statement whose Action line matches the first in substance. Drop it.
## Tool
tool: Bash:python3
scope: read
