# Shelf: research (verbatim from the owner's spec)

## Short form
Research. Retrieve: resolve identifier or discard, primary over recap, access date. Extract: sentence, number with unit, sample, mark paraphrase. Gap: claim list, search only the first unsupported, stop when filled or open. Conflict: two sources side by side, name the disagreement, no average, state what would decide it. Synthesize: one claim per sentence, source or label unsupported. Monitor: diff last memo, expire on a code clock, delta only.
Now: assisted. Deep-research URL hallucination is worse than search-augmented. Volume is not reliability.

## Directive definitions
Retrieve. Resolve the identifier before summarizing. Prefer the primary source over the recap. Record the access date. Discard a hit that does not open.
Extract. Pull the sentence, not the gist. Pull the number with its unit. Pull the sample or scope. Mark a paraphrase as a paraphrase.
Gap. List claims in the draft. Mark each supported or not. Search only for the first unsupported claim. Stop the search when that claim is filled or declared open.
Conflict. Place both sources side by side. Name the exact point of disagreement. Do not average them. State what evidence would decide it.
Synthesize. One claim per sentence. Attach a source or the label unsupported. Cut any sentence that does neither. Lead with the answer, then the conflicts.
Monitor. Diff against the last memo. Expire a claim past its half-life. Add only new sources. Keep the old conclusion visible if it changed.

## Status and ceiling
Deep-research agents emit far more citations and hallucinate URLs at higher rates than search-augmented models: about 3–13% of citation URLs have no record of ever existing, and deep-research pools near 11% against about 5% for search-augmented models. Volume is not reliability.
* Retrieve. Assisted. It resolves an identifier when the tool returns one, and invents one when the tool is skipped. High chance a resolve-or-discard rule makes this reliable by 2027.
* Extract. Assisted. Quote-and-unit works when the page is in context. It paraphrases under compression. Medium chance.
* Gap. Assisted, and the right shape. It can list claims. It keeps searching after the gap is filled unless stopped. Medium-high chance a stop rule fixes this.
* Conflict. Weak to assisted. It can place two quotes side by side. It still averages them in the sentence after. Medium chance the side-by-side form is reliable. Low chance it stops preferring a smooth answer.
* Synthesize. Assisted. One-claim-one-source is enforceable. Unsupported sentences still sneak in. Medium chance.
* Monitor. Assisted if the last memo is a file. It diffs well and expires claims only if the clock is code. High chance, because the clock should not be a model.
