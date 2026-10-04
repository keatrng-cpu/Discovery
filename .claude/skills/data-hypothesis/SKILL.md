---
name: data-hypothesis
description: Use when a comparison and slice need writing as a saved query, with no chart. Quiet for charting or answering with a number only.
---
## Trigger
A question of the form compare A to B over a slice. Quiet when a chart is requested before the query exists; write the query first.
## Done-when
check: exit-code
A file hypothesis.md holds a line "comparison: ...", a line "slice: ..." and a fenced saved query. Check: running the saved query with `python3` exits 0. An empty result set is valid: report "rows: 0".
## Rung
rung: L1
One fast-model pass drafts comparison, slice and query; python3 runs it. Escalate only if the query fails to run.
## Forbidden move
Jumping to a chart (adding a png, svg or chart html) before the query is saved, or writing a comparison with no slice.
## Tool
tool: Bash:python3
scope: read
