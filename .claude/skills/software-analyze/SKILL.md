---
name: software-analyze
description: Use when a failing path, stack trace, or traceback must be mapped to the entry file with a log line that proves it ran. Quiet for fixing, reproducing, or touring a repo.
---
## Trigger
A failing path, stack trace, or error log is present and the owning file is unknown. Quiet when the ask is to edit, to run tests, or to explain the whole repo.
## Done-when
check: quote
One command, `python3 analyze_check.py record.json --log app.log --repo .`, with one exit code. It does not exist in the repo yet: it is the program the desk would run. Inputs: the record, the log, the repo. It exits 0 only if the quoted log line sits verbatim at its stated line number in the log; that line names the entry file given as file:line from the trace, and the file:line exists in the tree; the broken invariant is quoted verbatim from a source line at a stated file:line; each do-not-touch path is listed by `git ls-files`. A log with no matching line is a valid result: the record says "unmatched", names no file, and the command exits 0.

## Rung
rung: L1
Code greps the stack, the path and the log; one fast-model pass drafts the invariant and the do-not-touch list, then the program above reads every field. Escalate only if the quoted log line fails to match the named entry file.

## Forbidden move
Guessing a file from a noisy log that the grep did not return; naming a file with no quoted line.
## Tool
tool: Bash:python3
scope: read
Python reads the log line by number and the source line by file:line; `git ls-files` (read verb) lists the tree for the do-not-touch paths.
