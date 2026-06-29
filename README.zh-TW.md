# Seed Audio 1.0 Skill

<p align="center">
  <strong>透過 EvoLink 使用 Seed Audio 1.0 產生語音、對話、環境聲、音效與混合音訊場景。</strong>
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
  <a href="#-menu">選單</a> -
  <a href="#installation">安裝</a> -
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

> **AI Agent？** 可以略過 README，直接閱讀為 agent 準備的 [**llms-install.md**](llms-install.md) 分步安裝指南。

---

## 📑 選單

- [這是什麼？](#what-is-this)
- [安裝](#installation)
- [取得 API Key](#getting-an-api-key)
- [疑難排解](#troubleshooting)
- [相容性](#compatibility)
- [授權](#license)

<a id="what-is-this"></a>

## 這是什麼？

| 欄位 | 值 |
|---|---|
| Skill | Seed Audio 1.0 Skill |
| 模型 | Seed Audio 1.0 (`doubao-seed-audio-1-0`) |
| 維護入口 | `api-skill` |
| 使用者入口 | agent skill 安裝和 API Key 設定 |

當你想完成以下事情時，可以使用這個倉庫：

- 用完整的非同步建立與輪詢流程呼叫 EvoLink Seed-Audio API
- 透過 `npx evolink-seed-audio` 安裝 agent skill
- 產生旁白、多角色對話、環境聲、音效與混合音訊場景
- 查看請求參數、回應結構、callback、錯誤與音色參考

---

<a id="installation"></a>

## 安裝

### 快速安裝 (Codex)

```bash
npx evolink-seed-audio -y --path ~/.codex/skills
```

### 透過 npm 安裝（推薦）

```bash
npx evolink-seed-audio
```

agent 靜默安裝：

```bash
npx evolink-seed-audio -y
```

安裝到指定 skills 目錄：

```bash
npx evolink-seed-audio -y --path ~/.codex/skills
```

### 手動安裝

```bash
git clone https://github.com/cheercheung/seed-audio-1-0-skill.git
cd seed-audio-1-0-skill
node bin/cli.js -y --path ~/.codex/skills
```

### Agent 自動安裝

Codex:

```text
執行以下命令安裝 Seed Audio skill：
npx evolink-seed-audio@latest -y --path ~/.codex/skills

然後設定 EVOLINK_API_KEY 並閱讀：
~/.codex/skills/seed-audio-1-0/SKILL.md
```

Claude Code:

```text
執行以下命令安裝 Seed Audio skill：
npx evolink-seed-audio@latest -y --path ~/.claude/skills

然後設定 EVOLINK_API_KEY 並閱讀：
~/.claude/skills/seed-audio-1-0/SKILL.md
```

Hermes Agent:

```text
執行以下命令安裝 Seed Audio skill：
npx evolink-seed-audio@latest -y --path ~/.hermes/skills

然後設定 EVOLINK_API_KEY 並閱讀：
~/.hermes/skills/seed-audio-1-0/SKILL.md
```

一行命令：

```bash
EVOLINK_API_KEY=your_key_here npx evolink-seed-audio@latest -y --path ~/.codex/skills
```

---

<a id="getting-an-api-key"></a>

## 取得 API Key

1. 開啟 [EvoLink API Keys](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=api-key)。
2. 建立或複製一個 API key。
3. 在 shell 中匯出它：

```bash
export EVOLINK_API_KEY="your_key_here"
```

4. 啟動一個生成任務：

```bash
scripts/seed-audio-generate.sh \
  --prompt "Create a short welcome narration with a warm studio voice." \
  --format mp3
```

<a id="troubleshooting"></a>

## 疑難排解

| 問題 | 可能原因 | 處理方式 |
|---|---|---|
| `EVOLINK_API_KEY is not set` | 缺少 API key | 匯出 `EVOLINK_API_KEY` 後重試。 |
| `create request failed` | key 無效、請求體錯誤或網路失敗 | 使用 `--dry-run` 執行，然後查看 `docs/errors.md`。 |
| `POLL_TIMEOUT` | 任務沒有在本地輪詢視窗內完成 | 稍後查詢 `GET /v1/tasks/{task_id}`。不要自動重新提交。 |
| 沒有找到音訊 URL | 回應結構變更，或任務還沒有生成可用資源 | 保存完整任務 JSON，並與 `docs/response-schema.md` 對照。 |

---

<a id="compatibility"></a>

## 相容性

| Agent 或執行環境 | 安裝方式 | 狀態 |
|---|---|---|
| Codex | `npx evolink-seed-audio -y --path ~/.codex/skills` | 支援 |
| Claude Code | `npx evolink-seed-audio -y --path ~/.claude/skills` | 支援 |
| Hermes Agent | `npx evolink-seed-audio -y --path ~/.hermes/skills` | 支援路徑安裝 |
| Node.js | `>=16` | 由 `package.json` 要求 |
| Shell | bash + curl + python3 | 由 `scripts/seed-audio-generate.sh` 要求 |

---

<a id="license"></a>

## 授權

MIT。見 [LICENSE](LICENSE)。

<p align="center">
  Powered by <a href="https://evolink.ai?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=footer">EvoLink</a>
</p>
