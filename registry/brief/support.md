# Shelf: support (support and ops; verbatim from the owner's spec)

## Short form
Support. Classify: policy id or escalate. Draft: that intent, quote policy, no refund promise. Known path: workflow, system state, agent not improvising. Exception: record and stop. Resolve: typed tool, idempotency key. Refund, cancel, delete denied. Incident: log order, quote the line, no gap fill.

## Directive definitions
Classify. Assign a policy id. Quote the policy line. If no id fits, escalate. Do not invent a policy.
Draft. Answer only the classified intent. Include the policy line. Do not promise a refund or exception here.
Known path. Follow the workflow steps. Agent does not improvise. Output is the system state. Variance goes to exception.
Exception. Stop. Record what failed the path. Hand off. Do not guess a remedy.
Resolve. Call the typed tool. Use an idempotency key. Refund, cancel, and delete wait for a person.
Incident. Order events by log time. Quote the log line. Do not fill a gap with a likely story.

## Status and ceiling
Narrow, typed, idempotent tools are the production pattern. Long untyped resolution is not.
* Classify. Assisted to reliable against a policy id list. Invented policies die if the id must resolve. High chance.
* Draft. Assisted. Policy quote in the reply works. Promise creep is the failure. Medium chance.
* Known path. Reliable as a workflow. The agent should not be in this directive. Stays a workflow.
* Exception. Reliable as a stop. It becomes weak the moment it is allowed to remedy. High chance the stop holds if it is code.
* Resolve. Assisted inside a typed tool. Refund, cancel, delete stay gated. Low chance those gates drop.
* Incident. Assisted. Log order works. Gap-filling is the failure. Medium chance.
