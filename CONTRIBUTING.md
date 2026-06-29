# Contributing

Thank you for improving the Seed Audio 1.0 Skill repository.

## Scope

Good contributions include:

- API example fixes
- documentation corrections
- troubleshooting notes
- agent install improvements
- validation script updates

Do not add fabricated API behavior, pricing, benchmark claims, prompts, or model availability claims.

## Local Checks

Run before opening a pull request:

```bash
python3 scripts/validate_repo.py
npm pack --dry-run --json
node --check bin/cli.js
bash -n scripts/seed-audio-generate.sh
```

Real API smoke tests require owner approval because they may spend credits.

## Pull Requests

Include:

- What changed
- Why it changed
- Verification commands and results
- Known skips or blockers

