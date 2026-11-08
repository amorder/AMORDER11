# DOCS — AMORDER video production standards

This folder preserves and adapts the reusable video-production skills and technical standards from the uploaded DOCS package for AMORDER.

## Start here

- [Core skill](SKILL.md) — the overall creative, research, rights, production and release standard.
- [Video & Motion Creation](skills/video-motion-creation/skill.md) — the reusable production skill for films, explainers, Shorts and Reels.
- [Marketing-agency Reel standard](skills/video-motion-creation/MARKETING_AGENCY_STANDARD.md) — visual coverage, motion, sound and scored release gate.
- [Publishing automation](skills/video-motion-creation/PUBLISHING_AUTOMATION.md) — safe, verified publishing rules.
- [Blender Python workflow](docs/BLENDER_PYTHON_API_WORKFLOW.md) — reproducible procedural scenes and motion.
- [Open-source AI production](docs/OPEN_SOURCE_AI_PRODUCTION.md) — local-model, licensing and provenance requirements.
- [Video factory architecture](docs/VIDEO_FACTORY_ARCHITECTURE.md) — job stages, worker boundaries and failure handling.
- [Delivery quality gate](DELIVERY_QUALITY_GATE.md) — final pass/fail review checklist.

## AMORDER integration

The active AMORDER production path remains:

- Short render: \`.github/workflows/render-public-short.yml\` and \`tools/render_public_short.py\`
- Long-form render: \`.github/workflows/render-public-episode.yml\` and \`tools/render_public_episode.py\`
- Blender scene generation: \`tools/blender_scenes.py\`
- Public post records and storyboards: \`posts/\`
- Approved public media: \`assets/\`

These documents define creative and technical standards. They do not automatically enable another production engine, deploy a worker, connect a new model provider, grant publishing permission or schedule posts.

## What was intentionally not imported

The uploaded archive also contained example episode packages, dated job/output folders, media manifests and a separate set of GitHub Actions workflows. Those were not copied into AMORDER's active workflows. This avoids publishing unrelated sample/client material or silently running a second automation system. The reusable documentation has been adapted to AMORDER's public-content-only repository boundary.

## Global creative defaults

- English narration, on-screen text, titles and captions.
- Broad global audience; explain local references and technical terms.
- Calm, natural, confident and professional voice. No robotic cadence, exaggerated hype or clickbait.
- Minimal, modern, cinematic realism with meaningful camera and object motion.
- Free/open-source and local tools first; no unapproved paid services or generation credits.
- Human creative approval before release; automated technical checks cannot approve creative quality.
