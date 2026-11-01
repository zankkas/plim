#!/usr/bin/env python3
"""Tests for scripts/doctor.py.

The doctor is the kit's claim that drift is detectable. These tests prove it
detects, not just that it passes: every check is given a deliberately broken
workspace and must report the break.

Run: python3 -m unittest discover -s tests -v
"""
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import doctor  # noqa: E402


def make_workspace(tmp: Path, skills: dict[str, dict[str, str | None]]) -> Path:
    """Build a throwaway workspace. keys: skill name; values: files to write."""
    (tmp / "README.md").write_text("# test\n")
    for name, files in skills.items():
        skill_dir = tmp / "skills" / name
        skill_dir.mkdir(parents=True, exist_ok=True)
        for filename, content in files.items():
            target = skill_dir / filename
            target.parent.mkdir(parents=True, exist_ok=True)
            if content is not None:
                target.write_text(content)
    return tmp


GOOD_SKILL = {
    "SKILL.md": '---\nname: demo\ndescription: "Short and useful. Triggers: demo."\n---\n\n# Demo\n',
    "evals/cases.json": '{"skill": "demo", "cases": [{"id": "c1"}]}',
}


class DoctorFindsDrift(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def test_clean_workspace_passes(self):
        make_workspace(self.root, {"demo": GOOD_SKILL})
        self.assertEqual(doctor.run(self.root), 0)

    def test_loose_file_in_skills(self):
        make_workspace(self.root, {"demo": GOOD_SKILL})
        (self.root / "skills" / "stray.md").write_text("loose")
        self.assertIn("stray.md is loose", " ".join(doctor.check_skills(self.root)))

    def test_nested_skill_flagged(self):
        make_workspace(self.root, {"outer": {"inner/SKILL.md": "---\nname: x\n---\n"}})
        self.assertTrue(any("nested skills" in f for f in doctor.check_skills(self.root)))

    def test_over_budget_description(self):
        long_description = 'description: "' + ("word " * 80).strip() + '"'
        make_workspace(self.root, {"demo": {"SKILL.md": f"---\nname: demo\n{long_description}\n---\n"}})
        findings = doctor.check_budget(self.root)
        self.assertTrue(any("budget" in f for f in findings), findings)

    def test_folded_description_is_measured(self):
        folded = "description: >\n  Short line one.\n  Short line two.\n"
        make_workspace(self.root, {"demo": {"SKILL.md": f"---\nname: demo\n{folded}---\n"}})
        self.assertEqual(doctor.check_budget(self.root), [])

    def test_missing_evals(self):
        make_workspace(self.root, {"demo": {"SKILL.md": GOOD_SKILL["SKILL.md"]}})
        self.assertTrue(any("no evals" in f for f in doctor.check_evals(self.root)))

    def test_unparseable_evals(self):
        make_workspace(self.root, {"demo": {"SKILL.md": GOOD_SKILL["SKILL.md"], "evals/cases.json": "{nope"}})
        self.assertTrue(any("does not parse" in f for f in doctor.check_evals(self.root)))

    def test_empty_evals(self):
        make_workspace(self.root, {"demo": {"SKILL.md": GOOD_SKILL["SKILL.md"], "evals/cases.json": '{"cases": []}'}})
        self.assertTrue(any("holds no cases" in f for f in doctor.check_evals(self.root)))

    def test_broken_link_in_readme(self):
        make_workspace(self.root, {"demo": GOOD_SKILL})
        (self.root / "README.md").write_text("[gone](./does-not-exist.md)\n")
        self.assertTrue(any("link target missing" in f for f in doctor.check_links(self.root)))

    def test_status_mirror_flagged(self):
        make_workspace(self.root, {"demo": GOOD_SKILL})
        (self.root / "STATUS.md").write_text("status copy\n")
        self.assertTrue(any("status mirror" in f for f in doctor.check_mirrors(self.root)))


if __name__ == "__main__":
    unittest.main()
