# Seed Audio 1.0 Skill

<p align="center">
  <strong>通过 EvoLink 使用 Seed Audio 1.0 生成语音、对话、环境声、音效和混合音频场景。</strong>
</p>

<p align="center">
  <a href="https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=banner">
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
  <a href="#-menu">菜单</a> -
  <a href="#installation">安装</a> -
  <a href="#seed-audio-10-api-quick-start">API 快速开始</a> -
  <a href="#getting-an-api-key">API Key</a> -
  <a href="https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=readme-top">在 EvoLink 上使用</a>
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

> **AI Agent？** 可以跳过 README，直接阅读为 agent 准备的 [**llms-install.md**](llms-install.md) 分步安装指南。

---

## 📑 菜单

- [这是什么？](#what-is-this)
- [安装](#installation)
- [获取 API Key](#getting-an-api-key)
- [Seed Audio 1.0 API 快速开始](#seed-audio-10-api-quick-start)
- [文件结构](#file-structure)
- [故障排查](#troubleshooting)
- [兼容性](#compatibility)
- [许可证](#license)
- [社区](#community)
- [Star 历史](#star-history)

<a id="what-is-this"></a>

## 这是什么？

| 字段 | 值 |
|---|---|
| Skill | Seed Audio 1.0 Skill |
| 模型 | Seed Audio 1.0 (`doubao-seed-audio-1-0`) |
| 维护入口 | `api-skill` |
| 用户入口 | API 快速开始和 agent skill 安装 |

当你想完成这些事情时，可以使用这个仓库：

- 用完整的异步创建和轮询流程调用 EvoLink Seed-Audio API
- 通过 `npx evolink-seed-audio` 安装 agent skill
- 生成旁白、多角色对话、环境声、音效和混合音频场景
- 查看请求参数、响应结构、callback、错误和音色参考

---

<a id="installation"></a>

## 安装

### 快速安装 (OpenClaw)

```bash
openclaw skills add https://github.com/cheercheung/seed-audio-1-0-skill
```

### 通过 npm 安装（推荐）

```bash
npx evolink-seed-audio
```

agent 静默安装：

```bash
npx evolink-seed-audio -y
```

安装到指定 skills 目录：

```bash
npx evolink-seed-audio -y --path ~/.claude/skills
```

### 手动安装

```bash
git clone https://github.com/cheercheung/seed-audio-1-0-skill.git
cd seed-audio-1-0-skill
openclaw skills add .
```

### Agent 自动安装

Claude Code:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.claude/skills

然后设置 EVOLINK_API_KEY 并阅读：
~/.claude/skills/seed-audio-1-0/SKILL.md
```

OpenCode:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.opencode/skills

然后设置 EVOLINK_API_KEY 并阅读：
~/.opencode/skills/seed-audio-1-0/SKILL.md
```

OpenClaw:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.openclaw/skills

然后设置 EVOLINK_API_KEY 并阅读：
~/.openclaw/skills/seed-audio-1-0/SKILL.md
```

一行命令:

```bash
EVOLINK_API_KEY=your_key_here npx evolink-seed-audio@latest -y --path ~/.claude/skills
```

---

<a id="getting-an-api-key"></a>

## 获取 API Key

1. 打开 [EvoLink API Keys](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=api-key)。
2. 创建或复制一个 API key。
3. 在 shell 中导出它：

```bash
export EVOLINK_API_KEY="your_key_here"
```

4. 启动一个生成任务：

```bash
scripts/seed-audio-generate.sh \
  --prompt "Create a short welcome narration with a warm studio voice." \
  --format mp3
```

---

<a id="seed-audio-10-api-quick-start"></a>

## Seed Audio 1.0 API 快速开始

### 快速 API 请求

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/audios/generations \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "doubao-seed-audio-1-0",
    "prompt": "Create a 20-second premium product video audio bed: soft electronic music, subtle camera whoosh, a glass bottle placed on marble, calm female narration, clean studio ambience.",
    "format": "mp3",
    "sample_rate": 24000
  }'
```

这个 API 是异步的。创建请求会返回任务 `id`；持续查询，直到任务状态变为 `completed`、`failed` 或 `cancelled`：

```bash
curl --request GET \
  --url "https://api.evolink.ai/v1/tasks/{task_id}" \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}"
```

### 完整首次运行流程

```bash
node examples/javascript/complete-flow.mjs
```

或者使用仓库自带脚本：

```bash
scripts/seed-audio-generate.sh \
  --prompt "Create a cinematic 15-second rainforest ambience with distant birds, light rain, and a calm documentary narrator." \
  --format mp3
```

### 生成模式

| 模式 | 使用方式 |
|---|---|
| 文本生成音频 | 只传入 `prompt`。 |
| 声音参考 | 最多传入 3 个 `audio_references`；在 prompt 中用 `@audio1`、`@audio2`、`@audio3` 引用。 |
| 参考图片 | 传入一个 `image_urls` 条目。不要把 `image_urls` 和 `audio_references` 一起使用。 |
| Callback | 传入 `callback_url` 接收任务终态。 |

### 脚本参考

```bash
scripts/seed-audio-generate.sh --help
npx evolink-seed-audio@latest --llms
npx evolink-seed-audio@latest --skill
```

### API 参数

| 参数 | 必填 | 说明 |
|---|---:|---|
| `model` | 是 | 使用 `doubao-seed-audio-1-0` |
| `prompt` | 是 | 最多 1500 个字符 |
| `audio_references` | no | 最多 3 个预设声音或参考音频 URL |
| `image_urls` | no | 一个参考图片 URL |
| `format` | no | `wav`、`mp3`、`pcm`、`ogg_opus`；默认 `wav` |
| `sample_rate` | no | `8000`、`16000`、`24000`、`32000`、`44100`、`48000` |
| `speech_rate` | no | `0.5` 到 `2.0` |
| `loudness_rate` | no | `0.5` 到 `2.0` |
| `pitch_rate` | no | `-12` 到 `12` 个半音 |
| `callback_url` | no | 用于接收任务终态的 HTTPS callback URL |

更多信息见 [docs/api-reference.md](docs/api-reference.md)、[docs/task-lifecycle.md](docs/task-lifecycle.md)、[docs/response-schema.md](docs/response-schema.md)、[docs/errors.md](docs/errors.md)、[docs/callbacks.md](docs/callbacks.md)、[docs/voices.md](docs/voices.md) 和 [references/api-params.md](references/api-params.md)。

---

<a id="file-structure"></a>

## 文件结构

```text
.
├── README.md
├── README.es.md ... README.ru.md
├── SKILL.md
├── llms-install.md
├── _meta.json
├── package.json
├── bin/cli.js
├── scripts/seed-audio-generate.sh
├── docs/
├── examples/
├── references/
└── assets/banner.jpg
```

---

<a id="troubleshooting"></a>

## 故障排查

| 问题 | 可能原因 | 处理方式 |
|---|---|---|
| `EVOLINK_API_KEY is not set` | 缺少 API key | 导出 `EVOLINK_API_KEY` 后重试。 |
| `create request failed` | key 无效、请求体错误或网络失败 | 使用 `--dry-run` 运行，然后查看 `docs/errors.md`。 |
| `POLL_TIMEOUT` | 任务没有在本地轮询窗口内完成 | 稍后查询 `GET /v1/tasks/{task_id}`。不要自动重新提交。 |
| 没有找到音频 URL | 响应结构变化，或任务还没有生成可用资源 | 保存完整任务 JSON，并与 `docs/response-schema.md` 对照。 |

---

<a id="compatibility"></a>

## 兼容性

| Agent 或运行环境 | 安装方式 | 状态 |
|---|---|---|
| Claude Code | `npx evolink-seed-audio -y --path ~/.claude/skills` | 支持 |
| OpenCode | `npx evolink-seed-audio -y --path ~/.opencode/skills` | 支持路径安装 |
| OpenClaw | `openclaw skills add` 或 `npx ... --path ~/.openclaw/skills` | 支持 |
| Cursor | `npx ... --path ~/.cursor/skills` 或项目 `.cursor/skills` | 支持 |
| Node.js | `>=16` | 由 `package.json` 要求 |
| Shell | bash + curl + python3 | 由 `scripts/seed-audio-generate.sh` 要求 |

---

<a id="license"></a>

## 许可证

MIT。见 [LICENSE](LICENSE)。

---

<a id="community"></a>

## 社区

- [在 EvoLink 上使用 Seed-Audio](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community)
- [创建 EvoLink API key](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-api-key)
- [阅读官方 API 文档](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-docs)
- [阅读官方音色列表](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0-voices?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-voices)

---

<a id="star-history"></a>

## Star 历史

```text
仓库公开后会显示 Star 历史。
```

<p align="center">
  Powered by <a href="https://evolink.ai?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=footer">EvoLink</a>
</p>
