---
name: personal-admin-draft
description: Use when one email thread needs a reply drafted to match what was asked. Quiet for sending, for several threads at once, or for triage.
---
## Trigger
Exactly one thread id is named and a reply is wanted. Quiet when more than one thread is named, or when the ask is to send.
## Done-when
check: quote
Program greps the draft's quoted ask line in the named thread's message text at the cited message locator (quote: msg N, line L); exits 0 only if the quote is verbatim there. No thread or no ask yields "no draft: unsupported", which is valid.
## Rung
rung: L1
One fast-model pass writes the draft text; a program greps the ask quote. Escalate only if the grep fails.
## Forbidden move
Sending, replying, or forwarding the draft, or answering a question the thread never asked.
## Tool
tool: none
scope: none
gate: ABSENT send, reply, forward (prepare the draft text and stop; a person sends)
