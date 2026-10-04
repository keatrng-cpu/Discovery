import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from unittest import mock

HERE = os.path.dirname(os.path.abspath(__file__))
DESK = os.path.dirname(HERE)
sys.path.insert(0, DESK)
import desk  # noqa: E402
import gate  # noqa: E402

SYN = {
    "software": {"shelf": "software", "stakes": "low", "gates": [], "keywords": ["widget", "gadget", "sprocket"],
              "directives": {
                  "measure": {"keywords": ["measure", "calipers", "tolerance"], "rung": "L1", "checkKind": "count",
                              "doneWhen": "count == 3", "gated": False},
                  "polish": {"keywords": ["polish", "buff", "shine"], "rung": "L1", "checkKind": "count",
                             "doneWhen": "count == 1", "gated": False},
                  "ship": {"keywords": ["ship", "freight"], "rung": "L3", "checkKind": "human-only",
                           "doneWhen": "person signs", "gated": True}}},
    "legal": {"shelf": "legal", "stakes": "high", "gates": ["order"], "keywords": ["gizmo", "doohickey", "sprocket"],
             "directives": {"draft": {"keywords": ["draft", "write up"], "rung": "L1", "checkKind": "quote",
                                      "doneWhen": "quote", "gated": False}}},
}


def run_main(argv):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = desk.main(argv)
    return rc, buf.getvalue()


class GateTests(unittest.TestCase):
    def test_verbs_are_whole_tokens(self):
        self.assertEqual(gate.verb_hit("mcp__Figma__design_thing"), [])
        self.assertEqual(gate.verb_hit("mcp__x__reorder_items"), [])
        self.assertIn("order", gate.verb_hit("mcp__shop__place_order"))
        self.assertEqual(gate.verb_hit("mcp__Gmail__SendMessage"), ["send"])
        self.assertIn("hardware-start", gate.verb_hit("mcp__lab__hardwareStart"))

    def test_registry_mirror_matches_code(self):
        reg = desk.load_tools()
        self.assertEqual(set(reg["deny_verbs"]) - {"hardware-start"}, gate.DENY_VERBS)

    def test_no_registered_tool_is_denied_by_its_own_name_unless_act(self):
        reg = desk.load_tools()
        for t in reg["tools"]:
            if t["scope"] != "act":
                self.assertEqual(gate.verb_hit(t["name"]), [], t["name"])


