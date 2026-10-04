---
name: personal-admin-triage
description: Use when an inbox needs sorting by a stated rule, headers first. Quiet for replying, drafting, or any task with no rule given.
---
## Trigger
A mailbox or thread list is present and a triage rule (sender, label, subject, age) is stated. Quiet when no rule exists or the ask is to reply.
## Done-when
check: count
One command, triage-verify (a program the desk would run; not yet in the repo), reads the triage log and the header list and exits 0 only if all hold. The header-scan entry precedes the first open entry. Every open entry carries a non-empty reason. The opened thread ids equal the rule-marked header ids (symmetric difference 0), printed "opened: N/N". 0/0 is valid.
## Rung
rung: L0
A program alone reads the log. No model pass is needed to compare id sets.
## Forbidden move
Opening a thread the rule did not mark, opening before the header scan, or replying while triaging.
## Tool
tool: mcp__Gmail__search_threads
scope: read
