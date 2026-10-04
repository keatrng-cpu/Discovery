---
name: support-resolve
description: Use when a ticket resolution must be prepared as a typed, idempotent tool call. Quiet for refund, cancel, or delete execution.
---
## Trigger
A classified ticket with an approved path needs a resolution call prepared. Refund, cancel, and delete requests stop here for a person.
## Done-when
check: schema
The prepared request validates against its typed schema and carries a non-empty idempotency key, with the action not in refund, cancel, delete. The execution itself is not performed by this skill.
## Rung
rung: L1
One fast-model pass fills the typed fields; code validates the schema. Escalate never; stop for a person.
## Forbidden move
Executing or promising a refund, cancel, or delete, or calling an untyped tool without an idempotency key.
## Tool
tool: none
scope: none
gate: ABSENT refund, cancel, delete, typed resolution tool (prepare the request sheet with idempotency key, stop; a person executes)
