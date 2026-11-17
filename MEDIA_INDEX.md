# AMORDER public media library

This is the public share index for public-safe AMORDER educational media. Files linked here are stored in this repository and served from GitHub's raw-content HTTPS host for direct download and Buffer ingestion.

> **Public repository notice:** Every linked file is publicly accessible and can be copied. Only reviewed, public-safe media belongs here. Do not add broker records, credentials, private analytics, internal logs or confidential implementation details.

## November 9, 2026 — A Paper Fill Is Not a Result

### YouTube full episode

- **Runtime:** 4:37
- **Format:** 1920×1080, 30 fps, H.264 video + AAC audio
- **Captions:** burned into video; separate SRT available
- **File:** [Download MP4](https://raw.githubusercontent.com/amorder/AMORDER11/main/assets/amorder-ko-paper-case-study-youtube-2026-11-09.mp4)
- **Repository file:** [Browse on GitHub](https://github.com/amorder/AMORDER11/blob/main/assets/amorder-ko-paper-case-study-youtube-2026-11-09.mp4)
- **Subtitles:** [YouTube SRT](https://raw.githubusercontent.com/amorder/AMORDER11/main/subtitles/amorder-ko-paper-case-study-youtube-2026-11-09.srt)
- **Thumbnail:** [JPG](https://raw.githubusercontent.com/amorder/AMORDER11/main/assets/amorder-ko-paper-case-study-thumbnail-2026-11-09.jpg)

### Instagram vertical episode

- **Runtime:** 2:36
- **Format:** 1080×1920, 30 fps, H.264 video + AAC audio
- **Captions:** burned into video; separate SRT available
- **File:** [Download MP4](https://raw.githubusercontent.com/amorder/AMORDER11/main/assets/amorder-ko-paper-case-study-instagram-2026-11-09.mp4)
- **Repository file:** [Browse on GitHub](https://github.com/amorder/AMORDER11/blob/main/assets/amorder-ko-paper-case-study-instagram-2026-11-09.mp4)
- **Subtitles:** [Instagram SRT](https://raw.githubusercontent.com/amorder/AMORDER11/main/subtitles/amorder-ko-paper-case-study-instagram-2026-11-09.srt)

### Production sources and records

- [Public case-study record](https://github.com/amorder/AMORDER11/blob/main/posts/2026-11-09-when-clocks-disagree.md)
- [YouTube/Instagram episode storyboard](https://github.com/amorder/AMORDER11/blob/main/posts/2026-11-09-when-clocks-disagree.episode.json)
- [Short storyboard](https://github.com/amorder/AMORDER11/blob/main/posts/2026-11-09-when-clocks-disagree.short.json)
- [Render manifest and technical metadata](https://github.com/amorder/AMORDER11/blob/main/assets/amorder-ko-paper-case-study-manifest-2026-11-09.json)

### Release status

The long-form render workflow completed successfully and committed both long-form MP4s, subtitle sidecars, manifest and thumbnail. Its independent validation step confirmed H.264/AAC, the expected dimensions, captions and non-empty files.

The short MP4 and SRT remained present on main after the long-form render commit. The current files are available here:

- **Short trailer:** [Download MP4](https://raw.githubusercontent.com/amorder/AMORDER11/main/assets/amorder-ko-paper-case-study-2026-11-09.mp4)
- **Short subtitles:** [SRT](https://raw.githubusercontent.com/amorder/AMORDER11/main/subtitles/amorder-ko-paper-case-study-2026-11-09.srt)

The short-form visual revision 7 render (run 42849598771) and long-form visual revision 6 render (run 42849607033) both completed successfully on November 10. Both jobs passed their independent media validation and committed their generated assets. The files listed above are the current committed outputs.

**Automatic release gate:** the owner has authorized automatic publication of public-safe AMORDER educational media. No per-video human signoff is required. Before Buffer publishing, the automation must still complete technical validation, full-file decode, representative-frame and motion checks, subtitle/safe-zone checks, narration/audio checks, source/rights/factual review, disclosure verification, and duplicate/status checks. Any failed or uncertain check keeps the affected destination on HOLD.

**Disclosure on every public video:** Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns.

## Visual production upgrade — November 10, 2026

The AMORDER renderers now use a hybrid cinematic pipeline:

- **Blender Eevee PBR hero scenes:** graphite/anodised stage, additional edge softbox, subtle surface micro-detail, restrained emissive cyan/amber accents and scene-specific 3D compositions.
- **Animated motion design across the full edit:** FFmpeg overlays for tracking sweeps, moving signal nodes, orbital markers, pulsing data bars and pause/bracket motifs, chosen by the shot's visual key and rendered at 30 fps.
- **Editorial continuity:** overlays remain restrained and avoid the caption areas; scene cuts, narration, subtitles and paper-trading disclosure remain part of the existing production pipeline.
- **Performance-conscious rendering:** one Blender scene render per shot, with motion graphics composited at delivery frame rate. This avoids impractical per-frame full-resolution Blender renders in GitHub Actions.

### Source changes

- [Blender PBR scene builder](https://github.com/amorder/AMORDER11/blob/main/tools/blender_scenes.py)
- [Animated motion-graphics library](https://github.com/amorder/AMORDER11/blob/main/tools/motion_graphics.py)
- [Short-form renderer](https://github.com/amorder/AMORDER11/blob/main/tools/render_public_short.py)
- [Long-form renderer](https://github.com/amorder/AMORDER11/blob/main/tools/render_public_episode.py)
- [Regression checks](https://github.com/amorder/AMORDER11/blob/main/tools/test_caption_contract.py)

### Render status

- Short, visual revision 7: [GitHub Actions run](https://github.com/amorder/AMORDER11/actions/runs/42849598771) — completed successfully; independent MP4 validation and asset commit passed.
- Long-form, visual revision 6: [GitHub Actions run](https://github.com/amorder/AMORDER11/actions/runs/42849607033) — completed successfully; independent media validation and asset commit passed.
- The latest Buffer history confirms the November 9 vertical case-study asset was sent to Instagram and YouTube on November 10.

## November 13, 2026 — A Clean Chart Is Not Proof of Clean Data

- [Public content record](https://github.com/amorder/AMORDER11/blob/main/posts/2026-11-13-clean-chart-not-clean-data.md)
- [Short storyboard](https://github.com/amorder/AMORDER11/blob/main/posts/2026-11-13-clean-chart-not-clean-data.short.json)
- Topic: feed coverage, bar timestamps, pagination and corporate-action adjustment settings.
- [First render attempt](https://github.com/amorder/AMORDER11/actions/runs/43427943599) — failed during Blender animation export; no usable MP4 was produced.
- [Latest render attempt](https://github.com/amorder/AMORDER11/actions/runs/43430121736) — completed with conclusion **cancelled** at the 180-minute job limit while Blender was rendering scene 6; no final MP4 was produced.
- [Latest public secret guard](https://github.com/amorder/AMORDER11/actions/runs/43430121745) — passed.
- The MP4, SRT and manifest are not yet committed. Instagram and YouTube remain HOLD; no Buffer post has been created for this asset.
- Do not treat this storyboard or the cancelled render as a finished or published video. The full independent decode, visual/motion, subtitle/safe-zone, audio, source/rights, privacy and disclosure gates did not run and must pass before release.



## November 14, 2026 — Submitted Is Not Filled

- [Public content record](https://github.com/amorder/AMORDER11/blob/main/posts/2026-11-14-submitted-is-not-filled.md)
- [Short storyboard](https://github.com/amorder/AMORDER11/blob/main/posts/2026-11-14-submitted-is-not-filled.short.json)
- Topic: order lifecycle integrity — accepted, new, partially filled, pending cancel, canceled, rejected, expired and filled are distinct states.
- [Render workflow run 43598788407](https://github.com/amorder/AMORDER11/actions/runs/43598788407) — failed during Blender scene 3 with SIGSEGV before a usable scene MP4 was produced; no independent validation or asset commit.
- [Second render attempt 43623624656](https://github.com/amorder/AMORDER11/actions/runs/43623624656) — Blender/Kokoro rendering completed, but the technical validator rejected the probed average frame rate 91260/3043 (29.990141 fps) against the exact 30/1 contract; no independent release gate or asset commit.
- [Public secret guard 43598788472](https://github.com/amorder/AMORDER11/actions/runs/43598788472) — passed.
- The expected MP4, SRT and manifest are not yet committed. The independent decode, visual/motion, subtitle/safe-zone, audio and source release gates have not yet passed. Instagram and YouTube remain HOLD; no Buffer video post has been created.
- The story is based on Alpaca's public order lifecycle documentation and contains no account, order or performance data.


## November 15, 2026 — Paper Trading Has Blind Spots

- [Public content record](https://github.com/amorder/AMORDER11/blob/main/posts/2026-11-15-paper-trading-blind-spots.md)
- [Short storyboard](https://github.com/amorder/AMORDER11/blob/main/posts/2026-11-15-paper-trading-blind-spots.short.json)
- Topic: paper-simulation limitations — live exchange routing, market impact, latency, queue position, displayed liquidity and simulator assumptions.
- Primary source: [Alpaca — Paper Trading](https://docs.alpaca.markets/us/docs/paper-trading).
- [First render attempt 43716423585](https://github.com/amorder/AMORDER11/actions/runs/43716423585) — Blender/Kokoro render and technical H.264/AAC, 1080x1920, nominal 30 fps and full-decode checks passed; the independent validator failed because one SRT cue exceeded 120 characters.
- [Preflight attempt 43738542416](https://github.com/amorder/AMORDER11/actions/runs/43738542416) — caption-contract regression test failed because the newly added SRT assertion used an incorrect escaped newline; no render started. The assertion was corrected.
- [Corrected render 43738749524](https://github.com/amorder/AMORDER11/actions/runs/43738749524) — completed successfully. It committed the 94.094-second vertical MP4, SRT and manifest. Independent automated release score: 100/100.
- Exact export: 1080x1920, H.264/AAC, 30 fps, 35,030,485 bytes. Full-file decode passed. Six representative scene midpoints varied; sampled motion coverage 100%; zero black frames and zero frozen sections. SRT: 24 cues, maximum 96 characters; safe-zone subtitle margin 290 px. Audio mean -15.5 dB, peak -1.5 dB.
- **Non-blocking warning:** Blender 5.0.1 exited with SIGSEGV after the final scene MP4 was written. The output then passed ffprobe, full decode and every independent release gate. The crash report content was not available, so the precise Blender/EGL root cause remains undetermined; no unchanged rerun was made.
- [Latest secret guard 43804950026](https://github.com/amorder/AMORDER11/actions/runs/43804950026) — passed on the current main head.
- Instagram Reel: **sent** on November 16 at 01:27:58 UTC — [verified public Reel](https://www.instagram.com/reel/DfyK7krR9RR/).
- YouTube Short: **scheduled**, not published, for November 19 at 14:58 UTC (20:28 IST). No public URL exists until Buffer confirms sent.
- Buffer analytics were reviewed privately. The Instagram snapshot was early; prior comparable Reels had materially different runtimes/reporting ages, and the 156.82-second prior Reel had no metrics returned. No like-for-like retention conclusion is supported. Private reach/watch-time analytics are not stored in this public repository.
- No human watch-through or headphone/speaker audition is claimed.

## November 16, 2026 — When One Unit Is Too Much

- [Public content record](https://github.com/amorder/AMORDER11/blob/main/posts/2026-11-16-one-unit-too-much.md)
- [Short storyboard](https://github.com/amorder/AMORDER11/blob/main/posts/2026-11-16-one-unit-too-much.short.json)
- Topic: position-size arithmetic — planned loss, stop distance, point/tick value, permitted increments and the valid decision to pass when the minimum unit is too large.
- Sources: [CME Group — Proper Position Size](https://www.cmegroup.com/education/courses/trade-and-risk-management/proper-position-size) and [SEC Investor Bulletin — Stop Orders](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-15), updated August 18, 2026.
- Final asset: [1080x1920 H.264/AAC MP4](https://raw.githubusercontent.com/amorder/AMORDER11/main/assets/amorder-one-unit-too-much-2026-11-16.mp4), 65.257 seconds, 30 fps, 28,335,598 bytes; [SRT](https://raw.githubusercontent.com/amorder/AMORDER11/main/subtitles/amorder-one-unit-too-much-2026-11-16.srt); [manifest](https://github.com/amorder/AMORDER11/blob/main/assets/amorder-one-unit-too-much-manifest-2026-11-16.json).
- Blender evidence: 720x1280 at 12 fps, six distinct scenes, genuine keyframed camera/object motion, 100% sampled motion coverage over 65 frames; zero sampled black frames and zero frozen-run seconds.
- Audio and captions: mean -15.5 dB, peak -1.5 dB; 17 SRT cues, maximum 96 characters, 290 px subtitle bottom margin. Full decode and all independent automated release checks passed. Score 100/100. No human watch-through or headphone/speaker audition is claimed.
- [Final render workflow run 43901178823](https://github.com/amorder/AMORDER11/actions/runs/43901178823) — completed successfully, including render, independent technical/media validation and asset commit.
- Instagram Reel: **sent** November 17 at 08:58:59 IST; Buffer post `6afb4271afba1286ca70aee9`; [verified public Reel](https://www.instagram.com/reel/Df09whguCJd/).
- YouTube Short: **scheduled, not published**, for November 20 at 18:58 IST using Buffer custom scheduling; Buffer post `6afb426c9509e7b0ff1377a3`; no public URL until sent.
- Earlier render failures were resolved without weakening tests: the duplicated scene narration and standard-stop wording were corrected; the undefined `BASE` commit variable was fixed with regression coverage; Blender scene rendering and the independent manifest validator were raised to 12 fps. See the public content record for exact run IDs and repair history.
- Optional HyperFrames smoke test [43911598190](https://github.com/amorder/AMORDER11/actions/runs/43911598190) remains failed because its sample references the unavailable `aptos` font without an `@font-face` declaration. It was not used in this Blender production.
