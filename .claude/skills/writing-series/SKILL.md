---
name: writing-series
description: Use when a new piece must follow a standing brand file and match the previous piece. Quiet for a one-off piece with no brand file.
---
## Trigger
A brand file and a previous piece are present. Quiet when no brand file exists; session chat is never the memory.
## Done-when
check: exit-code
`cmp` over two files exits 0: bans.expected (the ban lines read from the brand file's "Bans" heading) and bans.kept (the same lines minus any whose phrase occurs in the new piece, so a piece that restates a ban also drops it). Exit 1 names the first differing line. One check: the new piece keeps the brand file's bans. The previous piece is context for voice, not a second measured check. A missing brand file is a valid result: stop and report "brand file absent".
## Rung
rung: L1
One fast-model pass drafts with the brand file loaded; a program builds bans.kept and cmp compares. Escalate only if cmp exits 1 after one repair.
## Forbidden move
Taking rules from session chat instead of the brand file, or restating the rules inside the draft (a restated ban phrase also fails cmp).
## Tool
tool: Bash:cmp
scope: read
