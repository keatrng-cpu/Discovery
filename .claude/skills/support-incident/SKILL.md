---
name: support-incident
description: Use when an incident timeline must be ordered from logs with each event quoted. Quiet for root-cause guesses or fixes.
---
## Trigger
Log files or log lines are present and a timeline is asked for. Quiet when no logs exist.
## Done-when
check: quote
One command with one exit code: `python3 desk/check_incident.py --timeline timeline.json --logs <files>`. It does not exist yet, so checkRunnable is false and the program is what the desk would run. Inputs are the timeline events and the log files. Exit 0 asserts every event has `<file>:<line>`, `ts`, and `quote`, and the quote equals the line at that locator. Exit 0 asserts each `ts` equals the timestamp parsed from its log line. Exit 0 asserts events are in non-decreasing `ts` order, ties keeping `<file>:<line>` order. An event with no matching log line fails, so no gap is filled. An empty log yields `events: 0` and exits 0.
## Rung
rung: L1
One fast-model pass drafts the timeline; code verifies each quote, its timestamp, and the time order. Escalate only if a quote fails to match.
## Forbidden move
Filling a gap with a likely story: stating a cause or event no log line supports.
## Tool
tool: Bash:python3
scope: read
