---
name: data-anomaly
description: Use when an odd row or day needs isolating, recomputing and naming before any explanation. Quiet for explaining causes or fixing data.
---
## Trigger
A metric spike, dip or odd value with a data file or query. Quiet when the ask is why it happened; isolate first.
## Done-when
check: count
`python3` filters the slice, recomputes the metric on it, and prints "anomaly: <row id or date>" with the recomputed value and the original value. Check: slice row count is above 0 and both values are printed, or the output says "anomaly: none" and exits 0.
## Rung
rung: L1
One fast-model pass proposes the slice; python3 reruns it. Escalate only if the rerun disagrees with the original value.
## Forbidden move
Offering a cause story before the slice has rerun (a rule for the writer; the count check does not read it).
## Tool
tool: Bash:python3
scope: read
