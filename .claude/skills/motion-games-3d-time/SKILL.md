---
name: motion-games-3d-time
description: Use when a single frame at a given time t must be drawn from a renderer that is a function of t. Quiet for full renders and generic video generators.
---
## Trigger
A time t and a renderer that takes t as its only time input. Quiet when no t-addressable renderer exists (generic video generator) or when the ask is a full render.
## Done-when
check: exit-code
Render the frame at t twice into two files; `cmp frame_t_a.png frame_t_b.png` exits 0 and the output directory holds exactly one frame file. A renderer that is not a function of t fails the cmp and the result is "unsupported", which is valid.
## Rung
rung: L0
A program alone: call the renderer with t, then cmp. No model pass. Escalate only if cmp exits non-zero on a renderer expected to be deterministic.
## Forbidden move
Rendering the full sequence to reach frame t, or drawing any frame other than t.
## Tool
tool: Bash:cmp
scope: read
