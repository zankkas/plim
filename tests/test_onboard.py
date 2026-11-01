#!/usr/bin/env python3
"""Tests for the onboard filler.

The filler is the part of onboarding a machine can prove: given answers, the
workspace files are written, skipped fields stay empty, and nothing is invented.
"""

import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILL = ROOT / "skills" / "onboard" / "fill.py"
EXAMPLES = (
    "First-principles thinker",
    "Infrastructure instinct",
    "Over-structures before validating",
    "Defers decisions when uncertain",
    "Can get lost thinking",
)


def run(dest, answers, extra=None):
    path = dest.parent / "answers.json"
    path.write_text(json.dumps(answers), encoding="utf-8")
    cmd = [
        sys.executable,
        str(FILL),
        "--dest",
        str(dest),
        "--answers",
        str(path),
        "--date",
        "2026-10-31",
    ]
    if extra:
        cmd.extend(extra)
    return subprocess.run(cmd, capture_output=True, text=True)


def required(**overrides):
    answers = {
        "human_name": "Ada",
        "workspace_name": "Lab",
        "live_tracker": "GitHub issues in ada/lab",
        "default_domain": "lab",
        "background": "Builds small tools and writes about them.",
    }
    answers.update(overrides)
    return answers


def snapshot(root):
    files = []
    for folder in ("templates", "wiki/templates"):
        files.extend(p for p in (root / folder).rglob("*") if p.is_file())
    return {p.relative_to(root): p.read_bytes() for p in files}


