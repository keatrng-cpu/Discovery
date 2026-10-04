---
name: support-incident
description: Use when an incident timeline must be ordered from logs with each event quoted. Quiet for root-cause guesses or fixes.
---
## Trigger
Log files or log lines are present and a timeline is asked for. Quiet when no logs exist.
## Done-when
check: quote
`python3` check exits 0 only if every timeline event quotes its log line with `<file>:<line>` locator and timestamps are non-decreasing; each missing interval is printed as `gap: <t1>..<t2>`. An empty log yields `events: 0` and exits 0.
## Rung
rung: L1
One fast-model pass drafts the timeline; code verifies quotes and order. Escalate only if a quote fails to match.
## Forbidden move
Filling a gap with a likely story: stating a cause or event no log line supports.
## Tool
tool: Bash:python3
scope: read
