---
name: personal-admin-book
description: Use when a reservation, appointment, flight, or event details must be prepared for a person to book. Quiet for actually booking anything.
---
## Trigger
A booking is wanted (travel, appointment, reservation, calendar event). Always gated: prepare the details, then stop.
## Done-when
check: schema
Bash:jq -e exits 0 on one JSON file holding the sheet and two calendar-event snapshots: sheet has non-empty what, who, when, where, price, source_link and booked false; events_before equals events_after (state unchanged, no booking made).
## Rung
rung: L0
A jq filter validates the sheet and the unchanged state. A person books afterward.
## Forbidden move
Creating the event or reservation, submitting a booking form, or reporting a booking as done. Preparing is not booking.
## Tool
tool: none
scope: none
gate: ABSENT book, calendar create_event (prepare the booking sheet, stop; a person books)
