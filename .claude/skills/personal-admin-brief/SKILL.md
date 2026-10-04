---
name: personal-admin-brief
description: Use when a day or week of calendar events needs a list of real overlaps. Quiet for scheduling, booking, or building an agenda.
---
## Trigger
Calendar events with start and end times for a stated window are present. Quiet when only prose about the schedule exists.
## Done-when
check: count
A program over the events JSON computes pairs where startA < endB and startB < endA. Exit 0 only if the brief lists exactly those pairs ("overlaps: N/N"), each naming both event ids and both time ranges. A back-to-back (endA == startB) is not listed. Zero overlaps is a valid result and prints "overlaps: 0/0". No calendar data means "unread", not a brief.
## Rung
rung: L1
Code finds the overlaps; one fast-model pass words the brief. Escalate only if the program and the brief disagree on N.
## Forbidden move
Calling a back-to-back or a near-miss a conflict, or naming an overlap from prose without times from the calendar.
## Tool
tool: mcp__Google_Calendar__list_events
scope: read
