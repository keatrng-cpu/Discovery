---
name: personal-admin-pack
description: Use when a meeting agenda must be assembled from sources, one item per source. Quiet for free brainstorming or for items with no source.
---
## Trigger
A meeting and a set of source threads or documents are present. Quiet when no source is attached.
## Done-when
check: quote
One program, per item: the source id is unique across items (duplicate source ids = 0, one item per source) and the verbatim quote with locator greps in that source (items: N/N sourced). Unsourced items are dropped; an empty agenda is valid.
## Rung
rung: L1
One fast-model pass proposes items; a program greps quotes and checks source ids.
## Forbidden move
Adding an agenda item from memory alone, two items from one source, or paraphrasing a source into a quote it does not contain.
## Tool
tool: mcp__Gmail__get_thread
scope: read
