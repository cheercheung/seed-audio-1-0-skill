# Seed Audio 1.0 Skill

<p align="center">
  <strong>EvoLink üzerinden Seed Audio 1.0 ile konuşma, diyalog, ambiyans, ses efektleri ve karma ses sahneleri oluşturun.</strong>
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
  <a href="#-menu">Menü</a> -
  <a href="#installation">Kurulum</a> -
  <a href="#getting-an-api-key">API Anahtarı</a> -
  <a href="https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=readme-top">EvoLink’te dene</a>
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

> **AI ajanı mısın?** README yerine, ajanlar için hazırlanmış adım adım kurulum kılavuzu olan [**llms-install.md**](llms-install.md) dosyasına geç.

---

## 📑 Menü

- [Bu nedir?](#what-is-this)
- [Kurulum](#installation)
- [API anahtarı alma](#getting-an-api-key)
- [Sorun giderme](#troubleshooting)
- [Uyumluluk](#compatibility)
- [Lisans](#license)

<a id="what-is-this"></a>

## Bu nedir?

| Alan | Değer |
|---|---|
| Skill | Seed Audio 1.0 Skill |
| Model | Seed Audio 1.0 |
| Bakımı yapılan yüzey | `api-skill` |
| Kullanıcı girişleri | agent skill kurulumu ve API anahtarı ayarı |

Şunları yapmak istediğinizde bu depoyu kullanın:

- tam bir asenkron oluşturma ve sorgulama akışıyla EvoLink Seed-Audio API’sini çağırmak
- `npx evolink-seed-audio` ile bir ajan skill’i kurmak
- anlatım, çok karakterli diyalog, ambiyans, ses efektleri ve karma ses sahneleri üretmek
- istek parametrelerini, yanıt biçimlerini, callback’leri, hataları ve ses referanslarını incelemek

---

<a id="installation"></a>

## Kurulum

### Hızlı kurulum (Codex)

```bash
npx evolink-seed-audio -y --path ~/.codex/skills
```

### npm ile kurulum (önerilir)

```bash
npx evolink-seed-audio
```

Ajanlar için sessiz kurulum:

```bash
npx evolink-seed-audio -y
```

Belirli bir skills dizinine kurulum:

```bash
npx evolink-seed-audio -y --path ~/.codex/skills
```

### Manuel kurulum

```bash
git clone https://github.com/cheercheung/seed-audio-1-0-skill.git
cd seed-audio-1-0-skill
node bin/cli.js -y --path ~/.codex/skills
```

### Agent otomatik kurulumu

Codex:

```text
Seed Audio skillini şu komutla kurun:
npx evolink-seed-audio@latest -y --path ~/.codex/skills

Ardından EVOLINK_API_KEY ayarlayın ve şunu okuyun:
~/.codex/skills/seed-audio-1-0/SKILL.md
```

Claude Code:

```text
Seed Audio skillini şu komutla kurun:
npx evolink-seed-audio@latest -y --path ~/.claude/skills

Ardından EVOLINK_API_KEY ayarlayın ve şunu okuyun:
~/.claude/skills/seed-audio-1-0/SKILL.md
```

Hermes Agent:

```text
Seed Audio skillini şu komutla kurun:
npx evolink-seed-audio@latest -y --path ~/.hermes/skills

Ardından EVOLINK_API_KEY ayarlayın ve şunu okuyun:
~/.hermes/skills/seed-audio-1-0/SKILL.md
```

Tek satır:

```bash
EVOLINK_API_KEY=your_key_here npx evolink-seed-audio@latest -y --path ~/.codex/skills
```

---

<a id="getting-an-api-key"></a>

## API anahtarı alma

1. [EvoLink API Keys](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=api-key) sayfasını açın.
2. Bir API anahtarı oluşturun veya kopyalayın.
3. Shell içinde dışa aktarın:

```bash
export EVOLINK_API_KEY="your_key_here"
```

4. Bir üretim görevi başlatın:

```bash
scripts/seed-audio-generate.sh \
  --prompt "Create a short welcome narration with a warm studio voice." \
  --format mp3
```

<a id="troubleshooting"></a>

## Sorun giderme

| Sorun | Olası neden | Eylem |
|---|---|---|
| `EVOLINK_API_KEY is not set` | API anahtarı eksik | `EVOLINK_API_KEY` değerini export edip tekrar deneyin. |
| `create request failed` | Geçersiz anahtar, istek gövdesi veya ağ hatası | `--dry-run` ile çalıştırın, sonra `docs/errors.md` dosyasını kontrol edin. |
| `POLL_TIMEOUT` | Yerel sorgulama bitmeden görev tamamlanmadı | Daha sonra `GET /v1/tasks/{task_id}` ile sorgulayın. Otomatik yeniden göndermeyin. |
| Ses URL’si bulunamadı | Yanıt biçimi değişmiş olabilir veya görevde henüz oluşturulmuş çıktı yoktur | Tam görev JSON’unu kaydedin ve `docs/response-schema.md` ile karşılaştırın. |

---

<a id="compatibility"></a>

## Uyumluluk

| Ajan veya runtime | Kurulum yöntemi | Durum |
|---|---|---|
| Codex | `npx evolink-seed-audio -y --path ~/.codex/skills` | Desteklenir |
| Claude Code | `npx evolink-seed-audio -y --path ~/.claude/skills` | Desteklenir |
| Hermes Agent | `npx evolink-seed-audio -y --path ~/.hermes/skills` | Yol belirterek kurulum desteklenir |
| Node.js | `>=16` | `package.json` tarafından gereklidir |
| Shell | bash + curl + python3 | `scripts/seed-audio-generate.sh` tarafından gereklidir |

---

<a id="license"></a>

## Lisans

MIT. Bkz. [LICENSE](LICENSE).

<p align="center">
  Powered by <a href="https://evolink.ai?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=footer">EvoLink</a>
</p>
