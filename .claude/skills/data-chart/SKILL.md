---
name: data-chart
description: Use when a chart must be bound to an existing saved query result. Quiet when no saved query exists; run hypothesis first.
---
## Trigger
A saved query and its result are present and a chart is asked for. Quiet when the query is missing or the ask adds extra series.
## Done-when
check: quote
The chart spec (json or svg source) names the query file as its data source. Check: one labeled value is quoted from the chart spec with file and line, the same value is quoted from the query result with file and line, the two are equal, the title states the comparison, and the spec has exactly one series unless the ask said otherwise.
## Rung
rung: L1
One fast-model pass writes the spec; python3 reads back the value and series count. Escalate only on a value mismatch.
## Forbidden move
Adding a decorative second series, or plotting values not taken from the saved query result.
## Tool
tool: Bash:python3
scope: read
