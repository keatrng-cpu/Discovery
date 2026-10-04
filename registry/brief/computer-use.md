# Shelf: computer-use (computer use; verbatim from the owner's spec)

## Short form
Computer use. Perceive: target in this screenshot, say if a modal covers it. Plan: one action from an external list, ask if screen disagrees. Act: state diff or fail. Recover: revert and stop. Remember: write state.json, later step reads it back. Finish: submit only on match. Ceiling not awarded. Long multi-app runs are not a skill. June 2026 OSWorld 2.0 binary completion was about 20.6 percent, partial about 54.8 percent. Later tables disagree. Do not treat a leaderboard as a pass.

## Directive definitions
Perceive. Name the target. Confirm it is in the screenshot. If a modal covers it, say so. Do not click a remembered location.
Plan. Next action from the step list. One action. If the list and the screen disagree, ask. Do not guess.
Act. Perform that action. Capture the state after. Pass only on the diff. A click is not a result.
Recover. Name the bad step. Revert it. Confirm the prior state. Then stop.
Remember. Write the needed fact to the state file. Read it back at the later step. Do not rely on the transcript.
Finish. Check the final state against the instruction. Submit only on match. Early submit fails the card. Ceiling not awarded.

## Status and ceiling
This is the shelf where numbers conflict, so the conflict is the finding. The June 2026 OSWorld 2.0 paper reported 20.6% binary completion and 54.8% partial for the best agent then, on workflows of often 300 steps. Later aggregator tables claim far higher scores for newer setups. Those tables are not reconciled here. Failure modes in the paper were missing information, perception, verification, and memory. Agents guess instead of asking, and they submit early.
* Perceive. Assisted and improving. Screenshot-confirm helps. Occlusion still fools it. Medium chance short tasks are reliable. Low chance long ones are.
* Plan. Weak on long tasks. One action from a list works. Divergence from the list is the failure. Medium chance if the list is external.
* Act. Assisted. State diff is the right check and is rarely what the agent uses. Medium chance.
* Recover. Weak. It can name a bad step. It rarely reverts cleanly. Medium-low chance.
* Remember. Weak in the transcript, assisted if the fact is a file. High chance the file version works. The transcript version does not get better just because the model does.
* Finish. Weak. Early submit is the measured habit. Medium chance a final-state check blocks it. Ceiling stays unawarded through 2027.
