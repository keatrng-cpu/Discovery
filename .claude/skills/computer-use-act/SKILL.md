---
name: computer-use-act
description: Use when one performed GUI action must be proven by before and after state files. Quiet for choosing the action or for reading screens.
---
## Trigger
One approved action has been performed by the host's approved GUI driver (not by this skill), and pre-state.json and post-state.json both exist. Quiet when the action is not yet chosen or no pre-state was captured.
## Done-when
check: state-diff
python3 loads pre-state.json and post-state.json and prints each changed field as field: before -> after. Pass only if the printed diff is exactly the one expected change (field plus before and after values). An empty diff or any extra changed field fails; a click returning success is not a result. If post-state.json is missing the result is 'unread', not pass.
## Rung
rung: L1
One fast-model pass reads the printed diff against the expected change; python3 produces the diff. Escalate only when the diff is empty or unexpected, and then to recover, not a retry.
## Forbidden move
Reporting success because the click or keystroke ran, with no after-state diff; or performing the click or keystroke from this skill, which holds no act tool.
## Tool
tool: Bash:python3
scope: read
