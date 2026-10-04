# plan.md

## Stage
scaffold -> shelves -> merge -> seeds -> invention -> report. Current: report written; contract rows re-run by the Stop hook.

## Files to change (named)
Done. Anything further goes through the router: `python3 desk/desk.py route "<task>"`.

## Files not to touch
trace/trace.jsonl (appended by the PostToolUse hook only). Workers may touch only .claude/skills/<their shelf>-*/ and registry/shelf/<their shelf>.json; desk.py merge-shelves rejects any branch that touches anything else. registry/tools.json, .claude/settings.json, .claude/hooks/, desk/gate.py, contract.md are CODEOWNERS-protected: a person changes them.

## Tokens
Measured from transcripts, written to artifacts/tokens.json (basis stated per figure there).
- Lead pass: input 36.1M processed (265 uncached, 1.7M cache write, 34.4M cache read) over about 100 API messages; output recorded 318,573 (this includes reasoning; visible text alone is about 100k by characters / 4, an estimate). The lead ran on four model ids because the model was switched mid-thread by the user.
- One worker pass (median author, `author:security-review`): 8 API calls, 852,938 prompt tokens processed (59,718 cache write, 793,204 cache read, 16 uncached); recorded output 93, which is a snapshot and a lower bound.
- Output per workflow, from the harness meter: shelf swarm 1,109,648 across 198 agents (mean about 5,600 per agent); final verification and seed and invention runs 285,660 (interrupted by a usage limit) plus 253,177 on resume.
- Every subagent starts with an inherited prefix: median 85,174 prompt tokens before it does any work (363 measured agents). 428 agents ran in total.
- Not available: a per-agent output total. The recorded subagent output is a snapshot, and the harness meter exists per workflow only.

## Report

