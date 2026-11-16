# When One Unit Is Too Much

- **Publication date:** 2026-11-16
- **Language / audience:** English / global
- **Channels:** Instagram Reels and YouTube Shorts
- **Topic:** How planned loss, stop distance and unit value determine a risk-based position size, and why the minimum permitted unit may still be too large

## Viewer promise
Learn why position size is the last step of a risk calculation, and why the correct planned size can be zero when the minimum permitted unit exceeds the risk limit.

## Editorial and production
- **Opening hook:** "If the smallest tradable unit breaks your risk limit, the disciplined position size may be zero. Size comes last."
- **Visual direction:** six original Blender Eevee PBR setups: bounded risk chamber, calibrated stop-distance rail, single unit token, modular size blocks, minimum-unit gate and brand stage
- **Motion:** genuine keyframed camera and object animation in every scene, with scene-specific FFmpeg motion graphics
- **Delivery:** one shared 1080x1920, 9:16, constant 30 fps, H.264/AAC vertical master; burned English captions and SRT sidecar
- **Runtime:** target 85-115 seconds where the narration supports it; hard maximum strictly below 160 seconds
- **Voice:** Kokoro-82M ONNX, af_heart; calm international English
- **Audio:** no copyrighted music or third-party sound effects; original restrained sound design only
- **Visual safety:** schematic educational graphics only; no symbols, account data, broker UI, trade records or performance claims

## Claim ledger and primary sources
- CME Group's position-sizing lesson identifies stop location and the amount a trader is prepared to risk as key inputs to position size.
- CME Group illustrates planned risk per contract using stop distance in ticks and the value of each tick.
- The SEC states that a stop price triggers a market order and is not a guaranteed execution price; the actual execution price can differ.

Sources:
- [CME Group — Proper Position Size](https://www.cmegroup.com/education/courses/trade-and-risk-management/proper-position-size)
- [SEC Investor Bulletin — Stop, Stop-Limit, and Trailing Stop Orders](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-15) (updated August 18, 2026)

No universal risk percentage is prescribed. No numerical example, market statistic, trade result or return claim is used.

## Rights and provenance
- Original Blender Eevee scenes and procedural graphics; no stock footage or third-party video
- Kokoro-82M model weights: Apache-2.0
- kokoro-onnx runtime: MIT
- Noto Sans: OFL family licence
- No copyrighted music or third-party sound effects
- Rights references: [Kokoro-82M model card](https://huggingface.co/hexgrad/Kokoro-82M), [kokoro-onnx MIT licence](https://github.com/thewh1teagle/kokoro-onnx/blob/main/LICENSE)

## Disclosure
Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns.

## Assets
- Storyboard: [posts/2026-11-16-one-unit-too-much.short.json](https://github.com/amorder/AMORDER11/blob/main/posts/2026-11-16-one-unit-too-much.short.json)
- Expected MP4: `assets/amorder-one-unit-too-much-2026-11-16.mp4` (pending render)
- Expected SRT: `subtitles/amorder-one-unit-too-much-2026-11-16.srt`
- Expected manifest: `assets/amorder-one-unit-too-much-manifest-2026-11-16.json`

## Release gates
- [ ] Blender keyframed render completed; at least five distinct supported animated visual setups
- [ ] 1080x1920, 9:16, H.264/AAC, nominal 30 fps; runtime strictly below 160 seconds
- [ ] Exact public HTTPS MP4 availability verified
- [ ] Full FFmpeg decode; representative-frame variation; no black/frozen sections
- [ ] Safe-zone and subtitle readability checks; SRT text/timing matches narration
- [ ] Audio stream, loudness, clipping and subtitle/narration alignment checks pass
- [ ] Sources, rights, privacy, factual accuracy and disclosure checks pass
- [ ] Automated quality score at least 85/100; no critical gate failed

## Publishing record
| Destination | Status | Public URL |
|---|---|---|
| Instagram Reel | pending_render | pending |
| YouTube Short | pending_render | pending |

No destination is reported as published until Buffer confirms the post as `sent` and a public URL is verified. No human watch-through or headphone/speaker audition is claimed.
