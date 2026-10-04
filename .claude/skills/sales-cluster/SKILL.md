---
name: sales-cluster
description: Use when customer or interview quotes need grouping into segments with a quote under each group. Quiet for drafting frames, copy, or tests.
---
## Trigger
A file of raw quotes (interviews, reviews, call notes) is present and the ask is to group them. Quiet when no quotes exist, or when the ask is for new frames or copy.
## Done-when
check: quote
Write clusters.json as {group: [{quote, source, line}]}. A python3 script reads quotes.txt and exits 0 only if every group holds at least one quote that appears verbatim in quotes.txt at the cited line. It prints "groups: N, quoted: N/N". Zero quotes in, zero groups out: it prints "groups: 0, quoted: 0/0" and exits 0.
## Rung
rung: L1
A fast model groups; the script matches each quote string to its cited line. Escalate only if verbatim matching fails after one re-cite.
## Forbidden move
Inventing a segment that no quote supports, or paraphrasing a quote so the verbatim match passes.
## Tool
tool: Bash:python3
scope: read
