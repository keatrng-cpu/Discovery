---
name: sales-brief
description: Use when a prospect meeting needs a pre-call brief from public facts and the likely objection. Quiet for outreach copy, metrics estimates, or after-the-meeting notes.
---
## Trigger
A named prospect and a meeting still ahead are present. Quiet when the meeting is past, when the prospect is unnamed, or when the ask is to write outreach.
## Done-when
check: quote
Every fact line in brief.md carries a verbatim quote and public URL fetched by firecrawl_scrape. A python3 script reads brief.md and exits 0 only if each fact's quote is found in the saved page text, no number appears outside a quoted span, exactly one line starts "objection:" with non-empty text, and a "prepared:" date line is earlier than the "meeting:" date line. It prints "facts: N, quoted: N/N, objection: 1, prepared: before". Facts not found print "unsupported"; "no public facts found" is a valid result (objection and dates still required).
## Rung
rung: L1
A fast model drafts from scraped pages; the script matches quotes, flags bare numbers, and checks the objection line and prepared-before-meeting dates. Escalate only if a quote fails to match after one re-fetch.
## Forbidden move
Inventing metrics: revenue, headcount, growth, or spend figures with no quoted public source.
## Tool
tool: mcp__FireCrawl__firecrawl_scrape
scope: read
