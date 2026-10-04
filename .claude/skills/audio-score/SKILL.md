---
name: audio-score
description: Use when temp music must be placed under a rule file and the hook checked. Quiet for composing a new theme, cutting speech, or ordering takes.
---
## Trigger
A rule file (cue names, windows, levels) and existing music assets are present. Quiet when the ask is to compose or generate a theme; that is outside this directive.
## Done-when
check: exit-code
A python3 script reads the placement list and the rule file and exits 0 only if the hook cue starts and ends inside its rule window and uses an asset the rule file names; it prints "hook: ok" or "hook: <cue> outside <start>-<end>". Only the hook is checked; other cues are not claimed. An unplaced hook is a valid result and prints "hook: absent".
## Rung
rung: L1
A fast-model pass proposes temp placements from the rules; code checks the hook window. Escalate only if the hook check fails twice.
## Forbidden move
Composing or generating a new theme to fill the hook, or placing a cue the rule file does not name.
## Tool
tool: Bash:python3
scope: read
