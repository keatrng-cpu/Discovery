---
name: software-review
description: Use when a diff or pull request needs review comments that each quote a line. Quiet for applying fixes.
---
## Trigger
A diff or pull request is present. Quiet when asked to fix the code or to run tests.
## Done-when
check: quote
Every comment carries file:line and the quoted line text, and the quote appears verbatim at that line in `git diff` output. Any comment with no matching quote is dropped; zero surviving comments is a valid result: report "findings: 0".
## Rung
rung: L1
One fast-model pass drafts comments; code greps each quote against the diff. Comment type (logic, security, performance) is a label for the reader, not part of this check. Escalate only to a stronger verifier if a quote fails to match.
## Forbidden move
Posting a comment that cannot point at a line, or over-commenting style. Cross-file logic that no single line shows is reported as unsupported, not smoothed.
## Tool
tool: Bash:git
scope: read
