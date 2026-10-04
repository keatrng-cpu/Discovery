---
name: strategy-what-if
description: Use when one binding variable is moved and the decision is shown under that move. Quiet for scenario brainstorms or for moving several inputs.
---
## Trigger
A decision with named variables and a request to test a change. Quiet when more than one variable is to move or no decision exists.
## Done-when
check: count
`python3` over the output table prints "moved: 1" and "held: H" where H equals the count of other variables in the base case, and every held cell equals its base value. Exit 0 only if exactly one row is marked "moved" and a "Decision:" line appears for base and moved cases. A second moved variable prints "moved: 2" and exits 1.
## Rung
rung: L1
A fast model fills the table; code compares held cells to the base case and counts moved rows. Drift in held cells is caught as a string diff.
## Forbidden move
Drifting: changing a second variable, or a held value, while showing the moved case.
## Tool
tool: Bash:python3
scope: read
