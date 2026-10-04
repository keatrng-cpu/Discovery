---
name: markets-monitor
description: Use when a ticker card must be refreshed against the last card: add only the delta, expire stale claims, keep the kill condition. Quiet for a first-time memo or a full rewrite.
---
## Trigger
A previous card file and new material both exist. Quiet when there is no prior card.
## Done-when
check: state-diff
`git diff --no-index --unified=0 <old card> <new card>` is parsed by a program against the card format: claim lines read "claim | expires YYYY-MM-DD | text", the kill condition is one line starting "KILL:", added lines start "DELTA ". Pass only if every added line starts "DELTA ", every removed line carries an expires date earlier than the clock date, and no "KILL:" line is removed or changed (new card still holds the old KILL: line byte-equal). A removed line that is not expired, or a rewritten card, fails. An empty diff is a valid result: the card is unchanged.
## Rung
rung: L1
Code diffs the cards and checks dates against the clock; one fast-model pass writes the delta lines. Escalate only if the diff shows lines outside the delta.
## Forbidden move
Rewriting the whole card, keeping a stale claim, or dropping the kill condition.
## Tool
tool: Bash:git
scope: read
