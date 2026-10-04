---
name: recruiting-compare
description: Use when several candidates must be laid side by side on the same scorecard lines with missing evidence kept missing. Quiet for single candidates or hire calls.
---
## Trigger
Two or more candidates' screen notes share one accepted scorecard. Quiet for a single candidate or when lines differ between candidates.
## Done-when
check: count
`jq` counts cells: each candidate has exactly N cells for N scorecard lines (candidates x N matched), every cell is a quote or null, and no rank, total, or fluency-based field exists. A null cell stays null and passes; a filled-in blank, dropped line, or rank field fails.
## Rung
rung: L1
One fast-model pass builds the grid; jq counts cells per candidate. Escalate only if the count fails after one repair pass.
## Forbidden move
Ranking or scoring candidates on writing polish or fluency, or filling a missing cell from another line. Missing stays missing.
## Tool
tool: Bash:jq
scope: read
