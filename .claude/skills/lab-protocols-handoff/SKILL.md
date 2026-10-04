---
name: lab-protocols-handoff
description: Use when a protocol graph must be written for a graph editor and a manual node edit resynced with untouched nodes preserved. Quiet for first-time graph drafting or hardware starts.
---
## Trigger
A graph file and an editor-format target are present, or a manually edited copy is present to resync. Quiet when there is no editor format: report "editor: absent" and stop.
## Done-when
check: state-diff
One program, python3 handoff-check.py (the desk would run it; it does not exist yet, so this is assisted), takes the resynced graph file, the editor-format file, and the expected projection (pre-edit graph with only the person's edits applied), and exits 0 with the exit code quoted. It asserts both files parse as their formats, so the editor can open the graph and the scientist can run either view. It asserts each file's node projection (id, action, params) equals the expected one, differing nodes: 0, count quoted, edited values present. No manual edit gives an identical projection.
## Rung
rung: L1
One fast-model pass maps the edit onto the graph; the program does the diff. Escalate only if an untouched node differs.
## Forbidden move
Rewriting untouched nodes on resync: regenerating the whole graph, renumbering ids, or reordering nodes.
## Tool
tool: Bash:python3
scope: read
