---
name: markets-filing
description: Use when a figure or statement must be pulled from an SEC filing (10-K, 10-Q, 8-K) with a quote and page or item. Quiet for news recaps, summaries, or trading asks.
---
## Trigger
A filing document (text or PDF) is present and the ask is a quoted line with its location. Quiet when only a news recap exists, or the ask is a summary or a trade.
## Done-when
check: quote
Each claim is one verbatim line from the filing text plus its page or item locator (for example "Item 7, p. 31"). A program extracts the text per page (pdftotext, pages split on form feed) or per item (text between an "Item N" heading and the next one), then greps the quote inside the stated page or item only. The run passes only if every quote is found at its own stated locator; a quote found elsewhere, or a locator that does not exist, fails. A figure that cannot be placed is listed as "skipped" and is a valid result. Zero claims placed is a valid result.
## Rung
rung: L1
A fast model selects candidate lines; code confirms each quote exists on the stated page or under the stated item. Escalate only when a quote fails to match.
## Forbidden move
Using the news recap as the filing, or stating a figure it could not place (tables and exhibits slip: skip them, do not paraphrase).
## Tool
tool: Bash:pdftotext
scope: read
