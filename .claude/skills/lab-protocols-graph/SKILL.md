---
name: lab-protocols-graph
description: Use when transcribed protocol steps must become a node graph with one node per instrument action and parameters on the node. Quiet for copying a method or for starting hardware.
---
## Trigger
Transcribed steps (with GAPs kept) and a graph schema are present, and the ask is a graph. Quiet when no schema is supplied: report "schema: absent" and stop.
## Done-when
check: schema
A jq -e filter encoding the supplied schema's required node fields (id, action, params as an object, source step locator) and edge fields (from and to each equal an existing node id; handoff names the material or output passed) exits 0 over the graph file; the exit code is quoted. An edge with no handoff field or a dangling id fails the filter. One node per instrument action; every parameter is a field on its node, none in prose. A GAP stays a GAP field and is not filled. An empty step list yields an empty graph and empty edge list, and the filter exits 0. Full JSON Schema validation needs a validator that is not registered.
## Rung
rung: L1
One fast-model pass drafts nodes and edges; a program validates. Escalate only on validator failure that repair cannot clear.
## Forbidden move
Fake edges: linking nodes only because they are adjacent in the text, or putting parameters in a description string.
## Tool
tool: Bash:jq
scope: read
