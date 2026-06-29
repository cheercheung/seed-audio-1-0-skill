# Seed Audio 1.0 Skill

<p align="center">
  <strong>Gere fala, diálogos, ambiências, efeitos sonoros e cenas de áudio mistas com o Seed Audio 1.0 pela EvoLink.</strong>
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
  <a href="#installation">Instalar</a> -
  <a href="#seed-audio-10-api-quick-start">Início rápido da API</a> -
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
- [Início rápido da API Seed Audio 1.0](#seed-audio-10-api-quick-start)
- [Estrutura de arquivos](#file-structure)
- [Solução de problemas](#troubleshooting)
- [Compatibilidade](#compatibility)
- [Licença](#license)
- [Comunidade](#community)
- [Histórico de estrelas](#star-history)

<a id="what-is-this"></a>

## O que é isto?

| Campo | Valor |
|---|---|
| Skill | Seed Audio 1.0 Skill |
| Modelo | Seed Audio 1.0 (`doubao-seed-audio-1-0`) |
| Superfície mantida | `api-skill` |
| Entradas do usuário | início rápido da API e instalação do skill para agentes |

Use este repositório quando quiser:

- chamar a API Seed-Audio da EvoLink com um fluxo assíncrono completo de criação e consulta
- instalar um skill de agente com `npx evolink-seed-audio`
- gerar narração, diálogo com vários personagens, ambiências, efeitos sonoros e cenas de áudio mistas
- inspecionar parâmetros de solicitação, formatos de resposta, callbacks, erros e referências de voz

---

<a id="installation"></a>

## Instalação

### Instalação rápida (OpenClaw)

```bash
openclaw skills add https://github.com/cheercheung/seed-audio-1-0-skill
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
npx evolink-seed-audio -y --path ~/.claude/skills
```

### Instalação manual

```bash
git clone https://github.com/cheercheung/seed-audio-1-0-skill.git
cd seed-audio-1-0-skill
openclaw skills add .
```

### Instalação automática para agentes

Claude Code:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.claude/skills

Depois defina EVOLINK_API_KEY e leia:
~/.claude/skills/seed-audio-1-0/SKILL.md
```

OpenCode:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.opencode/skills

Depois defina EVOLINK_API_KEY e leia:
~/.opencode/skills/seed-audio-1-0/SKILL.md
```

OpenClaw:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.openclaw/skills

Depois defina EVOLINK_API_KEY e leia:
~/.openclaw/skills/seed-audio-1-0/SKILL.md
```

Comando de uma linha:

```bash
EVOLINK_API_KEY=your_key_here npx evolink-seed-audio@latest -y --path ~/.claude/skills
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

---

<a id="seed-audio-10-api-quick-start"></a>

## Início rápido da API Seed Audio 1.0

### Solicitação rápida da API

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

A API é assíncrona. A solicitação de criação retorna um `id` de tarefa; consulte até que a tarefa esteja `completed`, `failed` ou `cancelled`:

```bash
curl --request GET \
  --url "https://api.evolink.ai/v1/tasks/{task_id}" \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}"
```

### Fluxo completo da primeira execução

```bash
node examples/javascript/complete-flow.mjs
```

Ou use o script incluído:

```bash
scripts/seed-audio-generate.sh \
  --prompt "Create a cinematic 15-second rainforest ambience with distant birds, light rain, and a calm documentary narrator." \
  --format mp3
```

### Modos de geração

| Modo | Como usar |
|---|---|
| Texto para áudio | Passe apenas `prompt`. |
| Referência de voz | Passe até 3 `audio_references`; use `@audio1`, `@audio2` e `@audio3` no prompt. |
| Imagem de referência | Passe um item `image_urls`. Não combine `image_urls` com `audio_references`. |
| Callback | Passe `callback_url` para receber estados terminais da tarefa. |

### Referência do script

```bash
scripts/seed-audio-generate.sh --help
npx evolink-seed-audio@latest --llms
npx evolink-seed-audio@latest --skill
```

### Parâmetros da API

| Parâmetro | Obrigatório | Notas |
|---|---:|---|
| `model` | sim | Use `doubao-seed-audio-1-0` |
| `prompt` | sim | Até 1500 caracteres |
| `audio_references` | no | Até 3 vozes predefinidas ou URLs de áudio de referência |
| `image_urls` | no | Uma URL de imagem de referência |
| `format` | no | `wav`, `mp3`, `pcm`, `ogg_opus`; padrão `wav` |
| `sample_rate` | no | `8000`, `16000`, `24000`, `32000`, `44100`, `48000` |
| `speech_rate` | no | `0.5` a `2.0` |
| `loudness_rate` | no | `0.5` a `2.0` |
| `pitch_rate` | no | `-12` a `12` semitons |
| `callback_url` | no | URL HTTPS de callback para estados terminais da tarefa |

Consulte [docs/api-reference.md](docs/api-reference.md), [docs/task-lifecycle.md](docs/task-lifecycle.md), [docs/response-schema.md](docs/response-schema.md), [docs/errors.md](docs/errors.md), [docs/callbacks.md](docs/callbacks.md), [docs/voices.md](docs/voices.md) e [references/api-params.md](references/api-params.md).

---

<a id="file-structure"></a>

## Estrutura de arquivos

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
| Claude Code | `npx evolink-seed-audio -y --path ~/.claude/skills` | Compatível |
| OpenCode | `npx evolink-seed-audio -y --path ~/.opencode/skills` | Compatível por instalação com caminho |
| OpenClaw | `openclaw skills add` ou `npx ... --path ~/.openclaw/skills` | Compatível |
| Cursor | `npx ... --path ~/.cursor/skills` ou `.cursor/skills` do projeto | Compatível |
| Node.js | `>=16` | Exigido por `package.json` |
| Shell | bash + curl + python3 | Exigido por `scripts/seed-audio-generate.sh` |

---

<a id="license"></a>

## Licença

MIT. Veja [LICENSE](LICENSE).

---

<a id="community"></a>

## Comunidade

- [Teste Seed-Audio na EvoLink](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community)
- [Crie uma chave API da EvoLink](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-api-key)
- [Leia a documentação oficial da API](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-docs)
- [Leia a lista oficial de vozes](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0-voices?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-voices)

---

<a id="star-history"></a>

## Histórico de estrelas

```text
O histórico de estrelas ficará disponível depois que o repositório estiver público.
```

<p align="center">
  Powered by <a href="https://evolink.ai?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=footer">EvoLink</a>
</p>
