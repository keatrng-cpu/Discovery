---
name: software-reproduce
description: Use when a reported bug needs the smallest failing command with pinned input and actual output beside expected, shown red before any edit. Quiet for fixing or analysis.
---
## Trigger
A bug report and an existing test harness are present. Quiet when asked to fix it, or when no harness exists.
## Done-when
check: exit-code
The named smallest command (pytest or python3 -m unittest, one test id, pinned input file) exits non-zero before any edit, and the report quotes the actual output line next to the expected value. Red is the pass here. If git status shows any edited file, the check fails. No harness in the repo is a valid result: report "harness: absent" and stop; status holds as reliable only when a harness exists.
## Rung
rung: L1
A fast model drafts the command; code runs it and reads the exit code. Escalate only if the command exits 0 on the buggy tree.
## Forbidden move
Editing source to make the failure appear, or reporting a failure that was not run red.
## Tool
tool: Bash:pytest
scope: read
