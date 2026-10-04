---
name: legal-extract
description: Use when one named clause type must be pulled from a contract with its quote and section. Quiet for scoring, comparing, or drafting.
---
## Trigger
A contract file and one named clause type (for example indemnity or termination) are present. Quiet when no clause type is named, or when the ask is risk, compare, or edits.
## Done-when
check: quote
Each result row has a verbatim quote that is a substring of the source text and a section locator (section number, page, line). An empty result is valid: print "clause: none found in <sections searched>" and pass. One clause type per pass; a second type is a second pass.
## Rung
rung: L1
A fast model finds the clause; a program string-matches each quote against the source and confirms the locator. Escalate only when a quote fails the substring match.
## Forbidden move
Paraphrasing instead of quoting, or filling an empty result with a near clause. Write "none found" instead.
## Tool
tool: Bash:python3
scope: read
