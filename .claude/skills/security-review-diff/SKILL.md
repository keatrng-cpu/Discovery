---
name: security-review-diff
description: Use when a changed or flagged line needs its file, line, and reach written down. Quiet for reproducing an attack, exploit writing, or ranking.
---
## Trigger
A diff, branch, or scanner finding is present and the ask is to say where the risk sits and what it reaches. Defensive only. Quiet when the ask is to demonstrate, reproduce, or continue into an attack.
## Done-when
check: quote
Each item is exactly three parts: a quoted source line with `file:line` taken from `git diff` or `git show` output, one sentence naming what that line can reach (a file, a secret, a network call, a data store), then the word "STOP". The output has no reproduction steps, input strings, or attack sequence. Empty is valid: "diff: 0 items" when the diff has no security-relevant line. A line that cannot be quoted from git output is dropped, not paraphrased.
## Rung
rung: L1
One fast-model pass drafts reach from the quoted lines; git supplies the quotes. Escalate only if a quoted line fails to match git output.
## Forbidden move
Continuing past the reach sentence into how to trigger it: payload text, exploit steps, or a proof of concept. The stop is enforced by the harness, not by a reminder.
## Tool
tool: Bash:git
scope: read
