---
name: motion-games-3d-level
description: Use when a level needs one change to terrain, light, character, or interaction, validated in the editor, reverted if the path breaks. Quiet for multi-class edits.
---
## Trigger
A level edit in exactly one change class: terrain, light, character, or interaction. Quiet when the ask spans classes or wants unattended level building.
## Done-when
check: state-diff
A program reads `level_classes.json` (change class to file globs) and `git diff --name-only`, and exits 0 only if every changed path matches the named class's globs and none match another class's. A path in two classes or none (for example a shared scene file) is reported "class not separable", not passed. An empty diff after a revert is valid. The editor path check is quoted separately; with no editor check the result is "unvalidated".
## Rung
rung: L1
One fast-model pass makes the single-class edit; the program confirms scope. Escalate only if a path is not separable.
## Forbidden move
Treating tool success as scene success: calling the level done because the edit command exited 0, or changing a second class in the same pass.
## Tool
tool: Bash:git
scope: read
