# Model Repository Intake

## Basic

- Model: Doubao Seed-Audio 1.0
- Provider: ByteDance / Doubao
- EvoLink model page: https://evolink.ai/seed-audio-1-0
- EvoLink docs:
  - https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0
  - https://docs.evolink.ai/en/api-manual/audio-series/doubao-seed-audio/doubao-seed-audio-1-0-voices
- Repository name: doubao-seed-audio-api-skill
- Pipeline: skill-api
- Mode: scaffold + review
- Owner approval status: local scaffold approved by user request; public GitHub/npm release not approved

## Strategy

- Target audience: developers and agent users building audio-generation workflows
- Primary user intent: generate audio via API or install an agent skill
- Primary conversion CTA: EvoLink API key and model page
- Secondary CTA: official API docs and runnable examples
- Existing related repositories: awesome-suno-api, gpt-image-2-gen-skill
- Old repositories to preserve as entrance pages: none identified

## Eligibility

- EvoLink access status: official EvoLink docs exist; model page exists in local material
- Search/distribution demand: Seed-Audio launch materials and keyword monitoring exist
- Source material availability: official API docs, voice docs, local strategy notes
- API availability: endpoint documented as `POST /v1/audios/generations`
- Skill feasibility: async API can be wrapped by a script with polling
- Duplicate/replacement risk: no existing Seed-Audio API skill repo found locally
- Decision: eligible
- Reason: clear model/API docs, concrete developer workflow, audio-to-video conversion path

## Skill/API Fields

- API endpoint: `POST /v1/audios/generations`
- Lifecycle: async
- Package name: evolink-seed-audio
- Skill slug: doubao-seed-audio
- ownerId: placeholder, blocks public release
- Required environment variables: EVOLINK_API_KEY
- Smoke-test level: static + dry-run
- API cost boundary: real API smoke test skipped pending owner approval

## Assumptions

- The repository remains local until owner approves public GitHub creation and npm publish.
- The first version is English-only; localization can follow after technical review.
- Real API smoke test is intentionally skipped to avoid spending credits without explicit approval.

