---
name: computer-use-act
description: Use when one planned GUI action is performed and must be proven by before and after state. Quiet for choosing the action or for reading screens.
---
## Trigger
One approved action and a captured pre-action state exist. Quiet when the action is not yet chosen or no pre-state was captured.
## Done-when
check: state-diff
Capture state after the action and diff it against the pre-state. Pass only if the diff shows the expected change (field plus before and after values). An empty diff or an unexpected extra change fails. A click that returned success is not a result.
## Rung
rung: L1
One fast-model pass performs the step; code produces the diff. Escalate only when the diff is empty or unexpected, and then to recover, not a retry.
## Forbidden move
Reporting success because the click or keystroke ran, with no after-state diff.
## Tool
tool: Bash:playwright
scope: read
