---
name: lab-protocols-campaign
description: Use when an iterative instrument campaign needs bounds, a stop condition, and an iteration log prepared. Quiet for any request to start or run hardware.
---
## Trigger
A validated graph and a goal for repeated runs are present. The skill prepares the plan and stops; it never starts hardware.
## Done-when
check: human-only
The campaign file holds bounds (per parameter min and max) set before the loop, a stop condition, and an empty iteration log with one field per iteration. A program may count those fields, but the start is a person's: the file carries a "STARTED-BY:" line that stays blank until a person writes it. Done is a person confirming the plan; the skill cannot confirm it.
## Rung
rung: L3
Human-only: a stronger plan pass drafts the file, then a person reviews. Never escalate to run hardware.
## Forbidden move
Starting or simulating-as-real a hardware run, or writing a loop with no bound or no stop condition.
## Tool
tool: none
scope: none
gate: ABSENT hardware-start, instrument control (prepare bounds, stop, and log; a person starts the hardware)
