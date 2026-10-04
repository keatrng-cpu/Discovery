---
name: recruiting-extract
description: Use when a resume must be filled into accepted scorecard fields only, with the source line quoted. Quiet for drafting scorecards or judging candidates.
---
## Trigger
An accepted scorecard and a resume are both present and the ask is to fill the scorecard fields. Quiet when the scorecard is not yet accepted.
## Done-when
check: schema
`jq` validates the output against the scorecard schema: keys equal the accepted scorecard fields exactly, and each value is null or an object with a value and a quote string and a resume line locator. An extra key or a missing key fails; a null field passes. An all-null result is valid.
## Rung
rung: L1
One fast-model pass fills fields under the schema; jq verifies. Escalate only on a schema failure that survives one repair pass.
## Forbidden move
Inferring a trait or filling a blank from tone, school, or fluency. A field without a quoted resume line stays null.
## Tool
tool: Bash:jq
scope: read
