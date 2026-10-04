# Shelf: reverse-engineering (reverse engineering; verbatim from the owner's spec)

## Short form
Reverse engineering. Interoperability and defensive understanding only. Triage: format and architecture from file tools, disagree stops. Static: functions, call graph, strings, graph must regenerate. Lift: score a known architecture first, model only on the unmatched remainder. Dynamic: drop a claim the trace contradicts. Protocol: round-trip captures in hand, do not generalize. Summarize: name only with a string, call, or trace. State: resume from files. Function-name exact match is about 2 to 7 percent. No decryption chain, no bypass.

## Directive definitions
Interoperability and defensive understanding. Deterministic tools first. No decryption chain, no bypass, no weaponizing directive.
Triage. Identify format from the file tool. Identify architecture from the header. Name the entry. Disagreeing tools stop the card.
Static. List functions from the disassembler. Build the call graph. Extract strings. The graph must regenerate.
Lift. Recover a spec against a known architecture first. Score that recovery. Only then touch the unknown target. Model only on the unmatched remainder.
Dynamic. Trace under emulation. Compare the trace to the static claim. A claim the trace contradicts is dropped.
Protocol. Parse a saved capture. Round-trip that capture. Do not generalize past the captures in hand.
Summarize. Name a function only with cited evidence. Evidence is a string, a call, or a trace. A plausible name without evidence is not a finding.
State. Write artifacts to files. A new session resumes from those files. Chat is not the investigation.

## Status and ceiling
Function naming from stripped decompilation is weak: across seven models, exact name match was about 2–7%, and token overlap was low, worse as optimization rose. Matching decompilation on retro-game functions, with a compile-and-compare loop, reached about 74% in one pipeline. Hybrid ISA recovery did most of the work with no model at all.
* Triage. Assisted to reliable. Format and architecture from file tools work. Disagreeing tools are the stop. High chance.
* Static. Reliable as disassembler output. The model should not redraw the graph. Stays a tool.
* Lift. Assisted against a known architecture with a score. The unknown target is the remainder. Medium chance known-ISA lift is routine. Low chance unknown-ISA lift is reliable.
* Dynamic. Assisted. Trace-versus-claim works if emulation exists. Medium chance.
* Protocol. Assisted on captures in hand. Generalizing past them is the failure. Medium chance round-trip holds. Low chance a spec from a few captures is trustworthy.
* Summarize. Weak. Plausible names are the common output and the measured miss. Low chance exact naming becomes reliable. Evidence-cited names can be required. The requirement does not make them right.
* State. Reliable as files. High chance, because it is not a model problem. No decryption, bypass, or weaponizing probability belongs on this shelf.
