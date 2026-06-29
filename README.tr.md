# Seed Audio 1.0 Skill

<p align="center">
  <strong>EvoLink üzerinden Seed Audio 1.0 ile konuşma, diyalog, ambiyans, ses efektleri ve karma ses sahneleri oluşturun.</strong>
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
  <a href="#-menu">Menü</a> -
  <a href="#installation">Kurulum</a> -
  <a href="#seed-audio-10-api-quick-start">API Hızlı Başlangıç</a> -
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
- [Seed Audio 1.0 API Hızlı Başlangıç](#seed-audio-10-api-quick-start)
- [Dosya yapısı](#file-structure)
- [Sorun giderme](#troubleshooting)
- [Uyumluluk](#compatibility)
- [Lisans](#license)
- [Topluluk](#community)
- [Yıldız geçmişi](#star-history)

<a id="what-is-this"></a>

## Bu nedir?

| Alan | Değer |
|---|---|
| Skill | Seed Audio 1.0 Skill |
| Model | Seed Audio 1.0 (`doubao-seed-audio-1-0`) |
| Bakımı yapılan yüzey | `api-skill` |
| Kullanıcı girişleri | API hızlı başlangıcı ve ajan skill kurulumu |

Şunları yapmak istediğinizde bu depoyu kullanın:

- tam bir asenkron oluşturma ve sorgulama akışıyla EvoLink Seed-Audio API’sini çağırmak
- `npx evolink-seed-audio` ile bir ajan skill’i kurmak
- anlatım, çok karakterli diyalog, ambiyans, ses efektleri ve karma ses sahneleri üretmek
- istek parametrelerini, yanıt biçimlerini, callback’leri, hataları ve ses referanslarını incelemek

---

<a id="installation"></a>

## Kurulum

### Hızlı kurulum (OpenClaw)

```bash
openclaw skills add https://github.com/cheercheung/seed-audio-1-0-skill
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
npx evolink-seed-audio -y --path ~/.claude/skills
```

### Manuel kurulum

```bash
git clone https://github.com/cheercheung/seed-audio-1-0-skill.git
cd seed-audio-1-0-skill
openclaw skills add .
```

### Ajan otomatik kurulumu

Claude Code:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.claude/skills

Sonra EVOLINK_API_KEY değerini ayarlayın ve şunu okuyun:
~/.claude/skills/seed-audio-1-0/SKILL.md
```

OpenCode:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.opencode/skills

Sonra EVOLINK_API_KEY değerini ayarlayın ve şunu okuyun:
~/.opencode/skills/seed-audio-1-0/SKILL.md
```

OpenClaw:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.openclaw/skills

Sonra EVOLINK_API_KEY değerini ayarlayın ve şunu okuyun:
~/.openclaw/skills/seed-audio-1-0/SKILL.md
```

Tek satır komut:

```bash
EVOLINK_API_KEY=your_key_here npx evolink-seed-audio@latest -y --path ~/.claude/skills
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

---

<a id="seed-audio-10-api-quick-start"></a>

## Seed Audio 1.0 API Hızlı Başlangıç

### Hızlı API isteği

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

API asenkrondur. Oluşturma isteği bir görev `id` değeri döndürür; görev `completed`, `failed` veya `cancelled` olana kadar sorgulayın:

```bash
curl --request GET \
  --url "https://api.evolink.ai/v1/tasks/{task_id}" \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}"
```

### Tam ilk çalıştırma akışı

```bash
node examples/javascript/complete-flow.mjs
```

Ya da paketle gelen script’i kullanın:

```bash
scripts/seed-audio-generate.sh \
  --prompt "Create a cinematic 15-second rainforest ambience with distant birds, light rain, and a calm documentary narrator." \
  --format mp3
```

### Üretim modları

| Mod | Nasıl kullanılır |
|---|---|
| Metinden sese | Yalnızca `prompt` gönderin. |
| Ses referansı | En fazla 3 `audio_references` gönderin; prompt içinde `@audio1`, `@audio2` ve `@audio3` olarak referans verin. |
| Referans görsel | Bir `image_urls` öğesi gönderin. `image_urls` ile `audio_references` değerlerini birlikte kullanmayın. |
| Callback | Terminal görev durumlarını almak için `callback_url` gönderin. |

### Script referansı

```bash
scripts/seed-audio-generate.sh --help
npx evolink-seed-audio@latest --llms
npx evolink-seed-audio@latest --skill
```

### API parametreleri

| Parametre | Gerekli | Notlar |
|---|---:|---|
| `model` | evet | `doubao-seed-audio-1-0` kullanın |
| `prompt` | evet | En fazla 1500 karakter |
| `audio_references` | no | En fazla 3 hazır ses veya referans ses URL’si |
| `image_urls` | no | Bir referans görsel URL’si |
| `format` | no | `wav`, `mp3`, `pcm`, `ogg_opus`; varsayılan `wav` |
| `sample_rate` | no | `8000`, `16000`, `24000`, `32000`, `44100`, `48000` |
| `speech_rate` | no | `0.5` ile `2.0` arası |
| `loudness_rate` | no | `0.5` ile `2.0` arası |
| `pitch_rate` | no | `-12` ile `12` yarım ton arası |
| `callback_url` | no | Terminal görev durumları için HTTPS callback URL’si |

Bkz. [docs/api-reference.md](docs/api-reference.md), [docs/task-lifecycle.md](docs/task-lifecycle.md), [docs/response-schema.md](docs/response-schema.md), [docs/errors.md](docs/errors.md), [docs/callbacks.md](docs/callbacks.md), [docs/voices.md](docs/voices.md) ve [references/api-params.md](references/api-params.md).

---

<a id="file-structure"></a>

## Dosya yapısı

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
| Claude Code | `npx evolink-seed-audio -y --path ~/.claude/skills` | Desteklenir |
| OpenCode | `npx evolink-seed-audio -y --path ~/.opencode/skills` | Yol belirterek kurulum desteklenir |
| OpenClaw | `openclaw skills add` veya `npx ... --path ~/.openclaw/skills` | Desteklenir |
| Cursor | `npx ... --path ~/.cursor/skills` veya proje `.cursor/skills` | Desteklenir |
| Node.js | `>=16` | `package.json` tarafından gereklidir |
| Shell | bash + curl + python3 | `scripts/seed-audio-generate.sh` tarafından gereklidir |

---

<a id="license"></a>

## Lisans

MIT. Bkz. [LICENSE](LICENSE).

---

<a id="community"></a>

## Topluluk

- [Seed-Audio’yu EvoLink’te dene](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community)
- [EvoLink API anahtarı oluştur](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-api-key)
- [Resmi API belgelerini oku](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-docs)
- [Resmi ses listesini oku](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0-voices?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-voices)

---

<a id="star-history"></a>

## Yıldız geçmişi

```text
Depo herkese açık olduğunda yıldız geçmişi kullanılabilir.
```

<p align="center">
  Powered by <a href="https://evolink.ai?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=footer">EvoLink</a>
</p>
