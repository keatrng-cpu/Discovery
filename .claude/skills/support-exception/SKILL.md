---
name: support-exception
description: Use when a ticket fails its path and the work must stop with a record and hand-off. Quiet when the path succeeded.
---
## Trigger
A known path step failed or a variance was reported. Quiet when state matches the workflow.
## Done-when
check: exit-code
`jq -e --slurpfile f failed_state.json --slurpfile c state.json '(keys-["failed_step","observed","expected","handoff_owner","stopped"]|length==0) and (.failed_step|type=="string" and length>0) and (.handoff_owner|type=="string" and length>0) and (.stopped==true) and (.expected|length>0) and (.observed==$f[0]) and (.observed!=.expected) and ($c[0]==$f[0])' record.json` exits 0 only if the record has exactly the allowed keys (a remedy or any other extra field fails), names the failed step and handoff owner, carries observed equal to the failure-time snapshot, differs from expected, and the current state still equals that snapshot, so no fix was tried outside the record. Otherwise exits non-zero. The stop is this code check, not a model judgment. Stop is the valid result.
## Rung
rung: L0
Code validates the record. No model pass is needed.
## Forbidden move
Guessing a remedy: proposing, trying, or applying a fix after the failure instead of stopping.
## Tool
tool: Bash:jq
scope: read
