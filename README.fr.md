# Seed Audio 1.0 Skill

<p align="center">
  <strong>Générez de la parole, des dialogues, des ambiances, des effets sonores et des scènes audio mixtes avec Seed Audio 1.0 via EvoLink.</strong>
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
  <a href="#-menu">Menu</a> -
  <a href="#installation">Installer</a> -
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
- [Dépannage](#troubleshooting)
- [Compatibilité](#compatibility)
- [Licence](#license)

<a id="what-is-this"></a>

## Qu’est-ce que c’est ?

| Champ | Valeur |
|---|---|
| Skill | Seed Audio 1.0 Skill |
| Modèle | Seed Audio 1.0 |
| Surface maintenue | `api-skill` |
| Entrées utilisateur | installation du skill agent et configuration de clé API |

Utilisez ce dépôt lorsque vous voulez :

- appeler l’API EvoLink Seed-Audio avec un flux asynchrone complet de création et de polling
- installer un skill agent avec `npx evolink-seed-audio`
- générer de la narration, des dialogues multi-personnages, des ambiances, des effets sonores et des scènes audio mixtes
- inspecter les paramètres de requête, les formats de réponse, les callbacks, les erreurs et les références vocales

---

<a id="installation"></a>

## Installation

### Installation rapide (Codex)

```bash
npx evolink-seed-audio -y --path ~/.codex/skills
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
npx evolink-seed-audio -y --path ~/.codex/skills
```

### Installation manuelle

```bash
git clone https://github.com/cheercheung/seed-audio-1-0-skill.git
cd seed-audio-1-0-skill
node bin/cli.js -y --path ~/.codex/skills
```

### Installation automatique pour agents

Codex:

```text
Installez le skill Seed Audio avec:
npx evolink-seed-audio@latest -y --path ~/.codex/skills

Ensuite, configurez EVOLINK_API_KEY et lisez:
~/.codex/skills/seed-audio-1-0/SKILL.md
```

Claude Code:

```text
Installez le skill Seed Audio avec:
npx evolink-seed-audio@latest -y --path ~/.claude/skills

Ensuite, configurez EVOLINK_API_KEY et lisez:
~/.claude/skills/seed-audio-1-0/SKILL.md
```

Hermes Agent:

```text
Installez le skill Seed Audio avec:
npx evolink-seed-audio@latest -y --path ~/.hermes/skills

Ensuite, configurez EVOLINK_API_KEY et lisez:
~/.hermes/skills/seed-audio-1-0/SKILL.md
```

Commande en une ligne:

```bash
EVOLINK_API_KEY=your_key_here npx evolink-seed-audio@latest -y --path ~/.codex/skills
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
| Codex | `npx evolink-seed-audio -y --path ~/.codex/skills` | Pris en charge |
| Claude Code | `npx evolink-seed-audio -y --path ~/.claude/skills` | Pris en charge |
| Hermes Agent | `npx evolink-seed-audio -y --path ~/.hermes/skills` | Pris en charge par installation avec chemin |
| Node.js | `>=16` | Requis par `package.json` |
| Shell | bash + curl + python3 | Requis par `scripts/seed-audio-generate.sh` |

---

<a id="license"></a>

## Licence

MIT. Voir [LICENSE](LICENSE).

<p align="center">
  Powered by <a href="https://evolink.ai?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=footer">EvoLink</a>
</p>
