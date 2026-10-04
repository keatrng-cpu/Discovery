---
name: personal-admin-pay
description: Use when a bill, invoice, or purchase payment details must be prepared for a person to pay. Quiet for paying anything.
---
## Trigger
A payment is wanted (bill, invoice, fee, purchase). Always gated: prepare the details, then stop.
## Done-when
check: schema
Bash:jq -e exits 0 on the payment sheet JSON: non-empty payee, amount, due_date, source_document and paid false. Stop is enforced by the absent pay, payment, checkout tools, not by this check.
## Rung
rung: L0
A jq filter validates the sheet fields. A person pays afterward.
## Forbidden move
Submitting a payment, entering card or account numbers, checking out, or reporting a payment as made.
## Tool
tool: none
scope: none
gate: ABSENT pay, payment, checkout, form or browser submit (prepare the payment sheet, stop; a person pays)
