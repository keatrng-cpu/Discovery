---
name: personal-admin-brief
description: Use when a day or week of calendar events needs a list of real overlaps. Quiet for scheduling, booking, or building an agenda.
---
## Trigger
Calendar events with start and end times for a stated window are present. Quiet when only prose about the schedule exists.
## Done-when
check: count
Program computes every pair of calendar events with startA < endB and startB < endA from the structured times and prints the list (overlaps: N/N); the brief's list equals that list and names both events of each pair. Back-to-back (endA == startB) is excluded. 0/0 is valid. No calendar times means unread.
## Rung
rung: L0
A program computes and lists the pairs from the structured times; no model pass.
## Forbidden move
Calling a back-to-back or near-miss a conflict, or naming an overlap from prose without calendar times.
## Tool
tool: mcp__Google_Calendar__list_events
scope: read
