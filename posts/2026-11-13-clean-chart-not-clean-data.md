# A Clean Chart Is Not Proof of Clean Data

- **Publication date:** 2026-11-13
- **Language / audience:** English / global
- **Channels:** Instagram Reels and YouTube Shorts
- **Topic:** How feed selection, timestamps, pagination and adjustment settings affect market-data quality
- **Viewer promise:** A practical checklist for checking what a chart is actually showing before using it in a paper test

## Story and production
An original process-led explainer. It uses no live market snapshot, stock-specific call, account data, trading result or performance claim.

- **Opening hook:** "A chart can look smooth and still mislead."
- **Scene design:** six distinct Blender Eevee PBR setups: idea, source, timestamp, gaps, stand-down and brand.
- **Motion:** keyframed camera and object animation in each Blender scene, followed by FFmpeg motion-compensated delivery at 30 fps.
- **Target runtime:** 105–145 seconds; hard maximum strictly below 159 seconds (2:39).
- **Delivery:** 1080×1920, 9:16, 30 fps, H.264 MP4, AAC English narration, burned captions and SRT sidecar.
- **Voice:** Kokoro-82M v1.0 ONNX, af_heart; restrained original sound design only.
- **AI/rights provenance:** [hexgrad/Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) is listed as Apache-2.0; [kokoro-onnx](https://github.com/thewh1teagle/kokoro-onnx) is MIT. The renderer downloads `kokoro-v1.0.onnx` and `voices-v1.0.bin` from the [model-files-v1.1 release](https://github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files-v1.1); `af_heart` is listed in the upstream [voice catalogue](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md).
- **Visual rights:** original procedural Blender geometry and animation; no third-party footage or copyrighted music.
- **Disclosure:** shown on the closing card and included in both platform descriptions.

## Claim ledger and sources
1. Alpaca's market-data FAQ distinguishes IEX (a single exchange) from SIP (consolidated activity across US exchanges).
2. Alpaca's FAQ explains that a minute bar timestamp is the start of the aggregation interval.
3. The historical-bars API may return fewer points than the requested limit; check `next_page_token` when more pages are available.
4. The historical-bars API supports raw, split, dividend and all adjustment modes.

Sources:
- [Alpaca Market Data FAQ](https://docs.alpaca.markets/us/v1.1/docs/market-data-faq)
- [Alpaca Historical Bars API](https://docs.alpaca.markets/us/v1.1/reference/stockbars)

The feed, timestamp, pagination and adjustment statements above are grounded in those official documentation pages. The recommendation to record source, interval, timezone, session, pagination and adjustment settings is editorial guidance, not a claim about current market conditions.

## YouTube
**Title:** A Clean Chart Is Not Proof of Clean Data | AMORDER #Shorts

Why can a clean-looking chart still hide a data problem? This short walks through feed coverage, bar timestamps, pagination, session context and adjustment settings. No market performance or trade result is claimed.

Sources:
Alpaca Market Data FAQ: https://docs.alpaca.markets/us/v1.1/docs/market-data-faq
Alpaca Historical Bars API: https://docs.alpaca.markets/us/v1.1/reference/stockbars

Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns.

#AMORDER #MarketDataQuality #Shorts

## Instagram
A smooth chart is not a data-quality check. Before trusting a signal, verify the feed, bar timestamp, session, pagination and corporate-action adjustment. If the inputs are unclear, pause the paper test rather than guessing.

Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns.

#AMORDER #MarketDataQuality #RiskDiscipline

**Alt text:** Six cinematic graphite-studio Blender scenes use a lens, source panels, a clock-like timestamp, missing data blocks, a protective pause symbol and an orbital brand form to explain market-data feed coverage, timestamps, pagination and adjustment settings.

## Disclosure
Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns.

## Assets
- Storyboard: `posts/2026-11-13-clean-chart-not-clean-data.short.json`
- Expected MP4: `assets/amorder-clean-chart-not-clean-data-2026-11-13.mp4` (pending render)
- Expected SRT: `subtitles/amorder-clean-chart-not-clean-data-2026-11-13.srt`
- Expected manifest: `assets/amorder-clean-chart-not-clean-data-manifest-2026-11-13.json`

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

No destination is reported as published until Buffer confirms the post as `sent` and a public post URL is verified. No human watch-through or headphone/speaker audition is claimed. The release workflow must verify the audio stream, full decode, loudness, clipping and narration/subtitle alignment; only automated checks are reported under the standing publishing authorization.


## Render status — 2026-11-13
- [GitHub Actions run 43427943599](https://github.com/amorder/AMORDER11/actions/runs/43427943599) passed the caption-contract precheck and completed media-tool and Kokoro model installation. The Blender scene-render step is in progress.
- [Public secret-guard run 43428194762](https://github.com/amorder/AMORDER11/actions/runs/43428194762) passed.
- Independent MP4 validation, representative-frame/motion checks, subtitle/safe-zone checks, audio checks and final asset commit have not yet run. The MP4, SRT and manifest are not yet present in the public repository.
- Buffer history was checked before publishing: the last Instagram and YouTube video posts were sent on November 10, 2026, and no queued/sending post uses this new asset URL. Both channels are connected.
- No Instagram or YouTube post has been created for this asset. Both destinations remain HOLD until the final export passes every critical release gate.


## Render retry — 2026-11-13
- First daily render run [43427943599](https://github.com/amorder/AMORDER11/actions/runs/43427943599) failed in the Blender animation-export step. Blender rendered 100 frames for scene 1, but produced no MP4 at the expected path; the renderer stopped before independent MP4 validation, visual/motion checks, subtitle/audio/source gates and asset commit. No video was approved or published.
- Root cause is the Blender 5.0.1 FFMPEG animation writer not producing the expected MP4 in the hosted runner. The prior file-size-only gate was already replaced with media probing; this failure showed the file itself was absent.
- Fix committed in [42905ca](https://github.com/amorder/AMORDER11/commit/42905ca74cd421452d33c702c3bcadccd490a9eb): Blender now renders numbered PNG frames for each genuinely keyframed scene, verifies the exact frame count, then uses FFmpeg to encode and fully decode the H.264 scene MP4. The downstream ffprobe and final-file release gates remain mandatory and unchanged.
- A new render run will be triggered by the revision 2 storyboard. Instagram and YouTube remain HOLD until the new run completes all independent gates and commits the final assets.


## Caption-contract correction — 2026-11-13
- Retry run [43429892365](https://github.com/amorder/AMORDER11/actions/runs/43429892365) stopped before installing media tools or rendering. The regression test still expected Blender's old FFMPEG writer and rejected the new PNG-sequence pipeline; no media was produced and no release gates were bypassed.
- Test correction committed in [9cf34dc](https://github.com/amorder/AMORDER11/commit/9cf34dcfc3f8e4a1ba243ad56afae9f2c0db15fa): the static contract now requires exact PNG frame-count validation, FFmpeg H.264 scene encoding and a full scene-file decode.
- The latest secret-guard scan for the test update is pending. A revision 3 storyboard will trigger the next render attempt. No Instagram or YouTube post has been created.
