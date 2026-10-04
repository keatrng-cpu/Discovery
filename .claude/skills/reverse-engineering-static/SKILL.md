---
name: reverse-engineering-static
description: Use when a binary needs its function list, call graph, and strings from disassembler output. Quiet for naming, tracing, decrypting, or bypassing.
---
## Trigger
A binary is in hand and triage already named its format and architecture. The ask is the function list, the call graph, or the strings. Quiet when the ask is names or purposes (summarize), runtime behavior (dynamic), or anything that decrypts or bypasses.
## Done-when
check: exit-code
One combined output holding the function list, the call-graph edge list, and the strings is generated from `objdump -d` and `strings` output twice, and `cmp first.out second.out` exits 0 (all three regenerate byte for byte). A binary with no functions is a valid result: empty function and edge sections that regenerate empty, not a guess.
Status is assisted: the combined-output builder and a call-graph disassembler are not registered, so the program that builds the edges is written per task and the check is not runnable today.
## Rung
rung: L0
Programs only: objdump, nm, readelf, strings, then a script that builds the edges. The model never redraws the graph; escalate only if the two runs differ.
## Forbidden move
Redrawing or editing the call graph by hand or by model; adding an edge or function the disassembler output does not show; listing any function address or string the tool output does not contain.
## Tool
tool: Bash:objdump
scope: read
