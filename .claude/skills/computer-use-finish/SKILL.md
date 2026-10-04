---
name: computer-use-finish
description: Use when a GUI task is about to be submitted and the final state must be compared to the instruction. Quiet for mid-task steps.
---
## Trigger
The last step list item is done and a submit control is the only remaining action. Quiet before then.
## Done-when
check: state-diff
Prepare only: list each instruction-required field with its final-state value from final-state.json and print 'unmet: 0' or 'unmet: <field>' per mismatched or unread field, then stop. Submit is performed by a person; it is never performed here. Early submit fails the card. Ceiling not awarded.
## Rung
rung: L1
One fast-model pass lists fields and values; the unmet list is printed for a person. Stakes raise the verifier, not the doer.
## Forbidden move
Submitting early, before the final state is checked field by field against the instruction; or submitting at all.
## Tool
tool: none
scope: none
gate: ABSENT submit (prepare the field-by-field unmet list, stop; a person presses submit)
