---
name: research-retrieve
description: Use when a question needs sources fetched and each identifier resolved before anything is summarized. Quiet for summarizing a source already in hand or for checking a draft's claims.
---
## Trigger
A question or topic needs outside sources: papers, DOIs, preprints, pages. Quiet when the source text is already in context, or when the ask is to extract or synthesize.
## Done-when
check: quote
Every opened identifier (DOI, arXiv id, or URL the scrape tool returned and opened) is listed under "opened" and ends in exactly one place: "kept" or "dropped-recap". Every kept source has its identifier, a quoted title line with its locator (page or line), an access date (YYYY-MM-DD), and a tag "primary" (the publisher, DOI landing, arXiv, or original-document page) or "recap". A "recap" is kept only when the line "no-primary-opened" names the primary identifier that failed to open. A recap that opened while a primary of the same work also opened is not kept: it is listed under "dropped-recap" with the primary identifier that replaced it. Every hit that did not open is listed under "discarded" with the failing identifier. Zero kept sources is a valid result: print "retrieved: 0" and list the discards. Counts must satisfy: kept + dropped-recap = opened.
## Rung
rung: L1
A fast model searches and picks; the scrape result decides open or discard. Escalate only when a primary source cannot be found and only a recap opened.
## Forbidden move
Writing an identifier or URL the tool did not return, or keeping a recap when the primary source opened. A hit that does not open is discarded, never repaired by guessing.
## Tool
tool: mcp__FireCrawl__firecrawl_scrape
scope: read
