---
name: software-analyze
description: Use when a failing path, stack trace, or traceback must be mapped to the entry file with a log line that proves it ran. Quiet for fixing, reproducing, or touring a repo.
---
## Trigger
A failing path, stack trace, or error log is present and the owning file is unknown. Quiet when the ask is to edit, to run tests, or to explain the whole repo.
## Done-when
check: quote
One log line is quoted verbatim with its line number in the log file, and that line names the entry file taken from the failing path (file:line from the trace). `grep -n` of the quoted text in the log returns that same line number. A log with no matching line is a valid result: write "unmatched" and stop; do not guess a file.
## Rung
rung: L1
Code greps the stack and the path and the log; one fast-model pass drafts the invariant and the do-not-touch list as plain notes, which this directive does not check. Escalate only if the quoted log line fails to match the named entry file.
## Forbidden move
Guessing a file from a noisy log that the grep did not return; naming a file with no quoted line.
## Tool
tool: Bash:git
scope: read
