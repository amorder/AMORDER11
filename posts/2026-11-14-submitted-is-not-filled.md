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
