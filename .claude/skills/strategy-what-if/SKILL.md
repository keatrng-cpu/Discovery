---
name: strategy-what-if
description: Use when one binding variable is moved and the decision is shown under that move. Quiet for scenario brainstorms or for moving several inputs.
---
## Trigger
A decision with named variables and a request to test a change. Quiet when more than one variable is to move or no decision exists.
## Done-when
check: count
`python3` over the input and output table first reads the input line "Binding: <variable>" naming the binding variable; if none is named it prints "binding: none named" and exits 1 (valid result, no move is made). Otherwise it prints "moved: 1", "held: H" and "binding: ok" where H equals the count of other variables in the base case, the single row marked "moved" is the named binding variable, and every held cell equals its base value. A moved row that is not the binding variable prints "binding: mismatch" and exits 1. Exit 0 only if exactly one row is moved and a "Decision:" line appears for base and moved cases. A second moved variable prints "moved: 2" and exits 1.
## Rung
rung: L1
A fast model fills the table; code checks the moved row is the named binding variable, compares held cells to base, and counts moved rows.
## Forbidden move
Drifting: changing a second variable, or a held value, while showing the moved case.
## Tool
tool: Bash:python3
scope: read
