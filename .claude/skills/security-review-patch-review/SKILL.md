---
name: security-review-patch-review
description: Use when a proposed fix must be checked for whether the quoted vulnerable line actually changed. Quiet for writing the fix or opening the fix task.
---
## Trigger
A quoted finding with file:line and a proposed patch (branch, commit, or diff) are both present. Quiet when asked to write the fix, apply it, or open the fix task: a human opens that.
## Done-when
check: state-diff
`git diff <base>..<head> -- <file>` is run and the result is one of: "changed: <quoted old line> -> <quoted new line>" with hunk locator, or "unchanged: <quoted line> at <file>:<line>". An empty diff is a valid result and reads "unchanged". A moved or renamed line that cannot be matched is reported "unmatched", not changed.
## Rung
rung: L0
The diff is a program. No model judgement of whether the fix is good; only whether the quoted line changed.
## Forbidden move
Declaring the vulnerability fixed because the patch looks plausible, without a diff hunk touching the quoted line.
## Tool
tool: Bash:git
scope: read
