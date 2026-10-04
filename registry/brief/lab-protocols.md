# Shelf: lab-protocols (lab protocols; verbatim from the owner's spec)

## Short form
Lab protocols. Transcribe: copy named method, keep units, mark gaps. Graph: one node per instrument action, parameters on the node, schema valid. Repair: failing node only, show validator. Campaign: bounds, stop, iteration log, person starts hardware. Handoff: editor can open the graph, manual edit resyncs, untouched nodes stay.
Now: simulated protocol graphs are strong. Hardware stays gated.

## Directive definitions
Transcribe. Copy steps from the named method. Keep quantities and units. Do not invent a missing step. Mark gaps as gaps.
Graph. One node per instrument action. Parameters on the node, not in prose. Edges only for real handoffs. Schema must validate.
Repair. Touch the failing node only. Revalidate the graph. Do not restyle the rest. Show the validator output.
Campaign. Set bounds before the loop. Set a stop condition. Log each iteration. A person starts the hardware.
Handoff. Write the graph the editor can open. Accept a manual node edit. Resync without rewriting untouched nodes. Scientist can run either view.

## Status and ceiling
Simulated labs have reported about 97% first-attempt protocol graphs, with a validator in the loop. Hardware is not that number.
* Transcribe. Reliable on a named method in text. It invents a step when the source skips one, unless gaps are required. High chance the gap rule holds.
* Graph. Assisted to reliable against a schema. Nodes and parameters validate. Fake edges are the failure. High chance.
* Repair. Reliable if the validator names the node. It restyles the graph if allowed to. High chance a one-node rule holds.
* Campaign. Assisted plan, gated start. Bounds and stop conditions can be written. A person starts hardware. Low chance that gate opens.
* Handoff. Assisted. Sync with a graph editor works in demos. Untouched-node preservation needs a diff. Medium chance.
