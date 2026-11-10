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

A revision 5 short render is currently running against the latest storyboard and updated regression check. The direct URLs are stable and will resolve to the latest committed file after that run finishes.

**Automatic release gate:** the owner has authorized automatic publication of public-safe AMORDER educational media. No per-video human signoff is required. Before Buffer publishing, the automation must still complete technical validation, full-file decode, representative-frame and motion checks, subtitle/safe-zone checks, narration/audio checks, source/rights/factual review, disclosure verification, and duplicate/status checks. Any failed or uncertain check keeps the affected destination on HOLD.

**Disclosure on every public video:** Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns.
