---
name: motion-games-3d-time
description: Use when a single frame at a given time t must be drawn from a renderer that is a function of t. Quiet for full renders and generic video generators.
---
## Trigger
A time t and a renderer that takes t as its only time input. Quiet when no t-addressable renderer exists (generic video generator) or when the ask is a full render.
## Done-when
check: exit-code
Render the frame at t into `frame_t.png`, then `cmp frame_t.png expected_t.png` must exit 0; `expected_t.png` is the reference frame the brief gives for that t. One check: the frame at t matches the brief at t. No reference frame: report unchecked. A renderer that is not a function of t: report unsupported. Both are valid results.
## Rung
rung: L0
A program alone: call the renderer with t, then cmp. No model pass. Escalate only if cmp exits non-zero on a reference that should match.
## Forbidden move
Rendering the full sequence to reach frame t, or drawing any frame other than t (a second frame file in the output directory is the failure).
## Tool
tool: Bash:cmp
scope: read
