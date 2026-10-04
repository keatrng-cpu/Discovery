---
name: markets-cross
description: Use when a filing line and a news line on the same fact must be shown side by side with agreement marked. Quiet for single-source extraction or a blended summary.
---
## Trigger
Both a filing and a news source are present for one claim. Quiet when only one source exists, or the ask is a merged narrative.
## Done-when
check: quote
Output has two verbatim quotes per claim, one labelled filing with page or item, one labelled news with its source, and a verdict of agree, disagree, or unplaced. A program confirms each quote appears in its own source; the run passes only if all do. A claim with no filing line is marked "unplaced", which is a valid result.
## Rung
rung: L1
A fast model pairs the lines; code verifies each quote against its source file. Escalate only when a quote fails to match.
## Forbidden move
Merging the filing and the news into one voice, or smoothing a disagreement into a single number.
## Tool
tool: mcp__FireCrawl__firecrawl_scrape
scope: read
