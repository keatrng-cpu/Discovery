---
name: personal-admin-draft
description: Use when one email thread needs a reply drafted to match what was asked. Quiet for sending, for several threads at once, or for triage.
---
## Trigger
Exactly one thread id is named and a reply is wanted. Quiet when more than one thread is named, or when the ask is to send.
## Done-when
check: state-diff
Draft count for the thread rises by exactly 1, sent count is unchanged, and the draft quotes the sender's ask line with its message locator ("ask: <line> @msg N"). A person reads the draft for match-to-ask; send is never part of this check. No thread, no ask found, or unreadable thread is a valid result: write "no draft: unsupported" and create nothing.
## Rung
rung: L1
One fast-model pass writes the draft against the quoted ask; a program diffs draft and sent counts. Escalate only if the diff shows a sent message.
## Forbidden move
Sending, replying, or forwarding the draft, or answering a question the thread never asked. The send tool is absent; a person sends.
## Tool
tool: mcp__Gmail__create_draft
scope: draft
