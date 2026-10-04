---
name: motion-games-3d-still
description: Use when one frame of one subject is asked for and a score is wanted before any animation. Quiet for motion, multi-frame renders, or engine edits.
---
## Trigger
A request for a single frame with one named subject, to be scored. Quiet when the ask is to animate, render a sequence, or touch a level or engine project.
## Done-when
check: schema
`jq -e '(.frames|length)==1 and (.subject|type=="string") and (.score|type=="number")' still.json` exits 0, where still.json names the one frame file and its score from an external scorer. If no scorer ran, still.json carries "score": null and the result is reported as unscored; that is a valid result. A human score is recorded as assisted, never as a pass.
## Rung
rung: L1
One fast-model pass drafts the frame spec for the single subject; jq validates the record. Escalate only when the record fails validation.
## Forbidden move
Animating, or adding a second subject or second frame, before the still is scored. Do not write a score the scorer did not return.
## Tool
tool: Bash:jq
scope: read
