---
name: recruiting-compare
description: Use when several candidates must be laid side by side on the same scorecard lines with missing evidence kept missing. Quiet for single candidates or hire calls.
---
## Trigger
Two or more candidates' screen notes share one accepted scorecard. Quiet for a single candidate or when lines differ between candidates.
## Done-when
check: count
`jq` joins the grid to each candidate's screen notes by scorecard line and compares: for every candidate and every line, the grid cell equals that candidate's screen-note value for that line (a null note gives a null cell; a cell filled where the note is null, or a value taken from another line, fails). Each candidate has exactly N cells for N lines, and no rank, total, or fluency field exists. A null cell stays null and passes; exit code 0 on all-match.
## Rung
rung: L0
A jq join lays the existing per-line notes into a candidates-by-lines grid with nulls preserved; no model pass.
## Forbidden move
Ranking or scoring candidates on writing polish or fluency, or filling a missing cell from another line. Missing stays missing.
## Tool
tool: Bash:jq
scope: read
