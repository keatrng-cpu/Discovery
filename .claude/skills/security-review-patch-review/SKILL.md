---
name: security-review-patch-review
description: Use when a proposed fix must be checked for whether the quoted vulnerable line actually changed. Quiet for writing the fix or opening the fix task.
---
## Trigger
A quoted finding with file:line and a proposed patch (branch, commit, or diff) are both present. Quiet when asked to write the fix, apply it, or open the fix task: a human opens that.
## Done-when
check: state-diff
Run `git diff -U0 <base>..<head> -- <file>` and read it against the quoted file:line. Exactly one verdict:
- "changed: <old> -> <new>" with the @@ hunk locator, when a hunk covers the line and its "-" line equals the quote.
- "unchanged: <quote> at <file>:<line>", when no hunk covers it. An empty diff is valid and reads unchanged.
- "unmatched", when the base line at file:line is not the quote.
## Rung
rung: L0
The diff is a program. No model judgement of whether the fix is good; only whether the quoted line changed.
## Forbidden move
Opening, filing, or drafting the fix task, issue, or pull request, so the human hand-off drops out. Also declaring the vulnerability fixed from a plausible patch without a diff hunk touching the quoted line.
## Tool
tool: Bash:git
scope: read
No write tool is used here. A person opens the fix task; the verdict is reported and the work stops.
