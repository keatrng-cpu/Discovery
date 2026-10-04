---
name: computer-use-finish
description: Use when a GUI task is about to be submitted and the final state must be compared to the instruction. Quiet for mid-task steps.
---
## Trigger
The last step list item is done and a submit control is the only remaining action. Quiet before then.
## Done-when
check: state-diff
List each field the instruction requires and the final-state value for it. Submit only if every field matches, with 'unmet: 0'. Any mismatch or unread field means no submit and an 'unmet: <field>' line. Ceiling not awarded.
## Rung
rung: L1
One fast-model pass lists the fields; python3 compares each field of final-state.json to the instruction file (exit 0 only when all equal). Stakes raise the verifier, not the doer.
## Forbidden move
Submitting early, before the final state is checked field by field against the instruction.
## Tool
tool: Bash:python3
scope: read
