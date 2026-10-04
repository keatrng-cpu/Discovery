---
name: legal-authority
description: Use when a case or statute cite must be resolved and its holding quoted, or dropped. Quiet for contract clause work.
---
## Trigger
A cite and the proposition it supports are present. Quiet when no cite or proposition is given.
## Done-when
check: quote
Each cite opens at a source, and a quoted holding line with a page or paragraph locator is a substring of the opened text. A cite that does not open is dropped and printed "dropped: <cite>". A cite whose quoted line is not a substring of the opened text, or whose pin locator does not exist, fails the card. Zero surviving cites is valid.
## Rung
rung: L3
Weak directive: a stronger pass reads each opened source; a person must review for subtle misquotes and whether the holding supports the proposition, since the substring check cannot see either (review is outside the check). Do not descend to a cheaper rung.
## Forbidden move
Keeping a cite that was not opened, or inventing a pin cite or holding quote.
## Tool
tool: mcp__FireCrawl__firecrawl_scrape
scope: read
