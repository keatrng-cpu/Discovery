# Shelf: security-review (security review; verbatim from the owner's spec)

## Short form
Security review. Defensive only. Scan is tool stdout. Diff: file, line, reach, then stop. Rank by written rubric on that quote. Patch review: did the quoted line change. Human opens the fix. No exploit skill.

## Directive definitions
Defensive only. No exploit, payload, or bypass directive.
Scan. Run the dependency tool. Run the secret scanner. Report tool output. A model hunch is not a finding.
Diff. Name the file and line. Name what it can reach. Stop there. No reproduction of an attack.
Rank. Apply the written rubric. Tie the rank to the quoted line. Do not rank unquoted code.
Patch review. Read the proposed fix. Say whether the quoted line changed. A human opens the fix task.

## Status and ceiling
Defensive only.
* Scan. Reliable as tool output. A model hunch is not a finding. Stays reliable because the tool is the finding.
* Diff. Assisted. File and line plus reach is writable. It wants to continue into an attack. The stop has to be the harness. Medium chance the stop holds. The continue path is out of scope.
* Rank. Assisted against a rubric. Unquoted ranks are the failure. Medium chance.
* Patch review. Assisted. "Did the quoted line change" is a diff. A human opens the fix task. High chance the diff is reliable. Low chance the human leaves.
