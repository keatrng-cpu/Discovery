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


if __name__ == "__main__":
    unittest.main()
