---
name: markets-memo
description: Use when a one-page investment memo needs a thesis and an observable kill condition. Quiet for orders, position sizing, or pure extraction.
---
## Trigger
Sourced facts exist and the ask is a thesis memo. Quiet when the ask is to buy, sell, or size a position.
## Done-when
check: human-only
A person reads the memo and confirms it states a thesis and that its kill condition is an observable naming a metric, a threshold, and a date. No program can judge observability.
## Rung
rung: L3
A strong model drafts; a person checks the thesis and kill condition. Do not claim a pass without that read.
## Forbidden move
Writing a kill condition that cannot be observed (for example "if sentiment turns"), or adding an order or a size. Tag every line fact or inference.
## Tool
tool: none
scope: none
gate: ABSENT broker, order (prepare the thesis and kill condition, stop; a person places any order or size)
