---
name: support-draft
description: Use when a reply must answer one already-classified ticket intent with the policy line quoted. Quiet for classifying, refunds, or exceptions.
---
## Trigger
A classified intent with policy id and policy line is present. Quiet when no classification exists or the ask is to grant a refund or exception.
## Done-when
check: quote
One command with one exit code: `python3 desk/check_draft.py --draft draft.txt --intent intent.txt --policy-list <file>`. It does not exist yet, so checkRunnable is false and the program is what the desk would run. Inputs are the draft, the classified intent, and the policy id list. Exit 0 asserts the draft contains the classified policy line verbatim, matching the entry at the cited `<file>:<n>`, and prints `quoted: <policy-id> line <n>`. Exit 0 asserts every draft sentence answers only the classified intent. Exit 0 asserts the draft states or implies no refund, credit, waiver, or exception that the policy line does not grant. A draft that cannot quote its line is not a pass; the result is `unsupported`, which is valid.
## Rung
rung: L1
One fast-model pass drafts; code checks the policy line is quoted verbatim. Escalate only if the check fails.
## Forbidden move
Promise creep: the draft says or implies a refund, credit, waiver, or exception the policy line does not grant.
## Tool
tool: Bash:python3
scope: read
