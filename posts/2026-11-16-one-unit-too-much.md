# When One Unit Is Too Much

- **Publication date:** 2026-11-16
- **Language / audience:** English / global
- **Channels:** X (text-first companion), Instagram Reels and YouTube Shorts
- **Topic:** How planned loss, stop distance and unit value determine a risk-based position size, and why the minimum permitted unit may still be too large

## Viewer promise
Learn why position size is the last step of a risk calculation, and why the correct planned size can be zero when the minimum permitted unit exceeds the risk limit.

## X text-first companion

Position size comes last: set a risk budget, measure stop distance, apply point/tick value, then round down. If one unit exceeds the limit, zero is valid. Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns. #AMORDER

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

## Improvement versus recent vertical releases
- The latest committed vertical manifest (2026-11-15) records 94.094 seconds, 1080x1920 at 30 fps, H.264/AAC, six scenes, genuine Blender keyframed animation, 100% sampled motion coverage, 24 subtitle cues, zero sampled black frames, zero frozen-run seconds, mean audio -15.5 dB and peak -1.5 dB, with a 290 px bottom subtitle margin and an automated score of 100/100.
- The 2026-11-09 release used separate masters: a 156.82-second 1080x1920 Instagram export and a 277.83-second 1920x1080 YouTube export. Today's workflow retains one shared 9:16 master for both destinations.
- A 2026-11-08 vertical MP4 exists, but no committed manifest was found, so its exact motion/audio/export checks cannot be compared. November 14 and 13 storyboards have no committed MP4/manifest and are not counted as completed releases.
- This episode narrows the subject to one decision boundary—whether the minimum permitted unit fits the risk limit—and uses six distinct Blender visual keys. The Blender scene rate is being raised from the previous manifest's 6 fps to the required 12 fps, with motion-compensated 30 fps delivery; the new manifest must confirm this before release.

## Production repair log
- Earlier render runs [43876452663](https://github.com/amorder/AMORDER11/actions/runs/43876452663) and [43878038044](https://github.com/amorder/AMORDER11/actions/runs/43878038044) were superseded before media validation after source review and narration repair.
- Deterministic editorial defect: scenes 1 and 2 contained identical narration. Scene 2 was rewritten to explain the risk budget before position-size arithmetic. Regression coverage now rejects duplicate narration across scenes; the contract test passed on run 43880610537.
- Render attempt [43880610537](https://github.com/amorder/AMORDER11/actions/runs/43880610537) produced a 65.257-second 1080x1920, 30 fps H.264/AAC MP4 with burned captions and SRT. Automated checks reported score 100/100, 100% sampled motion coverage, zero black frames, zero frozen-run seconds, mean audio -15.5 dB, peak -1.5 dB, and 290 px bottom subtitle margin. These are evidence from an uncommitted attempt, not an approved release.
- That attempt failed at the asset commit step because the workflow referenced undefined `${BASE}` under `set -u`. The workflow was corrected to derive the commit message from exported `${OUTPUT%.mp4}`, and a regression assertion was added. The public secret guard passed after these changes.
- A further requirement audit found the renderer and manifest validator still used 6 fps Blender scenes, while the standing production specification requires 12 fps Blender renders interpolated to 30 fps. The renderer constant, Blender CLI default, independent manifest validator, regression test and delivery-quality documentation were all updated to require 12 fps. No quality gate was weakened.
- Corrected 12 fps render run [43901178823](https://github.com/amorder/AMORDER11/actions/runs/43901178823) is pending / rendering. The caption-contract step must pass, the manifest must confirm 12 fps Blender animation and 30 fps delivery, and all media/source/privacy gates must pass before any video post is created. No November 16 MP4, SRT or manifest is committed yet.

## Publishing record
| Destination | Status | Buffer post ID | Public URL |
|---|---|---|---|
| X text-first post | scheduled (2026-11-16 16:14 UTC) | 6afb24d7aa36fe9e61225417 | not available until sent |
| Instagram Reel | pending_render | pending | pending |
| YouTube Short | pending_render | pending | pending |

No destination is reported as published until Buffer confirms the post as `sent` and a public URL is verified. No human watch-through or headphone/speaker audition is claimed.
