# Seed Audio 1.0 Skill

<p align="center">
  <strong>Genera voz, diálogos, ambientes, efectos de sonido y escenas de audio mixtas con Seed Audio 1.0 a través de EvoLink.</strong>
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
  <a href="#-menu">Menú</a> -
  <a href="#installation">Instalar</a> -
  <a href="#seed-audio-10-api-quick-start">Inicio rápido de API</a> -
  <a href="#getting-an-api-key">Clave API</a> -
  <a href="https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=readme-top">Probar en EvoLink</a>
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

> **¿Agente de IA?** Salta el README y ve directamente a [**llms-install.md**](llms-install.md), con instrucciones de instalación paso a paso diseñadas para ti.

---

## 📑 Menú

- [¿Qué es esto?](#what-is-this)
- [Instalación](#installation)
- [Obtener una clave API](#getting-an-api-key)
- [Inicio rápido de la API de Seed Audio 1.0](#seed-audio-10-api-quick-start)
- [Estructura de archivos](#file-structure)
- [Solución de problemas](#troubleshooting)
- [Compatibilidad](#compatibility)
- [Licencia](#license)
- [Comunidad](#community)
- [Historial de estrellas](#star-history)

<a id="what-is-this"></a>

## ¿Qué es esto?

| Campo | Valor |
|---|---|
| Skill | Seed Audio 1.0 Skill |
| Modelo | Seed Audio 1.0 (`doubao-seed-audio-1-0`) |
| Superficie mantenida | `api-skill` |
| Entradas de usuario | inicio rápido de API e instalación del skill para agentes |

Usa este repositorio cuando quieras:

- llamar a la API Seed-Audio de EvoLink con un flujo asíncrono completo de creación y consulta
- instalar un skill de agente con `npx evolink-seed-audio`
- generar narración, diálogo de varios personajes, ambientes, efectos de sonido y escenas de audio mixtas
- revisar parámetros de solicitud, formatos de respuesta, callbacks, errores y referencias de voz

---

<a id="installation"></a>

## Instalación

### Instalación rápida (OpenClaw)

```bash
openclaw skills add https://github.com/cheercheung/seed-audio-1-0-skill
```

### Instalar con npm (recomendado)

```bash
npx evolink-seed-audio
```

Instalación silenciosa para agentes:

```bash
npx evolink-seed-audio -y
```

Instalar en un directorio de skills específico:

```bash
npx evolink-seed-audio -y --path ~/.claude/skills
```

### Instalación manual

```bash
git clone https://github.com/cheercheung/seed-audio-1-0-skill.git
cd seed-audio-1-0-skill
openclaw skills add .
```

### Instalación automática para agentes

Claude Code:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.claude/skills

Después configura EVOLINK_API_KEY y lee:
~/.claude/skills/seed-audio-1-0/SKILL.md
```

OpenCode:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.opencode/skills

Después configura EVOLINK_API_KEY y lee:
~/.opencode/skills/seed-audio-1-0/SKILL.md
```

OpenClaw:

```text
Install the Seed Audio skill by running:
npx evolink-seed-audio@latest -y --path ~/.openclaw/skills

Después configura EVOLINK_API_KEY y lee:
~/.openclaw/skills/seed-audio-1-0/SKILL.md
```

Comando de una línea:

```bash
EVOLINK_API_KEY=your_key_here npx evolink-seed-audio@latest -y --path ~/.claude/skills
```

---

<a id="getting-an-api-key"></a>

## Obtener una clave API

1. Abre [EvoLink API Keys](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=api-key).
2. Crea o copia una clave API.
3. Expórtala en tu shell:

```bash
export EVOLINK_API_KEY="your_key_here"
```

4. Inicia una tarea de generación:

```bash
scripts/seed-audio-generate.sh \
  --prompt "Create a short welcome narration with a warm studio voice." \
  --format mp3
```

---

<a id="seed-audio-10-api-quick-start"></a>

## Inicio rápido de la API de Seed Audio 1.0

### Solicitud rápida de API

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

La API es asíncrona. La solicitud de creación devuelve un `id` de tarea; consulta el estado hasta que la tarea esté `completed`, `failed` o `cancelled`:

```bash
curl --request GET \
  --url "https://api.evolink.ai/v1/tasks/{task_id}" \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}"
```

### Flujo completo del primer uso

```bash
node examples/javascript/complete-flow.mjs
```

O usa el script incluido:

```bash
scripts/seed-audio-generate.sh \
  --prompt "Create a cinematic 15-second rainforest ambience with distant birds, light rain, and a calm documentary narrator." \
  --format mp3
```

### Modos de generación

| Modo | Cómo usarlo |
|---|---|
| Texto a audio | Pasa solo `prompt`. |
| Referencia de voz | Pasa hasta 3 `audio_references`; menciónalas como `@audio1`, `@audio2` y `@audio3` en el prompt. |
| Imagen de referencia | Pasa un elemento `image_urls`. No combines `image_urls` con `audio_references`. |
| Callback | Pasa `callback_url` para recibir estados terminales de la tarea. |

### Referencia del script

```bash
scripts/seed-audio-generate.sh --help
npx evolink-seed-audio@latest --llms
npx evolink-seed-audio@latest --skill
```

### Parámetros de API

| Parámetro | Obligatorio | Notas |
|---|---:|---|
| `model` | sí | Usa `doubao-seed-audio-1-0` |
| `prompt` | sí | Hasta 1500 caracteres |
| `audio_references` | no | Hasta 3 voces predefinidas o URL de audio de referencia |
| `image_urls` | no | Una URL de imagen de referencia |
| `format` | no | `wav`, `mp3`, `pcm`, `ogg_opus`; predeterminado `wav` |
| `sample_rate` | no | `8000`, `16000`, `24000`, `32000`, `44100`, `48000` |
| `speech_rate` | no | `0.5` a `2.0` |
| `loudness_rate` | no | `0.5` a `2.0` |
| `pitch_rate` | no | `-12` a `12` semitonos |
| `callback_url` | no | URL HTTPS de callback para estados terminales de la tarea |

Consulta [docs/api-reference.md](docs/api-reference.md), [docs/task-lifecycle.md](docs/task-lifecycle.md), [docs/response-schema.md](docs/response-schema.md), [docs/errors.md](docs/errors.md), [docs/callbacks.md](docs/callbacks.md), [docs/voices.md](docs/voices.md) y [references/api-params.md](references/api-params.md).

---

<a id="file-structure"></a>

## Estructura de archivos

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

## Solución de problemas

| Problema | Causa probable | Acción |
|---|---|---|
| `EVOLINK_API_KEY is not set` | Falta la clave API | Exporta `EVOLINK_API_KEY` y vuelve a intentarlo. |
| `create request failed` | Clave no válida, cuerpo de solicitud incorrecto o fallo de red | Ejecuta con `--dry-run` y revisa `docs/errors.md`. |
| `POLL_TIMEOUT` | La tarea no terminó antes de que finalizara el sondeo local | Consulta `GET /v1/tasks/{task_id}` más tarde. No la vuelvas a enviar automáticamente. |
| No se encontró URL de audio | La forma de la respuesta cambió o la tarea aún no tiene recurso generado | Guarda el JSON completo de la tarea y compáralo con `docs/response-schema.md`. |

---

<a id="compatibility"></a>

## Compatibilidad

| Agente o runtime | Método de instalación | Estado |
|---|---|---|
| Claude Code | `npx evolink-seed-audio -y --path ~/.claude/skills` | Compatible |
| OpenCode | `npx evolink-seed-audio -y --path ~/.opencode/skills` | Compatible mediante instalación por ruta |
| OpenClaw | `openclaw skills add` o `npx ... --path ~/.openclaw/skills` | Compatible |
| Cursor | `npx ... --path ~/.cursor/skills` o `.cursor/skills` del proyecto | Compatible |
| Node.js | `>=16` | Requerido por `package.json` |
| Shell | bash + curl + python3 | Requerido por `scripts/seed-audio-generate.sh` |

---

<a id="license"></a>

## Licencia

MIT. Consulta [LICENSE](LICENSE).

---

<a id="community"></a>

## Comunidad

- [Prueba Seed-Audio en EvoLink](https://evolink.ai/seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community)
- [Crea una clave API de EvoLink](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-api-key)
- [Lee la documentación oficial de la API](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-docs)
- [Lee la lista oficial de voces](https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0-voices?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=community-voices)

---

<a id="star-history"></a>

## Historial de estrellas

```text
El historial de estrellas estará disponible después de que el repositorio sea público.
```

<p align="center">
  Powered by <a href="https://evolink.ai?utm_source=github&utm_medium=repo&utm_campaign=seed-audio-1-0-skill&utm_content=footer">EvoLink</a>
</p>
