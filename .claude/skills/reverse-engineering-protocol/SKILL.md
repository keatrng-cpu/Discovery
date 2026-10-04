---
name: reverse-engineering-protocol
description: Use when a saved packet capture must be parsed and round-tripped for interoperability, staying within the captures in hand. Quiet for live traffic, crafting packets, or generalizing a spec.
---
## Trigger
One or more saved captures are in hand and the ask is to parse them and show the parse reproduces them. Quiet for live interception, crafting or replaying traffic, or decrypting or bypassing anything.
## Done-when
check: exit-code
For every capture, parse then re-serialize, and `cmp capture.bin roundtrip.bin` exits 0. The parse covers only fields seen in those captures. A capture that does not round-trip is reported as failed, and an empty capture set is a valid result.
## Rung
rung: L1
One fast-model pass drafts the parser; code runs the round-trip and the cmp. Escalate only if a capture fails the round-trip.
## Forbidden move
Generalizing a field layout, length rule, or message type past the captures in hand; calling a spec from a few captures trustworthy.
## Tool
tool: Bash:cmp
scope: read
