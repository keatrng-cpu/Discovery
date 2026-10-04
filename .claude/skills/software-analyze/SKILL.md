---
name: software-analyze
description: Use when a failing path, stack trace, or traceback must be mapped to the entry file, the broken invariant, and the files not to touch. Quiet for fixing, reproducing, or touring a repo.
---
## Trigger
A failing path, stack trace, or error log is present and the owning file is unknown. Quiet when the ask is to edit, to run tests, or to explain the whole repo.
## Done-when
check: quote
The map names four items, each with a locator: the entry file taken from the failing path (file:line quoted from the trace), the one invariant the bug breaks, the list of files the change must not touch, and one log line quoted verbatim with its line number in the log file that proves the entry file ran. A log with no matching line is a valid result: write "unmatched" and stop; do not guess a file.
## Rung
rung: L1
Code greps the stack and the path; one fast-model pass names the invariant. Escalate only if the quoted log line fails to match the named entry file.
## Forbidden move
Guessing a file from a noisy log that the grep did not return; naming a file with no quoted line.
## Tool
tool: Bash:git
scope: read
