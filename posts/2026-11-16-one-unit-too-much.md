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
- **Runtime:** 65.257 seconds
- **Blender profile:** 720x1280 scene renders at 12 fps, 2 render samples; Lanczos delivery upscale and motion-compensated 30 fps finishing
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
- [Storyboard](https://github.com/amorder/AMORDER11/blob/main/posts/2026-11-16-one-unit-too-much.short.json)
- [Final MP4](https://raw.githubusercontent.com/amorder/AMORDER11/main/assets/amorder-one-unit-too-much-2026-11-16.mp4)
- [SRT sidecar](https://raw.githubusercontent.com/amorder/AMORDER11/main/subtitles/amorder-one-unit-too-much-2026-11-16.srt)
- [Release manifest](https://github.com/amorder/AMORDER11/blob/main/assets/amorder-one-unit-too-much-manifest-2026-11-16.json)

## Automated release evidence
- [Render workflow run 43901178823](https://github.com/amorder/AMORDER11/actions/runs/43901178823) completed successfully; all 23 job steps completed, including independent technical validation, visual/subtitle/audio/source release gates and asset commit.
- Exact export: 65.257 seconds, 1080x1920, H.264/AAC, 30 fps, 28,335,598 bytes.
- Blender scene profile: 720x1280 at 12 fps; six scene midpoints; 100% sampled motion coverage across 65 frames.
- Motion checks: zero sampled black frames and zero frozen-run seconds; minimum scene-difference score 8.32.
- Audio: mean -15.5 dB, peak -1.5 dB.
- Subtitles: 17 cues, maximum 96 characters; subtitle bottom margin 290 px.
- Full-file decode, caption/narration text agreement, safe-zone checks, source/disclosure checks and technical export checks passed.
- Automated release score: 100/100. This is automated evidence only; no human watch-through or headphone/speaker audition is claimed.

## Production repair log
- Runs [43876452663](https://github.com/amorder/AMORDER11/actions/runs/43876452663) and [43878038044](https://github.com/amorder/AMORDER11/actions/runs/43878038044) were superseded before media validation after factual wording and duplicated narration were corrected.
- Render [43880610537](https://github.com/amorder/AMORDER11/actions/runs/43880610537) produced a technically valid candidate but failed at the asset commit step because the workflow referenced an undefined shell variable. The workflow commit-message expression was corrected and regression coverage added.
- The renderer, Blender CLI default, independent manifest validator, regression test and delivery-quality documentation were updated to require 12 fps Blender scene animation and 30 fps delivery.
- Corrected run [43901178823](https://github.com/amorder/AMORDER11/actions/runs/43901178823) completed the render, independent release gate and commit. The final committed manifest records the evidence above.
- Optional HyperFrames smoke test [43911598190](https://github.com/amorder/AMORDER11/actions/runs/43911598190) failed before browser/render checks because its example references an unavailable `aptos` font without an `@font-face` declaration. HyperFrames is not part of this asset's production path and was not used; Blender remained the primary renderer.

## Publishing record
| Destination | Status | Buffer post ID | Scheduled / sent time | Verified public URL |
|---|---|---|---|---|
| Instagram Reel | sent | `6afb4271afba1286ca70aee9` | 2026-11-17 08:58:59 IST | [Instagram Reel](https://www.instagram.com/reel/Df09whguCJd/) |
| YouTube Short | scheduled (custom time) | `6afb426c9509e7b0ff1377a3` | 2026-11-20 18:58 IST | Not available until sent |

The YouTube post is scheduled, not published. No destination is reported as published unless Buffer confirms `sent` and a public URL is verified.
