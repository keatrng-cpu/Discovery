---
name: scientific-design
description: Use when an accepted hypothesis needs a draft experiment plan with materials on hand, ordered steps, and a kill failure. Quiet for running anything or starting an instrument.
---
## Trigger
A hypothesis record with measurement, direction, and control exists, plus a list of materials the lab already has. Quiet when the ask is to start an instrument or run the protocol: that is a person's act.
## Done-when
check: human-only
Only a scientist can accept the plan. The draft lists materials on hand (flagging any not on the inventory), the steps in order, and the single failure result that would kill the idea. No program passes it. The draft ends at "awaiting scientist acceptance" and the directive is not done until a person says so.
## Rung
rung: L3
Draft once, then stop. No model pass can stand in for the scientist's acceptance.
## Forbidden move
Treating the draft as accepted, or starting hardware, or listing a material the lab does not have as if it were on hand.
## Tool
tool: none
scope: none
gate: ABSENT hardware-start, accept (prepare the plan, stop; a scientist accepts and a person starts any instrument)
