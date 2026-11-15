# Paper Trading Has Blind Spots

- **Publication date:** 2026-11-15
- **Language / audience:** English / global
- **Channels:** Instagram Reels, YouTube Shorts
- **Topic:** What paper-trading simulations omit and why a simulated fill is not a forecast of live execution

## Viewer promise
A paper fill can be useful for testing code and process, but it does not reproduce every condition of live execution. This explainer identifies the limitations in Alpaca's published paper-trading specification and gives viewers a practical way to document them.

## Editorial and production
- **Opening hook:** "A paper-trading fill can look convincing. But it is not proof that a live order would have filled the same way."
- **Visual direction:** six original Blender Eevee PBR setups in a cinematic graphite studio; physically based glass and metal, motivated softbox lighting, restrained cyan/amber accents and clear negative space
- **Motion:** genuine keyframed camera and object movement in each Blender scene; FFmpeg motion-compensated finishing and scene-specific animated overlays
- **Planned runtime:** 105–145 seconds; hard maximum strictly below 160 seconds
- **Delivery:** 1080×1920, 9:16, constant 30 fps, H.264 MP4, AAC English narration, burned English captions and SRT sidecar
- **Voice:** Kokoro-82M ONNX, af_heart; calm international English
- **Audio:** no copyrighted music or third-party sound effects; original restrained sound design only
- **Visual safety:** all graphics are schematic; no market values, broker UI, real orders or trading account data

## Claim ledger and primary source
All material factual claims are supported by the same official source:
- Alpaca's paper environment does not route orders to a live exchange; it simulates fills using real-time quotes.
- Published limitations include market impact, information leakage, latency-related slippage, queue position for non-marketable limit orders, price improvement, regulatory fees and dividends.
- Paper order quantity is not checked against NBBO quantities; a simulated fill can exceed displayed available liquidity.
- Other simulators may differ in fill prices, fill assumptions, liquidity assumptions, return methodologies and market data sources.

Source: [Alpaca — Paper Trading](https://docs.alpaca.markets/us/docs/paper-trading) (accessed 2026-11-15).

## Platform copy

### YouTube
**Title:** Paper Trading Has Blind Spots | AMORDER #Shorts

A simulated fill is not a forecast of live execution. This short explains what Alpaca's published paper-trading documentation says the simulation does not model: market impact, information leakage, latency-related slippage, queue position for non-marketable limit orders, price improvement, regulatory fees and dividends. It also explains the displayed-liquidity limitation and why simulator assumptions differ.

Source: Alpaca — Paper Trading: https://docs.alpaca.markets/us/docs/paper-trading

Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns.

#AMORDER #PaperTrading #RiskManagement #Shorts

### Instagram
A paper-trading fill is useful evidence about a simulation — not a promise about live execution. This explainer covers market impact, latency, queue position, displayed liquidity and why simulator assumptions matter.

Source: Alpaca Paper Trading documentation: https://docs.alpaca.markets/us/docs/paper-trading

Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns.

#AMORDER #PaperTrading #MarketData #RiskManagement

**Alt text:** Six original cinematic graphite-studio Blender scenes use a glass simulation chamber, quote plane, separated metal plates, schematic liquidity columns and modular glass systems to explain why paper-trading fills do not reproduce every condition of live execution.

## Rights and provenance
- Original Blender scenes and procedural graphics; no stock footage or third-party video
- Kokoro-82M model weights: Apache-2.0
- kokoro-onnx runtime: MIT
- Noto Sans: OFL family licence
- No copyrighted music or third-party sound effects
- Rights references: [Kokoro-82M model card](https://huggingface.co/hexgrad/Kokoro-82M), [kokoro-onnx MIT licence](https://github.com/thewh1teagle/kokoro-onnx/blob/main/LICENSE)

## Disclosure
Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns.

## Assets
- Storyboard: `posts/2026-11-15-paper-trading-blind-spots.short.json`
- Expected MP4: `assets/amorder-paper-trading-blind-spots-2026-11-15.mp4` (pending render)
- Expected SRT: `subtitles/amorder-paper-trading-blind-spots-2026-11-15.srt`
- Expected manifest: `assets/amorder-paper-trading-blind-spots-manifest-2026-11-15.json`

## Release gates
- [ ] Blender keyframed render completed; at least five distinct animated visual setups
- [ ] 1080×1920, 9:16, H.264/AAC, constant 30 fps; runtime below 160 seconds
- [ ] Public HTTPS MP4 fetch returns non-empty MP4 bytes
- [ ] Full FFmpeg decode and ffprobe verification pass
- [ ] Representative frames show scene variation; no black/frozen sections
- [ ] Motion coverage and safe-zone checks pass
- [ ] English SRT matches narration, is readable and stays within safe areas
- [ ] Audio stream, loudness, clipping and subtitle/narration alignment checks pass
- [ ] Claims, public sources, rights, privacy and disclosure checks pass
- [ ] Automated quality score at least 85/100; no critical gate failed

## Publishing record
| Destination | Buffer post ID | Public URL | Status |
|---|---|---|---|
| Instagram Reel | pending | pending | HOLD — pending render and independent release gates |
| YouTube Short | pending | pending | HOLD — pending render and independent release gates |

No destination is reported as published until Buffer confirms the post as `sent` and a public post URL is verified. No human watch-through or headphone/speaker audition is claimed; only automated checks will be reported.