class OnboardFiller(unittest.TestCase):
    def setUp(self):
        self.sources = snapshot(ROOT)

    def assert_sources_unchanged(self):
        self.assertEqual(self.sources, snapshot(ROOT))

    def test_missing_required_writes_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "ws"
            dest.mkdir()
            result = run(dest, required(background=""))
            self.assertEqual(result.returncode, 2, result.stderr)
            self.assertFalse((dest / ".agents" / "SOUL.md").exists())
            self.assert_sources_unchanged()

    def test_help_names_the_answer_fields(self):
        result = subprocess.run(
            [sys.executable, str(FILL), "--help"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        for field in (
            "human_name",
            "workspace_name",
            "live_tracker",
            "default_domain",
            "background",
            "trait_name",
            "trait_consequence",
        ):
            self.assertIn(field, result.stdout)

    def test_required_answers_fill_the_workspace(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "ws"
            dest.mkdir()
            result = run(dest, required())
            self.assertEqual(result.returncode, 0, result.stderr)
            soul = (dest / ".agents" / "SOUL.md").read_text(encoding="utf-8")
            profile = (dest / ".agents" / "PROFILE.md").read_text(encoding="utf-8")
            compass = (dest / ".agents" / "compass.md").read_text(encoding="utf-8")
            adapter = (dest / "AGENTS.md").read_text(encoding="utf-8")
            note = (dest / ".agents" / "session-notes" / "lab.md").read_text(encoding="utf-8")
            for text in (soul, profile, compass, adapter, note):
                self.assertNotIn("{{", text)
            self.assertIn("Ada", soul)
            self.assertIn("Builds small tools", profile)
            self.assertIn("GitHub issues in ada/lab", compass)
            self.assertIn("session-notes/lab.md", adapter)
            self.assertIn("| `directives/` |", compass)
            self.assertNotIn(".agents/directives/", compass)
            self.assertIn("directives/` and `skills/`", adapter)
            self.assertIn("# lab: Session Notes", note)
            self.assertIn("*Last updated: 2026-10-31: Workspace onboarded*", soul)
            for example in EXAMPLES:
                self.assertNotIn(example, profile)
            self.assertNotIn("## Voice (for public output)", profile)
            self.assert_sources_unchanged()

    def test_no_tracker_sentence_is_written_as_given(self):
        sentence = "No live tracker yet. Report current work as unverified."
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "ws"
            dest.mkdir()
            result = run(dest, required(live_tracker=sentence))
            self.assertEqual(result.returncode, 0, result.stderr)
            compass = (dest / ".agents" / "compass.md").read_text(encoding="utf-8")
            self.assertIn(sentence, compass)
            self.assertNotIn("github.com", compass.lower())

    def test_optional_trait_is_written_and_a_half_pair_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "ws"
            dest.mkdir()
            answers = required(
                trait_name="Cuts scope",
                trait_consequence="When the design grows, ask what the smallest proof is.",
            )
            result = run(dest, answers)
            self.assertEqual(result.returncode, 0, result.stderr)
            profile = (dest / ".agents" / "PROFILE.md").read_text(encoding="utf-8")
            self.assertIn("**Cuts scope**:", profile)
            self.assertNotIn("{{TRAIT}}", profile)

            refused = run(dest, required(trait_name="Cuts scope"), extra=["--force"])
            self.assertEqual(refused.returncode, 2, refused.stderr)
            self.assertIn("trait_consequence", refused.stderr)

    def test_second_run_refuses_without_force(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "ws"
            dest.mkdir()
            first = run(dest, required())
            self.assertEqual(first.returncode, 0, first.stderr)
            soul = (dest / ".agents" / "SOUL.md").read_text(encoding="utf-8")
            second = run(dest, required(human_name="Grace"))
            self.assertEqual(second.returncode, 3, second.stderr)
            self.assertEqual(soul, (dest / ".agents" / "SOUL.md").read_text(encoding="utf-8"))
            forced = run(dest, required(human_name="Grace"), extra=["--force"])
            self.assertEqual(forced.returncode, 0, forced.stderr)
            self.assertIn("Grace", (dest / ".agents" / "SOUL.md").read_text(encoding="utf-8"))

    def test_gateway_is_consumed_and_own_boot_file_is_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "ws"
            dest.mkdir()
            gateway = "# Plim\n\n<!-- plim:gateway — boot gateway -->\n"
            (dest / "AGENTS.md").write_text(gateway, encoding="utf-8")
            result = run(dest, required())
            self.assertEqual(result.returncode, 0, result.stderr)
            adapter = (dest / "AGENTS.md").read_text(encoding="utf-8")
            self.assertNotIn("plim:gateway", adapter)
            self.assertIn("GitHub issues in ada/lab", adapter)
            self.assertIn("session-notes/lab.md", adapter)

        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "ws"
            dest.mkdir()
            (dest / "AGENTS.md").write_text("# My own boot file\n", encoding="utf-8")
            refused = run(dest, required())
            self.assertEqual(refused.returncode, 2, refused.stderr)
            self.assertIn("was not generated by plim", refused.stderr)
            self.assertFalse((dest / ".agents" / "SOUL.md").exists())
            self.assertEqual((dest / "AGENTS.md").read_text(encoding="utf-8"),
                             "# My own boot file\n")

    def test_unsafe_domain_and_path_are_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "ws"
            dest.mkdir()
            bad_domain = run(dest, required(default_domain="../lab"))
            self.assertEqual(bad_domain.returncode, 2, bad_domain.stderr)
            self.assertFalse((dest / ".agents").exists())
            bad_path = run(dest, required(specs_dir="../secrets"))
            self.assertEqual(bad_path.returncode, 2, bad_path.stderr)

    def test_specs_dir_is_kept_only_when_given(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "ws"
            dest.mkdir()
            skipped = run(dest, required())
            self.assertEqual(skipped.returncode, 0, skipped.stderr)
            compass = (dest / ".agents" / "compass.md").read_text(encoding="utf-8")
            self.assertNotIn("SPECS_DIR", compass)
            self.assertNotIn("Active design and implementation specs", compass)
            given = run(dest, required(specs_dir="_spec"), extra=["--force"])
            self.assertEqual(given.returncode, 0, given.stderr)
            compass = (dest / ".agents" / "compass.md").read_text(encoding="utf-8")
            self.assertIn("`_spec/{project}/`", compass)


class OnboardSkillContract(unittest.TestCase):
    def test_eval_ids_agree(self):
        folder = ROOT / "skills" / "onboard" / "evals"
        data = json.loads((folder / "cases.json").read_text(encoding="utf-8"))
        md = (folder / "cases.md").read_text(encoding="utf-8")
        ids = [case["id"] for case in data["cases"]]
        found = re.findall(r"\*\*(ob-[a-z0-9-]+)\*\*", md)
        self.assertEqual(found, ids)
        for case_id in ids:
            self.assertEqual(data["cases"][ids.index(case_id)]["id"], case_id)

    def test_skill_matches_the_filler_contract(self):
        text = (ROOT / "skills" / "onboard" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("python3 skills/onboard/fill.py --dest . --answers", text)
        self.assertIn("No live tracker yet. Report current work as unverified.", text)
        self.assertIn("--force", text)
        self.assertIn("Do not invent a tracker, a board, or a repository.", text)


if __name__ == "__main__":
    unittest.main()
