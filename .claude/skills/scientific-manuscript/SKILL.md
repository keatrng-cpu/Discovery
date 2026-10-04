---
name: scientific-manuscript
description: Use when result files must be drafted into manuscript text with a labeled self-review. Quiet for deciding whether the claim is true or publishable.
---
## Trigger
Result files and a figure exist and a draft is wanted. Quiet when no result files exist, or when the ask is a verdict on the science: a human owns the claim.
## Done-when
check: quote
A program extracts every number in the draft and each must appear in a result file; each is listed with a file and line locator. Any number with no locator fails. The self-review section is headed "DRAFT self-review" and contains no verdict words (accept, reject, publishable). A draft with zero unsupported numbers, or an empty draft for empty results, is a valid result.
## Rung
rung: L1
One fast-model pass drafts from the result files; code matches numbers to locators. Escalate only on an unlocated number.
## Forbidden move
Upgrading the self-review into a verdict, or stating a claim as settled. Self-review overrates; the human owns the claim.
## Tool
tool: Bash:python3
scope: read
