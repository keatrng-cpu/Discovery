---
name: lab-protocols-repair
description: Use when a protocol graph fails its validator and exactly the failing node must be fixed. Quiet when the validator does not name a node, or for restyling a graph.
---
## Trigger
A graph and validator output that names a failing node id are both present. Quiet when the validator names no node: report "node: unnamed" and stop.
## Done-when
check: state-diff
`git diff` of the graph file shows changes only inside the named node's object; every other node and edge is byte-identical (changed lines outside that node: 0). The validator output is shown before and after, and the node id no longer appears in the failure list. Nothing to fix (validator already clean) is a valid result with an empty diff.
## Rung
rung: L1
One fast-model pass edits one node; git does the diff. Escalate only if the node still fails after one edit.
## Forbidden move
Restyling the rest of the graph: reordering keys, renaming nodes, reformatting whitespace, or touching a node the validator did not name.
## Tool
tool: Bash:git
scope: read
