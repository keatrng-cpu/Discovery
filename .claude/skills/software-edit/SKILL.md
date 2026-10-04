---
name: software-edit
description: Use when a frozen plan names files and a constrained diff must be applied and stopped there. Quiet for planning, analysis, or running the verify gate.
---
## Trigger
A frozen plan lists the files to change and any signature change. Quiet when no plan exists or the plan is still open.
## Done-when
check: state-diff
One command, `python3 edit_check.py plan.json`, with one exit code. It does not exist in the repo yet: it is the program the desk would run, reading `git diff`. Input: the frozen plan. It exits 0 only if the sorted `git diff --name-only` equals the plan's file list; `git diff -U0` shows no added or removed `def` or `class` line unless the plan lists that signature change; each hunk the plan marks non-obvious has an added one-line comment inside it. An empty diff is a valid result when the plan needs no change: it prints "diff: empty" and exits 0.

## Rung
rung: L1
One fast-model pass applies the plan; git output is compared to the plan for files, signature lines and hunk notes. Escalate only if the diff touches a file outside the plan.

## Forbidden move
Drift: editing an unnamed file, renaming a public signature, or tidying beyond the plan.
## Tool
tool: Bash:git
scope: read
