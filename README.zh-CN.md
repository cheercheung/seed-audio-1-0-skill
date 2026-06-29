# Seed Audio 1.0 Skill

<p align="center">
  <strong>通过 EvoLink 使用 Seed Audio 1.0 生成语音、对话、环境声、音效和混合音频场景。</strong>
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
  <a href="#-menu">菜单</a> -
  <a href="#installation">安装</a> -
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
- [故障排查](#troubleshooting)
- [兼容性](#compatibility)
- [许可证](#license)

<a id="what-is-this"></a>

## 这是什么？

| 字段 | 值 |
|---|---|
| Skill | Seed Audio 1.0 Skill |
| 模型 | Seed Audio 1.0 (`doubao-seed-audio-1-0`) |
| 维护入口 | `api-skill` |
| 用户入口 | agent skill 安装和 API Key 设置 |

当你想完成这些事情时，可以使用这个仓库：

- 用完整的异步创建和轮询流程调用 EvoLink Seed-Audio API
- 通过 `npx evolink-seed-audio` 安装 agent skill
- 生成旁白、多角色对话、环境声、音效和混合音频场景
- 查看请求参数、响应结构、callback、错误和音色参考

---

<a id="installation"></a>

## 安装

### 快速安装 (Codex)

```bash
npx evolink-seed-audio -y --path ~/.codex/skills
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
npx evolink-seed-audio -y --path ~/.codex/skills
```

### 手动安装

```bash
git clone https://github.com/cheercheung/seed-audio-1-0-skill.git
cd seed-audio-1-0-skill
node bin/cli.js -y --path ~/.codex/skills
```

### Agent 自动安装

Codex:

```text
运行以下命令安装 Seed Audio skill：
npx evolink-seed-audio@latest -y --path ~/.codex/skills

然后设置 EVOLINK_API_KEY 并阅读：
~/.codex/skills/seed-audio-1-0/SKILL.md
```

Claude Code:

```text
运行以下命令安装 Seed Audio skill：
npx evolink-seed-audio@latest -y --path ~/.claude/skills

然后设置 EVOLINK_API_KEY 并阅读：
~/.claude/skills/seed-audio-1-0/SKILL.md
```

Hermes Agent:

```text
运行以下命令安装 Seed Audio skill：
npx evolink-seed-audio@latest -y --path ~/.hermes/skills

然后设置 EVOLINK_API_KEY 并阅读：
~/.hermes/skills/seed-audio-1-0/SKILL.md
```

一行命令：

```bash
EVOLINK_API_KEY=your_key_here npx evolink-seed-audio@latest -y --path ~/.codex/skills
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
| Codex | `npx evolink-seed-audio -y --path ~/.codex/skills` | 支持 |
| Claude Code | `npx evolink-seed-audio -y --path ~/.claude/skills` | 支持 |
| Hermes Agent | `npx evolink-seed-audio -y --path ~/.hermes/skills` | 支持路径安装 |
| Node.js | `>=16` | 由 `package.json` 要求 |
| Shell | bash + curl + python3 | 由 `scripts/seed-audio-generate.sh` 要求 |

---

<a id="license"></a>

## 许可证

MIT。见 [LICENSE](LICENSE)。

<p align="center">
  Powered by <a href="https://evolink.ai?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=footer">EvoLink</a>
</p>
