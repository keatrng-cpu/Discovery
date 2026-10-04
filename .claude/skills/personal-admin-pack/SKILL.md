---
name: personal-admin-pack
description: Use when a meeting agenda must be assembled from sources, one item per source. Quiet for free brainstorming or for items with no source.
---
## Trigger
A meeting and a set of source threads or documents are present. Quiet when no source is attached.
## Done-when
check: quote
One command, pack-verify (a program the desk would run; not yet in the repo), reads the agenda and exits 0 only if all hold. Each kept item's verbatim quote greps at its cited locator in that item's own source. No two kept items cite the same source. Prints "items: N/N sourced". Unsourced items are dropped; an empty agenda (0/0) is valid.
## Rung
rung: L1
One fast-model pass proposes items; a program greps quotes.
## Forbidden move
Adding an agenda item from memory alone, two items from one source, or paraphrasing a source into a quote it does not contain.
## Tool
tool: mcp__Gmail__get_thread
scope: read
