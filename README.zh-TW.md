# Seed Audio 1.0 Skill

<p align="center">
  <strong>透過 EvoLink 使用 Seed Audio 1.0 產生語音、對話、環境聲、音效與混合音訊場景。</strong>
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
  <a href="#-menu">選單</a> -
  <a href="#installation">安裝</a> -
  <a href="#seed-audio-10-api-quick-start">API 快速開始</a> -
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
- [Seed Audio 1.0 API 快速開始](#seed-audio-10-api-quick-start)
- [檔案結構](#file-structure)
- [疑難排解](#troubleshooting)
- [相容性](#compatibility)
- [授權](#license)
- [社群](#community)
- [Star 歷史](#star-history)

<a id="what-is-this"></a>

## 這是什麼？

| 欄位 | 值 |
|---|---|
| Skill | Seed Audio 1.0 Skill |
| 模型 | Seed Audio 1.0 (`doubao-seed-audio-1-0`) |
| 維護入口 | `api-skill` |
| 使用者入口 | API 快速開始與 agent skill 安裝 |

當你想完成以下事情時，可以使用這個倉庫：

- 用完整的非同步建立與輪詢流程呼叫 EvoLink Seed-Audio API
- 透過 `npx evolink-seed-audio` 安裝 agent skill
- 產生旁白、多角色對話、環境聲、音效與混合音訊場景
- 查看請求參數、回應結構、callback、錯誤與音色參考

---

<a id="installation"></a>

## 安裝

### 快速安裝 (OpenClaw)

```bash
openclaw skills add https://github.com/cheercheung/seed-audio-1-0-skill
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
npx evolink-seed-audio -y --path ~/.claude/skills
```

### 手動安裝

```bash
git clone https://github.com/cheercheung/seed-audio-1-0-skill.git
cd seed-audio-1-0-skill
openclaw skills add .
```

### Agent 自動安裝

Claude Code:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.claude/skills

然後設定 EVOLINK_API_KEY 並閱讀：
~/.claude/skills/seed-audio-1-0/SKILL.md
```

OpenCode:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.opencode/skills

然後設定 EVOLINK_API_KEY 並閱讀：
~/.opencode/skills/seed-audio-1-0/SKILL.md
```

OpenClaw:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.openclaw/skills

然後設定 EVOLINK_API_KEY 並閱讀：
~/.openclaw/skills/seed-audio-1-0/SKILL.md
```

一行命令:

```bash
EVOLINK_API_KEY=your_key_here npx evolink-seed-audio@latest -y --path ~/.claude/skills
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

---

<a id="seed-audio-10-api-quick-start"></a>

## Seed Audio 1.0 API 快速開始

### 快速 API 請求

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

這個 API 是非同步的。建立請求會回傳任務 `id`；持續查詢，直到任務狀態變成 `completed`、`failed` 或 `cancelled`：

```bash
curl --request GET \
  --url "https://api.evolink.ai/v1/tasks/{task_id}" \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}"
```

### 完整首次執行流程

```bash
node examples/javascript/complete-flow.mjs
```

或者使用倉庫內建腳本：

```bash
scripts/seed-audio-generate.sh \
  --prompt "Create a cinematic 15-second rainforest ambience with distant birds, light rain, and a calm documentary narrator." \
  --format mp3
```

### 生成模式

| 模式 | 使用方式 |
|---|---|
| 文字生成音訊 | 只傳入 `prompt`。 |
| 聲音參考 | 最多傳入 3 個 `audio_references`；在 prompt 中用 `@audio1`、`@audio2`、`@audio3` 引用。 |
| 參考圖片 | 傳入一個 `image_urls` 項目。不要把 `image_urls` 和 `audio_references` 一起使用。 |
| Callback | 傳入 `callback_url` 接收任務終態。 |

### 腳本參考

```bash
scripts/seed-audio-generate.sh --help
npx evolink-seed-audio@latest --llms
npx evolink-seed-audio@latest --skill
```

### API 參數

| 參數 | 必填 | 說明 |
|---|---:|---|
| `model` | 是 | 使用 `doubao-seed-audio-1-0` |
| `prompt` | 是 | 最多 1500 個字元 |
| `audio_references` | no | 最多 3 個預設聲音或參考音訊 URL |
| `image_urls` | no | 一個參考圖片 URL |
| `format` | no | `wav`、`mp3`、`pcm`、`ogg_opus`；預設 `wav` |
| `sample_rate` | no | `8000`、`16000`、`24000`、`32000`、`44100`、`48000` |
| `speech_rate` | no | `0.5` 到 `2.0` |
| `loudness_rate` | no | `0.5` 到 `2.0` |
| `pitch_rate` | no | `-12` 到 `12` 個半音 |
| `callback_url` | no | 用於接收任務終態的 HTTPS callback URL |

更多資訊見 [docs/api-reference.md](docs/api-reference.md)、[docs/task-lifecycle.md](docs/task-lifecycle.md)、[docs/response-schema.md](docs/response-schema.md)、[docs/errors.md](docs/errors.md)、[docs/callbacks.md](docs/callbacks.md)、[docs/voices.md](docs/voices.md) 和 [references/api-params.md](references/api-params.md)。

---

<a id="file-structure"></a>

## 檔案結構

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
| Claude Code | `npx evolink-seed-audio -y --path ~/.claude/skills` | 支援 |
| OpenCode | `npx evolink-seed-audio -y --path ~/.opencode/skills` | 支援路徑安裝 |
| OpenClaw | `openclaw skills add` 或 `npx ... --path ~/.openclaw/skills` | 支援 |
| Cursor | `npx ... --path ~/.cursor/skills` 或專案 `.cursor/skills` | 支援 |
| Node.js | `>=16` | 由 `package.json` 要求 |
| Shell | bash + curl + python3 | 由 `scripts/seed-audio-generate.sh` 要求 |

---

<a id="license"></a>

## 授權

MIT。見 [LICENSE](LICENSE)。

---

<a id="community"></a>

## 社群

- [在 EvoLink 上使用 Seed-Audio](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community)
- [建立 EvoLink API key](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-api-key)
- [閱讀官方 API 文件](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-docs)
- [閱讀官方音色列表](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0-voices?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-voices)

---

<a id="star-history"></a>

## Star 歷史

```text
倉庫公開後會顯示 Star 歷史。
```

<p align="center">
  Powered by <a href="https://evolink.ai?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=footer">EvoLink</a>
</p>
