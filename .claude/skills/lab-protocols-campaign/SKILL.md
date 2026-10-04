---
name: lab-protocols-campaign
description: Use when an iterative instrument campaign needs bounds, a stop condition, and an iteration log prepared. Quiet for any request to start or run hardware.
---
## Trigger
A validated graph and a goal for repeated runs are present. The skill prepares the plan and stops; it never starts hardware.
## Done-when
check: schema
A jq -e filter over the campaign file exits 0, exit code quoted: every parameter has min and max set before the loop, the stop condition field is non-empty, and the iteration log schema lists its required fields with zero entries. grep -c '^STARTED-BY:$' prints 1, so the line is blank until a person writes it. Starting the hardware is the gate, not part of this check.
## Rung
rung: L1
One fast-model pass drafts the file; a program reads it. Never escalate to run hardware.
## Forbidden move
Starting or simulating-as-real a hardware run, or writing a loop with no bound or no stop condition.
## Tool
tool: none
scope: none
gate: ABSENT hardware-start, instrument control (prepare bounds, stop, and log; a person starts the hardware)
