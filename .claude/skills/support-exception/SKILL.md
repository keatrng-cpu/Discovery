---
name: support-exception
description: Use when a ticket fails its path and the work must stop with a record and hand-off. Quiet when the path succeeded.
---
## Trigger
A known path step failed or a variance was reported. Quiet when state matches the workflow.
## Done-when
check: exit-code
One command with one exit code: `jq -e --slurpfile f failed_state.json --slurpfile c state.json '(keys-["failed_step","observed","expected","handoff_owner","stopped"]|length==0) and (.failed_step|type=="string" and length>0) and (.handoff_owner|type=="string" and length>0) and (.stopped==true) and (.expected|length>0) and (.observed==$f[0]) and (.observed!=.expected) and ($c[0]==$f[0])' record.json`. Inputs are record.json, failed_state.json, and state.json. Exit 0 asserts the record has exactly the allowed keys, so a remedy field fails. Exit 0 asserts it names a non-empty failed step and handoff owner with stopped true. Exit 0 asserts observed equals the failure-time snapshot and differs from expected. Exit 0 asserts current state still equals that snapshot, so no fix was tried. Stop is the valid result.
## Rung
rung: L0
Code validates the record. No model pass is needed.
## Forbidden move
Guessing a remedy: proposing, trying, or applying a fix after the failure instead of stopping.
## Tool
tool: Bash:jq
scope: read
