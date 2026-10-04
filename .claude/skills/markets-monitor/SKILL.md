---
name: markets-monitor
description: Use when a ticker card must be refreshed against the last card: add only the delta, expire stale claims, keep the kill condition. Quiet for a first-time memo or a full rewrite.
---
## Trigger
A previous card file and new material both exist. Quiet when there is no prior card.
## Done-when
check: state-diff
The diff between the old and new card shows only added delta lines and removed expired lines; every claim carries a date and any older than the stated expiry is gone; the kill condition line is present and unchanged unless a delta changes it. An empty delta is a valid result: the card is unchanged.
## Rung
rung: L1
Code diffs the cards and checks dates against the clock; one fast-model pass writes the delta lines. Escalate only if the diff shows lines outside the delta.
## Forbidden move
Rewriting the whole card, keeping a stale claim, or dropping the kill condition.
## Tool
tool: Bash:git
scope: read
