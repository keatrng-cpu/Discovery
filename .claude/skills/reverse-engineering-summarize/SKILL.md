---
name: reverse-engineering-summarize
description: Use when a function in a stripped binary needs a proposed name or summary, each backed by a cited string, call, or trace line. Quiet for listing functions or any name without evidence.
---
## Trigger
A function from disassembly or decompilation needs a name or a one-line purpose. Quiet when the ask is only listing functions, or decrypting or bypassing anything.
## Done-when
check: quote
Each proposed name carries a quoted evidence line: a string with its offset, a call target with its address, or a trace line with its line number. A program confirms the quote appears in the tool output at that locator. A function with no evidence stays "unnamed", a valid result. The check proves the evidence exists, not that the name is right.
## Rung
rung: L1
One fast-model pass proposes names from the evidence; code checks each quote. Exact naming is a measured miss (about 2 to 7 percent), so report unnamed rather than smooth it.
## Forbidden move
Giving a plausible name with no string, call, or trace behind it.
## Tool
tool: Bash:strings
scope: read
