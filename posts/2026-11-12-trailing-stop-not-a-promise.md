# A Trailing Stop Is Not a Price Promise

- **Publication date:** 2026-11-12
- **Language / audience:** English / global
- **Channels:** X (separate text-first companion), Instagram Reels, YouTube Shorts
- **Topic:** Why a trailing-stop trigger is not a guaranteed execution price

## Story and production
A concise explanation of the high-water mark, the one-way trailing rule, market-order execution, gaps and regular-hours limitations. No stock-specific call, trade result, account information or performance claim is used.

- **Opening hook:** "A trailing stop can trigger and still fill at a different price."
- **Scene design:** six distinct Blender Eevee PBR setups: idea, timestamp, source, gaps, stand-down and brand.
- **Motion:** keyframed camera and object animation in every Blender scene; FFmpeg motion-compensated delivery at 30 fps.
- **Target runtime:** 105-145 seconds; hard maximum strictly below 159 seconds (2:39).
- **Delivery:** 1080x1920, 9:16, 30 fps, H.264 MP4, AAC English narration, burned captions and SRT sidecar.
- **Voice:** Kokoro-82M ONNX, af_heart; restrained original sound design only.
- **Editorial note:** this explainer distinguishes a trigger condition from an execution price and includes the broker-specific regular-hours caveat without implying that every broker follows the same rules.
- **Evidence-based improvement:** the latest successful vertical asset (2026-11-09) ran 156.82 seconds, close to the 159-second hard cap. This cut targets 105-145 seconds, opens with the trigger-versus-fill distinction within the first sentence, and uses six scene setups. The 2026-11-07 and 2026-11-06 Buffer assets were 22.937 and 21.859 seconds respectively; matching technical manifests were not present in the public asset index, so no unsupported motion-coverage or audience-performance comparison is claimed.

## YouTube
**Title:** A Trailing Stop Is Not a Price Promise | AMORDER #Shorts

A trailing stop can trigger and still fill at a different price. This short explains the high-water mark, why the stop can ratchet upward but not downward, and why gaps, market hours and execution rules matter.

Sources:
SEC Investor Bulletin: https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-15
Alpaca order documentation: https://docs.alpaca.markets/us/docs/orders-at-alpaca

Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns.

#AMORDER #RiskEducation #Shorts

## Instagram
A trailing stop is an order rule, not a guaranteed execution price. Learn what the high-water mark does, why the stop can ratchet upward, and how gaps or market hours can change the result.

Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns.

#AMORDER #RiskEducation

**Alt text:** Six cinematic graphite-studio 3D scenes use glass, metal, a clock-like high-water marker and a broken signal line to explain how a trailing stop moves, triggers and may fill at a different price.

## X text-first companion
**Copy sent:**
"Trailing stops can follow a favorable move, but the trigger is not a guaranteed fill. Fast markets and gaps can change execution. Know your broker's rules. Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns. #AMORDER"

- **Buffer post ID:** 6af4aefd24e81672d7964a7b
- **Public URL:** https://x.com/2118017267829190656/status/2120678973537398850
- **Sent at:** 2026-11-12T00:44:02.459Z
- **Verified status:** sent (re-read from Buffer)
- This matching text-first post was queued on 2026-11-11 and sent on 2026-11-12; no duplicate was created in this cycle.

