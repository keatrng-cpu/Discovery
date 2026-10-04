---
name: strategy-constrain
description: Use when options must be ranked by time and money with a reason the runner-up lost. Quiet for brainstorming new options or for ranking by taste.
---
## Trigger
A closed list of options plus a time and money budget. Quiet when the options are not yet listed or the ask is to generate more.
## Done-when
check: count
`python3` compares the output to the input option list and prints "rank: N/N" and "new: 0". Each option has a "time:" and "money:" value, the order is ascending by time then money, and a line starting "Runner-up lost:" names the second option with a reason quoting its time or money. Exit 0 only if every ranked name is in the input list (a name outside the list prints "new: 1" and exits 1). A list with fewer than two options prints "rank: 1/1" with no runner-up and is valid.
## Rung
rung: L1
A fast model ranks; code diffs names against the input and checks ordering. Whether the reason is sound is not checked.
## Forbidden move
Adding a new idea: any option in the ranking that was not in the input list.
## Tool
tool: Bash:python3
scope: read
