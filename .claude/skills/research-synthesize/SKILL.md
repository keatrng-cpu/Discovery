---
name: research-synthesize
description: Use when findings must be written up one claim per sentence with a source or an unsupported label. Quiet for fetching sources or for tracking changes over time.
---
## Trigger
Extracted, sourced findings exist and a written answer is wanted. Quiet when no sources have been gathered yet.
## Done-when
check: count
A script splits the answer into sentences and exits 0 only when every sentence carries exactly one source id or the literal label "unsupported" (a sentence with two source ids or two labels is two claims and fails), the first sentence begins "Answer:", every sentence beginning "Conflict:" comes after all non-conflict sentences, and the printed count "claims: N/N sourced-or-labeled" has N equal to the sentence count. An empty answer is valid: "claims: 0/0".
## Rung
rung: L1
A fast model writes; the sentence-count script checks. Lead with the answer, then conflicts. Escalate only if the count fails after one rewrite.
## Forbidden move
Keeping a sentence that has neither a source nor the unsupported label, or putting two claims in one sentence.
## Tool
tool: Bash:python3
scope: read