class RouterTests(unittest.TestCase):
    def setUp(self):
        p = mock.patch.object(desk, "skill_state", return_value="none")
        p.start()
        self.addCleanup(p.stop)

    def test_verified_skill_is_novelty_low_and_keeps_its_registered_rung(self):
        with mock.patch.object(desk, "skill_state", return_value="verified"):
            c = self.r("please measure the widget with calipers to check tolerance")["contracts"][0]
        self.assertEqual((c["novelty"], c["rung"], c["token cap"]), ("low", "L1", "20000"))
        self.assertIn("count == 3", c["check"])

    def r(self, task):
        return desk.route(task, shelves=SYN)

    def test_ready_picks_one_directive(self):
        res = self.r("please measure the widget with calipers to check tolerance")
        self.assertEqual((res["status"], res["shelf"], res["directive"]), ("ready", "software", "measure"))
        self.assertEqual(len(res["contracts"]), 1)

    def test_unsupported_is_a_valid_result(self):
        res = self.r("plan my holiday to Lisbon")
        self.assertEqual(res["status"], "unsupported")
        self.assertEqual(res["contracts"], [])

    def test_shared_keyword_alone_is_ambiguous_not_guessed(self):
        res = self.r("something about a sprocket")
        self.assertEqual(res["status"], "ambiguous")
        self.assertCountEqual(res["candidates"], ["software", "legal"])

    def test_shelf_without_directive_evidence_is_ambiguous(self):
        res = self.r("the gadget")
        self.assertEqual(res["status"], "ambiguous")
        self.assertEqual(res["shelf"], "software")

    def test_and_means_split(self):
        res = self.r("measure the widget with calipers and polish it until it has a shine, buff it")
        self.assertEqual(res["status"], "split")
        self.assertEqual([c["directive"] for c in res["contracts"]], ["measure", "polish"])

    def test_gate_verb_raises_stakes_and_in_order_to_does_not(self):
        hi = self.r("measure the widget with calipers then send it and pay the vendor")
        self.assertEqual(hi["stakes"], "high")
        self.assertIn("ABSENT", hi["contracts"][0]["gate"])
        lo = self.r("in order to measure the widget use calipers")
        self.assertEqual(lo["stakes"], "low")

    def test_nouns_that_are_only_tool_name_synonyms_do_not_raise_stakes(self):
        for word in ("checkout service", "reply rate", "buy-in", "broker mix"):
            res = self.r(f"measure the widget with calipers for the {word}")
            self.assertEqual(res["stakes"], "low", word)

    def test_owner_gate_verbs_in_prose_do_raise_stakes(self):
        for verb in ("order", "send", "pay", "hire", "sign", "diagnose", "exploit", "payload", "bypass", "decrypt", "hardware start"):
            self.assertEqual(self.r(f"measure the widget with calipers then {verb} it")["stakes"], "high", verb)

    def test_unverified_skill_is_novelty_high_and_rung_not_trusted(self):
        c = self.r("measure the widget with calipers")["contracts"][0]
        self.assertEqual(c["novelty"], "high")
        self.assertEqual(c["rung"], "L3")

    def test_novelty_and_stakes_high_is_l4(self):
        c = self.r("write up a draft about the gizmo")["contracts"][0]
        self.assertEqual((c["stakes"], c["novelty"], c["rung"]), ("high", "high", "L4"))

    def test_rendered_contract_lints_and_token_cap_matches_rung(self):
        res = self.r("write up a draft about the gizmo")
        d = desk.parse_contract(desk.render_result(res))
        self.assertEqual(desk.lint_contract(d), [])
        d["token cap"] = "1"
        self.assertTrue(desk.lint_contract(d))
        res = self.r("plan my holiday to Lisbon")
        self.assertEqual(desk.lint_contract(desk.parse_contract(desk.render_result(res))), [])


class ContractCheckTests(unittest.TestCase):
    def make(self, rows):
        d = tempfile.mkdtemp()
        body = "# c\nSTATUS: RED\n\n## Done-when\n| id | row | check |\n|---|---|---|\n" + "".join(f"| {i} | row {i} | `{c}` |\n" for i, c in rows)
        p = os.path.join(d, "contract.md")
        open(p, "w").write(body)
        return p

    def test_all_pass_is_green_and_write_updates_status(self):
        p = self.make([("a", "true"), ("b", "exit 0")])
        rc, out = run_main(["contract-check", p, "--write"])
        self.assertEqual(rc, 0)
        self.assertIn("STATUS: GREEN", open(p).read())

    def test_one_failure_is_red(self):
        p = self.make([("a", "true"), ("b", "exit 3")])
        rc, out = run_main(["contract-check", p])
        self.assertEqual(rc, 1)
        self.assertIn("FAIL b", out)

    def test_a_green_status_line_is_not_trusted(self):
        p = self.make([("a", "exit 1")])
        open(p, "w").write(open(p).read().replace("STATUS: RED", "STATUS: GREEN"))
        self.assertEqual(run_main(["contract-check", p])[0], 1)

    def test_no_rows_is_a_failure(self):
        d = tempfile.mkdtemp()
        p = os.path.join(d, "contract.md")
        open(p, "w").write("# c\nSTATUS: GREEN\n")
        self.assertEqual(run_main(["contract-check", p])[0], 1)


