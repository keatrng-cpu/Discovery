---
name: sales-frame
description: Use when a product or offer needs candidate sales frames: buyer, job, what they pay for. Quiet for clustering quotes, writing copy, or any ask to send or spend.
---
## Trigger
An offer, product note, or market description is present and the ask is to propose frames. Quiet when quotes need grouping (sales-cluster), when a winning frame exists and copy is wanted (sales-asset), or when the ask is to send or spend.
## Done-when
check: schema
Write frames to frames.json as a list of {buyer, job, pays_for}. `jq -e 'all(.[]; (.buyer|length>0) and (.job|length>0) and (.pays_for|length>0))' frames.json` exits 0. Any frame with an empty buyer is deleted, and the dropped count is printed. An empty list `[]` is a valid result when no buyer can be named.
## Rung
rung: L1
One fast-model pass drafts the frames; jq validates the fields. Escalate only if the jq check fails twice for the same frame.
## Forbidden move
Keeping a frame whose buyer is blank, generic ("everyone", "businesses"), or implied, so a job and a price float with no one to pay.
## Tool
tool: Bash:jq
scope: read
