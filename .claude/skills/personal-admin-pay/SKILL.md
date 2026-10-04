---
name: personal-admin-pay
description: Use when a bill, invoice, or purchase payment details must be prepared for a person to pay. Quiet for paying anything.
---
## Trigger
A payment is wanted (bill, invoice, fee, purchase). Always gated: prepare the details, then stop.
## Done-when
check: schema
Bash:jq -e exits 0 on one JSON file holding the sheet and the action log: sheet has non-empty payee, amount, due_date, source_document and paid false; action_log has no entry with a verb in pay, payment, checkout, purchase (state unchanged, no payment made).
## Rung
rung: L0
A jq filter validates the sheet fields and the clean action log. A person pays afterward.
## Forbidden move
Submitting a payment, entering card or account numbers, checking out, or reporting a payment as made.
## Tool
tool: none
scope: none
gate: ABSENT pay, payment, checkout (prepare the payment sheet, stop; a person pays)
