---
name: computer-use-recover
description: Use when a GUI step went wrong and must be named, its revert confirmed, then stopped. Quiet for planning or retrying.
---
## Trigger
A step produced an unexpected state diff, a saved pre-step snapshot exists, and a revert has been carried out by a person or the host's approved GUI driver. Quiet when no snapshot was saved: report that revert cannot be confirmed.
## Done-when
check: exit-code
Output first prints 'bad step: <step id or steps.md:L<n>>' naming the step that caused the unexpected diff; without that line the result fails. After the revert is made by a person or host driver (this skill holds no act tool), `cmp pre-step-snapshot post-revert-snapshot` exits 0; then stop with no further action. Non-zero cmp is reported as 'revert unconfirmed' and also stops. The check is the cmp exit code.
## Rung
rung: L1
One fast-model pass names the bad step from the diff; cmp checks the revert. Never a second attempt at the failed step in the same pass.
## Forbidden move
Continuing or retrying the task after the revert, claiming a revert without confirming the prior state, or reverting from this skill instead of naming the step and stopping.
## Tool
tool: Bash:cmp
scope: read
