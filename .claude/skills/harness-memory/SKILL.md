---
name: harness-memory
description: Use when storing or retrieving agent memory keyed by stage (analyze, reproduce, edit, verify). Quiet for episode summaries, skill text, hooks, or logs.
---
## Trigger
A note must be saved or recalled during a coding task. The key is the stage: analyze, reproduce, edit, or verify. Quiet when asked for a story-like summary of a past session.
## Done-when
check: schema
`jq -n -e --arg s STAGE --slurpfile m memory.jsonl --slurpfile r recalled.jsonl '($s|IN("analyze","reproduce","edit","verify")) and all($m[]; (.stage|IN("analyze","reproduce","edit","verify")) and (.body|type=="string" and length<=280 and (contains("\n")|not))) and $r == [$m[]|select(.stage==$s)]'` exits 0 only if: STAGE is one of analyze, reproduce, edit, verify; every stored record carries one of those stages (store at the stage); every stored body is a string of at most 280 characters with no newline (longer or multi-line bodies are episode blobs); recalled.jsonl equals exactly the stage filter of memory.jsonl (retrieve by stage, not by similar story). An empty memory.jsonl and zero recalled records are valid results; do not fill them with a similar story.
## Rung
rung: L0
jq alone checks the recalled set. Assisted: choosing the stage for a note is a judgment, and no stage-keyed store with a retrieval api is registered; the checked rule is the stage on every recalled record.
## Forbidden move
Storing an episode blob, or retrieving by similar story instead of by stage.
## Tool
tool: Bash:jq
scope: read
