---
name: scientific-triage
description: Use when a pile of papers or records must be cut to a capped set by a written inclusion rule before a deep read. Quiet when no written rule exists or when the ask is to interpret a paper.
---
## Trigger
A candidate list (papers, records, datasets) and a written inclusion rule file are both present. Quiet when the rule is only in someone's head: write it down first, then triage. Quiet for deep reading or summarizing.
## Done-when
check: count
A program reads the rule file and the triage table. Every row has one of included, excluded, unread. Each excluded row cites a rule id from the rule file. Included count is at most the stated cap. Included + excluded + unread equals the candidate total. Unread rows are listed by id, not dropped. An empty included set and a nonzero unread count are valid results: print "included: 0/N unread: M" and exit 0.
## Rung
rung: L1
One fast-model pass applies the rule row by row; code does the counts and the cap. Escalate only if the count program fails, not because a paper looks interesting.
## Forbidden move
Including a paper because it is interesting when no rule id admits it. Excluding by vibe with no rule id. Silently dropping what was not read instead of recording it as unread.
## Tool
tool: Bash:python3
scope: read
