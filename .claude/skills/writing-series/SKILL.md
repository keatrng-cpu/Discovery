---
name: writing-series
description: Use when a new piece must follow a standing brand file and match the previous piece. Quiet for a one-off piece with no brand file.
---
## Trigger
A brand file and a previous piece are present. Quiet when no brand file exists; session chat is never the memory.
## Done-when
check: exit-code
`cmp` over two files exits 0: bans.expected (the brand file's "Bans" lines whose phrase is absent from the previous piece, so these are the bans the previous piece kept, plus the brand file's rule lines) and bans.kept (the same lines minus any whose phrase occurs in the new piece, so a piece that breaks a ban or restates a rule also drops it). Exit 1 names the first differing line. One check: the new piece matches the previous piece's bans and restates no rule, with the brand file as the only source. The extractor that builds both files does not exist yet; the desk would run it. A missing brand file is a valid result: stop and report "brand file absent".
## Rung
rung: L1
One fast-model pass drafts with the brand file loaded; a program builds bans.kept and cmp compares. Escalate only if cmp exits 1 after one repair.
## Forbidden move
Taking rules from session chat instead of the brand file, or restating the rules inside the draft (a restated ban phrase also fails cmp).
## Tool
tool: Bash:cmp
scope: read
