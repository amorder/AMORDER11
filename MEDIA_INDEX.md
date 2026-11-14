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
- [Render workflow run 43598788407](https://github.com/amorder/AMORDER11/actions/runs/43598788407) — running with the optimized Blender profile: 720x1280 base, 6 fps, 2 TAA samples, FFmpeg motion-compensated 1080x1920/30 fps delivery.
- [Public secret guard 43598788472](https://github.com/amorder/AMORDER11/actions/runs/43598788472) — passed.
- The expected MP4, SRT and manifest are not yet committed. The independent decode, visual/motion, subtitle/safe-zone, audio and source release gates have not yet passed. Instagram and YouTube remain HOLD; no Buffer video post has been created.
- The story is based on Alpaca's public order lifecycle documentation and contains no account, order or performance data.
