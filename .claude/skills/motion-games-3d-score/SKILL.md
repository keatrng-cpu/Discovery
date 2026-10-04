---
name: motion-games-3d-score
description: Use when a contact sheet has been scored and the worst frame needs fixing and rescoring before any full render. Quiet without an external score.
---
## Trigger
A contact sheet with a per-frame score file from an external scorer. Quiet when no external score exists, or when the ask is the full render.
## Done-when
check: count
One program over contact.json, before.json, after.json and the threshold exits 0 only if: before.json names the worst-scoring frame; exactly that frame's entry differs in after.json (changed frames: 1) and no other; after.json carries its rescore; and render_started is false unless every rescore is at or above the threshold. Below threshold is a valid result and an unchanged rescore is reported, not hidden; no external score means unscored.
## Rung
rung: L1
One fast-model pass redraws the single worst frame; a program counts changed frames. Escalate only if the count is not 1.
## Forbidden move
Fixing more than the worst frame, or starting the full render before the threshold is met (a rescore that does not rise is reported, not hidden).
## Tool
tool: Bash:python3
scope: read
