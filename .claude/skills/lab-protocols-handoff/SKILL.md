---
name: lab-protocols-handoff
description: Use when a protocol graph must be written for a graph editor and a manual node edit resynced with untouched nodes preserved. Quiet for first-time graph drafting or hardware starts.
---
## Trigger
A graph file and an editor-format target are present, or a manually edited copy is present to resync. Quiet when there is no editor format: report "editor: absent" and stop.
## Done-when
check: state-diff
Build the expected node projection (id, action, params) from the pre-edit graph with only the person's edits applied. A diff of that expected projection against the jq projection of the resynced graph file and of the editor-format file is empty for both, so the scientist can run either view. Differing nodes: 0, count quoted; edited values appear. No manual edit gives an empty diff. The graph editor connector is absent, so opening in the editor is not checked.
## Rung
rung: L1
One fast-model pass maps the edit onto the graph; git and jq do the diff. Escalate only if an untouched node differs.
## Forbidden move
Rewriting untouched nodes on resync: regenerating the whole graph, renumbering ids, or reordering nodes.
## Tool
tool: Bash:git
scope: read
