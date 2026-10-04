---
name: research-extract
description: Use when exact sentences, numbers with units, and sample sizes must be pulled from a source that is in context. Quiet for finding sources or for merging several sources.
---
## Trigger
A source page or PDF text is in context and the ask is its stated facts. Quiet when the source is not yet fetched, or when two sources are being compared.
## Done-when
check: quote
Each extracted item is a verbatim sentence found in the source text at a stated page or line, with any number carried with its unit and the sample or scope quoted beside it. Each item not verbatim is tagged "paraphrase". A source with no matching sentence yields "absent"; zero items is a valid result.
## Rung
rung: L1
A fast model selects sentences; a substring match against the pdftotext or page text confirms each quote. Escalate only when a quote fails the match twice.
## Forbidden move
Paraphrasing under compression without the paraphrase tag, or giving a number without its unit and sample.
## Tool
tool: Bash:pdftotext
scope: read
