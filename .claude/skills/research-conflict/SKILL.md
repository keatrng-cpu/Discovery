---
name: research-conflict
description: Use when two sources disagree on a claim and the disagreement must be shown, not smoothed. Quiet for single-source questions or for building a summary.
---
## Trigger
Two or more sources state different things about the same point. Quiet when only one source exists or the sources agree.
## Done-when
check: human-only
A person reads the side-by-side table: two verbatim quotes with locators, one line naming the exact point of disagreement, one line stating what evidence would decide it, and checks that the sentence after the quotes contains no figure absent from both quotes and no midpoint or blended conclusion. A program can confirm only that the quotes are verbatim; whether the sentence after averages them is a human judgment.
## Rung
rung: L3
Weak directive: a stronger model drafts the table and a person reviews it. Escalating the model does not remove the pull toward a smooth answer.
## Forbidden move
Averaging the two sources, or writing a blended figure or a midpoint conclusion in the sentence after the quotes.
## Tool
tool: none
scope: none
