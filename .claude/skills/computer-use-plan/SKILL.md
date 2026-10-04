---
name: computer-use-plan
description: Use when the next GUI action must be chosen from an external step list. Quiet for performing the action or for tasks with no step list.
---
## Trigger
An external step list file and a current screenshot or screen description are both present. Quiet when no list exists; ask for one instead of inventing steps.
## Done-when
check: quote
Output is exactly one action, quoted verbatim from one line of the step list with its line number (steps.md:L7). If the screen disagrees with that step, output ASK plus the one-line disagreement and no action. Two actions, or an action absent from the list, fails.
## Rung
rung: L1
One fast-model pass picks the line; code string-matches it against the list. Escalate only after a failed match, never to guess.
## Forbidden move
Diverging from the step list: inventing, merging, or reordering steps, or guessing when the screen and list disagree instead of asking.
## Tool
tool: none
scope: none