### What was built
A router, a registry, and a set of gates for Claude Code. `desk.py route` turns a task into a contract (shelf, directive, stakes, novelty, check, gate, rung, token cap) with code, not a model. 22 shelves, 123 directives (the owner's "Book and pay" is split into `book` and `pay` under the rule that an "and" is two directives). Each directive has a skill file, a registry entry, and a tool or none. Hooks block done while the contract is red, deny gate verbs and un-added act tools, and keep a hash-chained trace.

### Result, stated at the level each claim is true
| claim | count | basis |
|---|---|---|
| directives authored | 123 of 123 | lint: 0 errors |
| verified (2 draft-blind lenses x 3 votes, majority) | 88 of 123 | artifacts/verdicts/*.final.* |
| check runnable today (a registered tool or repo program produces it) | 13 of 123 | registry checkRunnable, verified by lens A5 |
| meets the owner's "maximized" test (runnable check, verified, gate is an absent tool, rung L0 or L1) | 8 | software/verify, research/gap, markets/print, reverse-engineering/triage, support/known-path, support/exception, computer-use/remember, harness/memory |
| directives carrying a real gate (irreversible tool absent) | 21 | gated true, tool none, gate named |
| seed skills passing their held-out check | 4 of 4 | graded by the lead's checkers, exit 0 |
| seed skills passing the tune-set check | 2 of 4 | research-gap (9 assertions) and markets-print (2) failed on tune |

Authored is not maximized: 8 of 123 meet the owner's definition. The other 115 name the check form and tool but ship no check program, or were voted down.

Per shelf, verified of authored: software 5/7, research 6/6, scientific 4/6, lab-protocols 2/5, data 3/7, markets 6/6, legal 6/6, design-systems 5/5, motion-games-3d 4/6, audio 2/4, writing 5/6, sales 5/6, support 4/6, recruiting 5/5, education 2/5, personal-admin 5/6, computer-use 2/6, strategy 4/5, clinical-notes 4/4, security-review 1/4, harness 3/5, reverse-engineering 5/7.

The 35 still voted down fail on: A3 (done-when does not enforce an element the brief names) 15, B7 (absentTools lists code or registered tools) 12, B3 (more than one check) 11, B4 (rung dearer than needed) 4, A1 (opinion, not a program-readable check) 3, A4 (empty must pass as a result) 2, A5 (checkRunnable claimed without a program) 2. A directive can fail several rules. They are flagged unverified in the registry; the router treats them as novelty high rather than trusting them.

### Files created
559 tracked files: 125 skills (123 directives plus router and invention), 305 artifacts (verdict votes, claims, router contracts, seed outputs, tokens), 54 fixtures (tune and held-out for four seeds, four checkers), 53 registry files (22 shelf files, 23 briefs, tools, seeds, gaps), desk/ (router, gate, trace, tests, search tool), 5 hook files, 4 agents, settings, contract.md, plan.md, state.json, CLAUDE.md (45 lines), CODEOWNERS.

### Checks run
- Contract rows d1 to d10, run by `desk.py contract-check` and by the Stop hook: router held-out 5/5 contracts emitted, valid, matching; Stop hook blocks a verify task with a failing test (exit 2) and releases the fixed copy (exit 0); PreToolUse denies a send, an order, a purchase, an un-added act tool and an unregistered MCP tool; four held-out seed checks exit 0; invention 3 candidates and 1 kill, all naming registry tools; tokens written; lint 0 errors; trace chain intact (2,158 records at last check); trace tamper by edit, delete and reorder fails.
- 48 unit tests pass. 30 hook cases pass (earlier I said 31; that count included the summary line).
- Each of the four held-out checkers was proven to accept a correct answer and reject wrong ones before any worker ran.
- The software-verify screenshot gate was proven load-bearing: a project whose tests pass but whose render differs fails on the compare.
- Four non-seed `jq` checks were read; two (known-path, remember) were smoke-tested on good and bad input.

### Findings you should know
1. **Seed passes are closed-loop, and n=1 per cell.** The seed skills' done-when is the checker, so the agent runs it and corrects. From the transcripts: research-gap held-out FAIL then OK (2 runs), markets-print held-out FAIL, FAIL, OK (3 runs), research-gap tune 3 runs and never OK, reverse-engineering ran the checker twice per fixture (first run a usage slip, then OK), software-verify has no checker in its loop and was graded afterwards. "Held-out" here means the input was unseen by the skill's author, not that the answer was right first time.
2. **No tuning-set advantage showed up; single-run variance did.** The two tune-set failures are the reverse of the usual gap. Treat a single pass as weak evidence either way. The promotion gate refuses to promote on a tune-set win and requires held-out plus a token or time drop; it is unit-tested, and nothing was promoted.
3. **The verifier rubric was clarified once, in one direction.** Round 3 told authors a composite check is one check if it is one command with one exit code. Rule B3 was changed to say the same before the final vote, and applied to all 123. It can only relax, so it could not flip an earlier pass to a fail. Rules A3 and B3 pulled against each other for multi-element directives until then.
4. **A single verifier vote is noisy.** 14 directives passed one round and failed a later one on unchanged claims. Across the three final votes per lens, 11% of judgments split. Final verdicts use a per-lens majority, at least 2 votes, both lenses must pass.
5. **The held-out router run found a real bug of mine.** `checkout` (a synonym I added for pay) raised stakes on "checkout service". Pre-fix: shelf and directive 4 of 4, stakes wrong 1 of 5, novelty wrong 4 of 5 (verdicts were not final). Fixed by detecting gate verbs in task prose with the owner's list only; tool-name denial keeps the wider set. Post-fix 5 of 5. That is a fix made after seeing the held-out result, so read 5 of 5 as post-fix.
6. **The live gate caught my own commands three times** (heredoc text containing trace-touching words, a compound command, an unregistered read tool). I fixed the heredoc handling and did not register a tool to unlock myself.
7. **Process faults found and fixed:** the Stop hook counter lived in tracked state and re-dirtied the tree on every stop (moved to an ignored file); one worker's edits were uncommitted (the lead committed exactly those in-scope files, and the scope check merged them); a usage limit interrupted the final workflow and it resumed from cache with all prior votes intact.
8. **Cost, plainly.** 428 agents, each paying about 85k tokens of inherited prefix, so the prefix dominates the input total (about 177M input tokens processed across subagents, almost all cache reads). 123 skill descriptions add about 18.6k characters (roughly 4.6k tokens by an estimate) to the static prompt every turn. If that matters, move non-seed skills out of `.claude/skills/` and load them by path from the router.

### Not built: tool absent
- Gated by design, never added: broker or order, mail send, payment, hiring, signature, instrument or hardware control.
- Not connected here: cite-resolution service (legal authority stays weak), disassembler and emulator (reverse-engineering static, dynamic, lift), game engine or 3D editor connector, audio editor and pronunciation list service, a protocol-graph schema validator. n8n failed to connect. Brevo, Lightfield, Sentry, Stripe and monday need authorization in the claude.ai connector settings.
- Invention's shadow run was **not executed**: candidates 1 and 2 need frozen fixtures that do not exist yet, and candidate 3 is the kill. Nothing was promoted.
- Check programs for the other 115 directives were not written; their done-when names the check form, and `checkRunnable` says false where that is so.
- The trace chain cannot detect an edit to the last record or truncation of the tail; real append-only needs a filesystem attribute or a remote write-once sink. Shell enforcement in the PreToolUse hook is pattern matching, not a sandbox.
- No pull request: the remote has only this branch, so there is no base branch to merge into. A person has to create one that shares this history.

## Addendum: auto-routing layer (connectors, plugins, skills)

### What was built
- `registry/capabilities.json`: 44 entries (38 live: 24 connectors and 14 skills; 6 not live and ignored by the router) and 5 venture bundles. `desk/caps.py` is the matcher: a strong signal scores 3, distinct weak signals 1 each (cap 3), a venture bundle +1 per member, route at 3, top 5, at most 18 tools. Code only; no model call.
- Hooks in `.claude/settings.json`: SessionStart injects `registry/capabilities.index.md` (generated, 7,395 chars) once; UserPromptSubmit injects the matched entries, the exact `ToolSearch select:` call, a gate line, and the desk router line when `route` returns one ready directive.
- 130 read or draft MCP tools registered in `registry/tools.json` with `added_by` naming the user request. No act tool was registered. Every `load` tool is allowed by the PreToolUse gate and every `never_auto` tool is denied by it (unit test).
- New commands: `caps`, `caps-lint` (also run by `lint`), `caps-register`, `caps-index`, `caps-eval`, `caps-score`. Contract rows d11 to d13.

### Measured (held-out: 60 prompts a draft-blind model wrote from the capability list only; labels are that model's judgment; thresholds committed in 08164dc before any held-out run)
| system | recall | precision | no-tool prompts that fired | against the pre-registered bar |
|---|---|---|---|---|
| keyword matcher alone | 0.385 | 0.889 | 0.062 | FAIL recall (bar 0.80) |
| model shown only the index (subagent proxy) | 0.942 | 0.982 | 0.0 | pass |
| union (what the two hooks deliver) | 0.962 | 0.938 | 0.062 | pass |
- The matcher failed on plain-language prompts that name no tool (21 of 44 positive prompts got no injection). Signals were tuned on a 30-prompt tune set of my own before the single held-out run; none was changed after it. The index is the answer to that failure, not a retune.
- The index figure is a proxy: a subagent told to choose capabilities, which overstates what a model does unprompted in a real session. Same model family as the labeler, n=60, one run. Treat 0.94 as an upper bound.
- Latency over 7 runs each: matched prompt 146 ms median, chit-chat 81 ms, session start 22 ms. Per-prompt injection averaged 244 chars on the held-out prompts (max 1,308); the index is about 7.4k chars once per session.

### Not built, not verified
- The hooks were exercised by subprocess with the documented payloads. They were not observed firing inside a live session, and an interactive session holds project hooks back until the folder is trusted.
- No `permissions.allow` entries were added, so the harness may still ask to approve each MCP call.
- Project scope only: other repos and accounts see nothing until this is packaged as a plugin.
- The route log (ids and a char count, no prompt text) is written to the ignored trace directory but nothing joins it to tool use yet.
- Account skill descriptions (the firecrawl skill's is two words) cannot be changed from this repo.
- `mcp__Supabase__execute_sql` is registered read; a scope label cannot stop a write, so the rule is SELECT only by instruction.
