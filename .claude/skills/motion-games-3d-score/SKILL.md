---
name: motion-games-3d-score
description: Use when a contact sheet has been scored and the worst frame needs fixing and rescoring before any full render. Quiet without an external score.
---
## Trigger
A contact sheet with a per-frame score file from an external scorer. Quiet when no external score exists, or when the ask is the full render.
## Done-when
check: count
A program over before.json and after.json prints `changed frames: 1`, meaning only the worst-scoring frame's entry differs. That count is the single check. Below threshold is a valid result and no full render is started; the render gate is the Forbidden move, not a second check.
## Rung
rung: L1
One fast-model pass redraws the single worst frame; a program counts changed frames. Escalate only if the count is not 1.
## Forbidden move
Fixing more than the worst frame, or starting the full render before the threshold is met (a rescore that does not rise is reported, not hidden).
## Tool
tool: Bash:python3
scope: read
