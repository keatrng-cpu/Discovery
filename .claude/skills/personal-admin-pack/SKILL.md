---
name: personal-admin-pack
description: Use when a meeting agenda must be assembled from sources, one item per source. Quiet for free brainstorming or for items with no source.
---
## Trigger
A meeting and a set of source threads or documents are present. Quiet when no source is attached.
## Done-when
check: quote
Program greps each item's verbatim quote at its cited locator in that item's own source and prints "items: N/N sourced"; exits 0 only if every kept item greps. Unsourced items are dropped; an empty agenda (0/0) is valid.
## Rung
rung: L1
One fast-model pass proposes items; a program greps quotes.
## Forbidden move
Adding an agenda item from memory alone, two items from one source, or paraphrasing a source into a quote it does not contain.
## Tool
tool: mcp__Gmail__get_thread
scope: read
