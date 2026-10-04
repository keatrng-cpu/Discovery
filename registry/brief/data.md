# Shelf: data (data analysis; verbatim from the owner's spec)

## Short form
Data. Profile: rows, nulls, types, grain, flag id-used-as-measure, save. Clean: one field, one rule, counts before and after, dropped rows queryable. Hypothesis: comparison, slice, saved query, no chart yet. Chart: bind to that query, one labeled value matches, no second series. Anomaly: isolate, recompute, name row or day, no cause first. Reconcile: one metric definition, both totals, unmatched keys, do not average. Define: formula, grain, exclusion, human signs before queries.
Now: profile and one-field clean reliable. Define gated.

## Directive definitions
Profile. Count rows, nulls, and types. Name the grain. Flag a column that is an id used as a measure. Save the profile.
Clean. One field, one rule. Count rows before and after. Keep the dropped rows queryable. Do not clean a second field in the same directive.
Hypothesis. Write the comparison. Write the slice. Save the query. Do not add a chart yet.
Chart. Bind the chart to the query result. Match one labeled value to the query. Title states the comparison. No second series unless asked.
Anomaly. Isolate the slice. Recompute it. Name the row or day. Do not explain cause before the slice reruns.
Reconcile. Use one written metric definition. Show both system totals. List the unmatched keys. Do not average the totals.
Define. Write the formula. Write the grain. Write the exclusion. A human signs it before anyone queries.

## Status and ceiling
* Profile. Reliable. Counts, nulls, types, grain are tool output. Stays reliable.
* Clean. Reliable one field at a time. It cleans a second field if the directive is loose. High chance.
* Hypothesis. Assisted. Comparison and slice are easy. It jumps to a chart. Medium chance the saved-query rule holds.
* Chart. Assisted. Binding a chart to a query works. Decorative series are the failure. Medium-high chance.
* Anomaly. Assisted. Isolating a slice works. Cause stories arrive before the rerun. Medium chance.
* Reconcile. Assisted, high value. It lists unmatched keys if both extracts exist. It averages if asked for "the" number. Medium chance.
* Define. Assisted draft, gated. Formula and grain are writable. The signature stays human. Low chance the gate drops.
