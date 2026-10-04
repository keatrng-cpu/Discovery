---
name: data-chart
description: Use when a chart must be bound to an existing saved query result. Quiet when no saved query exists; run hypothesis first.
---
## Trigger
A saved query and its result are present and a chart is asked for. Quiet when the query is missing or the ask adds extra series.
## Done-when
check: quote
The chart spec (json or svg source) names the query file as its data source. Check: one script, `python3 check_chart.py <spec> hypothesis.md <query-result>`, with one exit code, that exits 0 only if each of these holds: the title contains the hypothesis.md "comparison:" text; the series count is 1 unless the ask said otherwise; one labeled value in the spec equals the same value in the query result. It prints each quote with file and line. It does not exist in the repo yet, so the desk would write it.
## Rung
rung: L1
One fast-model pass writes the spec; python3 reads back the value and series count. Escalate only on a value mismatch.
## Forbidden move
Adding a decorative second series (the spec must keep exactly one series unless the ask said otherwise), a title that does not name the saved comparison line, or plotting values not taken from the saved query result.
## Tool
tool: Bash:python3
scope: read
