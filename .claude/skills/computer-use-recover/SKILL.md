---
name: computer-use-recover
description: Use when a GUI step went wrong and must be named, reverted, and confirmed, then stopped. Quiet for planning or retrying.
---
## Trigger
A step produced an unexpected state diff and a saved pre-step snapshot exists. Quiet when no snapshot was saved: report that revert cannot be confirmed.
## Done-when
check: exit-code
Name the bad step by its step-list line. Revert it. Then `cmp pre-step-snapshot post-revert-snapshot` exits 0. After that, take no further action. Non-zero cmp means report 'revert unconfirmed' and stop.
## Rung
rung: L1
One fast-model pass reverts; cmp checks it. Never a second attempt at the failed step in the same pass.
## Forbidden move
Continuing or retrying the task after the revert, or claiming a revert without confirming the prior state.
## Tool
tool: Bash:cmp
scope: read
