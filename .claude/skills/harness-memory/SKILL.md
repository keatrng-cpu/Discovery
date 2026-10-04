---
name: harness-memory
description: Use when storing or retrieving agent memory keyed by stage (analyze, reproduce, edit, verify). Quiet for episode summaries, skill text, hooks, or logs.
---
## Trigger
A note must be saved or recalled during a coding task. The key is the stage: analyze, reproduce, edit, or verify. Quiet when asked for a story-like summary of a past session.
## Done-when
check: schema
Recall is a stage filter, `jq -c --arg s STAGE 'select(.stage==$s)' memory.jsonl > recalled.jsonl`. Then `jq -s -e --arg s STAGE '($s|IN("analyze","reproduce","edit","verify")) and all(.[]; .stage==$s and (.body|type=="string" and length<=280 and (contains("\n")|not)))' recalled.jsonl` exits 0: STAGE is one of the four, every recalled record carries exactly the requested stage (a record recalled by similar story fails), every body is a string of at most 280 characters with no newline (longer or multi-line bodies are episode blobs). Zero recalled records is a valid result; do not fill it with a similar story.
## Rung
rung: L0
jq alone checks the recalled set. Assisted: choosing the stage for a note is a judgment, and no stage-keyed store with a retrieval api is registered; the checked rule is the stage on every recalled record.
## Forbidden move
Storing an episode blob, or retrieving by similar story instead of by stage.
## Tool
tool: Bash:jq
scope: read
