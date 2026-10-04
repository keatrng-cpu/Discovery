---
name: data-profile
description: Use when a dataset or table needs rows, nulls, types and grain counted and saved. Quiet for cleaning, charting or any ask that changes the data.
---
## Trigger
A csv, table or extract is present and the ask is to know its shape. Quiet when the ask is to fix values, chart, or answer a business question.
## Done-when
check: count
`python3` over the file prints rows, per-column null count, per-column type, the grain (the column set unique per row, or "none"), and one line "id-as-measure: <col>" for each id column used as a measure, then writes profile.json with keys rows, columns (null count and type each), grain, id_as_measure. Check: a second python3 recount of the file must equal profile.json on rows, on every per-column null count, on grain (distinct tuples of the grain columns equal rows, or grain is "none"), and the number of "id-as-measure:" lines equals the length of id_as_measure; any mismatch is a nonzero count of differences. An empty file is a valid result: rows 0, grain "none".
## Rung
rung: L0
Code alone: a script counts; no model reads the rows. Escalate only if the file cannot be parsed.
## Forbidden move
Stating a count, null total or grain from reading a sample instead of tool output, or summing a numeric id column as if it were a measure.
## Tool
tool: Bash:python3
scope: read
