#!/usr/bin/env python3
"""Small, dependency-free checks for the public vault template."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "AGENTS.md", "README.md", ".gitignore", ".gitattributes",
    ".obsidian/app.json", ".obsidian/appearance.json", ".obsidian/core-plugins.json",
    "docs/PROMOTION_WORKFLOW.md", "docs/SPECIALIZATION.md", "docs/OBSIDIAN.md", "docs/UPGRADE.md",
    "docs/TERMINOLOGY.md", "docs/GOVERNANCE.md", "terminology/README.md", "templates/term.md",
    "tests/fixtures/v0.2-instance-lifecycle.md",
)
REQUIRED_DIRS = ("inbox", "concepts", "literature", "methods", "projects", "maps", "templates", "bibliography")
TEMPLATES = {
    "concept.md": ("type", "status", "tags", "projects"),
    "literature.md": ("type", "status", "tags", "projects", "citekey", "zotero_item_key"),
    "method.md": ("type", "status", "tags", "projects"),
    "project-portal.md": ("type", "status", "tags", "projects", "repository"),
    "inbox-capture.md": ("type", "status", "tags", "projects", "captured"),
    "term.md": ("type", "status", "preferred_en", "preferred_zh", "abbreviations", "aliases_en", "aliases_zh"),
}
FORBIDDEN_OBSIDIAN = (".obsidian/workspace.json", ".obsidian/workspace-mobile.json", ".obsidian/graph.json")
ABSOLUTE_USER_PATH = re.compile(r"(?i)(?:[a-z]:[\\/]users[\\/][^\\/\s]+[\\/]|/(?:home|users)/[^/\s]+/)")
SECRET_MARKERS = (
    r"-----BEGIN (?:[A-Z0-9]+ )*PRIVATE KEY-----",
    r"\bAKIA[0-9A-Z]{16}\b",
    r"\bghp_[A-Za-z0-9]{36}\b",
    r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b",
)
LIFECYCLE_TERMS = (
    "TEMPLATE_OWNED", "INSTANCE_OWNED", "INSTANCE_SPECIALIZED", "BOOTSTRAP_ONLY",
    "PORT", "ADAPT", "SKIP", "ALREADY_PRESENT",
    "Generated from", "Last reviewed", "Reconciled through",
)


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def tracked_files() -> set[str]:
    result = subprocess.run(["git", "ls-files"], cwd=ROOT, text=True, capture_output=True, check=True)
    return set(result.stdout.splitlines())


def main() -> None:
    for path in REQUIRED_FILES:
        if not (ROOT / path).is_file():
            fail(f"missing required file: {path}")
    for path in REQUIRED_DIRS:
        if not (ROOT / path).is_dir():
            fail(f"missing required directory: {path}")

    upgrade = (ROOT / "docs/UPGRADE.md").read_text(encoding="utf-8")
    specialization = (ROOT / "docs/SPECIALIZATION.md").read_text(encoding="utf-8")
    fixture = (ROOT / "tests/fixtures/v0.2-instance-lifecycle.md").read_text(encoding="utf-8")
    for term in LIFECYCLE_TERMS:
        if term not in upgrade:
            fail(f"upgrade contract missing lifecycle term: {term}")
    for term in ("TEMPLATE_BASELINE.md", "TEMPLATE_UPGRADES.md", "per-file ownership metadata"):
        if term not in specialization:
            fail(f"specialization contract missing lifecycle boundary: {term}")
    for term in ("69837fd75c779bf9aa7415f7d087ffbc0fd54394", "OS-local temporary directory", "Formal execution"):
        if term not in fixture:
            fail(f"synthetic scenario definition is incomplete: {term}")
    if "JSON/YAML" not in upgrade:
        fail("upgrade contract does not prohibit a machine-readable upgrade manifest")

    governance = (ROOT / "docs/GOVERNANCE.md").read_text(encoding="utf-8")
    for term in ("CAPTURE", "ROUTINE_UPDATE", "CANONICAL_CHANGE", "Generated output", "Evidence", "Interpretation", "Decision", "nested `AGENTS.md`"):
        if term not in governance:
            fail(f"governance contract missing: {term}")

    tracked = tracked_files()
    for path in FORBIDDEN_OBSIDIAN:
        if path in tracked:
            fail(f"machine-specific Obsidian state is tracked: {path}")
    allowed_obsidian = {".obsidian/app.json", ".obsidian/appearance.json", ".obsidian/core-plugins.json"}
    unexpected = sorted(path for path in tracked if path.startswith(".obsidian/") and path not in allowed_obsidian)
    if unexpected:
        fail(f"unexpected tracked Obsidian state: {', '.join(unexpected)}")

    for name, fields in TEMPLATES.items():
        text = (ROOT / "templates" / name).read_text(encoding="utf-8")
        if not text.startswith("---\n") or "\n---\n" not in text:
            fail(f"template lacks YAML front matter: templates/{name}")
        front_matter = text.split("\n---\n", 1)[0]
        for field in fields:
            if not re.search(rf"^{re.escape(field)}:", front_matter, re.MULTILINE):
                fail(f"template field missing: templates/{name} ({field})")

    term = (ROOT / "templates/term.md").read_text(encoding="utf-8")
    term_front = term.split("\n---\n", 1)[0]
    if not re.search(r"^type: term$", term_front, re.MULTILINE):
        fail("term form must identify type: term")
    if not re.search(r"^status: active$", term_front, re.MULTILINE):
        fail("term form must start active after review")
    for field in ("abbreviations", "aliases_en", "aliases_zh"):
        if not re.search(rf"^{field}: \[\]$", term_front, re.MULTILINE):
            fail(f"term form must start with an empty {field} list")
    for section in ("Definition", "Domain and usage", "Provenance and sources", "Wording guidance"):
        if f"## {section}" not in term:
            fail(f"term form missing section: {section}")

    for path in sorted(tracked):
        if Path(path).suffix.lower() not in {".md", ".txt", ".json", ".yaml", ".yml", ".toml"} and Path(path).name not in {".gitignore", ".gitattributes", "AGENTS.md", "README.md"}:
            continue
        text = (ROOT / path).read_text(encoding="utf-8")
        if ABSOLUTE_USER_PATH.search(text):
            fail(f"obvious absolute user path in: {path}")
        for marker in SECRET_MARKERS:
            if re.search(marker, text):
                fail(f"possible secret material in: {path}")

    ignored = (".obsidian/workspace.json", ".obsidian/plugins/example/data.json", ".env", "example.key")
    for path in ignored:
        result = subprocess.run(["git", "check-ignore", "--quiet", path], cwd=ROOT)
        if result.returncode != 0:
            fail(f"documented ignored path is not ignored: {path}")
    print("PASS: research vault template validation")


if __name__ == "__main__":
    main()