class LintEntryTests(unittest.TestCase):
    TOOLS = {"tools": [{"name": "Bash:python3", "scope": "read"}, {"name": "act-tool", "scope": "act", "human_added": False},
                       {"name": "mcp__x__send_it", "scope": "act", "human_added": True}]}

    def entry(self, **kw):
        e = {"trigger": "t", "doneWhen": "exit 0", "checkKind": "exit-code", "rung": "L0", "forbidden": "f", "tool": "Bash:python3",
             "toolScope": "read", "gated": False, "status": "reliable", "checkRunnable": True, "keywords": ["software", "legal", "gamma"]}
        e.update(kw)
        return e

    def lint(self, name="d", **kw):
        errs, warns = [], []
        desk.lint_directive_entry("s", name, self.entry(**kw), self.TOOLS, errs, warns)
        return errs, warns

    def test_clean_entry(self):
        self.assertEqual(self.lint()[0], [])

    def test_human_only_cannot_be_reliable(self):
        self.assertTrue(any("human-only" in e for e in self.lint(checkKind="human-only")[0]))

    def test_directive_with_and_must_be_split(self):
        self.assertTrue(any("'and'" in e for e in self.lint(name="book-and-pay")[0]))

    def test_act_tool_without_human_add_fails(self):
        self.assertTrue(any("without a human add" in e for e in self.lint(tool="act-tool", toolScope="act")[0]))

    def test_gated_cannot_hold_an_act_tool_and_needs_a_gate_field(self):
        errs = self.lint(tool="mcp__x__send_it", toolScope="act", gated=True, status="gated")[0]
        self.assertTrue(any("gated directive cannot hold an act tool" in e for e in errs))
        self.assertTrue(any("'gate' field" in e for e in errs))

    def test_gate_verb_in_tool_name_fails(self):
        self.assertTrue(any("gate verb" in e for e in self.lint(tool="mcp__x__send_it", toolScope="act")[0]))

    def test_unknown_tool_fails(self):
        self.assertTrue(any("not in registry" in e for e in self.lint(tool="Bash:nothing")[0]))

    def test_check_runnable_needs_a_tool_or_a_repo_program(self):
        self.assertTrue(any("checkRunnable" in e for e in self.lint(tool="none", toolScope="none", checkRunnable=True)[0]))
        self.assertEqual(self.lint(tool="none", toolScope="none", checkRunnable=True, doneWhen="python3 fixtures/x/check.py exits 0")[0], [])
        self.assertTrue(any("human-only" in e for e in self.lint(checkKind="human-only", status="assisted", checkRunnable=True)[0]))
        self.assertTrue(any("true or false" in e for e in self.lint(checkRunnable="yes")[0]))

    def test_thin_keywords_fail(self):
        self.assertTrue(any("keywords" in e for e in self.lint(keywords=["a"])[0]))


