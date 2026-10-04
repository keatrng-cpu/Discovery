---
name: support-exception
description: Use when a ticket fails its path and the work must stop with a record and hand-off. Quiet when the path succeeded.
---
## Trigger
A known path step failed or a variance was reported. Quiet when state matches the workflow.
## Done-when
check: exit-code
`jq -e '(.failed_step|length>0) and (.observed|length>0) and (.expected|length>0) and (.handoff_owner|length>0) and (has("remedy")|not)' record.json` exits 0 only if the record names the failed step, observed vs expected state, and a handoff owner, and has no remedy field; otherwise exits non-zero. The stop is this code check, not a model judgment. Stop is the valid result.
## Rung
rung: L0
Code validates the record. No model pass is needed.
## Forbidden move
Guessing a remedy: proposing, trying, or applying a fix after the failure instead of stopping.
## Tool
tool: Bash:jq
scope: read
