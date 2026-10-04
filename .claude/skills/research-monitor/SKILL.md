---
name: research-monitor
description: Use when a saved research memo file must be refreshed against new sources with stale claims expired. Quiet for a first-time memo or when no memo file exists.
---
## Trigger
A prior memo exists as a file with a date and a half-life in days on each claim. Quiet when there is no memo file, because there is nothing to diff.
## Done-when
check: exit-code
One command, one exit code: `python3 memo_monitor.py <memo>`. It does not exist in the repo yet; it is the program the desk would run, so the check is not runnable today.
It computes expiry in code from each claim's date plus half-life days against today, and fails if an expired claim lacks an added line marked "expired" or an unexpired claim has one.
It reads the memo's deleted-line count from the diff against HEAD and fails unless it is 0, so the old conclusion stays visible.
It fails unless a changed conclusion appears as an added line marked "changed" beneath the old one.
It fails if a source id on an added line is already in the memo at HEAD, so only new sources are added.
No new sources and no expiries is valid: an empty diff exits 0.
## Rung
rung: L1
Code runs the clock and the diff; one fast-model pass reads new sources only. Escalate only when the diff touches an unexpired claim.
## Forbidden move
Deciding by model judgment that a claim has expired or is still fresh, or rewriting the memo whole so the old conclusion disappears.
## Tool
tool: Bash:python3
scope: read
