---
name: strategy-compress
description: Use when a plan, memo or thread must be cut to its assumptions and kill conditions. Quiet for summaries, rewrites or any ask to keep detail.
---
## Trigger
A source document and a request to compress it to assumptions and kill conditions. Quiet when the ask is a general summary, a rewrite, or a framing task.
## Done-when
check: count
`python3` over the output prints "assumptions: A" and "kill: K" where A and K are the counts of lines starting "A:" and "K:", each line carries a locator (source line or section) and a quote taken from the input, and nothing else is kept. An input that states no assumption or no kill condition is a valid result: write "assumptions: 0" or "kill: 0" and do not invent one. Exit 0 only if every kept line quotes the input.
## Rung
rung: L1
A fast model lists the lines; a script counts them and checks each locator quote appears in the source. Escalate only if a quote fails to match.
## Forbidden move
Keeping a line that is neither a stated assumption nor a kill condition, or inventing an unstated assumption. An assumption not stated does not exist.
## Tool
tool: Bash:python3
scope: read
