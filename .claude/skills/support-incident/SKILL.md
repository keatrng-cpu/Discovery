---
name: support-incident
description: Use when an incident timeline must be ordered from logs with each event quoted. Quiet for root-cause guesses or fixes.
---
## Trigger
Log files or log lines are present and a timeline is asked for. Quiet when no logs exist.
## Done-when
check: quote
`python3` check exits 0 only if every timeline event's quoted text equals the line at its `<file>:<line>` locator; an event with no matching log line fails, so no gap is filled. An empty log yields `events: 0` and exits 0. Time ordering is a separate sort step done by program and is not part of this check.
## Rung
rung: L1
One fast-model pass drafts the timeline; code verifies each quote against its locator. Escalate only if a quote fails to match.
## Forbidden move
Filling a gap with a likely story: stating a cause or event no log line supports.
## Tool
tool: Bash:python3
scope: read
