---
name: legal-diligence
description: Use when a deal's documents need an in-scope and not-read list with one row per issue. Quiet for single-document extraction.
---
## Trigger
A data room or document list and a stated scope are present. Quiet when scope is not stated.
## Done-when
check: count
Two lists print by document name, one per line: in-scope documents and not-read documents. A summary line "in scope: N; read: R; not read: U" prints with N equal to the number of in-scope names listed and equal to R plus U. A document with no read record is listed not-read, never implied-read. One sheet holds the issues: each row has a unique issue id and exactly one issue; every row's document name is in the read set (a not-read document has no row), and the printed row count equals the number of distinct issue ids.
## Rung
rung: L1
A fast model reads and logs issues on one sheet, one row per issue with document name and quote locator; a program reconciles the counts and checks each row's document is in the read set. Escalate only when N differs from R plus U.
## Forbidden move
Implying a document was read because it sits in scope.
## Tool
tool: none
scope: none
gate: ABSENT sign (prepare the coverage sheet and stop; a lawyer signs before anyone relies on it)
