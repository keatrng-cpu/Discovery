---
name: motion-games-3d-level
description: Use when a level needs one change to terrain, light, character, or interaction, validated in the editor, reverted if the path breaks. Quiet for multi-class edits.
---
## Trigger
A level edit in exactly one change class: terrain, light, character, or interaction. Quiet when the ask spans classes or wants unattended level building.
## Done-when
check: state-diff
`git diff --name-only` lists only files belonging to the one named change class, and the editor path check result is quoted. If no editor check ran, the result is "unvalidated"; a green tool exit alone is not a pass. A broken path means `git checkout -- <files>` restores the prior state, shown by an empty `git diff`.
## Rung
rung: L1
One fast-model pass makes the single-class edit; git diff confirms scope. Escalate only if the diff crosses classes.
## Forbidden move
Treating tool success as scene success: calling the level done because the edit command exited 0, or changing a second class in the same pass.
## Tool
tool: Bash:git
scope: read
