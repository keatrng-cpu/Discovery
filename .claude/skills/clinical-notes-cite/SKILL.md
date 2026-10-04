---
name: clinical-notes-cite
description: Use when each line of a drafted clinical note must be traced to the visit transcript and unsupported lines cut. Quiet for drafting, diagnosis, or notes with no transcript.
---
## Trigger
A drafted note and its source transcript are both present. Quiet when the transcript is absent: then every line is unsupported.
## Done-when
check: quote
Every line kept in the note is followed by a quote that is a verbatim substring of the transcript, with a turn or line locator. A program checks each substring against the transcript text. Any line without a matching quote is cut and listed as cut. A note where every line is cut, or a transcript that is empty, is a valid result: kept 0, cut N.
## Rung
rung: L1
One fast-model pass proposes a quote per line; a program verifies the substring. Escalate only if a quote fails the substring check twice.
## Forbidden move
Importing history: keeping a line from the chart, a prior visit, or general medical knowledge because it is plausible, when the patient or clinician did not say it in this transcript.
## Tool
tool: Bash:python3
scope: read
