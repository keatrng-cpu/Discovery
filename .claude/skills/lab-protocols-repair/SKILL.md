---
name: lab-protocols-repair
description: Use when a protocol graph fails its validator and exactly the failing node must be fixed. Quiet when the validator does not name a node, or for restyling a graph.
---
## Trigger
A graph and validator output that names a failing node id are both present. Quiet when the validator names no node: report "node: unnamed" and stop.
## Done-when
check: state-diff
Re-run the validator on the repaired graph and save its output. A diff of validator output before vs after (git diff --no-index) is quoted, with the re-run exit code: the named node's error line is removed and added error lines: 0. A graph already clean gives an empty diff and is a valid result.
## Rung
rung: L1
One fast-model pass edits one node; the validator and git do the checking. Escalate only if the node still fails after one edit.
## Forbidden move
Restyling the rest of the graph: reordering keys, renaming nodes, reformatting whitespace, or touching a node the validator did not name.
## Tool
tool: Bash:git
scope: read
