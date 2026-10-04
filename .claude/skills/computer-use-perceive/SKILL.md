---
name: computer-use-perceive
description: Use when a GUI target must be located in a screenshot before any action, including whether a modal covers it. Quiet for choosing or performing the action.
---
## Trigger
A screenshot file and a named target (button, field, tab, dialog) are present and the question is whether the target is visible and unobstructed. Quiet when no screenshot exists or when the ask is to click.
## Done-when
check: quote
Output names the target, quotes the screenshot path with a pixel bounding box for it (path:x,y,w,h), and prints occluded: yes|no, naming the covering modal or overlay when yes. 'target absent' and 'occluded: yes' are valid results and pass. A remembered coordinate with no screenshot locator fails.
## Rung
rung: L1
One fast-model pass reads the screenshot; code only checks that the locator and occluded line are present. Escalate only if the box falls outside the image bounds.
## Forbidden move
Clicking or reporting a remembered location instead of the one in this screenshot, or calling a target visible when a modal covers it.
## Tool
tool: Bash:playwright
scope: read
