import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import validate  # noqa: E402

HEADINGS = [
    "Purpose",
    "Use when",
    "Load first",
    "Steps",
    "Check before handing over",
    "Save to",
    "Needs a yes",
]


def workflow_text():
    return "# A workflow\n\n" + "\n".join(f"## {h}\n\nText.\n" for h in HEADINGS)


def write(root: Path, rel: str, text: str = "x\n"):
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)
    return p


def build_valid_repo(root: Path):
    write(root, ".gitignore", "/business/\n/departments/\n/outputs/\n/memory/\n/.env\n")
    write(root, "CLAUDE.md", "# Brain\n\nSee [setup](.claude/skills/setup/SKILL.md).\n")
    write(root, "README.md", "# Readme\n")
    for skill in validate.SKILLS:
        write(
            root,
            f".claude/skills/{skill}/SKILL.md",
            f"---\nname: {skill}\ndescription: Handles {skill} work.\n---\n\n# {skill}\n",
        )
    write(root, ".claude/skills/marketing/workflows/social-post.md", workflow_text())
    for rel in validate.REQUIRED_FILES:
        text = "setup_stage: not-started\n" if rel.endswith("business/profile.md") else "x\n"
        if "/connectors/" in rel:
            text = "# Tool\n\n## If it doesn't work\n\nFallback.\n"
        write(root, rel, text)


class ValidateTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        build_valid_repo(self.root)

    def tearDown(self):
        shutil.rmtree(self.root)

    def problems(self):
        return validate.check_repo(self.root)

    def assertProblemMentions(self, text):
        probs = self.problems()
        self.assertTrue(any(text in p for p in probs), f"{text!r} not in {probs}")

    def test_valid_repo_has_no_problems(self):
        self.assertEqual(self.problems(), [])

    def test_missing_skill(self):
        shutil.rmtree(self.root / ".claude/skills/finance")
        self.assertProblemMentions("finance")

    def test_extra_skill(self):
        write(self.root, ".claude/skills/random/SKILL.md", "---\nname: random\ndescription: x\n---\n")
        self.assertProblemMentions("random")

    def test_name_must_match_folder(self):
        write(self.root, ".claude/skills/hq/SKILL.md", "---\nname: headquarters\ndescription: x\n---\n")
        self.assertProblemMentions("hq/SKILL.md")

    def test_description_too_long(self):
        write(self.root, ".claude/skills/hq/SKILL.md", "---\nname: hq\ndescription: " + "a" * 501 + "\n---\n")
        self.assertProblemMentions("hq/SKILL.md")

    def test_workflow_missing_heading(self):
        write(self.root, ".claude/skills/marketing/workflows/social-post.md", "# x\n\n## Purpose\n\nx\n")
        self.assertProblemMentions("social-post.md")

    def test_workflow_headings_out_of_order(self):
        text = "# x\n\n" + "\n".join(f"## {h}\n\nx\n" for h in reversed(HEADINGS))
        write(self.root, ".claude/skills/marketing/workflows/social-post.md", text)
        self.assertProblemMentions("social-post.md")

    def test_example_workflows_checked(self):
        write(self.root, "examples/demo/departments/sales/workflows/custom.md", "# x\n")
        self.assertProblemMentions("custom.md")

    def test_dead_link(self):
        write(self.root, "CLAUDE.md", "See [gone](.claude/skills/nope.md).\n")
        self.assertProblemMentions("CLAUDE.md")

    def test_external_and_anchor_links_ignored(self):
        write(self.root, "CLAUDE.md", "[a](https://example.com) [b](#top) [c](mailto:x@y.z)\n")
        self.assertEqual(self.problems(), [])

    def test_missing_template(self):
        (self.root / ".claude/skills/setup/templates/business/voice.md").unlink()
        self.assertProblemMentions("voice.md")

    def test_profile_needs_setup_stage(self):
        write(self.root, ".claude/skills/setup/templates/business/profile.md", "name:\n")
        self.assertProblemMentions("setup_stage")

    def test_connector_needs_fallback(self):
        write(self.root, ".claude/skills/setup/connectors/gmail.md", "# Gmail\n")
        self.assertProblemMentions("gmail.md")

    def test_gitignore_entries(self):
        write(self.root, ".gitignore", "/business/\n")
        self.assertProblemMentions(".gitignore")

    def test_no_business_folder_at_root(self):
        write(self.root, "business/profile.md")
        self.assertProblemMentions("business/")



if __name__ == "__main__":
    unittest.main()
