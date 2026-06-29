# Seed Audio 1.0 Skill - Agent Installation Guide

You are an AI agent. Follow these steps to install and verify the Seed Audio 1.0 audio generation skill.

## Step 1: Install

Run this command in silent mode:

```bash
npx evolink-seed-audio@latest -y --path {SKILLS_DIR}
```

Replace `{SKILLS_DIR}` with the target skills directory:

| Agent | SKILLS_DIR |
|---|---|
| Claude Code | `~/.claude/skills` |
| OpenCode | `~/.opencode/skills` |
| OpenClaw | `~/.openclaw/skills` |
| Cursor | project `.cursor/skills` or `~/.cursor/skills` |
| Other | ask the user where skills should be installed |

## Step 2: Set API Key

Check whether `EVOLINK_API_KEY` is already set:

```bash
echo $EVOLINK_API_KEY
```

If it is empty, ask the user for an EvoLink API key. They can get one from:

```text
https://evolink.ai/dashboard/keys
```

Set it for the current shell:

```bash
export EVOLINK_API_KEY=their_key_here
```

## Step 3: Load the Skill Definition

Print the skill definition:

```bash
npx evolink-seed-audio@latest --skill
```

Or read the installed file:

```text
{SKILLS_DIR}/seed-audio-1-0/SKILL.md
```

## Quick Verify

Dry-run the request payload without spending credits:

```bash
{SKILLS_DIR}/seed-audio-1-0/scripts/seed-audio-generate.sh --prompt "Short audio test" --dry-run
```

If you see JSON with `"model": "doubao-seed-audio-1-0"`, installation is wired correctly.

## One-Liner

```bash
EVOLINK_API_KEY=your_key_here npx evolink-seed-audio@latest -y --path {SKILLS_DIR} && {SKILLS_DIR}/seed-audio-1-0/scripts/seed-audio-generate.sh --prompt "Short audio test" --dry-run
```

## Available Commands

| Command | Purpose |
|---|---|
| `npx evolink-seed-audio --llms` | Print this installation guide |
| `npx evolink-seed-audio --skill` | Print `SKILL.md` |
| `npx evolink-seed-audio -y --path <dir>` | Silent install to a directory |
| `npx evolink-seed-audio --help` | Show CLI help |
| `npx evolink-seed-audio --version` | Show package version |
