---
name: legal-compare
description: Use when a contract must be diffed against the house paper clause by clause. Quiet for single-clause extraction or drafting edits.
---
## Trigger
A counterparty draft and a house paper are both present. Quiet when either is missing.
## Done-when
check: count
The house paper clause list is the denominator. Each house clause yields exactly one row with status matched, changed, or missing; no row reads "fine" for silence. Output prints "rows: N; missing: M; changed: C; matched: K" with N equal to M+C+K and equal to the house clause count.
## Rung
rung: L1
A fast model classifies each clause and, for changed rows, shows both texts with section locators (reviewer aid, not part of the check); a program checks counts. Escalate only when the totals do not reconcile.
## Forbidden move
Treating a missing clause as fine, or dropping a row because the draft is silent.
## Tool
tool: Bash:python3
scope: read
