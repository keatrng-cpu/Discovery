---
name: legal-diligence
description: Use when a deal's documents need an in-scope and not-read list with one row per issue. Quiet for single-document extraction.
---
## Trigger
A data room or document list and a stated scope are present. Quiet when scope is not stated.
## Done-when
check: count
One command, diligence-check (a program the desk would run; it does not exist yet), takes the document list, the read log and the issue sheet, and exits 0 only if every assertion holds. It prints the in-scope and not-read lists by document name, one per line, plus "in scope: N; read: R; not read: U". Assert N equals the in-scope names listed and equals R plus U. Assert a document with no read record is listed not-read, never implied-read. Assert each issue row has a unique issue id, exactly one issue, and a document name in the read set, with the printed row count equal to the distinct issue ids.
## Rung
rung: L1
A fast model reads and logs issues on one sheet, one row per issue with document name and quote locator; a program reconciles the counts and checks each row's document is in the read set. Escalate only when N differs from R plus U.
## Forbidden move
Implying a document was read because it sits in scope.
## Tool
tool: none
scope: none
gate: ABSENT sign (prepare the coverage sheet and stop; a lawyer signs before anyone relies on it)
