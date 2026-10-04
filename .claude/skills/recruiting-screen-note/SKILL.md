---
name: recruiting-screen-note
description: Use when one screening note per scorecard line is needed for a candidate, evidence or blank. Quiet for overall ratings or hire calls.
---
## Trigger
An accepted scorecard and one candidate's extracted fields or resume are present, and the ask is a note per line. Quiet when asked for an overall score.
## Done-when
check: count
`jq` counts notes: the number of notes equals the number of scorecard lines (N/N), each note is a quote with locator or null, and no overall, vibe, or total field exists in the output. An unsupported line stays blank and passes; a missing or extra note, or any overall field, fails.
## Rung
rung: L1
One fast-model pass writes the notes; jq counts them against the scorecard. Escalate only if the count fails after one repair pass.
## Forbidden move
Adding an overall vibe score, summary rating, or recommendation field. One note per line, nothing aggregated.
## Tool
tool: Bash:jq
scope: read
