---
name: lab-protocols-handoff
description: Use when a protocol graph must be written for a graph editor and a manual node edit resynced with untouched nodes preserved. Quiet for first-time graph drafting or hardware starts.
---
## Trigger
A graph file and an editor-format target are present, or a manually edited copy is present to resync. Quiet when there is no editor format: report "editor: absent" and stop.
## Done-when
check: state-diff
After resync, `git diff` between the pre-edit graph and the resynced graph shows changes only in the nodes the person edited; the count of untouched nodes that differ is 0 (byte-identical). The edited node's new values appear in the output. No manual edit is a valid result with an empty diff.
## Rung
rung: L1
One fast-model pass maps the edit onto the graph; git does the diff. Escalate only if an untouched node differs.
## Forbidden move
Rewriting untouched nodes on resync: regenerating the whole graph, renumbering ids, or reordering nodes.
## Tool
tool: Bash:git
scope: read
