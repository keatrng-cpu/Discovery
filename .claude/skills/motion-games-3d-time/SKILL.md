---
name: motion-games-3d-time
description: Use when a single frame at a given time t must be drawn from a renderer that is a function of t. Quiet for full renders and generic video generators.
---
## Trigger
A time t and a renderer that takes t as its only time input. Quiet when no t-addressable renderer exists (generic video generator) or when the ask is a full render.
## Done-when
check: exit-code
Render the frame at t into an empty out/ directory as frame_t.png; one program exits 0 only if out/ holds exactly one file (frame_t.png, count 1, so no full render and no other frame) and cmp out/frame_t.png expected_t.png exits 0, where expected_t.png is the brief's reference frame for that t; no reference frame means unchecked, and a renderer that is not a function of t is reported unsupported, both valid results. One check: only frame t exists and it matches the brief at t.
## Rung
rung: L0
A program alone: call the renderer with t, then cmp. No model pass. Escalate only if cmp exits non-zero on a reference that should match.
## Forbidden move
Rendering the full sequence to reach frame t, or drawing any frame other than t (a second frame file in the output directory is the failure).
## Tool
tool: Bash:cmp
scope: read
