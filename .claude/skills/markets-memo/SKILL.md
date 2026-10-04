---
name: markets-memo
description: Use when a one-page investment memo needs a thesis and an observable kill condition. Quiet for orders, position sizing, or pure extraction.
---
## Trigger
Sourced facts exist and the ask is a thesis memo. Quiet when the ask is to buy, sell, or size a position.
## Done-when
check: exit-code
One command, one exit code: `python3 desk/memo_check.py <memo.md>` (a program the desk would run; it does not exist in the repo yet). Input is the memo file. Each assertion is one clause:
- Thesis: exactly one line starting "THESIS:".
- Kill condition: exactly one line starting "KILL:" that holds a metric name, a numeric threshold, and a YYYY-MM-DD date (regex).
- Tags: every other non-blank line starts "FACT:" or "INFERENCE:".
- No order, no size: no line contains an order or sizing verb or a share count or dollar amount to trade.
An empty memo, or a memo with no KILL: line, is a valid refusal result and exits 0 only when it prints "unsupported".
## Rung
rung: L1
One fast-model pass drafts the memo; the program does every check. Escalate only if the program fails for a reason other than a missing date.
## Forbidden move
Writing a kill condition that cannot be observed (for example "if sentiment turns"), or adding an order or a size.
## Tool
tool: none
scope: none
gate: ABSENT broker, order (prepare the thesis and kill condition, stop; a person places any order or size)
