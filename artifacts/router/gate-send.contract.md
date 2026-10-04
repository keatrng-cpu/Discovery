# contract (task)
task: Send the reply to that email thread to the customer and pay the invoice today
shelf: personal-admin
directive: pay
stakes: high
novelty: low
check: schema: Bash:jq -e exits 0 on the payment sheet JSON: non-empty payee, amount, due_date, source_document and paid false. Stop is enforced by the absent pay, payment, checkout tools, not by this check.
gate: ABSENT: send, book, pay
rung: L0
token cap: 0
verifier: check program + two-lens draft-blind verifier + human gate
skill: .claude/skills/personal-admin-pay/SKILL.md
files: plan.md state.json artifacts/personal-admin/pay.out
status: ready
