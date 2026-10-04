---
name: writing-draft
description: Use when an outline with claim ids and a voice file are both present and prose is wanted. Quiet when either is missing or the ask is to shorten.
---
## Trigger
An outline file with claim ids and a voice file are both present. Quiet when only one exists, or when the ask is cutting, channel change, or fact-checking.
## Done-when
check: count
`python3` over the draft, the outline, and the voice file exits 0 and prints "violations: 0": one check, mapping against the outline file plus the voice file's ban list. violations = banned-default phrases (lines under the voice file's "Bans" heading) that occur in the draft + paragraphs carrying zero or more than one outline id tag (a paragraph with two claims or an untagged paragraph) + tags that are not outline ids (an unmapped paragraph is a new claim) + outline ids used more than once + outline ids missing from the draft. A new claim hidden inside a correctly tagged paragraph, and voice style beyond the ban list, are not detectable by program and stay a human read. A missing voice file is a valid result: stop and report "voice file absent".
## Rung
rung: L1
One fast-model pass writes one tagged paragraph per outline claim under the voice file; a program counts mapping violations. Escalate only if the count stays above zero after two repairs. Voice style beyond the bans gets a human read.
## Forbidden move
Adding a claim that is not in the outline, to fill a paragraph or smooth a transition.
## Tool
tool: Bash:python3
scope: read
