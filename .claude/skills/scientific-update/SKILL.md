---
name: scientific-update
description: Use when an assay result forces a revision of an existing hypothesis: cite the result, drop the failed branch, keep the rest, propose one next measurement.
---
## Trigger
An old hypothesis record and a result file are both present. Quiet when there is no result file yet (nothing forces a change) or when a new hypothesis from scratch is wanted.
## Done-when
check: quote
One program reads one update record (JSON) with fields cited, dropped, kept, next_measurements, plus the old hypothesis record and the result file. It passes only if: every cited entry's quote equals the text at its file:line locator in the result file; every old branch id is in exactly one of dropped or kept; every dropped branch points at a cited quote; len(next_measurements) is at most 1. A quote not at its locator, an unplaced branch, or two or more proposed measurements fails. No change forced (dropped empty, next_measurements empty) is a valid result.
## Rung
rung: L1
One fast-model pass writes the update record (shape only, not the check); a program resolves quote locators and counts branches and measurements. Escalate only on a failed check.
## Forbidden move
Keeping a dead branch in the hypothesis because it was the old one, or citing a result that is not in the file, or proposing more than the next measurement.
## Tool
tool: Bash:python3
scope: read
