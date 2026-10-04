---
name: scientific-manuscript
description: Use when result files must be drafted into manuscript text with a labeled self-review. Quiet for deciding whether the claim is true or publishable.
---
## Trigger
Result files and a figure exist and a draft is wanted. Quiet when no result files exist, or when the ask is a verdict on the science: a human owns the claim.
## Done-when
check: quote
One program scans the single draft file, body and self-review alike, and prints each flagged line with its line number; it passes when it flags zero lines. A line is flagged if it holds a number with no file:line locator in a result file, or a verdict or settled-claim word (accept, reject, publishable, proves, confirms, established). An empty draft for empty results is a valid result.
## Rung
rung: L1
One fast-model pass drafts from the result files; code matches numbers to locators and scans for verdict words. Head the self-review "DRAFT self-review". Escalate only on an unlocated number.
## Forbidden move
Upgrading the self-review into a verdict, or stating a claim as settled. Self-review overrates; the human owns the claim.
## Tool
tool: Bash:python3
scope: read
