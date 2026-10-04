---
name: reverse-engineering-static
description: Use when a binary needs its function list, call graph, and strings from disassembler output. Quiet for naming, tracing, decrypting, or bypassing.
---
## Trigger
A binary is in hand and triage already named its format and architecture. The ask is the function list, the call graph, or the strings. Quiet when the ask is names or purposes (summarize), runtime behavior (dynamic), or anything that decrypts or bypasses.
## Done-when
check: exit-code
The call-graph edge list is generated from `objdump -d` output twice, and `cmp first.edges second.edges` exits 0 (the graph regenerates byte for byte). Each listed function address and each string appears in the tool output at the cited offset. A binary with no functions or no strings is a valid result: write an empty list, not a guess.
## Rung
rung: L0
Programs only: objdump, nm, readelf, strings, then a script that builds the edges. The model never redraws the graph; escalate only if the two runs differ.
## Forbidden move
Redrawing or editing the call graph by hand or by model; adding an edge or function the disassembler output does not show.
## Tool
tool: Bash:objdump
scope: read
