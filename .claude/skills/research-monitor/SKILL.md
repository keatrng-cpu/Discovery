---
name: research-monitor
description: Use when a saved research memo file must be refreshed against new sources with stale claims expired. Quiet for a first-time memo or when no memo file exists.
---
## Trigger
A prior memo exists as a file with a date on each claim. Quiet when there is no memo file, because there is nothing to diff.
## Done-when
check: state-diff
`git diff` of the memo shows only added sources, expired claims moved by a date comparison run in code against the half-life field, and the old conclusion left visible with a "changed" mark if it changed. No new sources is a valid result: an empty diff.
## Rung
rung: L1
Code runs the clock and the diff; one fast-model pass reads new sources only. Escalate only when the diff touches an unexpired claim.
## Forbidden move
Letting the model judge expiry, or rewriting the memo whole so the old conclusion disappears.
## Tool
tool: Bash:git
scope: read
