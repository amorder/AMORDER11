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
- For a standard stop order, the SEC states that the trigger becomes a market order and the execution price can differ from the stop price. This wording does not generalize the rule to stop-limit orders.

Sources:
- [CME Group — Proper Position Size](https://www.cmegroup.com/education/courses/trade-and-risk-management/proper-position-size)
- [SEC Investor Bulletin — Stop, Stop-Limit, and Trailing Stop Orders](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-15) (updated August 18, 2026)

No universal risk percentage is prescribed. No numerical example, market statistic, trade result or return claim is used. The November 9 paper-fill case study also mentioned risk-based sizing; this short is deliberately narrower, focusing on the minimum-increment feasibility boundary and the disciplined decision to pass, without reusing that case study or any specific trade.

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

## Production repair log
- Initial render run [43876452663](https://github.com/amorder/AMORDER11/actions/runs/43876452663) was superseded before completion after source review narrowed the SEC execution-price statement to standard stop orders.
- Corrected render run [43878038044](https://github.com/amorder/AMORDER11/actions/runs/43878038044) reached the Blender rendering step, then was superseded by the editorial repair below. No MP4/SRT validation or asset commit occurred in that run.
- Deterministic editorial defect: scenes 1 and 2 contained identical narration. Scene 2 was rewritten to explain the risk budget before position-size arithmetic.
- Regression repair commit: [3a2b62a](https://github.com/amorder/AMORDER11/commit/3a2b62ad089d846ef106f93b3a256a406becdabd) updates the scene 2 narration and adds `tools/test_caption_contract.py` coverage that rejects duplicate narration across scenes. The workflow pre-render contract-test step passed on this commit (run 43880610537, step 4); the matching secret guard [43880610230](https://github.com/amorder/AMORDER11/actions/runs/43880610230) also passed.
- Corrected render attempt: [43880610537](https://github.com/amorder/AMORDER11/actions/runs/43880610537) is the single retry for this editorial repair. It is currently in the Blender rendering step; independent MP4 and release validation have not started, and no generated MP4/SRT/manifest is committed yet.
- No media is approved and no Buffer post has been created while these checks are pending.

## Publishing record
| Destination | Status | Public URL |
|---|---|---|
| Instagram Reel | pending_render | pending |
| YouTube Short | pending_render | pending |

No destination is reported as published until Buffer confirms the post as `sent` and a public URL is verified. No human watch-through or headphone/speaker audition is claimed.
