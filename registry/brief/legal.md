# Shelf: legal (contracts and legal; verbatim from the owner's spec)

## Short form
Legal. Extract: one clause type, quote, section, empty allowed. Risk: one party, written severity, quote only. Compare: missing clause is a row, changed obligation is a row. Draft: edit flagged clause only, original visible. Authority: resolve or drop, invented cite fails. Diligence: in scope, not read, one row per issue, lawyer signs.
Now: authority weak. All-pass verified legal research is well under reliable. Signature gated.

## Directive definitions
Extract. One clause type per pass. Quote the clause. Record the section. Empty is a result, not a failure.
Risk. Score from one party's view. Use a written severity rule. Tie the score to a quote. Do not score unquoted text.
Compare. Diff against the house paper. A missing clause is a row. A changed obligation is a row. Silence is not "fine."
Draft. Offer an edit for a flagged clause only. Keep the original visible. Do not rewrite the deal. Track the edit to the flag.
Authority. Resolve the cite. Quote the holding used. Drop a cite that does not open. Invented authority fails the card.
Diligence. List documents in scope. List documents not read. One sheet, one row per issue. A lawyer signs before anyone relies on it.

## Status and ceiling
On Legal Research Bench, all-pass with verified sources, the strongest tested model was fully correct on 42.9% of expert questions. More turns did not predict more accuracy. Conflict questions scored worse. Agentic citation checks still miss subtle misquotes. Hallucinated cites have not monotonically fallen across model generations.
* Extract. Assisted to reliable on a named clause type. Empty-as-result works if required. Medium-high chance.
* Risk. Assisted. A written severity rule plus a quote is enforceable. Unquoted scoring still happens. Medium chance. Gate stays.
* Compare. Assisted. Missing-clause rows work against a house paper. Silence-as-fine is the failure. Medium chance.
* Draft. Assisted, gated. Flagged-clause edits work. Whole-deal rewrites happen if the scope is loose. Medium chance the scope holds. A lawyer still signs.
* Authority. Weak. Resolve-or-drop is the right rule and is not yet reliable. Invented and mis-pinned cites remain the failure. Medium chance the drop rule is reliable by 2027. Low chance unverified cites become safe.
* Diligence. Assisted sheet. Coverage lists work. Unread documents get implied-read. Medium chance. Signature stays human.
