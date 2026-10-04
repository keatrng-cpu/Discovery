---
name: support-exception
description: Use when a ticket fails its path and the work must stop with a record and hand-off. Quiet when the path succeeded.
---
## Trigger
A known path step failed or a variance was reported. Quiet when state matches the workflow.
## Done-when
check: exit-code
`python3 exception_record.py record.json` exits 0 only if the record names the failed step, the observed vs expected state, and a handoff owner, and has no remedy field; otherwise exits non-zero. Stop is the valid result.
## Rung
rung: L0
Code writes and validates the record. No model pass is needed.
## Forbidden move
Guessing a remedy: proposing, trying, or applying a fix after the failure instead of stopping.
## Tool
tool: Bash:python3
scope: read
