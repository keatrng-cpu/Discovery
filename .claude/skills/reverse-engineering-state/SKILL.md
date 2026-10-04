---
name: reverse-engineering-state
description: Use when a reverse-engineering investigation must be written to files so a new session can resume it. Quiet for chat summaries or for new analysis.
---
## Trigger
Findings from triage, static, lift, dynamic, protocol, or summarize exist, or a session must resume one. Quiet when there is nothing yet to record.
## Done-when
check: schema
`jq -e` on the state file exits 0: it has the keys target, findings, and artifacts, and each path listed under artifacts exists on disk. A fresh session reads only those files and restates the same findings. An empty findings list is a valid result.
## Rung
rung: L0
Files and a schema query only. No model pass; escalate only if the state file fails the jq check.
## Forbidden move
Leaving findings in chat only, or resuming from memory instead of the files.
## Tool
tool: Bash:jq
scope: read
