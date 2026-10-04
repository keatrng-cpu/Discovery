---
name: computer-use-plan
description: Use when the next GUI action must be chosen from an external step list. Quiet for performing the action or for tasks with no step list.
---
## Trigger
An external step list file (steps.md), an executed-steps log (done.txt, one executed line number per line, empty if none), and a current screenshot or screen description are all present. Quiet when no list exists; ask for one instead of inventing steps.
## Done-when
check: quote
Output is exactly one action quoted verbatim from one line of steps.md with its line number (steps.md:L7), and L7 must be the next unexecuted step: the lowest non-blank line number of steps.md that is absent from done.txt. A python3 one-liner computes that line number and string-compares the quote; exit 0 only on exact match, so a skipped or reordered step fails. If the screen disagrees with that next step, output ASK with a one-line disagreement and no action. Two actions or an action not in the list fails.
## Rung
rung: L1
One fast-model pass picks the line; python3 derives the next unexecuted line from steps.md and done.txt and compares the quote (exit 0 on exact match). Escalate only after a failed match, never to guess.
## Forbidden move
Diverging from the step list: inventing, merging, skipping, or reordering steps (picking any line other than the next unexecuted one), or guessing when the screen and list disagree instead of asking.
## Tool
tool: Bash:python3
scope: read
