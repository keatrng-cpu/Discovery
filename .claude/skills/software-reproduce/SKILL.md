---
name: software-reproduce
description: Use when a reported bug needs the smallest failing command with pinned input, shown red before any edit. Quiet for fixing or analysis.
---
## Trigger
A bug report and an existing test harness are present. Quiet when asked to fix it, or when no harness exists.
## Done-when
check: exit-code
The named smallest command (pytest or python3 -m unittest, one test id, pinned input file) exits non-zero on the unedited tree. Red is the pass here. Exit 0 means the bug did not reproduce and the check fails. No harness in the repo is a valid result: report "harness: absent" and stop; status holds as reliable only when a harness exists.
## Rung
rung: L1
A fast model drafts the command; code runs it and reads the exit code. The actual-versus-expected note and the clean tree are reported alongside but are not part of this check. Escalate only if the command exits 0 on the buggy tree.
## Forbidden move
Editing source to make the failure appear, or reporting a failure that was not run red.
## Tool
tool: Bash:pytest
scope: read
