---
name: personal-admin-triage
description: Use when an inbox needs sorting by a stated rule, headers first. Quiet for replying, drafting, or any task with no rule given.
---
## Trigger
A mailbox or thread list is present and a triage rule (sender, label, subject, age) is stated. Quiet when no rule exists or the ask is to reply.
## Done-when
check: count
Read headers only (sender, subject, date, labels) via search. A program reads the triage log and exits 0 only if: every opened thread id was marked by a named rule id, each has a non-empty "why opened" line, and opened N equals rule-marked N ("opened: N/N"). Zero marked and zero opened is a valid result and prints "opened: 0/0". No reply text appears in the log.
## Rung
rung: L0
Header listing and rule match are code. No model pass is needed. Escalate only if the rule is ambiguous, then ask the owner for the rule.
## Forbidden move
Opening a thread the rule did not mark, or replying while triaging. Opening on a hunch without a recorded reason is the failure.
## Tool
tool: mcp__Gmail__search_threads
scope: read
