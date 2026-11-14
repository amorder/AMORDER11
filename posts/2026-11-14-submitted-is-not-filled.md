# Submitted Is Not Filled: Read the Order Status

- **Publication date:** 2026-11-14
- **Language / audience:** English / global
- **Channels:** Instagram Reels and YouTube Shorts
- **Topic:** Distinguishing an order request from accepted, new, partial, filled, canceled, rejected and expired order states
- **Viewer promise:** A simple way to keep a paper-trading record tied to confirmed order status instead of assumptions

## Story and production
An original process-led explainer. It uses no stock-specific call, account data, private broker payload, trading result or performance claim.

- **Opening hook:** "An order request is not proof of execution."
- **Scene design:** six distinct Blender Eevee PBR setups: idea, source, timestamp, gaps, stand-down and brand.
- **Motion:** keyframed camera and object animation in each Blender scene, followed by FFmpeg motion-compensated delivery at 30 fps.
- **Target runtime:** 105–145 seconds where the narration supports it; hard maximum strictly below 159 seconds (2:39).
- **Delivery:** 1080×1920, 9:16, 30 fps, H.264 MP4, AAC English narration, burned captions and SRT sidecar.
- **Blender render profile:** 720×1280 base, 6 fps, 2 Eevee TAA samples; FFmpeg motion-compensated interpolation and Lanczos upscale to the delivery format.
- **Voice:** Kokoro-82M v1.0 ONNX, af_heart; restrained original sound design only.
- **AI/rights provenance:** Kokoro-82M is listed as Apache-2.0; kokoro-onnx is MIT. The renderer uses the repository's documented public model files and voice catalogue.
- **Visual rights:** original procedural Blender geometry and animation; no third-party footage, broker screenshots or copyrighted music.
- **Disclosure:** shown on the closing card and included in both platform descriptions.

## Claim ledger and sources
1. Alpaca defines `accepted` as received by the broker but not yet routed to an execution venue.
2. Alpaca defines `new` as received and routed to exchanges for execution.
3. `partially_filled` means an order has executed only in part; `filled` means the order has been filled.
4. `pending_cancel` means the order is waiting for cancellation; `canceled` is a separate completed status.
5. `rejected` and `expired` are distinct statuses, not fills.
6. Alpaca's order documentation says an order may be canceled through the API until it reaches `filled`, `canceled` or `expired`.

