# Seed Audio 1.0 Skill

<p align="center">
  <strong>Erzeuge Sprache, Dialoge, Atmosphären, Soundeffekte und gemischte Audioszenen mit Seed Audio 1.0 über EvoLink.</strong>
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
  <a href="#installation">Installieren</a> -
  <a href="#seed-audio-10-api-quick-start">API-Schnellstart</a> -
  <a href="#getting-an-api-key">API-Schlüssel</a> -
  <a href="https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=readme-top">Auf EvoLink testen</a>
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

> **KI-Agent?** Überspringe das README und gehe direkt zu [**llms-install.md**](llms-install.md), den Schritt-für-Schritt-Installationsanweisungen für Agents.

---

## 📑 Menü

- [Was ist das?](#what-is-this)
- [Installation](#installation)
- [API-Schlüssel erhalten](#getting-an-api-key)
- [Seed Audio 1.0 API-Schnellstart](#seed-audio-10-api-quick-start)
- [Dateistruktur](#file-structure)
- [Fehlerbehebung](#troubleshooting)
- [Kompatibilität](#compatibility)
- [Lizenz](#license)
- [Community](#community)
- [Star-Verlauf](#star-history)

<a id="what-is-this"></a>

## Was ist das?

| Feld | Wert |
|---|---|
| Skill | Seed Audio 1.0 Skill |
| Modell | Seed Audio 1.0 (`doubao-seed-audio-1-0`) |
| Gepflegte Oberfläche | `api-skill` |
| Einstiege für Nutzer | API-Schnellstart und Agent-Skill-Installation |

Verwende dieses Repository, wenn du Folgendes tun möchtest:

- die EvoLink Seed-Audio API mit einem vollständigen asynchronen Create-and-Poll-Flow aufrufen
- einen Agent-Skill mit `npx evolink-seed-audio` installieren
- Erzählstimmen, Mehrpersonen-Dialoge, Atmosphären, Soundeffekte und gemischte Audioszenen erzeugen
- Request-Parameter, Antwortformate, Callbacks, Fehler und Stimmreferenzen prüfen

---

<a id="installation"></a>

## Installation

### Schnellinstallation (OpenClaw)

```bash
openclaw skills add https://github.com/cheercheung/seed-audio-1-0-skill
```

### Installation über npm (empfohlen)

```bash
npx evolink-seed-audio
```

Stille Installation für Agents:

```bash
npx evolink-seed-audio -y
```

In ein bestimmtes Skills-Verzeichnis installieren:

```bash
npx evolink-seed-audio -y --path ~/.claude/skills
```

### Manuelle Installation

```bash
git clone https://github.com/cheercheung/seed-audio-1-0-skill.git
cd seed-audio-1-0-skill
openclaw skills add .
```

### Automatische Agent-Installation

Claude Code:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.claude/skills

Setze anschließend EVOLINK_API_KEY und lies:
~/.claude/skills/seed-audio-1-0/SKILL.md
```

OpenCode:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.opencode/skills

Setze anschließend EVOLINK_API_KEY und lies:
~/.opencode/skills/seed-audio-1-0/SKILL.md
```

OpenClaw:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.openclaw/skills

Setze anschließend EVOLINK_API_KEY und lies:
~/.openclaw/skills/seed-audio-1-0/SKILL.md
```

Einzeiler:

```bash
EVOLINK_API_KEY=your_key_here npx evolink-seed-audio@latest -y --path ~/.claude/skills
```

---

<a id="getting-an-api-key"></a>

## API-Schlüssel erhalten

1. Öffne [EvoLink API Keys](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=api-key).
2. Erstelle oder kopiere einen API-Schlüssel.
3. Exportiere ihn in deiner Shell:

```bash
export EVOLINK_API_KEY="your_key_here"
```

4. Starte eine Generierungsaufgabe:

```bash
scripts/seed-audio-generate.sh \
  --prompt "Create a short welcome narration with a warm studio voice." \
  --format mp3
```

---

<a id="seed-audio-10-api-quick-start"></a>

## Seed Audio 1.0 API-Schnellstart

### Schneller API-Request

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

Die API ist asynchron. Der Create-Request gibt eine Task-`id` zurück; frage den Status ab, bis die Task `completed`, `failed` oder `cancelled` ist:

```bash
curl --request GET \
  --url "https://api.evolink.ai/v1/tasks/{task_id}" \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}"
```

### Vollständiger Erstdurchlauf

```bash
node examples/javascript/complete-flow.mjs
```

Oder verwende das mitgelieferte Skript:

```bash
scripts/seed-audio-generate.sh \
  --prompt "Create a cinematic 15-second rainforest ambience with distant birds, light rain, and a calm documentary narrator." \
  --format mp3
```

### Generierungsmodi

| Modus | Verwendung |
|---|---|
| Text zu Audio | Übergebe nur `prompt`. |
| Stimmreferenz | Übergebe bis zu 3 `audio_references`; referenziere sie im Prompt als `@audio1`, `@audio2` und `@audio3`. |
| Referenzbild | Übergebe ein Element in `image_urls`. Kombiniere `image_urls` nicht mit `audio_references`. |
| Callback | Übergebe `callback_url`, um terminale Task-Status zu erhalten. |

### Skriptreferenz

```bash
scripts/seed-audio-generate.sh --help
npx evolink-seed-audio@latest --llms
npx evolink-seed-audio@latest --skill
```

### API-Parameter

| Parameter | Erforderlich | Hinweise |
|---|---:|---|
| `model` | ja | `doubao-seed-audio-1-0` verwenden |
| `prompt` | ja | Bis zu 1500 Zeichen |
| `audio_references` | no | Bis zu 3 Preset-Stimmen oder Referenz-Audio-URLs |
| `image_urls` | no | Eine Referenzbild-URL |
| `format` | no | `wav`, `mp3`, `pcm`, `ogg_opus`; Standard `wav` |
| `sample_rate` | no | `8000`, `16000`, `24000`, `32000`, `44100`, `48000` |
| `speech_rate` | no | `0.5` bis `2.0` |
| `loudness_rate` | no | `0.5` bis `2.0` |
| `pitch_rate` | no | `-12` bis `12` Halbtöne |
| `callback_url` | no | HTTPS-Callback-URL für terminale Task-Status |

Siehe [docs/api-reference.md](docs/api-reference.md), [docs/task-lifecycle.md](docs/task-lifecycle.md), [docs/response-schema.md](docs/response-schema.md), [docs/errors.md](docs/errors.md), [docs/callbacks.md](docs/callbacks.md), [docs/voices.md](docs/voices.md) und [references/api-params.md](references/api-params.md).

---

<a id="file-structure"></a>

## Dateistruktur

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

## Fehlerbehebung

| Problem | Wahrscheinliche Ursache | Maßnahme |
|---|---|---|
| `EVOLINK_API_KEY is not set` | API-Schlüssel fehlt | Exportiere `EVOLINK_API_KEY` und versuche es erneut. |
| `create request failed` | Ungültiger Schlüssel, falscher Request Body oder Netzwerkfehler | Führe den Befehl mit `--dry-run` aus und prüfe `docs/errors.md`. |
| `POLL_TIMEOUT` | Die Task wurde vor Ende des lokalen Pollings nicht fertig | Frage später `GET /v1/tasks/{task_id}` ab. Nicht automatisch erneut senden. |
| Keine Audio-URL gefunden | Antwortformat hat sich geändert oder die Task hat noch kein erzeugtes Asset | Speichere das vollständige Task-JSON und vergleiche es mit `docs/response-schema.md`. |

---

<a id="compatibility"></a>

## Kompatibilität

| Agent oder Runtime | Installationsmethode | Status |
|---|---|---|
| Claude Code | `npx evolink-seed-audio -y --path ~/.claude/skills` | Unterstützt |
| OpenCode | `npx evolink-seed-audio -y --path ~/.opencode/skills` | Unterstützt per Pfadinstallation |
| OpenClaw | `openclaw skills add` oder `npx ... --path ~/.openclaw/skills` | Unterstützt |
| Cursor | `npx ... --path ~/.cursor/skills` oder Projekt `.cursor/skills` | Unterstützt |
| Node.js | `>=16` | Von `package.json` gefordert |
| Shell | bash + curl + python3 | Von `scripts/seed-audio-generate.sh` gefordert |

---

<a id="license"></a>

## Lizenz

MIT. Siehe [LICENSE](LICENSE).

---

<a id="community"></a>

## Community

- [Seed-Audio auf EvoLink testen](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community)
- [Einen EvoLink API-Schlüssel erstellen](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-api-key)
- [Offizielle API-Dokumentation lesen](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-docs)
- [Offizielle Stimmenliste lesen](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0-voices?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-voices)

---

<a id="star-history"></a>

## Star-Verlauf

```text
Der Star-Verlauf ist verfügbar, sobald das Repository öffentlich ist.
```

<p align="center">
  Powered by <a href="https://evolink.ai?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=footer">EvoLink</a>
</p>
