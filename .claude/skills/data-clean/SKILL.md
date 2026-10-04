---
name: data-clean
description: Use when exactly one field needs exactly one rule applied with before and after counts. Quiet for multi-field cleanup or analysis.
---
## Trigger
One named column and one named rule (trim, cast, dedupe, null-fill, drop). Quiet when the ask names several fields or says clean the data with no field; ask for one field.
## Done-when
check: count
`python3` applies the one rule to the one named field and prints "rows before: N", "rows after: M", "dropped: K", and writes dropped.csv holding all K dropped rows. Check: the same `python3` run exits nonzero unless N = M + K, K equals the data-row count of dropped.csv, and every column other than the named field is identical in each kept row to the original row. K = 0 with an empty dropped.csv is a valid result.
## Rung
rung: L0
Code alone: one deterministic rule per run. If the rule is ambiguous, stop and ask rather than escalate.
## Forbidden move
Cleaning a second field in the same directive (the loose-directive failure), or deleting dropped rows instead of keeping them queryable.
## Tool
tool: Bash:python3
scope: read
