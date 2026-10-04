---
name: lab-protocols-repair
description: Use when a protocol graph fails its validator and exactly the failing node must be fixed. Quiet when the validator does not name a node, or for restyling a graph.
---
## Trigger
A graph and validator output that names a failing node id are both present. Quiet when the validator names no node: report "node: unnamed" and stop.
## Done-when
check: state-diff
One program, python3 repair-check.py (the desk would run it; it does not exist yet, so this is assisted), takes the before graph, the after graph, and the before and after validator outputs, and exits 0 with the exit code quoted. It asserts the named node's error line is absent from the after output with zero added error lines. It asserts every node other than the named one is byte-identical between the two graph files. A graph already clean with no edit is a valid result.
## Rung
rung: L1
One fast-model pass edits one node; the program does the checking. Escalate only if the node still fails after one edit.
## Forbidden move
Restyling the rest of the graph: reordering keys, renaming nodes, reformatting whitespace, or touching a node the validator did not name.
## Tool
tool: Bash:python3
scope: read
