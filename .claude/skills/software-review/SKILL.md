---
name: software-review
description: Use when a diff or pull request needs review comments that each quote a line. Quiet for applying fixes.
---
## Trigger
A diff or pull request is present. Quiet when asked to fix the code or to run tests.
## Done-when
check: quote
One command, `python3 review_check.py comments.json --diff`, with one exit code. It does not exist in the repo yet: it is the program the desk would run against `git diff` output. Input: the comment list. It exits 0 only if every surviving comment is labeled logic, security, or performance; carries file:line and a quoted line; and the quote appears verbatim at that line in the diff. Any comment with another label (style) or no matching quote is dropped. Zero surviving comments is a valid result: it prints "findings: 0" and exits 0.
## Rung
rung: L1
One fast-model pass drafts comments; code greps each quote against the diff. Comment type (logic, security, performance) is a label for the reader, not part of this check. Escalate only to a stronger verifier if a quote fails to match.
## Forbidden move
Posting a comment that cannot point at a line, or over-commenting style. Cross-file logic that no single line shows is reported as unsupported, not smoothed.
## Tool
tool: Bash:git
scope: read