## Sources
- [SEC Investor Bulletin: Stop, Stop-Limit, and Trailing Stop Orders](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-15)
- [Alpaca: Placing Orders](https://docs.alpaca.markets/us/docs/orders-at-alpaca)

## Disclosure
Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns.

## Assets
- Storyboard: `posts/2026-11-12-trailing-stop-not-a-promise.short.json`
- Expected MP4: `assets/amorder-trailing-stop-not-a-promise-2026-11-12.mp4` (pending render)
- Expected SRT: `subtitles/amorder-trailing-stop-not-a-promise-2026-11-12.srt`
- Expected manifest: `assets/amorder-trailing-stop-not-a-promise-manifest-2026-11-12.json`

## Release gates
- [ ] Blender keyframed render completed; at least five distinct visual setups
- [ ] 1080x1920, 30 fps, H.264/AAC; runtime below 159 seconds
- [ ] Public HTTPS MP4 fetch returns non-empty MP4 bytes
- [ ] Full FFmpeg decode; representative-frame variation; no black/frozen sections
- [ ] Safe-zone and subtitle readability checks; SRT text/timing matches narration
- [ ] Audio stream, loudness and clipping checks pass
- [ ] Sources, rights, privacy and disclosure checks pass
- [ ] Automated quality score at least 85/100; no critical gate failed

## Publishing record
| Destination | Buffer post ID | Public URL | Status |
|---|---|---|---|
| X text-first | 6af4aefd24e81672d7964a7b | https://x.com/2118017267829190656/status/2120678973537398850 | sent |
| Instagram Reel | — | — | held_render_failed |
| YouTube Short | — | — | held_render_failed |

## Render status — 2026-11-12 12:53 ET
- Public render workflow run 43260259476 is still in progress at the Blender scene-render step. Caption-contract regression, media-tool installation and Kokoro model download passed.
- Independent MP4 validation, visual/subtitle/audio/source release gates and public asset commit have not started/completed.
- The MP4, SRT and manifest are not yet present in the public repository. Instagram and YouTube remain HOLD; no video Buffer post has been created.
- The latest private release poll completed successfully but logged "Waiting: vertical video render is not complete yet." It created no video posts.
- No human watch-through is claimed; only automated gates will be used under the standing authorization.


## Render watchdog checkpoint — 2026-11-12 13:05 ET
- GitHub still reports render run 43260259476 as in_progress more than 90 minutes after it started at 16:35:04Z, even though the job declares timeout-minutes: 90. The Blender render step remains in progress; independent MP4 validation, visual/subtitle/audio/source gates and asset commit remain pending.
- GitHub has not exposed the in-progress job log (the logs endpoint returned BlobNotFound). This is an ambiguous render state, not a successful render or a verified failure.
- Do not cancel, duplicate, rerun or publish while the original run remains active. Instagram and YouTube stay HOLD; no video Buffer posts exist.


## Render optimization and rerun — 2026-11-12 13:26 ET
- The first render attempt (run 43260259476) ended at the workflow's 90-minute job timeout. Its log shows 33 Blender output frames in approximately 86 minutes; the MP4 validation, independent release gates and asset commit were skipped. No media from that run is approved.
- Verified bottleneck: full 1080x1920 Blender Eevee rendering at 64 TAA samples on the hosted CPU runner. The renderer was optimized without replacing Blender scenes or weakening any release gate: each scene still uses genuine keyframed PBR camera/object animation at 12 fps, with depth of field and motion blur retained. Blender now renders at 720x1280 with 4 TAA samples; FFmpeg motion-compensates to 30 fps and Lanczos-upscales to the required 1080x1920 delivery.
- The render job timeout is now 180 minutes. The final delivery remains H.264/AAC, under 159 seconds, with burned English captions and an SRT sidecar. All full-decode, motion, black/frozen-frame, safe-zone, subtitle, audio, source/rights, privacy and disclosure gates remain mandatory.
- Focused public renderer/test commits: `bf760b7`, `913248e`, `4521880`, `d6a7b38`, `3767ea6`; storyboard revision 3 commit: `ad8d4c7`.
- New render run [43279634075](https://github.com/amorder/AMORDER11/actions/runs/43279634075) started from the revision 3 storyboard. Caption-contract regression, media-tool installation and Kokoro model download passed; the Blender scene-render step is currently in progress. The independent MP4 and release gates have not yet run.
- Latest public secret-guard run [43279634128](https://github.com/amorder/AMORDER11/actions/runs/43279634128) passed.
- The MP4, SRT and manifest are still absent from the public repository. Instagram and YouTube remain HOLD; no video Buffer post has been created. The X text-first companion remains verified as sent. No human watch-through is claimed.


## Final render outcome — 2026-11-13
- Render run [43279634075](https://github.com/amorder/AMORDER11/actions/runs/43279634075) failed at the first Blender scene export check. The log shows 80 frames rendered, but the scene MP4 did not meet the renderer's arbitrary 100 KB minimum-size check. Final MP4 validation, independent release gates and asset commit were skipped.
- Earlier run [43260259476](https://github.com/amorder/AMORDER11/actions/runs/43260259476) was cancelled after the hosted runner timeout. Neither run produced an approved public video.
- Renderer correction: commits [7b510e2](https://github.com/amorder/AMORDER11/commit/7b510e28e7a00089c983dc417a8507e847366969) and [cb39236](https://github.com/amorder/AMORDER11/commit/cb39236fe4bb313703353afe3efcc3f25d159e3a) replace the arbitrary per-scene size gate with ffprobe codec, dimensions, frame-rate and duration checks plus a full decode of every scene clip. The final deliverable still has its original size, duration, decode, motion, audio, subtitle, source, rights, privacy and disclosure gates.
- This November 12 storyboard remains unpublished. No Instagram or YouTube video post was created. The separate X text-first companion remains verified as sent.
