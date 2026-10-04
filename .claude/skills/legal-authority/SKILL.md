---
name: legal-authority
description: Use when a case or statute cite must be resolved and its holding quoted, or dropped. Quiet for contract clause work.
---
## Trigger
A cite and the proposition it supports are present. Quiet when no cite or proposition is given.
## Done-when
check: quote
Each cite is resolved: it opens at a source, and the cite string (reporter cite, docket, or statute number) is a substring of the opened text, so the opened page is the cited authority. Each kept cite carries a quoted holding line used, with a page or paragraph locator, and that line must be a substring of the opened text. A kept cite with no quoted holding is dropped. A candidate cite that does not open is dropped and printed "dropped: <cite>". Any cite kept or asserted in the output that did not open or resolve (invented), any quoted line not a substring of the opened text, or any pin locator that does not exist fails the card. Zero surviving cites is valid.
## Rung
rung: L3
Weak directive: a stronger pass reads each opened source; a person must review for subtle misquotes and whether the holding supports the proposition, since the substring check cannot see either (review is outside the check). Do not descend to a cheaper rung.
## Forbidden move
Keeping a cite that was not opened, or inventing a pin cite or holding quote.
## Tool
tool: mcp__FireCrawl__firecrawl_scrape
scope: read