class InventionAndPromotionTests(unittest.TestCase):
    TOOLS = {"tools": [{"name": "Bash:strings", "scope": "read"}, {"name": "mcp__Figma__get_variable_defs", "scope": "read"}],
             "proposed": [{"name": "cite-resolution API", "scope": "read", "human_add_required": True}]}
    SH = {"reverse-engineering": {"directives": {"summarize": {"status": "weak"}, "static": {"status": "reliable"}}},
          "legal": {"directives": {"authority": {"status": "weak"}}},
          "design-systems": {"directives": {"components": {"status": "assisted"}}}}

    def cand(self, **kw):
        c = {"shelf": "reverse-engineering", "directive": "summarize", "tool": "Bash:strings", "toolScope": "read",
             "doneWhen": "each name carries a string locator", "shadowRun": "run beside the current skill", "reason": "r", "kill": False}
        c.update(kw)
        return c

    def check(self, cands):
        p = tempfile.mkdtemp() + "/inv.json"
        json.dump({"candidates": cands}, open(p, "w"))
        with mock.patch.object(desk, "load_tools", return_value=self.TOOLS), mock.patch.object(desk, "load_shelves", return_value=self.SH):
            return run_main(["invent-check", p])[0]

    def good(self):
        return [self.cand(),
                self.cand(shelf="legal", directive="authority", tool="cite-resolution API", needsHumanAdd=True),
                self.cand(shelf="design-systems", directive="components", tool="mcp__Figma__get_variable_defs", kill=True)]

    def test_three_with_one_kill_passes(self):
        self.assertEqual(self.check(self.good()), 0)

    def test_two_candidates_fail(self):
        self.assertEqual(self.check(self.good()[:2]), 1)

    def test_no_kill_fails(self):
        g = self.good()
        g[2]["kill"] = False
        self.assertEqual(self.check(g), 1)

    def test_two_kills_fail(self):
        g = self.good()
        g[0]["kill"] = True
        self.assertEqual(self.check(g), 1)

    def test_invented_tool_fails(self):
        g = self.good()
        g[0]["tool"] = "magic-oracle"
        self.assertEqual(self.check(g), 1)

    def test_proposed_tool_needs_human_add_flag(self):
        g = self.good()
        del g[1]["needsHumanAdd"]
        self.assertEqual(self.check(g), 1)

    def test_act_scope_is_never_invented(self):
        g = self.good()
        g[0]["toolScope"] = "act"
        self.assertEqual(self.check(g), 1)

    def test_missing_done_when_is_discarded_as_a_failure(self):
        g = self.good()
        g[0]["doneWhen"] = ""
        self.assertEqual(self.check(g), 1)

    def test_reliable_directive_is_not_an_invention_target(self):
        g = self.good()
        g[0]["directive"] = "static"
        self.assertEqual(self.check(g), 1)

    def promo(self, base, cand):
        p = tempfile.mkdtemp() + "/p.json"
        json.dump({"baseline": base, "candidate": cand}, open(p, "w"))
        return run_main(["promote-gate", p])

    def test_promote_needs_heldout_pass_and_a_drop(self):
        rc, out = self.promo({"tokens": 1000, "seconds": 60}, {"tune_pass": True, "heldout_pass": True, "tokens": 800, "seconds": 70})
        self.assertEqual(rc, 0, out)

    def test_tuning_set_win_alone_does_not_promote(self):
        rc, out = self.promo({"tokens": 1000, "seconds": 60}, {"tune_pass": True, "tokens": 500, "seconds": 10})
        self.assertEqual(rc, 1)
        self.assertIn("tuning-set", out)

    def test_heldout_fail_does_not_promote(self):
        self.assertEqual(self.promo({"tokens": 1000, "seconds": 60}, {"tune_pass": True, "heldout_pass": False, "tokens": 1, "seconds": 1})[0], 1)

    def test_no_cost_drop_does_not_promote(self):
        self.assertEqual(self.promo({"tokens": 1000, "seconds": 60}, {"tune_pass": True, "heldout_pass": True, "tokens": 1200, "seconds": 90})[0], 1)


class MajorityVerdictTests(unittest.TestCase):
    def verdicts(self, files):
        d = tempfile.mkdtemp()
        os.makedirs(os.path.join(d, "artifacts", "verdicts"))
        for name, rows in files.items():
            with open(os.path.join(d, "artifacts", "verdicts", name), "w") as f:
                json.dump({"verdicts": [{"directive": k, "pass": v} for k, v in rows.items()]}, f)
        with mock.patch.object(desk, "ROOT", desk.Path(d)):
            return desk.final_verdicts("x")

    def test_two_of_three_per_lens_passes(self):
        got = self.verdicts({
            "x.final.a.1.json": {"d": True}, "x.final.a.2.json": {"d": True}, "x.final.a.3.json": {"d": False},
            "x.final.b.1.json": {"d": False}, "x.final.b.2.json": {"d": True}, "x.final.b.3.json": {"d": True}})
        self.assertTrue(got["d"])

    def test_one_lens_failing_the_majority_fails_the_directive(self):
        got = self.verdicts({
            "x.final.a.1.json": {"d": True}, "x.final.a.2.json": {"d": True}, "x.final.a.3.json": {"d": True},
            "x.final.b.1.json": {"d": False}, "x.final.b.2.json": {"d": False}, "x.final.b.3.json": {"d": True}})
        self.assertFalse(got["d"])

    def test_a_single_vote_per_lens_is_not_enough(self):
        got = self.verdicts({"x.final.a.1.json": {"d": True}, "x.final.b.1.json": {"d": True}})
        self.assertFalse(got["d"])

    def test_a_missing_lens_is_unverified_not_smoothed(self):
        got = self.verdicts({"x.final.a.1.json": {"d": True}, "x.final.a.2.json": {"d": True}, "x.final.a.3.json": {"d": True}})
        self.assertFalse(got["d"])

    def test_single_vote_round_files_still_work_as_the_fallback(self):
        got = self.verdicts({"x.r0.a.json": {"d": True}, "x.r0.b.json": {"d": True}})
        self.assertTrue(got["d"])


