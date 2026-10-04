---
name: computer-use-recover
description: Use when a GUI step went wrong and must be named, its revert confirmed, then stopped. Quiet for planning or retrying.
---
## Trigger
A step produced an unexpected state diff, a saved pre-step snapshot exists, and a revert has been carried out by a person or the host's approved GUI driver. Quiet when no snapshot was saved: report that revert cannot be confirmed.
## Done-when
check: exit-code
One composite command, check-recover.py (not yet in the repo; the desk would run it), takes the output text, pre-step-snapshot and post-revert-snapshot and has one exit code. It exits 0 only if the output's first line matches 'bad step: <step id or steps.md:L<n>>'. It also requires that a byte comparison of the two snapshots is identical. Any other result exits non-zero: a missing bad-step line fails, and a snapshot mismatch is reported 'revert unconfirmed'. The revert is made by a person or host driver (this skill holds no act tool); then stop with no further action.
## Rung
rung: L1
One fast-model pass names the bad step from the diff; the composite program checks the line and the revert. Never a second attempt at the failed step in the same pass.
## Forbidden move
Continuing or retrying the task after the revert, claiming a revert without confirming the prior state, or reverting from this skill instead of naming the step and stopping.
## Tool
tool: Bash:python3
scope: read
