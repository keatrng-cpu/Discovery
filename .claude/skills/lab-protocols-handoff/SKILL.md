---
name: lab-protocols-handoff
description: Use when a protocol graph must be written for a graph editor and a manual node edit resynced with untouched nodes preserved. Quiet for first-time graph drafting or hardware starts.
---
## Trigger
A graph file and an editor-format target are present, or a manually edited copy is present to resync. Quiet when there is no editor format: report "editor: absent" and stop.
## Done-when
check: state-diff
After `jq -e .` exits 0 on the editor-format file (quoted), a diff of the jq node projection (id, action, params) of the graph file against the editor-format file is empty, so the editor opens the graph and either view runs the same nodes. After resync, `git diff` between the pre-edit graph and the resynced graph shows changes only in person-edited nodes; untouched nodes that differ: 0; edited values appear. No manual edit gives an empty diff.
## Rung
rung: L1
One fast-model pass maps the edit onto the graph; git does the diff. Escalate only if an untouched node differs.
## Forbidden move
Rewriting untouched nodes on resync: regenerating the whole graph, renumbering ids, or reordering nodes.
## Tool
tool: Bash:git
scope: read
