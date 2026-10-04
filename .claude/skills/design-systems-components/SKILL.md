---
name: design-systems-components
description: Use when UI output may call only listed components and must record which one was used. Quiet for token values, page templates, or ban lists.
---
## Trigger
A component list exists and output is built from components. Quiet when no list is supplied: report "unsupported".
## Done-when
check: count
`python3` over the output prints "unlisted: 0" and a record line "component: <name>" for each use, exit 0. Any raw substitute (an element or markup standing in for a listed component) counts as unlisted and fails. An output using no components is a valid result: "unlisted: 0, used: 0".
## Rung
rung: L1
A fast model picks the component per slot; code counts unlisted use against the list. Same prompt must give the same component. Escalate only if the count is above 0.
## Forbidden move
Keeping the component list only in the prompt, so a raw substitute leaks through; the list must be what the tool exposes.
## Tool
tool: Bash:python3
scope: read
