# Paper Trading Has Blind Spots

- **Publication date:** 2026-11-15
- **Language / audience:** English / global
- **Channels:** Instagram Reels and YouTube Shorts
- **Topic:** What paper-trading simulations omit and why a simulated fill is not a forecast of live execution

## Viewer promise
A paper fill can be useful for testing code and process, but it does not reproduce every condition of live execution. This explainer identifies the limitations in Alpaca's published paper-trading specification and gives viewers a practical way to document them.

## Editorial and production
- **Opening hook:** "A paper-trading fill can look convincing. But it is not proof that a live order would have filled the same way. The gap matters."
- **Visual direction:** six original Blender Eevee PBR setups in a cinematic graphite studio; physically based glass and metal, motivated softbox lighting, restrained cyan/amber accents and clear negative space
- **Motion:** genuine keyframed camera and object movement in each Blender scene; FFmpeg motion-compensated finishing and scene-specific animated overlays
- **Delivery:** 1080x1920, 9:16, constant 30 fps, H.264 MP4, AAC English narration, burned English captions and SRT sidecar
- **Runtime:** 94.094 seconds
- **Voice:** Kokoro-82M ONNX, af_heart; calm international English
- **Audio:** no copyrighted music or third-party sound effects; original restrained sound design only
- **Visual safety:** all graphics are schematic; no market values, broker UI, real orders or trading account data

## Claim ledger and primary source
All material factual claims are supported by Alpaca's official paper-trading documentation:
- The paper environment does not route orders to a live exchange; it simulates fills using real-time quotes.
- Published limitations include market impact, information leakage, latency-related slippage, queue position for non-marketable limit orders, price improvement, regulatory fees and dividends.
- Paper order quantity is not checked against NBBO quantities; a simulated fill can exceed displayed available liquidity.
- Other simulators may use different fill prices, liquidity assumptions, return methodologies and market data sources.

Source: [Alpaca — Paper Trading](https://docs.alpaca.markets/us/docs/paper-trading), accessed 2026-11-15.

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
- Storyboard: [posts/2026-11-15-paper-trading-blind-spots.short.json](https://github.com/amorder/AMORDER11/blob/main/posts/2026-11-15-paper-trading-blind-spots.short.json)
- MP4: [download vertical master](https://raw.githubusercontent.com/amorder/AMORDER11/main/assets/amorder-paper-trading-blind-spots-2026-11-15.mp4)
- SRT: [subtitle sidecar](https://raw.githubusercontent.com/amorder/AMORDER11/main/subtitles/amorder-paper-trading-blind-spots-2026-11-15.srt)
- Manifest: [technical and release evidence](https://github.com/amorder/AMORDER11/blob/main/assets/amorder-paper-trading-blind-spots-manifest-2026-11-15.json)

## Automated release evidence
- [x] GitHub Actions render run [43738749524](https://github.com/amorder/AMORDER11/actions/runs/43738749524) completed successfully and committed the MP4, SRT and manifest
- [x] 1080x1920, 9:16, H.264/AAC, constant 30 fps; 94.094 seconds
- [x] Full FFmpeg decode and ffprobe verification passed
- [x] Six scene midpoint frames varied; 100% sampled motion coverage; zero black frames and zero frozen sections
- [x] English SRT matches narration; 24 cues, maximum 96 characters; subtitle safe-zone margin 290 px
- [x] Audio stream and measured levels passed: mean -15.5 dB, peak -1.5 dB
- [x] Sources, rights, public-safety and required disclosure checks passed
- [x] Independent automated release score 100/100 (threshold 85)
- No human watch-through or headphone/speaker audition is claimed

**Non-blocking renderer warning:** Blender 5.0.1 exited with SIGSEGV after the final scene MP4 had been written. The output file then passed ffprobe, full decode and every independent release gate. The crash report contents were not available, so the precise Blender/EGL root cause is undetermined. No unchanged rerun was made after the exact output passed.

## Buffer publication record

| Destination | Status | Public URL |
|---|---|---|
| Instagram Reel | **sent** — 2026-11-16 01:27:58 UTC | [View Reel](https://www.instagram.com/reel/DfyK7krR9RR/) |
| YouTube Short | **scheduled** — 2026-11-19 14:58 UTC (20:28 IST) | Not available until sent |

The Instagram post is verified as sent. The YouTube item remains scheduled, not published. No duplicate upload was created.

## Analytics and comparison
Buffer analytics were reviewed. The Instagram snapshot was early and the available prior Reels had materially different runtimes/reporting ages; the previous 156.82-second Reel had no metrics returned. No like-for-like retention comparison is supportable. YouTube has no current metrics because its November 15 item is still scheduled. Private reach/watch-time analytics are not stored in this public repository.
