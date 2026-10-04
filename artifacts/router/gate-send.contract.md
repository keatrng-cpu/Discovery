# contract (task)
task: Send the reply to that email thread to the customer and pay the invoice today
shelf: personal-admin
directive: pay
stakes: high
novelty: high
check: none authored: write the check before any edit
gate: ABSENT: pay, reply, send (prepare and stop)
rung: L4
token cap: 90000
verifier: check program + two-lens draft-blind verifier + human gate
skill: none (none)
files: plan.md state.json artifacts/personal-admin/pay.out
status: ready