class RegistryTests(unittest.TestCase):
    def test_all_shelves_and_the_split_book_pay(self):
        sh = desk.load_shelves()
        self.assertEqual(list(sh), desk.SHELF_ORDER)
        self.assertEqual(sum(len(s["directives"]) for s in sh.values()), 123)
        self.assertIn("book", sh["personal-admin"]["directives"])
        self.assertIn("pay", sh["personal-admin"]["directives"])
        self.assertNotIn("book-and-pay", sh["personal-admin"]["directives"])

    def test_every_directive_has_a_brief_line(self):
        for s, sh in desk.load_shelves().items():
            with open(os.path.join(desk.ROOT, "registry", "brief", f"{s}.md")) as fh:
                txt = fh.read().lower()
            for d in sh["directives"]:
                if d in ("book", "pay"):
                    continue
                self.assertTrue(any(l.startswith(d.replace("-", " ")) or l.startswith(d) for l in txt.splitlines()), f"{s}/{d}")


import caps  # noqa: E402


def _cap(cid="x", **kw):
    base = {"id": cid, "kind": "connector", "name": cid.title(), "status": "live", "priority": 1, "use": "u", "check": "schema",
            "load": ["mcp__Srv__read_thing"], "draft_tools": [], "never_auto": [], "strong": ["alpha"], "weak": ["beta", "gamma"]}
    base.update(kw)
    return base


def _map(*cs, bundles=()):
    return {"threshold": 3, "weights": {"strong": 3, "weak": 1, "bundle": 1}, "max_caps": 5, "max_tools": 18, "off_switch": ["offline only"],
            "account_skills": ["acct:skill"], "capabilities": list(cs), "bundles": list(bundles)}


def _reg(*tools):
    return {"tools": [{"name": n, "kind": "mcp", "scope": s, "check": "schema"} for n, s in tools]}


class CapsMatchTests(unittest.TestCase):
    def test_a_strong_signal_routes_and_nothing_else_does(self):
        r = caps.match("please alpha now", _map(_cap("a"), _cap("b", strong=["zzz"])))
        self.assertEqual([m["id"] for m in r["matched"]], ["a"])

    def test_one_weak_signal_is_not_enough_two_distinct_are_not_enough_three_are(self):
        m = _map(_cap("a", strong=["never"], weak=["w1", "w2", "w3"]))
        self.assertEqual(caps.match("w1", m)["matched"], [])
        self.assertEqual(caps.match("w1 w2", m)["matched"], [])
        self.assertEqual([x["id"] for x in caps.match("w1 w2 w3", m)["matched"]], ["a"])

    def test_a_venture_bundle_alone_never_loads_a_tool(self):
        b = {"id": "v", "signals": ["acme crew"], "members": ["a"]}
        m = _map(_cap("a", strong=["never"], weak=["w1", "w2"]), bundles=[b])
        self.assertEqual(caps.match("acme crew", m)["matched"], [])
        self.assertEqual(caps.match("acme crew w1", m)["matched"], [])
        self.assertEqual([x["id"] for x in caps.match("acme crew w1 w2", m)["matched"]], ["a"])

    def test_off_switch_and_negatives_and_empty(self):
        m = _map(_cap("a", neg=["blocked"]))
        self.assertEqual(caps.match("alpha offline only", m), {"off": True, "matched": []})
        self.assertEqual(caps.match("alpha blocked", m)["matched"], [])
        self.assertEqual(caps.match("   ", m), {"off": False, "matched": []})

    def test_only_live_entries_route(self):
        self.assertEqual(caps.match("alpha", _map(_cap("a", status="needs-auth")))["matched"], [])

    def test_ties_break_by_score_then_priority_and_the_list_is_capped(self):
        cs = [_cap(f"c{i}", priority=10 - i, strong=["alpha"]) for i in range(8)]
        got = [x["id"] for x in caps.match("alpha", _map(*cs))["matched"]]
        self.assertEqual(got, ["c7", "c6", "c5", "c4", "c3"])

    def test_signals_match_whole_words_only(self):
        self.assertEqual(caps.match("alphabet", _map(_cap("a")))["matched"], [])

    def test_render_names_the_exact_load_call_and_the_gate(self):
        r = caps.match("alpha", _map(_cap("a")))
        t = caps.render(r, None, ("send",))
        self.assertIn("select:mcp__Srv__read_thing", t)
        self.assertIn("Gate verbs in this prompt (send)", t)
        self.assertIsNone(caps.render({"off": False, "matched": []}))


