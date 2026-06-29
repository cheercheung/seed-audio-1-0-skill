# Seed Audio 1.0 Skill

<p align="center">
  <strong>Generate speech, dialogue, ambience, sound effects, and mixed audio scenes with Seed Audio 1.0 through EvoLink.</strong>
</p>

<p align="center">
  <a href="https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=banner">
    <img src="assets/banner.jpg" alt="seed-audio-1-0-agent-skill" width="100%" />
  </a>
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/evolink-seed-audio"><img src="https://img.shields.io/npm/v/evolink-seed-audio?color=cb3837&label=npm" alt="NPM version"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  <a href="https://github.com/cheercheung/seed-audio-1-0-skill/stargazers"><img src="https://img.shields.io/github/stars/cheercheung/seed-audio-1-0-skill?style=flat" alt="GitHub stars"></a>
  <a href="https://github.com/cheercheung/seed-audio-1-0-skill/commits/main/"><img src="https://img.shields.io/github/last-commit/cheercheung/seed-audio-1-0-skill" alt="Last commit"></a>
</p>

<p align="center">
  <a href="#-menu">Menu</a> -
  <a href="#installation">Install</a> -
  <a href="#getting-an-api-key">API Key</a> -
  <a href="https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=readme-top">Try on EvoLink</a>
</p>

<p align="center">
  <a href="README.md"><img src="https://img.shields.io/badge/🇺🇸_English-Read-111111" alt="English"></a>
  <a href="README.es.md"><img src="https://img.shields.io/badge/🇪🇸_Español-Ver-ffb703" alt="Español"></a>
  <a href="README.pt.md"><img src="https://img.shields.io/badge/🇵🇹_Português-Ver-2a9d8f" alt="Português"></a>
  <a href="README.ja.md"><img src="https://img.shields.io/badge/🇯🇵_日本語-表示-52b788" alt="日本語"></a>
  <a href="README.ko.md"><img src="https://img.shields.io/badge/🇰🇷_한국어-보기-4ea8de" alt="한국어"></a>
  <a href="README.de.md"><img src="https://img.shields.io/badge/🇩🇪_Deutsch-Ansehen-f4a261" alt="Deutsch"></a>
  <a href="README.fr.md"><img src="https://img.shields.io/badge/🇫🇷_Français-Voir-e76f51" alt="Français"></a>
  <a href="README.tr.md"><img src="https://img.shields.io/badge/🇹🇷_Türkçe-Görüntüle-d62828" alt="Türkçe"></a>
  <a href="README.zh-TW.md"><img src="https://img.shields.io/badge/🇹🇼_繁體中文-查看-8338ec" alt="繁體中文"></a>
  <a href="README.zh-CN.md"><img src="https://img.shields.io/badge/🇨🇳_简体中文-查看-ef476f" alt="简体中文"></a>
  <a href="README.ru.md"><img src="https://img.shields.io/badge/🇷🇺_Русский-Смотреть-577590" alt="Русский"></a>
</p>

> **AI Agent?** Skip the README, go straight to [**llms-install.md**](llms-install.md) for step-by-step installation instructions designed for you.

---

## 📑 Menu

- [What is This?](#what-is-this)
- [Installation](#installation)
- [Getting an API Key](#getting-an-api-key)
- [Troubleshooting](#troubleshooting)
- [Compatibility](#compatibility)
- [License](#license)

<a id="what-is-this"></a>

## What is This?

| Field | Value |
|---|---|
| Skill | Seed Audio 1.0 Skill |
| Model | Seed Audio 1.0 |
| Maintained surface | `api-skill` |
| User entrances | agent skill install and API key setup |

Use this repository when you want to:

- call the EvoLink Seed-Audio API with a complete async create-and-poll flow
- install an agent skill with `npx evolink-seed-audio`
- generate narration, multi-character dialogue, ambience, sound effects, and mixed audio scenes
- inspect request parameters, response shapes, callbacks, errors, and voice references

---

<a id="installation"></a>

## Installation

### Quick Install (Codex)

```bash
npx evolink-seed-audio -y --path ~/.codex/skills
```

### Install via npm (Recommended)

```bash
npx evolink-seed-audio
```

Silent install for agents:

```bash
npx evolink-seed-audio -y
```

Install to a specific skills directory:

```bash
npx evolink-seed-audio -y --path ~/.codex/skills
```

### Manual Install

```bash
git clone https://github.com/cheercheung/seed-audio-1-0-skill.git
cd seed-audio-1-0-skill
node bin/cli.js -y --path ~/.codex/skills
```

### Agent Auto-Install

Codex:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.codex/skills

Then set EVOLINK_API_KEY and read:
~/.codex/skills/seed-audio-1-0/SKILL.md
```

Claude Code:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.claude/skills

Then set EVOLINK_API_KEY and read:
~/.claude/skills/seed-audio-1-0/SKILL.md
```

Hermes Agent:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.hermes/skills

Then set EVOLINK_API_KEY and read:
~/.hermes/skills/seed-audio-1-0/SKILL.md
```

One-Liner:

```bash
EVOLINK_API_KEY=your_key_here npx evolink-seed-audio@latest -y --path ~/.codex/skills
```

---

<a id="getting-an-api-key"></a>

## Getting an API Key

1. Open [EvoLink API Keys](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=api-key).
2. Create or copy an API key.
3. Export it in your shell:

```bash
export EVOLINK_API_KEY="your_key_here"
```

4. Start a generation task:

```bash
scripts/seed-audio-generate.sh \
  --prompt "Create a short welcome narration with a warm studio voice." \
  --format mp3
```

<a id="troubleshooting"></a>

## Troubleshooting

| Issue | Likely cause | Action |
|---|---|---|
| `EVOLINK_API_KEY is not set` | Missing API key | Export `EVOLINK_API_KEY` and retry. |
| `create request failed` | Invalid key, request body, or network failure | Run with `--dry-run`, then check `docs/errors.md`. |
| `POLL_TIMEOUT` | The task did not finish before local polling ended | Query `GET /v1/tasks/{task_id}` later. Do not resubmit automatically. |
| No audio URL found | Response shape changed or task has no generated asset yet | Save the full task JSON and compare with `docs/response-schema.md`. |

---

<a id="compatibility"></a>

## Compatibility

| Agent or runtime | Install method | Status |
|---|---|---|
| Codex | `npx evolink-seed-audio -y --path ~/.codex/skills` | Supported |
| Claude Code | `npx evolink-seed-audio -y --path ~/.claude/skills` | Supported |
| Hermes Agent | `npx evolink-seed-audio -y --path ~/.hermes/skills` | Supported by path install |
| Node.js | `>=16` | Required by `package.json` |
| Shell | bash + curl + python3 | Required by `scripts/seed-audio-generate.sh` |

---

<a id="license"></a>

## License

MIT. See [LICENSE](LICENSE).

<p align="center">
  Powered by <a href="https://evolink.ai?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=footer">EvoLink</a>
</p>
