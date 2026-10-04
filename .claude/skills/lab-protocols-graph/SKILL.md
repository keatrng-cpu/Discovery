---
name: lab-protocols-graph
description: Use when transcribed protocol steps must become a node graph with one node per instrument action and parameters on the node. Quiet for copying a method or for starting hardware.
---
## Trigger
Transcribed steps (with GAPs kept) and a graph schema are present, and the ask is a graph. Quiet when no schema is supplied: report "schema: absent" and stop.
## Done-when
check: schema
The graph JSON validates against the supplied schema (validator exit 0, output quoted). One node per instrument action; every parameter is a field on its node, none live in prose. Every edge joins two nodes with a real handoff named in the source; a count of edges with no source step is 0. A GAP stays a GAP node field and is not filled. An empty step list yields an empty graph that validates.
## Rung
rung: L1
One fast-model pass drafts nodes; a program validates and counts edges. Escalate only on validator failure that repair cannot clear.
## Forbidden move
Fake edges: linking nodes only because they are adjacent in the text, or putting parameters in a description string.
## Tool
tool: Bash:jq
scope: read
