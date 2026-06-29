#!/usr/bin/env python3
"""Static validation for the Seed Audio API skill repository."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
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
    "assets/showcase/first-run.jpg",
    "assets/showcase/voice-reference.jpg",
    "assets/showcase/agent-install.jpg",
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
        "## 🖼️ Showcase",
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


def main() -> int:
    errors: list[str] = []

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

    package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
    meta = json.loads((ROOT / "_meta.json").read_text(encoding="utf-8"))
    if package["version"] != meta["version"]:
        errors.append("package.json version does not match _meta.json version")
    if meta["slug"] != "seed-audio-1-0":
        errors.append("_meta.json slug mismatch")
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
