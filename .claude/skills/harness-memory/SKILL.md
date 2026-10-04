---
name: harness-memory
description: Use when storing or retrieving agent memory keyed by stage (analyze, reproduce, edit, verify). Quiet for episode summaries, skill text, hooks, or logs.
---
## Trigger
A note must be saved or recalled during a coding task. The key is the stage: analyze, reproduce, edit, or verify. Quiet when asked for a story-like summary of a past session.
## Done-when
check: schema
`jq -s -e` over the memory jsonl exits 0: every record has stage in analyze, reproduce, edit, verify and a body that is a string of at most 280 characters with no newline. A longer or multi-line body is an episode blob and fails. Zero records is a valid result; do not fill it with a similar story.
## Rung
rung: L0
jq alone checks the schema and the body limit. Assisted: choosing the stage for a note is a judgment, and the checked rule is the stored shape.
## Forbidden move
Storing an episode blob, or retrieving by similar story instead of by stage.
## Tool
tool: Bash:jq
scope: read
