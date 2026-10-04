---
name: software-analyze
description: Use when a failing path, stack trace, or traceback must be mapped to the entry file with a log line that proves it ran. Quiet for fixing, reproducing, or touring a repo.
---
## Trigger
A failing path, stack trace, or error log is present and the owning file is unknown. Quiet when the ask is to edit, to run tests, or to explain the whole repo.
## Done-when
check: quote
Output one record, and a program reads each field: (1) a log line quoted verbatim with its line number in the log file, read back with python3 (line N of the log equals the quote); (2) that line names the entry file, given as file:line from the trace, and the file:line exists in the tree; (3) the broken invariant quoted verbatim from a source line at a stated file:line; (4) a do-not-touch list of paths, each present in `git ls-files`. A log with no matching line is a valid result: write "unmatched" and stop; do not guess a file.

## Rung
rung: L1
Code greps the stack, the path and the log; one fast-model pass drafts the invariant and the do-not-touch list, then the program above reads every field. Escalate only if the quoted log line fails to match the named entry file.

## Forbidden move
Guessing a file from a noisy log that the grep did not return; naming a file with no quoted line.
## Tool
tool: Bash:python3
scope: read
Python reads the log line by number and the source line by file:line; `git ls-files` (read verb) lists the tree for the do-not-touch paths.
