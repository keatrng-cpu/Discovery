---
name: data-define
description: Use when a metric needs its formula, grain and exclusion drafted for a human to sign. Quiet for querying a metric that is not yet signed.
---
## Trigger
A new or disputed metric. Quiet when a signed definition exists; use it. Draft only, then stop.
## Done-when
check: signature
A file definition.md holds "formula:", "grain:" and "exclusion:" lines and a "signed-by:" line left empty by the model. Check: a person's name on the signed-by line must exist before any query on the metric runs; absent that, queries are refused. The model never fills the signature.
## Rung
rung: L3
A strong model drafts the three lines; a person signs. No program can sign.
## Forbidden move
Filling the signed-by line, or running queries on the metric before a person signs.
## Tool
tool: none
scope: none
gate: ABSENT sign (draft formula, grain and exclusion, then stop; a person signs before anyone queries)
