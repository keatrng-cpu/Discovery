---
name: sales-brief
description: Use when a prospect meeting needs a pre-call brief from public facts and the likely objection. Quiet for outreach copy, metrics estimates, or after-the-meeting notes.
---
## Trigger
A named prospect and a meeting still ahead are present. Quiet when the meeting is past, when the prospect is unnamed, or when the ask is to write outreach.
## Done-when
check: quote
Every fact line in brief.md is either quoted or marked unsupported. A quoted fact line carries a verbatim quote and public URL fetched by firecrawl_scrape; an unsupported fact line carries the word "unsupported", no quote, and no number. A python3 script reads brief.md and exits 0 only if every quoted fact's quote is found in the saved page text (a quote not found exits 1), no digit appears outside a quoted span except on the one "prepared:" and one "meeting:" line (each an ISO date YYYY-MM-DD, prepared earlier than meeting), and exactly one line starts "objection:" with non-empty text. It prints "facts: N, quoted: Q, unsupported: U, objection: 1, prepared: before" with Q+U=N. Unsupported facts count as a result and do not fail the check; "no public facts found" (N=0) is a valid result (objection and dates still required).
## Rung
rung: L1
A fast model drafts from scraped pages; the script matches quotes, flags numbers outside quotes (dates on prepared:/meeting: excepted), accepts unsupported facts, and checks the objection line and prepared-before-meeting dates. Escalate only if a quote fails to match after one re-fetch.
## Forbidden move
Inventing metrics: revenue, headcount, growth, or spend figures with no quoted public source.
## Tool
tool: mcp__FireCrawl__firecrawl_scrape
scope: read
