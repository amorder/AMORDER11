# AMORDER11 — Content automation only

AMORDER11 is the public content operations repository for AMORDER. It stores reviewed post copy, platform-specific captions, approved public creative assets, source links, video storyboards, and Buffer publishing records.

It is not the trading system, research database, paper-trading ledger, or application-code repository. Those functions remain in the separate private repository amorder/AMORDER.

## Language and audience

- Default language: English.
- Default audience: a broad global audience.
- Do not mix languages or rely on region-specific slang unless explicitly requested.
- Use clear, natural voiceover, short on-screen headlines, readable captions, and restrained wording.
- Every video must keep the paper-trading disclosure visible in the creative and complete on the closing card.

## Daily content workflow

1. Create or update one Markdown post record under posts/, named YYYY-MM-DD-short-title.md or YYYY-MM-DD-episode.md.
2. Keep the post title, publication date, factual source links, platform-specific copy, disclosure, approved asset references, and publishing record in that file.
3. For the daily trailer, add a public-safe storyboard at posts/YYYY-MM-DD-short-title.short.json. The secret-free workflow .github/workflows/render-public-short.yml creates a vertical MP4 in assets/.
4. For the long-form episode, add a reviewed storyboard at posts/YYYY-MM-DD-episode.episode.json with separate YouTube and Instagram scene tracks. The workflow .github/workflows/render-public-episode.yml creates a 4–8 minute 16:9 YouTube master, a 2.5–3 minute vertical Instagram episode, and subtitle sidecars.
5. Both renderers create original Blender Eevee PBR scenes, cinematic lighting, restrained camera motion, English Kokoro narration and FFmpeg finishing. They do not access broker accounts, trading records, private research, Buffer, Alpaca or user-supplied secrets.
6. Publish or queue each connected destination through the existing AMORDER daily automation and connected Buffer integration. X remains text-first; Instagram uses Reels; YouTube uses long-form video and vertical Shorts. Use separate platform metadata and captions.
7. Update the same Markdown file with each Buffer post ID, public URL (when available), and confirmed status: sent, scheduled, draft, or error. Never label a failed post as published, and check for duplicates before retrying.

## Open-source creative toolchain

- **Blender Eevee PBR:** original cinematic 3D scene plates with physically based materials, controlled depth of field, softbox lighting and restrained color accents, rendered headlessly.
- **Kokoro-82M ONNX:** English synthetic narration; model weights from the public Hugging Face model family. No inference API key is required.
- **FFmpeg / ffprobe:** motion finishing, H.264/AAC encoding, and independent output validation.
- **Pillow:** crisp, high-resolution typography and caption overlays.
- **video-shotcraft:** motion-design reference for pacing, shot restraint, and visual QA. AMORDER scenes and copy remain original; no third-party footage, marks, or music are copied.

## Repository boundary

Allowed here: reviewed post copy, captions, educational scripts/storyboards, approved public images/videos, public source URLs, content calendar metadata, and Buffer publishing IDs/URLs/statuses.

Never store here: trading or strategy source code, candidate scans, symbol-specific research, raw market/broker data, private journals, account/order IDs, balances, positions, fills, trade-by-trade details, P&L/performance statistics, broker payloads, credentials, tokens, .env files, or internal logs.

Content may explain general research, data-quality, paper-trading, and risk-management concepts. Any paper-trading disclosure must clearly say it is simulated activity, not live-money performance, not investment advice, and not a promise of returns. Do not publish buy/sell calls, price targets, or fabricated metrics.

## Publishing and security

- Buffer workspace: My organization
- Connected destinations: Instagram professional account amorder11, YouTube channel AMORDERS, and X profile amorder11
- Time zone: Asia/Kolkata
- The existing daily AMORDER automation orchestrates publishing using the connected Buffer integration.
- The GitHub Actions secret guard is read-only. The short-render workflow only creates public creative media; it does not publish content and does not use stored secrets.
- GitHub Actions uses its repository-scoped generated token only to commit the rendered public asset.
- Never add Buffer, Alpaca, Hugging Face, or personal credentials to this public repo.

## Initial workflow test

- 2026-11-06 content workflow test: posts/2026-11-06-workflow-test.md
- 2026-11-06 AMORDER public workflow post: posts/2026-11-06-building-amorder-in-public.md
- AMORDER video renderer: tools/render_public_short.py
- Blender scene generator: tools/blender_scenes.py
- Short render workflow: .github/workflows/render-public-short.yml
