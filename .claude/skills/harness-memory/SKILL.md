---
name: harness-memory
description: Use when storing or retrieving agent memory keyed by stage (analyze, reproduce, edit, verify). Quiet for episode summaries, skill text, hooks, or logs.
---
## Trigger
A note must be saved or recalled during a coding task. The key is the stage: analyze, reproduce, edit, or verify. Quiet when asked for a story-like summary of a past session.
## Done-when
check: schema
`jq -e` over the memory file exits 0: every record has stage in analyze, reproduce, edit, verify and a short body (not an episode blob). Retrieval for one stage returns only records of that stage. Zero records for a stage is a valid result; do not fill it with a similar story.
## Rung
rung: L1
One fast pass sorts notes into stages; jq does the schema check. Assisted: the stage choice is a judgment.
## Forbidden move
Storing an episode blob, or retrieving by similar story instead of by stage.
## Tool
tool: Bash:jq
scope: read
