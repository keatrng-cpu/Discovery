---
name: personal-admin-pay
description: Use when a bill, invoice, or purchase payment details must be prepared for a person to pay. Quiet for paying anything.
---
## Trigger
A payment is wanted (bill, invoice, fee, purchase). Always gated: prepare the details, then stop.
## Done-when
check: human-only
A person confirms payee, amount, due date, and source document, then pays. No program can pass this; the agent's output ends at the prepared payment sheet.
## Rung
rung: L3
Human-only. Use the plan-level pass to assemble the sheet; never an act step.
## Forbidden move
Submitting a payment, entering card or account numbers, checking out, or reporting a payment as made.
## Tool
tool: none
scope: none
gate: ABSENT pay, payment, checkout (prepare the payment sheet, stop; a person pays)
