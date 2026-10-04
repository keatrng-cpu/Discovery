---
name: research-monitor
description: Use when a saved research memo file must be refreshed against new sources with stale claims expired. Quiet for a first-time memo or when no memo file exists.
---
## Trigger
A prior memo exists as a file with a date and a half-life in days on each claim. Quiet when there is no memo file, because there is nothing to diff.
## Done-when
check: state-diff
Two readings must agree. Clock: a python3 date computation (claim date plus half-life days against today, never a model's judgment) prints the expired claim ids; every printed id has an added line marked "expired" and no unprinted id has one. Diff: `git diff --numstat` of the memo file reports 0 deleted lines, so the old conclusion stays visible and a changed conclusion appears as an added line marked "changed" beneath it; every source id on an added line is absent from the memo at HEAD (`git show HEAD:<memo>`), so only new sources were added. No new sources and no expiries is a valid result: an empty diff.
## Rung
rung: L1
Code runs the clock and the diff; one fast-model pass reads new sources only. Escalate only when the diff touches an unexpired claim.
## Forbidden move
Deciding by model judgment that a claim has expired or is still fresh, or rewriting the memo whole so the old conclusion disappears.
## Tool
tool: Bash:git
scope: read
