---
name: research-conflict
description: Use when two sources disagree on a claim and the disagreement must be shown, not smoothed. Quiet for single-source questions or for building a summary.
---
## Trigger
Two or more sources state different things about the same point. Quiet when only one source exists or the sources agree.
## Done-when
check: quote
A script reads the side-by-side table and exits 0 only when: two quotes each appear verbatim in their cited source at a stated locator; one line begins "Disagreement:" and one line begins "Decider:" (what evidence would decide it); and the sentence after the quotes contains no number absent from both quotes and none of the blend words "average", "mean of", "midpoint", "between the two", "roughly", "split the difference". Status stays weak: a blended conclusion worded without a number or a listed word still needs a person's read, so the program catches the figure and the wording, not every smoothing.
## Rung
rung: L1
A fast model drafts the table; code checks the quotes, the two labeled lines, and the figures. Escalate to a person only when the script passes and the closing sentence still reads as a compromise.
## Forbidden move
Averaging the two sources, or writing a blended figure or a midpoint conclusion in the sentence after the quotes.
## Tool
tool: Bash:python3
scope: read
