# Seed Audio 1.0 Skill

<p align="center">
  <strong>EvoLink 経由で Seed Audio 1.0 を使い、音声、会話、環境音、効果音、複合オーディオシーンを生成します。</strong>
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
  <a href="#-menu">メニュー</a> -
  <a href="#installation">インストール</a> -
  <a href="#seed-audio-10-api-quick-start">API クイックスタート</a> -
  <a href="#getting-an-api-key">API キー</a> -
  <a href="https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=readme-top">EvoLink で試す</a>
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

> **AI エージェントですか？** README を読む代わりに、エージェント向けの手順がある [**llms-install.md**](llms-install.md) に進んでください。

---

## 📑 メニュー

- [これは何ですか？](#what-is-this)
- [インストール](#installation)
- [API キーの取得](#getting-an-api-key)
- [Seed Audio 1.0 API クイックスタート](#seed-audio-10-api-quick-start)
- [ファイル構成](#file-structure)
- [トラブルシューティング](#troubleshooting)
- [互換性](#compatibility)
- [ライセンス](#license)
- [コミュニティ](#community)
- [スター履歴](#star-history)

<a id="what-is-this"></a>

## これは何ですか？

| 項目 | 値 |
|---|---|
| Skill | Seed Audio 1.0 Skill |
| モデル | Seed Audio 1.0 (`doubao-seed-audio-1-0`) |
| 保守対象 | `api-skill` |
| ユーザー入口 | API クイックスタートとエージェント skill のインストール |

このリポジトリは、次のことをしたいときに使います。

- EvoLink Seed-Audio API を、作成からポーリングまでの非同期フローで呼び出す
- `npx evolink-seed-audio` でエージェント skill をインストールする
- ナレーション、複数人物の会話、環境音、効果音、複合オーディオシーンを生成する
- リクエストパラメータ、レスポンス形式、コールバック、エラー、音声リファレンスを確認する

---

<a id="installation"></a>

## インストール

### クイックインストール (OpenClaw)

```bash
openclaw skills add https://github.com/cheercheung/seed-audio-1-0-skill
```

### npm でインストール (推奨)

```bash
npx evolink-seed-audio
```

エージェント向けサイレントインストール:

```bash
npx evolink-seed-audio -y
```

指定した skills ディレクトリにインストール:

```bash
npx evolink-seed-audio -y --path ~/.claude/skills
```

### 手動インストール

```bash
git clone https://github.com/cheercheung/seed-audio-1-0-skill.git
cd seed-audio-1-0-skill
openclaw skills add .
```

### エージェント自動インストール

Claude Code:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.claude/skills

その後、EVOLINK_API_KEY を設定して次を読みます:
~/.claude/skills/seed-audio-1-0/SKILL.md
```

OpenCode:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.opencode/skills

その後、EVOLINK_API_KEY を設定して次を読みます:
~/.opencode/skills/seed-audio-1-0/SKILL.md
```

OpenClaw:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.openclaw/skills

その後、EVOLINK_API_KEY を設定して次を読みます:
~/.openclaw/skills/seed-audio-1-0/SKILL.md
```

ワンライナー:

```bash
EVOLINK_API_KEY=your_key_here npx evolink-seed-audio@latest -y --path ~/.claude/skills
```

---

<a id="getting-an-api-key"></a>

## API キーの取得

1. [EvoLink API Keys](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=api-key) を開きます。
2. API キーを作成またはコピーします。
3. シェルでエクスポートします:

```bash
export EVOLINK_API_KEY="your_key_here"
```

4. 生成タスクを開始します:

```bash
scripts/seed-audio-generate.sh \
  --prompt "Create a short welcome narration with a warm studio voice." \
  --format mp3
```

---

<a id="seed-audio-10-api-quick-start"></a>

## Seed Audio 1.0 API クイックスタート

### API の最小リクエスト

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

この API は非同期です。作成リクエストはタスクの `id` を返します。タスクが `completed`、`failed`、`cancelled` のいずれかになるまでポーリングしてください:

```bash
curl --request GET \
  --url "https://api.evolink.ai/v1/tasks/{task_id}" \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}"
```

### 初回実行の完全フロー

```bash
node examples/javascript/complete-flow.mjs
```

または同梱スクリプトを使います:

```bash
scripts/seed-audio-generate.sh \
  --prompt "Create a cinematic 15-second rainforest ambience with distant birds, light rain, and a calm documentary narrator." \
  --format mp3
```

### 生成モード

| モード | 使い方 |
|---|---|
| テキストから音声 | `prompt` だけを渡します。 |
| 音声リファレンス | 最大 3 つの `audio_references` を渡し、prompt 内で `@audio1`、`@audio2`、`@audio3` として参照します。 |
| 参照画像 | `image_urls` を 1 つ渡します。`image_urls` と `audio_references` は同時に使わないでください。 |
| Callback | 終端状態を受け取るために `callback_url` を渡します。 |

### スクリプトリファレンス

```bash
scripts/seed-audio-generate.sh --help
npx evolink-seed-audio@latest --llms
npx evolink-seed-audio@latest --skill
```

### API パラメータ

| パラメータ | 必須 | 説明 |
|---|---:|---|
| `model` | はい | `doubao-seed-audio-1-0` を使用 |
| `prompt` | はい | 最大 1500 文字 |
| `audio_references` | no | 最大 3 つのプリセット音声または参照音声 URL |
| `image_urls` | no | 参照画像 URL を 1 つ |
| `format` | no | `wav`、`mp3`、`pcm`、`ogg_opus`。既定は `wav` |
| `sample_rate` | no | `8000`、`16000`、`24000`、`32000`、`44100`、`48000` |
| `speech_rate` | no | `0.5` から `2.0` |
| `loudness_rate` | no | `0.5` から `2.0` |
| `pitch_rate` | no | `-12` から `12` 半音 |
| `callback_url` | no | 終端状態を受け取る HTTPS callback URL |

詳しくは [docs/api-reference.md](docs/api-reference.md)、[docs/task-lifecycle.md](docs/task-lifecycle.md)、[docs/response-schema.md](docs/response-schema.md)、[docs/errors.md](docs/errors.md)、[docs/callbacks.md](docs/callbacks.md)、[docs/voices.md](docs/voices.md)、[references/api-params.md](references/api-params.md) を参照してください。

---

<a id="file-structure"></a>

## ファイル構成

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

## トラブルシューティング

| 問題 | 考えられる原因 | 対応 |
|---|---|---|
| `EVOLINK_API_KEY is not set` | API キーがありません | `EVOLINK_API_KEY` をエクスポートして再試行します。 |
| `create request failed` | キー、リクエスト本文、またはネットワークに問題があります | `--dry-run` で実行し、`docs/errors.md` を確認します。 |
| `POLL_TIMEOUT` | ローカルのポーリング時間内にタスクが完了しませんでした | 後で `GET /v1/tasks/{task_id}` を問い合わせます。自動で再送信しないでください。 |
| 音声 URL が見つかりません | レスポンス形式が変わったか、タスクに生成済みアセットがまだありません | タスク JSON 全体を保存し、`docs/response-schema.md` と比較します。 |

---

<a id="compatibility"></a>

## 互換性

| エージェントまたはランタイム | インストール方法 | 状態 |
|---|---|---|
| Claude Code | `npx evolink-seed-audio -y --path ~/.claude/skills` | 対応 |
| OpenCode | `npx evolink-seed-audio -y --path ~/.opencode/skills` | パス指定インストールで対応 |
| OpenClaw | `openclaw skills add` または `npx ... --path ~/.openclaw/skills` | 対応 |
| Cursor | `npx ... --path ~/.cursor/skills` またはプロジェクトの `.cursor/skills` | 対応 |
| Node.js | `>=16` | `package.json` で必須 |
| Shell | bash + curl + python3 | `scripts/seed-audio-generate.sh` で必須 |

---

<a id="license"></a>

## ライセンス

MIT。詳しくは [LICENSE](LICENSE) を参照してください。

---

<a id="community"></a>

## コミュニティ

- [EvoLink で Seed-Audio を試す](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community)
- [EvoLink API キーを作成する](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-api-key)
- [公式 API ドキュメントを読む](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-docs)
- [公式音声リストを読む](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0-voices?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-voices)

---

<a id="star-history"></a>

## スター履歴

```text
リポジトリが公開されるとスター履歴を利用できます。
```

<p align="center">
  Powered by <a href="https://evolink.ai?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=footer">EvoLink</a>
</p>
