---
name: recruiting-decide
description: Use when a hiring decision sheet is to be prepared for a human to decide. Stops there; no hire, offer, or send.
---
## Trigger
A compare grid exists and the ask is to decide, pick, or hire. Prepare the sheet and stop; a person hires.
## Done-when
check: human-only
A person reads the sheet and decides. No program can pass a hire. The sheet lists the compare grid cells as quoted evidence, nulls as missing, and ends with the line "STOP: a human decides."
## Rung
rung: L3
Prepare the sheet only; a person decides. No model picks a winner.
## Forbidden move
Naming a winner, drafting an offer, or sending anything. The hire tool is absent; a reminder is not a gate.
## Tool
tool: none
scope: none
gate: ABSENT hire, offer, send (prepare the decision sheet from the compare grid, stop; a human decides and hires)
