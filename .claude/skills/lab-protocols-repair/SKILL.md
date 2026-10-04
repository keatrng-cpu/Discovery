---
name: lab-protocols-repair
description: Use when a protocol graph fails its validator and exactly the failing node must be fixed. Quiet when the validator does not name a node, or for restyling a graph.
---
## Trigger
A graph and validator output that names a failing node id are both present. Quiet when the validator names no node: report "node: unnamed" and stop.
## Done-when
check: state-diff
`git diff -U0` of the graph file, with each hunk mapped to the named node's line range by program, shows changed lines outside that node: 0; the count is quoted. The validator output that named the node is an input to the skill, not a second check. A graph already clean gives an empty diff and is a valid result.
## Rung
rung: L1
One fast-model pass edits one node; git does the diff. Escalate only if the node still fails after one edit.
## Forbidden move
Restyling the rest of the graph: reordering keys, renaming nodes, reformatting whitespace, or touching a node the validator did not name.
## Tool
tool: Bash:git
scope: read
