---
name: writing-series
description: Use when a new piece must follow a standing brand file and match the previous piece. Quiet for a one-off piece with no brand file.
---
## Trigger
A brand file and a previous piece are present. Quiet when no brand file exists; session chat is never the memory.
## Done-when
check: exit-code
`cmp` over the ban list extracted from the brand file and the ban list the new piece declares exits 0, and the previous piece's ban list matches the same file. The draft does not restate the rules. A missing brand file is a valid result: stop and report "brand file absent".
## Rung
rung: L1
One fast-model pass drafts with the brand file loaded; cmp compares the ban lists. Escalate only if cmp exits 1 after one repair.
## Forbidden move
Taking rules from session chat instead of the brand file, or restating the rules inside the draft.
## Tool
tool: Bash:cmp
scope: read