Sources:
- [Alpaca Trading API — Create an Order / Order Status](https://docs.alpaca.markets/us/reference/postorder)
- [Alpaca — Placing Orders / Order Lifecycle](https://docs.alpaca.markets/us/docs/orders-at-alpaca)

The recommendation to preserve submission, status updates, partial executions and final outcomes is editorial process guidance, not a claim about a current trade or account.

## YouTube
**Title:** Submitted Is Not Filled: Read Order Status | AMORDER #Shorts

An order request is not proof of execution. This short explains the difference between accepted, new, partially filled, pending cancel, canceled, rejected, expired and filled. Keep paper-trading records tied to broker-confirmed status updates; never infer a fill from submission alone.

Sources:
Alpaca Trading API — Create an Order / Order Status: https://docs.alpaca.markets/us/reference/postorder
Alpaca — Placing Orders / Order Lifecycle: https://docs.alpaca.markets/us/docs/orders-at-alpaca

Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns.

#AMORDER #PaperTrading #TradingDiscipline #Shorts

## Instagram
An order request is not proof of execution. Learn the difference between accepted, new, partially filled, pending cancel, canceled, rejected, expired and filled. Keep the paper-trading log tied to confirmed status updates, not assumptions.

Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns.

#AMORDER #PaperTrading #TradingDiscipline #RiskManagement

**Alt text:** Six cinematic graphite-studio Blender scenes use a lens, linked source panels, a precision clock, separated data blocks, a protective pause symbol and an orbital brand form to explain order status transitions and why submission is not proof of a fill.

## Disclosure
Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns.

## Assets
- Storyboard: `posts/2026-11-14-submitted-is-not-filled.short.json`
- Expected MP4: `assets/amorder-submitted-is-not-filled-2026-11-14.mp4` (pending render)
- Expected SRT: `subtitles/amorder-submitted-is-not-filled-2026-11-14.srt`
- Expected manifest: `assets/amorder-submitted-is-not-filled-manifest-2026-11-14.json`

## Release gates
- [ ] Blender keyframed render completed; at least five distinct visual setups
- [ ] 1080×1920, 30 fps, H.264/AAC; runtime below 159 seconds
- [ ] Public HTTPS MP4 fetch returns non-empty MP4 bytes
- [ ] Full FFmpeg decode; representative-frame variation; no black/frozen sections
- [ ] Safe-zone and subtitle readability checks; SRT text/timing matches narration
- [ ] Audio stream, narration, loudness and clipping checks pass
- [ ] Sources, rights, privacy and factual checks pass
- [ ] Required disclosure verified on the video and both platform descriptions
- [ ] Automated quality score at least 85/100; no critical gate failed

## Publishing record
| Destination | Buffer post ID | Public URL | Status |
|---|---|---|---|
| Instagram Reel | pending | pending | pending_render |
| YouTube Short | pending | pending | pending_render |

No destination is reported as published until Buffer confirms the post as `sent` and a public post URL is verified. No human watch-through or headphone/speaker audition is claimed; only automated checks are reported.


## Render retry — 2026-11-14
- First render attempt [43598788407](https://github.com/amorder/AMORDER11/actions/runs/43598788407) failed in the Blender subprocess for scene 3 (the timestamp setup). The log shows the 106-frame PNG sequence completed and the scene MP4 was encoded and decoded; Blender 5.0.1 then exited with SIGSEGV (signal 11) during process teardown. The parent renderer treated every non-zero Blender exit as fatal, so its own ffprobe, duration/FPS and full-decode checks plus final visual, subtitle, audio, source and asset-commit gates were skipped.
- Focused fix: the renderer now tolerates only exit codes -11/139 when the expected scene MP4 exists and is non-empty. It then still requires parent-level H.264/720×1280/6-fps metadata, expected duration and a complete FFmpeg decode. Any other exit code, missing file, malformed stream, wrong duration or decode error remains a hard failure.
- Regression coverage was added to the public render-contract test. The storyboard is revision 2 and this is the single controlled retry; no MP4, SRT, manifest or video Buffer post is claimed until the workflow and all release gates complete.
- Concrete creative improvement versus the prior 156.82-second near-cap vertical: this story is structured around six distinct moving Blender setups and a short direct opening hook; the final runtime remains unverified until the narration render completes.
- Prior-release evidence review: the November 9 manifest confirms the 156.82-second vertical export at 1080×1920, 30 fps, H.264/AAC with burned captions. The November 6 and November 7 content records report earlier exports, but their detailed manifests are absent from the current public tree; no unsupported motion-coverage or audience-metric claims are inferred from those missing records.


## X text-first companion
Submitted is not filled. New = routed; partial = some quantity executed; filled = complete. Log only broker-confirmed quantities.

Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns. #AMORDER

The X companion is text-only and is not represented as a video. It is queued separately from the Instagram Reel and YouTube Short release path.

## X publishing record
| Destination | Buffer post ID | Public URL | Status |
|---|---|---|---|
| X text companion | `6af8a08d918fe79d2e95c0c5` | pending until sent | scheduled (automatic Buffer queue; due 2026-11-15 00:32 UTC) |


## Controlled render retry status — 2026-11-14
- Public short render retry: [GitHub Actions run 43623624656](https://github.com/amorder/AMORDER11/actions/runs/43623624656), currently in progress at the Blender scene-render step. The independent MP4 validation, visual/subtitle/audio/source gates and generated-asset commit have not run yet.
- Latest public secret-guard run 43623740809 passed for the content record commit.
- Private automatic release poll [43623887146](https://github.com/amorder/AMORDER/actions/runs/43623887146) completed successfully and explicitly reported: “Waiting: vertical video render is not complete yet.” It created no YouTube or Instagram post. Both destinations remain HOLD.
