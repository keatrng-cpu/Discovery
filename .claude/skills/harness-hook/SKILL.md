---
name: harness-hook
description: Use when binding a check to a Claude Code lifecycle event in settings.json so exit code 2 blocks the model from continuing. Quiet for skill text, memory, trace, or promotion.
---
## Trigger
A lifecycle event (PreToolUse, PostToolUse, Stop) needs a blocking check. Quiet when the ask is a reminder, a prompt note, or any non-lifecycle behavior: only the harness executes hooks, prose does not.
## Done-when
check: exit-code
`python3 .claude/hooks/test_hooks.py` exits 0 (git ls-files lists the file, so the program exists). It feeds a case where the model would have continued (a failing test at Stop, a send or order at PreToolUse) and asserts the hook exits 2, and feeds a clean case and asserts exit 0. A hook that never fired is a failed run, not a pass.
## Rung
rung: L0
A program alone: run the hook with event JSON on stdin and read the exit code.
## Forbidden move
Exit 1 or exit 0 on a bad condition, or printing a warning and letting the model continue. Only exit 2 blocks.
## Tool
tool: Bash:python3
scope: read
