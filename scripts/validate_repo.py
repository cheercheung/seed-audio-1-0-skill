#!/usr/bin/env python3
"""Static validation for the Seed Audio API skill repository."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]

TRANSLATION_FILES = [
    "README.es.md",
    "README.pt.md",
    "README.ja.md",
    "README.ko.md",
    "README.de.md",
    "README.fr.md",
    "README.tr.md",
    "README.zh-TW.md",
    "README.zh-CN.md",
    "README.ru.md",
]

REQUIRED_FILES = [
    "README.md",
    *TRANSLATION_FILES,
    "SKILL.md",
    "llms-install.md",
    "_meta.json",
    "package.json",
    "bin/cli.js",
    "scripts/seed-audio-generate.sh",
    "docs/quickstart.md",
    "docs/api-reference.md",
    "docs/task-lifecycle.md",
    "docs/response-schema.md",
    "docs/errors.md",
    "docs/callbacks.md",
    "docs/voices.md",
    "references/api-params.md",
    "examples/curl/complete-flow.sh",
    "examples/javascript/complete-flow.mjs",
    "examples/python/complete_flow.py",
    "assets/banner.jpg",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "SUPPORT.md",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/docs_request.yml",
    ".github/pull_request_template.md",
    "LICENSE",
    ".gitignore",
    ".npmignore",
]

REQUIRED_SNIPPETS = {
    "README.md": [
        "doubao-seed-audio-1-0",
        "EVOLINK_API_KEY",
        "## 📑 Menu",
        "## Installation",
        "## Seed Audio 1.0 API Quick Start",
        "## Troubleshooting",
        "Powered by",
    ],
    "docs/api-reference.md": [
        "POST https://api.evolink.ai/v1/audios/generations",
        "GET https://api.evolink.ai/v1/tasks/{task_id}",
        "audio_references",
        "image_urls",
    ],
    "SKILL.md": [
        "name: seed-audio-1-0",
        "scripts/seed-audio-generate.sh",
        "TASK_SUBMITTED",
        "AUDIO_URL",
        "## When to Activate This Skill",
        "## After Installation",
        "## Core Principles",
        "## Flow",
        "## Script Output Protocol",
        "## Error Handling",
        "## Model Capabilities Summary",
    ],
    "llms-install.md": [
        "{SKILLS_DIR}",
        "## One-Liner",
        "npx evolink-seed-audio --llms",
    ],
    "CONTRIBUTING.md": [
        "python3 scripts/validate_repo.py",
        "Real API smoke tests require owner approval",
    ],
}


def run(cmd: list[str]) -> tuple[int, str]:
    result = subprocess.run(
        cmd,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return result.returncode, result.stdout.strip()


def markdown_h2(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.startswith("## ")]


def fenced_code_blocks(text: str) -> list[str]:
    blocks: list[str] = []
    in_block = False
    current: list[str] = []
    for line in text.splitlines():
        if line.startswith("```"):
            if in_block:
                blocks.append("\n".join(current))
                current = []
                in_block = False
            else:
                in_block = True
            continue
        if in_block:
            current.append(line)
    return blocks


def main() -> int:
    errors: list[str] = []
    release_mode = "--release" in sys.argv[1:]

    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if not path.is_file():
            errors.append(f"missing file: {rel}")
        elif path.stat().st_size == 0 and not rel.endswith(".gitkeep"):
            errors.append(f"empty file: {rel}")

    for rel, snippets in REQUIRED_SNIPPETS.items():
        path = ROOT / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for snippet in snippets:
            if snippet not in text:
                errors.append(f"{rel} missing snippet: {snippet}")

    readme_text = (ROOT / "README.md").read_text(encoding="utf-8")
    for rel in TRANSLATION_FILES:
        if rel not in readme_text:
            errors.append(f"README.md missing language link: {rel}")

    base_h2 = markdown_h2(readme_text)
    base_code_blocks = fenced_code_blocks(readme_text)
    expected_code_block_count = len(base_code_blocks)
    required_readme_tokens = [
        "doubao-seed-audio-1-0",
        "EVOLINK_API_KEY",
        "npx evolink-seed-audio",
        "scripts/seed-audio-generate.sh",
        "https://api.evolink.ai/v1/audios/generations",
    ]
    forbidden_translation_tokens = [
        "TODO",
        "translate to",
        "Default_Source",
        "README_en.md",
        "README_",
    ]
    for rel in TRANSLATION_FILES:
        text = (ROOT / rel).read_text(encoding="utf-8")
        h2 = markdown_h2(text)
        if len(h2) != len(base_h2):
            errors.append(f"{rel} h2 count mismatch: {len(h2)} != {len(base_h2)}")
        if not h2 or not h2[0].startswith("## 📑 "):
            errors.append(f"{rel} first h2 should be the localized menu section")
        code_blocks = fenced_code_blocks(text)
        if len(code_blocks) != expected_code_block_count:
            errors.append(f"{rel} code block count mismatch: {len(code_blocks)} != {expected_code_block_count}")
        for token in required_readme_tokens:
            if token not in text:
                errors.append(f"{rel} missing required technical token: {token}")
        for token in forbidden_translation_tokens:
            if token in text:
                errors.append(f"{rel} contains forbidden translation placeholder: {token}")

    package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
    meta = json.loads((ROOT / "_meta.json").read_text(encoding="utf-8"))
    if package["version"] != meta["version"]:
        errors.append("package.json version does not match _meta.json version")
    if meta["slug"] != "seed-audio-1-0":
        errors.append("_meta.json slug mismatch")
    if release_mode:
        if meta.get("ownerId") in {"", "REPLACE_WITH_EVOLINK_OWNER_ID"}:
            errors.append("_meta.json ownerId must be the real EvoLink owner ID before release")
        published_at = meta.get("publishedAt")
        if not isinstance(published_at, int) or published_at <= 0:
            errors.append("_meta.json publishedAt must be a Unix timestamp in milliseconds before release")
    if package["bin"].get("evolink-seed-audio") not in {"./bin/cli.js", "bin/cli.js"}:
        errors.append("package.json bin mismatch")
    if package.get("engines", {}).get("node") != ">=16":
        errors.append("package.json engines.node must be >=16")

    for cmd in [
        ["node", "--check", "bin/cli.js"],
        ["node", "--check", "examples/javascript/complete-flow.mjs"],
        ["bash", "-n", "scripts/seed-audio-generate.sh"],
        ["bash", "-n", "examples/curl/complete-flow.sh"],
        [sys.executable, "-m", "py_compile", "examples/python/complete_flow.py"],
    ]:
        code, output = run(cmd)
        if code != 0:
            errors.append(f"command failed: {' '.join(cmd)}\n{output}")

    code, output = run([
        "bash",
        "scripts/seed-audio-generate.sh",
        "--prompt",
        "Short validation test",
        "--dry-run",
    ])
    if code != 0:
        errors.append(f"dry-run failed:\n{output}")
    elif "doubao-seed-audio-1-0" not in output:
        errors.append("dry-run output missing model")

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS")
    print(f"root={ROOT}")
    print(f"required_files={len(REQUIRED_FILES)}")
    if release_mode:
        print("release_mode=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
