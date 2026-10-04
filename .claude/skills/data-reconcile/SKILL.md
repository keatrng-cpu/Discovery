---
name: data-reconcile
description: Use when two system extracts must be compared on one written metric definition. Quiet for blending or choosing a single number.
---
## Trigger
Two extracts and one written metric definition are present. Quiet when only one extract exists (report unsupported) or when the ask is for the number.
## Done-when
check: count
`python3` applies the written definition to both extracts and prints "total A: x", "total B: y", "unmatched keys: n" followed by each key with its source. Check: both totals printed, n equals the listed keys, and no averaged figure appears. Zero unmatched keys is valid; a missing extract is reported "unsupported" and exits 0.
## Rung
rung: L1
One fast-model pass maps columns to the definition; python3 totals and diffs the keys. Escalate only if the key column is ambiguous.
## Forbidden move
Averaging the two totals into one number, or reconciling with no written metric definition.
## Tool
tool: Bash:python3
scope: read
