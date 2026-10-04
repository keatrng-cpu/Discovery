---
name: reverse-engineering-state
description: Use when a reverse-engineering investigation must be written to files so a new session can resume it. Quiet for chat summaries or for new analysis.
---
## Trigger
Findings from triage, static, lift, dynamic, protocol, or summarize exist, or a session must resume one. Quiet when there is nothing yet to record.
## Done-when
check: state-diff
A fresh session reads only the state file and its listed artifacts and writes restated.json; then `jq -S .findings state.json > a.json; jq -S .findings restated.json > b.json; cmp a.json b.json` exits 0 (the resumed findings equal the saved findings). An empty findings list is a valid result.
Status is reliable as files, but the restate program is not registered, so the check is not runnable today.
## Rung
rung: L0
Files and jq only. No model pass; escalate only if the cmp of findings fails.
## Forbidden move
Leaving findings in chat only, or resuming from memory instead of the files.
## Tool
tool: Bash:jq
scope: read
