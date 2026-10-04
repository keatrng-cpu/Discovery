---
name: design-systems-components
description: Use when UI output may call only listed components and must record which one was used. Quiet for token values, page templates, or ban lists.
---
## Trigger
A component list exists and output is built from components. Quiet when no list is supplied: report "unsupported".
## Done-when
check: count
One python3 program takes the output of two runs of the same prompt plus the component list, and exits 0 only when every assertion holds: it prints "unlisted: N" with N equal to 0 for each run, prints a record line "component: <name>" for each use, treats any raw substitute (markup standing in for a listed component) as unlisted, and finds the same component names in both runs. An output using no components is a valid result: "unlisted: 0, used: 0".
## Rung
rung: L0
A program alone: the python3 count and run comparison decide pass or fail. No model pass.
## Forbidden move
Keeping the component list only in the prompt, so a raw substitute leaks through; the list must be what the tool exposes.
## Tool
tool: Bash:python3
scope: read
