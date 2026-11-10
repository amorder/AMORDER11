# AMORDER11 — Public Content Publishing Repository

AMORDER11 is the public-facing content repository for AMORDER. It holds reviewed, public-safe post copy, captions, storyboards, final creative assets and publication status for YouTube, Instagram and other approved channels.

The core AMORDER application, trading system, strategy implementation, research database and operational records are maintained separately in the private repository amorder/AMORDER.

## Public means downloadable

This repository is intentionally public. Anyone can view, clone, fork or download its contents. This includes committed source files, post records, storyboards, videos, commit history and information exposed in workflow logs. Removing a file in a later commit does not erase earlier copies from Git history or third-party caches.

Do not treat this repository as private storage. Publish only material approved for worldwide release. Do not commit secrets, private data, unreleased research or code whose implementation must remain confidential.

The current tools/ renderer scripts and GitHub Actions workflows are also public source code and can be copied. They are content-rendering utilities, not the AMORDER trading engine. Any proprietary renderer, unpublished production process or intellectual property that must not be copied must be moved to the private repository before further development there.

## Language and audience

- Default language: English.
- Default audience: a broad global audience.
- Use clear, natural voiceover, short on-screen headlines, readable captions and restrained wording.
- Every video must keep the complete paper-trading disclosure visible on its closing card.
- Do not invent performance, fills, returns, sources or trading outcomes.

## Public media library and share links

Final, public-safe MP4 exports, thumbnails, subtitle sidecars and render manifests are catalogued in [MEDIA_INDEX.md](MEDIA_INDEX.md). The index provides direct GitHub raw HTTPS download links that can be shared or supplied to the authorized Buffer publisher. The files remain versioned in this repository; keep the release status truthful; automatic publishing uses the owner's standing authorization and the independent release checks in DOCS/DELIVERY_QUALITY_GATE.md.

## Daily content workflow

1. Create or update a reviewed Markdown record under posts/, named YYYY-MM-DD-short-title.md or YYYY-MM-DD-episode.md.
2. Keep only approved public copy, verified public sources, disclosure, approved asset references and public-safe publishing status.
3. A reviewed short storyboard at posts/YYYY-MM-DD-short-title.short.json can trigger .github/workflows/render-public-short.yml, which creates a vertical MP4 in assets/.
4. A reviewed long-form storyboard at posts/YYYY-MM-DD-episode.episode.json can trigger .github/workflows/render-public-episode.yml, which creates a YouTube master, an Instagram episode and subtitle sidecars.
5. The renderers use Blender Eevee, Kokoro-82M ONNX, FFmpeg and Pillow. They do not connect to broker accounts, trading records, private research, Buffer or social publishing APIs.
6. Publish or queue approved posts through the separate AMORDER automation and connected Buffer integration. These GitHub rendering workflows do not publish directly to YouTube or Instagram.
7. Record only public-safe status and destination URLs. Do not store access tokens, account identifiers, private analytics or unpublished platform payloads.
8. Check existing publication status before retrying. Never label a failed post as published.

## Public repository boundary

Allowed: reviewed captions and scripts, educational storyboards, approved final videos/images, public source links and public-safe publishing records.

Never store: trading or strategy source code, private renderer implementation, candidate scans, symbol-specific research, raw market/broker data, private journals, account/order IDs, balances, positions, fills, trade-by-trade details, P&L/performance statistics, broker payloads, credentials, tokens, .env files, internal logs, unpublished creative or personal data.

Content may explain general research, data quality, paper-trading and risk-management concepts. Do not publish buy/sell calls, price targets, confidential strategy parameters or fabricated metrics. Every paper-trading disclosure must state that activity is simulated, is not live-money performance, is not investment advice and is not a promise of returns.

## Security and ownership

- The secret guard scans current files and Git history. A scan is a safety net, not permission to commit sensitive material.
- Rendering workflows use a repository-scoped GitHub token only to commit generated public assets. Keep external publishing, broker and personal credentials out of this repository and its workflow variables.
- The connected Buffer integration is used by the separate AMORDER automation. Never paste Buffer, Alpaca, Hugging Face or personal access tokens into files, logs or commit messages.
- CODEOWNERS identifies @amorder as the owner; GitHub branch rules must also require owner review for that file to be enforced.
- No separate open-source licence is granted for AMORDER branding or original content. See NOTICE.md.

## Creative toolchain

- Blender Eevee PBR for original cinematic 3D scenes.
- Kokoro-82M ONNX for English synthetic narration.
- FFmpeg / ffprobe for editing, H.264/AAC encoding and output validation.
- Pillow for high-resolution typography and caption overlays.
- video-shotcraft is used only as a reference for pacing and visual QA; AMORDER scenes and copy remain original.

## Initial workflow references

- Short renderer: tools/render_public_short.py
- Blender scene generator: tools/blender_scenes.py
- Long-form renderer: tools/render_public_episode.py
- Short workflow: .github/workflows/render-public-short.yml
- Long-form workflow: .github/workflows/render-public-episode.yml
- Secret guard: .github/workflows/secret-guard.yml


## Video production skill library

The uploaded DOCS production skill has been curated into the root [DOCS/](DOCS/README.md) folder. Start with the [Video & Motion Creation skill](DOCS/skills/video-motion-creation/skill.md) and the [Delivery Quality Gate](DOCS/DELIVERY_QUALITY_GATE.md).

The standards set the default for future AMORDER videos: global English, natural professional narration, minimal cinematic realism, Blender PBR hero scenes, scene-specific animated motion graphics, source and rights tracking, and automated release checks under the owner's standing auto-publishing authorization. They complement the existing renderers; they do not activate a second renderer or publisher.
