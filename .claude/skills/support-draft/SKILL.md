---
name: support-draft
description: Use when a reply must answer one already-classified ticket intent with the policy line quoted. Quiet for classifying, refunds, or exceptions.
---
## Trigger
A classified intent with policy id and policy line is present. Quiet when no classification exists or the ask is to grant a refund or exception.
## Done-when
check: quote
`python3` quote check exits 0 only if the draft contains the classified policy line verbatim, matching the entry at the cited `<file>:<n>`; it prints `quoted: <policy-id> line <n>`. A draft that cannot quote its line is not a pass; the result is `unsupported`. This is the only check. Promise creep and intent drift are not checked by it; a person reviews them, which is why status stays assisted. The check program is not written yet, so checkRunnable is false.
## Rung
rung: L1
One fast-model pass drafts; code checks the policy line is quoted verbatim. Escalate only if the check fails.
## Forbidden move
Promise creep: the draft says or implies a refund, credit, waiver, or exception the policy line does not grant.
## Tool
tool: Bash:python3
scope: read
