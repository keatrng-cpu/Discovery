---
name: markets-monitor
description: Use when a ticker card must be refreshed against the last card: add only the delta, expire stale claims, keep the kill condition. Quiet for a first-time memo or a full rewrite.
---
## Trigger
A previous card file and new material both exist. Quiet when there is no prior card.
## Done-when
check: state-diff
One command, one exit code: `python3 desk/card_check.py <old card> <new card>` (a program the desk would run; it does not exist in the repo yet). It runs `git diff --no-index --unified=0` on the two cards and reads the local date. Card format: claim lines read "claim | expires YYYY-MM-DD | text", the kill condition is one line starting "KILL:", added lines start "DELTA ". Each assertion is one clause:
- Compare: every added line starts "DELTA ".
- Expire: every removed line carries an expires date earlier than the local date, and no line left in the new card carries an expires date earlier than the local date.
- Kill: the new card holds the old "KILL:" line byte-equal.
- Delta only: a rewritten card fails.
An empty diff is a valid result only when the old card holds no expired claim; then the card is unchanged.
## Rung
rung: L1
Code diffs the cards and checks dates against the local date; one fast-model pass writes the delta lines. Escalate only if the diff shows lines outside the delta.
## Forbidden move
Rewriting the whole card, keeping a stale claim, or dropping the kill condition.
## Tool
tool: Bash:git
scope: read