class CapsRealMapTests(unittest.TestCase):
    def setUp(self):
        self.caps = caps.load_caps(str(desk.ROOT))
        self.reg = desk.load_tools()

    def test_the_real_map_lints_clean(self):
        errs, _ = caps.lint_caps(self.caps, self.reg, str(desk.ROOT), gate)
        self.assertEqual(errs, [])

    def test_the_matcher_and_the_gate_agree(self):
        # everything a route may load is allowed by PreToolUse; every never_auto tool is denied by it
        for c in self.caps["capabilities"]:
            if c["status"] != "live":
                continue
            for t in c.get("load", []):
                self.assertTrue(gate.decide(t, {}, self.reg)[0], t)
            for t in c.get("never_auto", []):
                self.assertFalse(gate.decide(t, {}, self.reg)[0], t)

    def test_no_route_ever_injects_a_never_auto_tool(self):
        never = {t for c in self.caps["capabilities"] for t in c.get("never_auto", [])}
        for p in ["send the invoice and show stripe revenue this month", "semrush keyword research and openseo map pack rank",
                  "supabase tables and netlify deploys and vercel runtime errors", "gmail inbox and google calendar slots and drive files"]:
            text = caps.render(caps.match(p, self.caps)) or ""
            self.assertFalse(any(t in text for t in never), p)

    def test_the_index_is_fresh_small_and_has_no_act_tool(self):
        text = caps.index_text(self.caps)
        self.assertEqual(open(os.path.join(str(desk.ROOT), caps.INDEX_REL)).read(), text)
        self.assertLessEqual(len(text), caps.INDEX_MAX)
        never = {t for c in self.caps["capabilities"] for t in c.get("never_auto", [])}
        self.assertFalse(any(t in text for t in never))

    def test_chit_chat_injects_nothing(self):
        for p in ["thanks, that makes sense", "yes go ahead", "rewrite that last paragraph shorter"]:
            self.assertIsNone(desk.auto_context(p)[0], p)


