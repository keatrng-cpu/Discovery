---
name: writing-draft
description: Use when an outline and a voice file are both present and prose is wanted. Quiet when either is missing or the ask is to shorten.
---
## Trigger
An outline file and a voice file are both present. Quiet when only one exists, or when the ask is cutting, channel change, or fact-checking.
## Done-when
check: count
`python3` over the draft, the outline, and the voice file exits 0 and prints "violations: 0": violations = paragraphs with no outline claim id or a repeated one (an unmapped paragraph is a new claim) + outline ids missing from the draft + hits of any phrase listed under the voice file's "Bans" heading (the banned defaults). One count, one exit code. The rest of the voice file is style a program cannot read; it stays a human read. A missing voice file is a valid result: stop and report "voice file absent".
## Rung
rung: L1
One fast-model pass writes the paragraphs under the voice file; a program counts the violations. Escalate only if the count stays above zero after two repairs.
## Forbidden move
Adding a claim that is not in the outline, to fill a paragraph or smooth a transition.
## Tool
tool: Bash:python3
scope: read
