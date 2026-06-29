# Seed Audio 1.0 Skill

<p align="center">
  <strong>EvoLink 経由で Seed Audio 1.0 を使い、音声、会話、環境音、効果音、複合オーディオシーンを生成します。</strong>
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
  <a href="#-menu">メニュー</a> -
  <a href="#installation">インストール</a> -
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
- [トラブルシューティング](#troubleshooting)
- [互換性](#compatibility)
- [ライセンス](#license)

<a id="what-is-this"></a>

## これは何ですか？

| 項目 | 値 |
|---|---|
| Skill | Seed Audio 1.0 Skill |
| モデル | Seed Audio 1.0 |
| 保守対象 | `api-skill` |
| ユーザー入口 | Agent スキルのインストールと API キー設定 |

このリポジトリは、次のことをしたいときに使います。

- EvoLink Seed-Audio API を、作成からポーリングまでの非同期フローで呼び出す
- `npx evolink-seed-audio` でエージェント skill をインストールする
- ナレーション、複数人物の会話、環境音、効果音、複合オーディオシーンを生成する
- リクエストパラメータ、レスポンス形式、コールバック、エラー、音声リファレンスを確認する

---

<a id="installation"></a>

## インストール

### クイックインストール (Codex)

```bash
npx evolink-seed-audio -y --path ~/.codex/skills
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
npx evolink-seed-audio -y --path ~/.codex/skills
```

### 手動インストール

```bash
git clone https://github.com/cheercheung/seed-audio-1-0-skill.git
cd seed-audio-1-0-skill
node bin/cli.js -y --path ~/.codex/skills
```

### Agent 自動インストール

Codex:

```text
次のコマンドで Seed Audio skill をインストールします:
npx evolink-seed-audio@latest -y --path ~/.codex/skills

その後、EVOLINK_API_KEY を設定して次を読んでください:
~/.codex/skills/seed-audio-1-0/SKILL.md
```

Claude Code:

```text
次のコマンドで Seed Audio skill をインストールします:
npx evolink-seed-audio@latest -y --path ~/.claude/skills

その後、EVOLINK_API_KEY を設定して次を読んでください:
~/.claude/skills/seed-audio-1-0/SKILL.md
```

Hermes Agent:

```text
次のコマンドで Seed Audio skill をインストールします:
npx evolink-seed-audio@latest -y --path ~/.hermes/skills

その後、EVOLINK_API_KEY を設定して次を読んでください:
~/.hermes/skills/seed-audio-1-0/SKILL.md
```

ワンライナー:

```bash
EVOLINK_API_KEY=your_key_here npx evolink-seed-audio@latest -y --path ~/.codex/skills
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
| Codex | `npx evolink-seed-audio -y --path ~/.codex/skills` | 対応 |
| Claude Code | `npx evolink-seed-audio -y --path ~/.claude/skills` | 対応 |
| Hermes Agent | `npx evolink-seed-audio -y --path ~/.hermes/skills` | パス指定インストールで対応 |
| Node.js | `>=16` | `package.json` で必須 |
| Shell | bash + curl + python3 | `scripts/seed-audio-generate.sh` で必須 |

---

<a id="license"></a>

## ライセンス

MIT。詳しくは [LICENSE](LICENSE) を参照してください。

<p align="center">
  Powered by <a href="https://evolink.ai?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=footer">EvoLink</a>
</p>
