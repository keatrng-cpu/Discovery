---
name: personal-admin-book
description: Use when a reservation, appointment, flight, or event details must be prepared for a person to book. Quiet for actually booking anything.
---
## Trigger
A booking is wanted (travel, appointment, reservation, calendar event). Always gated: prepare the details, then stop.
## Done-when
check: human-only
A person confirms the prepared sheet (what, who, when, where, price, source link) and performs the booking. No program can pass this; the agent's output ends at the prepared sheet.
## Rung
rung: L3
Human-only. Use the plan-level pass to assemble the sheet; never an act step.
## Forbidden move
Creating the event or reservation, submitting a booking form, or reporting a booking as done. Preparing is not booking.
## Tool
tool: none
scope: none
gate: ABSENT book, calendar create_event (prepare the booking sheet, stop; a person books)
