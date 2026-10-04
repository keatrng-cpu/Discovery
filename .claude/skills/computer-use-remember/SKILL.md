---
name: computer-use-remember
description: Use when a fact from an early GUI step is needed at a later step and must go through a file. Quiet when the fact is used immediately.
---
## Trigger
A fact observed at one step is needed at a later step. Quiet when the next step uses it directly.
## Done-when
check: exit-code
Write the fact to state.json. At the later step, read it back with `jq -e '.<key> == "<value>"' state.json`, which exits 0, and the value matches the quoted source. A missing key makes jq exit non-zero and the fact is reported 'unread', a valid result.
## Rung
rung: L0
A program writes and reads the file; no model pass is needed to check it.
## Forbidden move
Relying on the transcript to recall the fact at the later step instead of reading state.json.
## Tool
tool: Bash:jq
scope: read
