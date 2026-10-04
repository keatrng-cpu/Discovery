---
name: personal-admin-pack
description: Use when a meeting agenda must be assembled from sources, one item per source. Quiet for free brainstorming or for items with no source.
---
## Trigger
A meeting and a set of source threads or documents are present. Quiet when no source is attached.
## Done-when
check: quote
Every agenda item carries a source id and a verbatim quote with a locator ("item 3: <quote> @thread T msg N"). A program greps each quote in its source and exits 0 only if all match ("items: N/N sourced"). An item with no matching quote is dropped. Zero sourced items is a valid result: write "agenda: empty, no sources" and stop.
## Rung
rung: L1
A fast model selects items and quotes; a program verifies each quote string against the source text. Escalate only if a quote fails to resolve twice.
## Forbidden move
Adding an agenda item from memory alone, or paraphrasing a source into a quote it does not contain.
## Tool
tool: mcp__Gmail__get_thread
scope: read
