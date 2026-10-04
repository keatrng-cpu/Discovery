---
name: strategy-compress
description: Use when a plan, memo or thread must be cut to its assumptions and kill conditions. Quiet for summaries, rewrites or any ask to keep detail.
---
## Trigger
A source document and a request to compress it to assumptions and kill conditions. Quiet when the ask is a general summary, a rewrite, or a framing task.
## Done-when
check: count
`python3` over the output and the input prints "assumptions: A", "kill: K" and "other: 0". A and K count lines starting "A:" and "K:"; other counts every non-blank line that starts with neither, and any other > 0 exits 1 (the rest must be cut). Each A:/K: line carries a locator (source line or section) and a quote that appears verbatim in the input. An input that states no assumption or no kill condition is a valid result: write "assumptions: 0" or "kill: 0" and do not invent one. Exit 0 only if other is 0 and every quote matches the input.
## Rung
rung: L1
A fast model lists the lines; a script counts them, rejects any kept line that is not A: or K:, and checks each quote appears in the source.
## Forbidden move
Keeping a line that is neither a stated assumption nor a kill condition, or inventing an unstated assumption. An assumption not stated does not exist.
## Tool
tool: Bash:python3
scope: read
