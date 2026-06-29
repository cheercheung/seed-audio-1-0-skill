# Seed Audio 1.0 Skill

<p align="center">
  <strong>Générez de la parole, des dialogues, des ambiances, des effets sonores et des scènes audio mixtes avec Seed Audio 1.0 via EvoLink.</strong>
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
  <a href="#-menu">Menu</a> -
  <a href="#installation">Installer</a> -
  <a href="#seed-audio-10-api-quick-start">Démarrage rapide API</a> -
  <a href="#getting-an-api-key">Clé API</a> -
  <a href="https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=readme-top">Essayer sur EvoLink</a>
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

> **Agent IA ?** Ignorez le README et ouvrez directement [**llms-install.md**](llms-install.md), le guide d’installation pas à pas conçu pour les agents.

---

## 📑 Menu

- [Qu’est-ce que c’est ?](#what-is-this)
- [Installation](#installation)
- [Obtenir une clé API](#getting-an-api-key)
- [Démarrage rapide de l’API Seed Audio 1.0](#seed-audio-10-api-quick-start)
- [Structure des fichiers](#file-structure)
- [Dépannage](#troubleshooting)
- [Compatibilité](#compatibility)
- [Licence](#license)
- [Communauté](#community)
- [Historique des étoiles](#star-history)

<a id="what-is-this"></a>

## Qu’est-ce que c’est ?

| Champ | Valeur |
|---|---|
| Skill | Seed Audio 1.0 Skill |
| Modèle | Seed Audio 1.0 (`doubao-seed-audio-1-0`) |
| Surface maintenue | `api-skill` |
| Entrées utilisateur | démarrage rapide API et installation du skill agent |

Utilisez ce dépôt lorsque vous voulez :

- appeler l’API EvoLink Seed-Audio avec un flux asynchrone complet de création et de polling
- installer un skill agent avec `npx evolink-seed-audio`
- générer de la narration, des dialogues multi-personnages, des ambiances, des effets sonores et des scènes audio mixtes
- inspecter les paramètres de requête, les formats de réponse, les callbacks, les erreurs et les références vocales

---

<a id="installation"></a>

## Installation

### Installation rapide (OpenClaw)

```bash
openclaw skills add https://github.com/cheercheung/seed-audio-1-0-skill
```

### Installation via npm (recommandé)

```bash
npx evolink-seed-audio
```

Installation silencieuse pour agents :

```bash
npx evolink-seed-audio -y
```

Installer dans un répertoire de skills précis :

```bash
npx evolink-seed-audio -y --path ~/.claude/skills
```

### Installation manuelle

```bash
git clone https://github.com/cheercheung/seed-audio-1-0-skill.git
cd seed-audio-1-0-skill
openclaw skills add .
```

### Installation automatique pour agents

Claude Code:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.claude/skills

Ensuite, configurez EVOLINK_API_KEY et lisez :
~/.claude/skills/seed-audio-1-0/SKILL.md
```

OpenCode:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.opencode/skills

Ensuite, configurez EVOLINK_API_KEY et lisez :
~/.opencode/skills/seed-audio-1-0/SKILL.md
```

OpenClaw:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.openclaw/skills

Ensuite, configurez EVOLINK_API_KEY et lisez :
~/.openclaw/skills/seed-audio-1-0/SKILL.md
```

Commande en une ligne:

```bash
EVOLINK_API_KEY=your_key_here npx evolink-seed-audio@latest -y --path ~/.claude/skills
```

---

<a id="getting-an-api-key"></a>

## Obtenir une clé API

1. Ouvrez [EvoLink API Keys](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=api-key).
2. Créez ou copiez une clé API.
3. Exportez-la dans votre shell :

```bash
export EVOLINK_API_KEY="your_key_here"
```

4. Démarrez une tâche de génération :

```bash
scripts/seed-audio-generate.sh \
  --prompt "Create a short welcome narration with a warm studio voice." \
  --format mp3
```

---

<a id="seed-audio-10-api-quick-start"></a>

## Démarrage rapide de l’API Seed Audio 1.0

### Requête API rapide

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

L’API est asynchrone. La requête de création renvoie un `id` de tâche ; interrogez-la jusqu’à ce que la tâche soit `completed`, `failed` ou `cancelled` :

```bash
curl --request GET \
  --url "https://api.evolink.ai/v1/tasks/{task_id}" \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}"
```

### Flux complet de première exécution

```bash
node examples/javascript/complete-flow.mjs
```

Ou utilisez le script inclus :

```bash
scripts/seed-audio-generate.sh \
  --prompt "Create a cinematic 15-second rainforest ambience with distant birds, light rain, and a calm documentary narrator." \
  --format mp3
```

### Modes de génération

| Mode | Utilisation |
|---|---|
| Texte vers audio | Passez uniquement `prompt`. |
| Référence vocale | Passez jusqu’à 3 `audio_references` ; référencez-les dans le prompt avec `@audio1`, `@audio2` et `@audio3`. |
| Image de référence | Passez un élément `image_urls`. Ne combinez pas `image_urls` avec `audio_references`. |
| Callback | Passez `callback_url` pour recevoir les états terminaux de la tâche. |

### Référence du script

```bash
scripts/seed-audio-generate.sh --help
npx evolink-seed-audio@latest --llms
npx evolink-seed-audio@latest --skill
```

### Paramètres API

| Paramètre | Requis | Notes |
|---|---:|---|
| `model` | oui | Utilisez `doubao-seed-audio-1-0` |
| `prompt` | oui | Jusqu’à 1500 caractères |
| `audio_references` | no | Jusqu’à 3 voix prédéfinies ou URL audio de référence |
| `image_urls` | no | Une URL d’image de référence |
| `format` | no | `wav`, `mp3`, `pcm`, `ogg_opus` ; défaut `wav` |
| `sample_rate` | no | `8000`, `16000`, `24000`, `32000`, `44100`, `48000` |
| `speech_rate` | no | `0.5` à `2.0` |
| `loudness_rate` | no | `0.5` à `2.0` |
| `pitch_rate` | no | `-12` à `12` demi-tons |
| `callback_url` | no | URL HTTPS de callback pour les états terminaux de la tâche |

Consultez [docs/api-reference.md](docs/api-reference.md), [docs/task-lifecycle.md](docs/task-lifecycle.md), [docs/response-schema.md](docs/response-schema.md), [docs/errors.md](docs/errors.md), [docs/callbacks.md](docs/callbacks.md), [docs/voices.md](docs/voices.md) et [references/api-params.md](references/api-params.md).

---

<a id="file-structure"></a>

## Structure des fichiers

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

## Dépannage

| Problème | Cause probable | Action |
|---|---|---|
| `EVOLINK_API_KEY is not set` | Clé API manquante | Exportez `EVOLINK_API_KEY` puis réessayez. |
| `create request failed` | Clé invalide, corps de requête incorrect ou échec réseau | Exécutez avec `--dry-run`, puis consultez `docs/errors.md`. |
| `POLL_TIMEOUT` | La tâche ne s’est pas terminée avant la fin du polling local | Interrogez `GET /v1/tasks/{task_id}` plus tard. Ne renvoyez pas automatiquement la requête. |
| Aucune URL audio trouvée | La forme de la réponse a changé ou la tâche n’a pas encore d’asset généré | Enregistrez le JSON complet de la tâche et comparez-le à `docs/response-schema.md`. |

---

<a id="compatibility"></a>

## Compatibilité

| Agent ou runtime | Méthode d’installation | Statut |
|---|---|---|
| Claude Code | `npx evolink-seed-audio -y --path ~/.claude/skills` | Pris en charge |
| OpenCode | `npx evolink-seed-audio -y --path ~/.opencode/skills` | Pris en charge par installation avec chemin |
| OpenClaw | `openclaw skills add` ou `npx ... --path ~/.openclaw/skills` | Pris en charge |
| Cursor | `npx ... --path ~/.cursor/skills` ou `.cursor/skills` du projet | Pris en charge |
| Node.js | `>=16` | Requis par `package.json` |
| Shell | bash + curl + python3 | Requis par `scripts/seed-audio-generate.sh` |

---

<a id="license"></a>

## Licence

MIT. Voir [LICENSE](LICENSE).

---

<a id="community"></a>

## Communauté

- [Essayer Seed-Audio sur EvoLink](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community)
- [Créer une clé API EvoLink](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-api-key)
- [Lire la documentation API officielle](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-docs)
- [Lire la liste officielle des voix](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0-voices?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-voices)

---

<a id="star-history"></a>

## Historique des étoiles

```text
L’historique des étoiles sera disponible après la publication du dépôt.
```

<p align="center">
  Powered by <a href="https://evolink.ai?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=footer">EvoLink</a>
</p>
