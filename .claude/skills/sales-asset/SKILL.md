---
name: sales-asset
description: Use when a frame has won and one asset (page, email body, one-pager) is wanted for it. Quiet when no frame has won or when every frame is wanted.
---
## Trigger
A winning frame id is recorded and a brief naming the segment exists. Quiet when no frame has won, or when the ask covers several frames.
## Done-when
check: count
`python3 -c` over asset.md counts lines starting "frame:" and exits 0 only if the count is 1 and the id equals the winning id in state. It prints "frames: 1/1". With no winning frame it prints "frames: 0/0" and exits 0; no asset is written.
## Rung
rung: L1
One fast-model pass writes the single asset; the count is a program. Escalate only if the count reads above 1 after one regeneration.
## Forbidden move
Producing the other frames "for comparison", which is the waste this directive exists to prevent.
## Tool
tool: Bash:python3
scope: read