class CapsLintTests(unittest.TestCase):
    def lint(self, cap, reg, **kw):
        m = _map(cap, **kw)
        with mock.patch.object(caps, "index_text", return_value=""), mock.patch("builtins.open", mock.mock_open(read_data="")), \
                mock.patch("os.path.exists", side_effect=lambda q: str(q).endswith("capabilities.index.md")):
            return caps.lint_caps(m, reg, "/nonexistent", gate)[0]

    def test_clean_entry(self):
        self.assertEqual(self.lint(_cap(), _reg(("mcp__Srv__read_thing", "read"))), [])

    def test_an_act_tool_may_not_be_auto_loaded(self):
        errs = self.lint(_cap(), _reg(("mcp__Srv__read_thing", "act")))
        self.assertTrue(any("may not be auto-loaded" in e for e in errs), errs)

    def test_an_unregistered_tool_may_not_be_auto_loaded(self):
        errs = self.lint(_cap(), _reg())
        self.assertTrue(any("not in registry" in e for e in errs), errs)

    def test_a_gate_verb_tool_may_not_be_auto_loaded(self):
        errs = self.lint(_cap(load=["mcp__Srv__send_thing"]), _reg(("mcp__Srv__send_thing", "act")))
        self.assertTrue(any("gate verb" in e for e in errs), errs)

    def test_a_tool_in_both_load_and_never_auto_fails(self):
        errs = self.lint(_cap(never_auto=["mcp__Srv__read_thing"]), _reg(("mcp__Srv__read_thing", "read")))
        self.assertTrue(any("both load and never_auto" in e for e in errs), errs)

    def test_a_never_auto_tool_registered_as_read_fails(self):
        errs = self.lint(_cap(never_auto=["mcp__Srv__write_thing"]), _reg(("mcp__Srv__read_thing", "read"), ("mcp__Srv__write_thing", "read")))
        self.assertTrue(any("must be act or absent" in e for e in errs), errs)

    def test_bad_regex_unknown_skill_unknown_bundle_member_and_no_strong_signal_fail(self):
        errs = self.lint(_cap(strong=["("]), _reg(("mcp__Srv__read_thing", "read")))
        self.assertTrue(any("bad regex" in e for e in errs), errs)
        errs = self.lint(_cap(kind="skill", skill="nope:skill", load=[]), _reg())
        self.assertTrue(any("neither a listed account skill" in e for e in errs), errs)
        errs = self.lint(_cap(), _reg(("mcp__Srv__read_thing", "read")), bundles=[{"id": "v", "signals": ["x"], "members": ["ghost"]}])
        self.assertTrue(any("unknown member" in e for e in errs), errs)
        errs = self.lint(_cap(strong=[]), _reg(("mcp__Srv__read_thing", "read")))
        self.assertTrue(any("at least one strong signal" in e for e in errs), errs)

    def test_a_draft_tool_must_be_scope_draft(self):
        errs = self.lint(_cap(draft_tools=["mcp__Srv__read_thing"]), _reg(("mcp__Srv__read_thing", "read")))
        self.assertTrue(any("not scope draft" in e for e in errs), errs)


class CapsRegisterAndScoreTests(unittest.TestCase):
    def test_register_plan_adds_read_and_draft_and_refuses_gate_verbs_and_never_auto(self):
        c = _cap(load=["mcp__Srv__read_thing", "mcp__Srv__draft_thing", "mcp__Srv__send_thing", "mcp__Srv__wipe_thing"],
                 draft_tools=["mcp__Srv__draft_thing"], never_auto=["mcp__Srv__wipe_thing"])
        new, refused = caps.register_plan(_map(c), _reg(), gate, "t")
        self.assertEqual({e["name"]: e["scope"] for e in new}, {"mcp__Srv__read_thing": "read", "mcp__Srv__draft_thing": "draft"})
        self.assertEqual(sorted(t for t, _ in refused), ["mcp__Srv__send_thing", "mcp__Srv__wipe_thing"])
        self.assertNotIn("act", {e["scope"] for e in new})

    def test_register_plan_skips_tools_already_registered_and_not_live_entries(self):
        new, _ = caps.register_plan(_map(_cap(), _cap("n", status="not-installed", load=["mcp__Srv__other"])), _reg(("mcp__Srv__read_thing", "read")), gate)
        self.assertEqual(new, [])

    def test_score_sets_is_plain_arithmetic(self):
        items = [{"prompt": "a", "must": ["x", "y"], "ok": ["z"]}, {"prompt": "b", "must": ["w"], "ok": []}, {"prompt": "c", "must": [], "ok": []}]
        s = caps.score_sets(items, [["x", "z"], [], ["q"]])
        self.assertEqual(s, {"recall_micro": 0.333, "precision_micro": 1.0, "empty_on_positive": 1, "negative_fire_rate": 1.0})


if __name__ == "__main__":
    unittest.main()
