# Seed Audio 1.0 Skill

<p align="center">
  <strong>Gere fala, diálogos, ambiências, efeitos sonoros e cenas de áudio mistas com o Seed Audio 1.0 pela EvoLink.</strong>
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
  <a href="#installation">Instalar</a> -
  <a href="#getting-an-api-key">Chave API</a> -
  <a href="https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=readme-top">Testar na EvoLink</a>
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

> **Agente de IA?** Pule o README e vá direto para [**llms-install.md**](llms-install.md), com instruções de instalação passo a passo feitas para você.

---

## 📑 Menu

- [O que é isto?](#what-is-this)
- [Instalação](#installation)
- [Obtendo uma chave API](#getting-an-api-key)
- [Solução de problemas](#troubleshooting)
- [Compatibilidade](#compatibility)
- [Licença](#license)

<a id="what-is-this"></a>

## O que é isto?

| Campo | Valor |
|---|---|
| Skill | Seed Audio 1.0 Skill |
| Modelo | Seed Audio 1.0 |
| Superfície mantida | `api-skill` |
| Entradas do usuário | instalação do skill para agentes e configuração da chave API |

Use este repositório quando quiser:

- chamar a API Seed-Audio da EvoLink com um fluxo assíncrono completo de criação e consulta
- instalar um skill de agente com `npx evolink-seed-audio`
- gerar narração, diálogo com vários personagens, ambiências, efeitos sonoros e cenas de áudio mistas
- inspecionar parâmetros de solicitação, formatos de resposta, callbacks, erros e referências de voz

---

<a id="installation"></a>

## Instalação

### Instalação rápida (Codex)

```bash
npx evolink-seed-audio -y --path ~/.codex/skills
```

### Instalar via npm (recomendado)

```bash
npx evolink-seed-audio
```

Instalação silenciosa para agentes:

```bash
npx evolink-seed-audio -y
```

Instalar em um diretório de skills específico:

```bash
npx evolink-seed-audio -y --path ~/.codex/skills
```

### Instalação manual

```bash
git clone https://github.com/cheercheung/seed-audio-1-0-skill.git
cd seed-audio-1-0-skill
node bin/cli.js -y --path ~/.codex/skills
```

### Instalação automática para agentes

Codex:

```text
Instale o skill Seed Audio executando:
npx evolink-seed-audio@latest -y --path ~/.codex/skills

Depois configure EVOLINK_API_KEY e leia:
~/.codex/skills/seed-audio-1-0/SKILL.md
```

Claude Code:

```text
Instale o skill Seed Audio executando:
npx evolink-seed-audio@latest -y --path ~/.claude/skills

Depois configure EVOLINK_API_KEY e leia:
~/.claude/skills/seed-audio-1-0/SKILL.md
```

Hermes Agent:

```text
Instale o skill Seed Audio executando:
npx evolink-seed-audio@latest -y --path ~/.hermes/skills

Depois configure EVOLINK_API_KEY e leia:
~/.hermes/skills/seed-audio-1-0/SKILL.md
```

Uma linha:

```bash
EVOLINK_API_KEY=your_key_here npx evolink-seed-audio@latest -y --path ~/.codex/skills
```

---

<a id="getting-an-api-key"></a>

## Obtendo uma chave API

1. Abra [EvoLink API Keys](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=api-key).
2. Crie ou copie uma chave API.
3. Exporte-a no seu shell:

```bash
export EVOLINK_API_KEY="your_key_here"
```

4. Inicie uma tarefa de geração:

```bash
scripts/seed-audio-generate.sh \
  --prompt "Create a short welcome narration with a warm studio voice." \
  --format mp3
```

<a id="troubleshooting"></a>

## Solução de problemas

| Problema | Causa provável | Ação |
|---|---|---|
| `EVOLINK_API_KEY is not set` | Chave API ausente | Exporte `EVOLINK_API_KEY` e tente novamente. |
| `create request failed` | Chave inválida, corpo da solicitação incorreto ou falha de rede | Execute com `--dry-run` e verifique `docs/errors.md`. |
| `POLL_TIMEOUT` | A tarefa não terminou antes do fim da consulta local | Consulte `GET /v1/tasks/{task_id}` depois. Não reenvie automaticamente. |
| Nenhuma URL de áudio encontrada | O formato da resposta mudou ou a tarefa ainda não tem recurso gerado | Salve o JSON completo da tarefa e compare com `docs/response-schema.md`. |

---

<a id="compatibility"></a>

## Compatibilidade

| Agente ou runtime | Método de instalação | Status |
|---|---|---|
| Codex | `npx evolink-seed-audio -y --path ~/.codex/skills` | Compatível |
| Claude Code | `npx evolink-seed-audio -y --path ~/.claude/skills` | Compatível |
| Hermes Agent | `npx evolink-seed-audio -y --path ~/.hermes/skills` | Compatível por instalação com caminho |
| Node.js | `>=16` | Exigido por `package.json` |
| Shell | bash + curl + python3 | Exigido por `scripts/seed-audio-generate.sh` |

---

<a id="license"></a>

## Licença

MIT. Veja [LICENSE](LICENSE).

<p align="center">
  Powered by <a href="https://evolink.ai?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=footer">EvoLink</a>
</p>
