---
name: markets-memo
description: Use when a one-page investment memo needs a thesis, an observable kill condition, and fact versus inference labelled. Quiet for orders, position sizing, or pure extraction.
---
## Trigger
Sourced facts exist and the ask is a thesis memo. Quiet when the ask is to buy, sell, or size a position.
## Done-when
check: human-only
A person reads the memo and confirms the kill condition names a metric, a threshold, and a date, and that every line is tagged fact or inference. No program can judge observability. The memo must contain no order and no size.
## Rung
rung: L3
A strong model drafts; a person checks the kill condition. Do not claim a pass without that read.
## Forbidden move
Writing a kill condition that cannot be observed (for example "if sentiment turns"), or adding an order or a size.
## Tool
tool: none
scope: none
