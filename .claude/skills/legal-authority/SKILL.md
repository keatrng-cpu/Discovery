---
name: legal-authority
description: Use when a case or statute cite must be resolved and its holding quoted, or dropped. Quiet for contract clause work.
---
## Trigger
A cite and the proposition it supports are present. Quiet when no cite or proposition is given.
## Done-when
check: quote
Each cite opens at a source, and a quoted holding line with a page or paragraph locator is a substring of the opened text and supports the proposition. A cite that does not open is dropped and printed "dropped: <cite>". An invented or mis-pinned cite fails the card. Zero surviving cites is valid. A subtle misquote can still pass this check, so a person reviews.
## Rung
rung: L3
Weak directive: a stronger pass reads each opened source; a person confirms pin cites. Do not descend to a cheaper rung.
## Forbidden move
Keeping a cite that was not opened, or inventing a pin cite or holding quote.
## Tool
tool: mcp__FireCrawl__firecrawl_scrape
scope: read
