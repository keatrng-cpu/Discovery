---
name: scientific-design
description: Use when an accepted hypothesis needs a draft experiment plan with materials on hand, ordered steps, and a kill failure. Quiet for running anything or starting an instrument.
---
## Trigger
A hypothesis record with measurement, direction, and control exists, plus a list of materials the lab already has. Quiet when the ask is to start an instrument or run the protocol: that is a person's act.
## Done-when
check: schema
One program (not yet in desk/) runs on the draft plan record and the lab inventory list and passes only if: every listed material is in the inventory (any other fails), steps are numbered in order with at least one, exactly one kill failure is named, and the record ends at status awaiting-scientist-acceptance. It never accepts the plan; a scientist does.
## Rung
rung: L1
One fast-model pass drafts the plan record; a program checks it. Then stop: no pass stands in for the scientist's acceptance.
## Forbidden move
Treating the draft as accepted, or starting hardware, or listing a material the lab does not have as if it were on hand.
## Tool
tool: none
scope: none
gate: ABSENT hardware-start, accept (prepare the plan, stop; a scientist accepts and a person starts any instrument)
