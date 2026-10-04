---
name: support-draft
description: Use when a reply must answer one already-classified ticket intent with the policy line quoted. Quiet for classifying, refunds, or exceptions.
---
## Trigger
A classified intent with policy id and policy line is present. Quiet when no classification exists or the ask is to grant a refund or exception.
## Done-when
check: quote
`python3` check exits 0 only if the draft contains the classified policy line verbatim, printed as `quoted: <policy-id> line <n>`. A draft that cannot quote its line is not a pass; the result is `unsupported`.
## Rung
rung: L1
One fast-model pass drafts; code greps the draft for the exact policy line. Escalate only if the quote is missing.
## Forbidden move
Promise creep: the draft says or implies a refund, credit, waiver, or exception the policy line does not grant.
## Tool
tool: Bash:python3
scope: read
