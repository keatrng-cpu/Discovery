---
name: education-curriculum
description: Use when a learner or teacher asks for a course order or curriculum proposal. Prepares a proposal and stops; a person sets the order.
---
## Trigger
A request to order topics, plan a course, or set a curriculum. Quiet for one concept, one check, or one next step.
## Done-when
check: human-only
A person reads the proposal and sets the order. The proposal file is marked "status: proposed" and no "order set" field is written by the model. Only a person can mark it set.
## Rung
rung: L3
A planner may draft candidate orders; it never fixes one. A person decides.
## Forbidden move
Running an autonomous curriculum: fixing the order, presenting it as final, or starting lessons from it before a person sets it.
## Tool
tool: none
scope: none
gate: ABSENT accept (prepare the proposed order, stop; a person sets it)
