# Shelf: design-systems (design systems; verbatim from the owner's spec)

## Short form
Design. Tokens from source file, token name not hex. Ban list fails the output. Components: listed only, record which, reject raw substitute. Flows: one page type, visual diff, off-template fails. CLI: reject in the tool, return the failed rule. Markdown is not this directive.
Now: reliable only if the tool rejects. Prompt-only lists leak.

## Directive definitions
Tokens. Read values from the source file. Do not sample from a screenshot. Name the token, not the hex, in output. Mismatch fails.
Ban list. Name the banned pattern. Fail the output that contains it. Keep the list shorter than the system. Do not ban taste.
Components. Call only listed components. Reject a raw substitute. Record which component was used. Same prompt, same component.
Flows. One page type per directive. Diff against the template. Spacing and type come from tokens. Off-template regions are failures.
CLI. Reject off-system output in the tool, not in a plea. Return the rule that failed. Do not "almost" pass. Markdown guides do not count as this directive.

## Status and ceiling
No benchmark. Operator evidence says a markdown guide does not constrain output, and a rejecting tool does.
* Tokens. Reliable if read from the source file. Screenshot sampling is the failure. High chance.
* Ban list. Reliable if the fail is a test, not a plea. High chance.
* Components. Assisted. Listed-component calls work when the tool only exposes those components. Prompt-only lists leak. High chance once the tool is the list.
* Flows. Assisted. One page type plus a visual diff works. Off-template regions need the diff, not the model. Medium chance.
* CLI. This is the ceiling and it is a tool, not a model. Medium-high chance serious brands have one by 2027. A model cannot substitute for the reject.
