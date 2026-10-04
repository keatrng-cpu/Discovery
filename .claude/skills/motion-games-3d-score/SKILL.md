---
name: motion-games-3d-score
description: Use when a contact sheet has been scored and the worst frame needs fixing and rescoring before any full render. Quiet without an external score.
---
## Trigger
A contact sheet with a per-frame score file from an external scorer. Quiet when no external score exists, or when the ask is the full render.
## Done-when
check: count
After the fix, `python3 -c` over before.json and after.json prints "changed frames: 1" (only the worst-scoring frame's entry differs) and the rescored worst frame is higher than before. The full render stays blocked until the score file meets the stated threshold; below threshold is a valid result and no render is started.
## Rung
rung: L1
One fast-model pass redraws the single worst frame; a program counts changed frames and compares scores. Escalate only if the rescore does not rise.
## Forbidden move
Fixing more than the worst frame, or starting the full render before the threshold is met.
## Tool
tool: Bash:python3
scope: read
