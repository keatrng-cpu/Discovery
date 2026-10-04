---
name: software-edit
description: Use when a frozen plan names files and a constrained diff must be applied and stopped there. Quiet for planning, analysis, or running the verify gate.
---
## Trigger
A frozen plan lists the files to change and any signature change. Quiet when no plan exists or the plan is still open.
## Done-when
check: state-diff
`git diff --name-only` lists exactly the files named in the plan and no others (a sorted set comparison of the two lists). An empty diff is a valid result when the plan needs no change: report "diff: empty".
## Rung
rung: L1
One fast-model pass applies the plan; git compares the file list. Signature stability and per-hunk notes are working rules for the editor, not part of this check. Escalate only if the diff touches a file outside the plan.
## Forbidden move
Drift: editing an unnamed file, renaming a public signature, or tidying beyond the plan.
## Tool
tool: Bash:git
scope: read
