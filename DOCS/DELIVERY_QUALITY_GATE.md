# AMORDER video delivery quality gate

Mark every item PASS, FAIL or N/A and record evidence. Any critical failure blocks release. A high score cannot override missing rights, incorrect facts, missing disclosure or absent owner authorization. AMORDER has standing owner authorization for automatic publication of public-safe educational content; per-asset human signoff is not required while that authorization remains active. Never claim a human watched or approved a file when only automated checks were performed.

**Current daily publisher scope (supersedes the legacy single-short scope):** produce two distinct 9:16 Shorts (each strictly under 160 seconds) and one approximately 10-minute full episode per daily cycle. Each Short has its own storyboard, render, captions, manifest and separate YouTube Shorts and Instagram Reels records. The full episode has two complete platform masters: 16:9 horizontal for YouTube and a fully recomposed 9:16 version retaining the same complete episode for Instagram Reels. Validate every master independently and record six separate destination outcomes (two Shorts × two platforms, plus the full episode × two platforms). Never treat a storyboard commit, workflow completion, scheduled Buffer item or a successful HOLD as a published video.

## A. Story and editorial
- [ ] For Shorts/Reels, encoded runtime is strictly under 160 seconds (2:40); target 105–145 seconds where the narrative supports it.
- [ ] The story is designed for a 9:16 vertical master, not a blind crop of landscape content.
- [ ] One clear viewer promise and central question.
- [ ] Opening is immediately engaging and factually honest.
- [ ] Every scene adds information, perspective, emotion or a deliberate pause.
- [ ] Runtime is earned; no repeated clips, filler or meaningless motion.
- [ ] Technical terms are explained for a global audience.
- [ ] Fact, estimate, forecast, opinion and interpretation are distinguished.
- [ ] The ending delivers the promised takeaway without false certainty.
- [ ] English voiceover, titles, overlays, subtitles and metadata are proofread.

## B. Sources and factual accuracy
- [ ] Claim ledger covers every material statistic, quote, date, causal claim and contested interpretation.
- [ ] Primary sources are preferred; important claims are corroborated where appropriate.
- [ ] Units, geography, dates and timeframes match the narration and graphics.
- [ ] Every citation opens and supports the exact claim attributed to it.
- [ ] Names, pronunciation and figures are manually checked.
- [ ] Data graphics use sourced values and clear units/legends, or are marked illustrative.
- [ ] No fabricated trades, returns, source links, events, interviews or testimonials.

## C. Visual craft and motion
- [ ] Timecoded shot list records purpose, framing, camera/object movement and source/rights status.
- [ ] First 1.5 seconds has a meaningful visual/action hook.
- [ ] Moving footage/animation coverage meets the Reel standard or an exception is documented.
- [ ] Blender scenes render at 12 fps with genuine keyframed camera and object motion; FFmpeg motion-compensated interpolation delivers constant 30 fps, and the manifest records both rates and motion coverage.
- [ ] No still-image zooms are counted as genuine moving-shot coverage.
- [ ] No asset is repeated merely to pad runtime.
- [ ] Footage does not falsely imply an event, place, time or person.
- [ ] Camera motion is purposeful, smooth and coherent.
- [ ] 2D/3D graphics are accurate, legible and labelled as schematic where necessary.
- [ ] Typography is readable on phone and television, with safe margins.
- [ ] Colour preserves shadow/highlight detail and looks consistent.
- [ ] AI/reconstructed visuals are disclosed where confusion is possible.
- [ ] Thumbnail/title are accurate and not sensationalised.

## D. Narration and sound
- [ ] Full narration is auditioned, not judged from a short sample.
- [ ] Delivery is natural, calm, intelligible and suited to an international English audience.
- [ ] Names, figures, abbreviations, rhythm and pauses are reviewed.
- [ ] Music never masks narration.
- [ ] Music, effects, Foley and voices have documented rights.
- [ ] No clipping, pops, clicks, hum, distortion, missing audio or sync issues.
- [ ] Audio is listened to on headphones and ordinary speakers.
- [ ] Stems are retained where practical.

## E. Rights, privacy and disclosure
- [ ] Asset log records creator, source URL, licence/version, attribution, acquisition date and permitted use.
- [ ] Fonts, music, voice, footage, AI models and generated outputs are cleared separately.
- [ ] Contributor consent/releases are retained where required.
- [ ] No secrets, credentials, private broker data, trade records or unpublished research appear in the asset or logs.
- [ ] Simulated trading is clearly labelled as paper trading, not live-money performance or investment advice.
- [ ] No buy/sell calls, price targets, fabricated metrics or return promises.

## F. Technical export
- [ ] Correct aspect ratio, resolution, FPS and duration for the intended destination.
- [ ] ffprobe confirms expected video/audio streams, codec and duration.
- [ ] Full media decode completes without corruption.
- [ ] No black/frozen frames, flashes, missing shots or broken transitions.
- [ ] Subtitles are synced, spelled correctly and within safe areas.
- [ ] Audio peaks/loudness are checked against the actual delivery target.
- [ ] Cover art and platform metadata match the exported video.

## G. Release authority
- [ ] The exact exported file completes a full decode; representative frames and frame-to-frame motion are inspected automatically; black/frozen/blank sections and subtitle safe zones are checked.
- [ ] Audio stream, loudness, clipping, sync, narration/subtitle agreement and duration are checked automatically; missing or ambiguous audio blocks release.
- [ ] Sources, rights, disclosure and factual claims are checked against approved primary sources and public-safe records.
- [ ] Owner standing authorization for automatic publication is active; no per-asset human signoff is required under that authorization.
- [ ] Only the existing authorized AMORDER automation and connected Buffer integration publish.
- [ ] Remote post ID/permalink/status is re-read and recorded before calling it published.

**Release decision:** PASS only when all critical sections pass and the scorecard in the Reel standard is at least 85/100. Otherwise: HOLD, document the failure and revise.


## G. Long-form episode and six-destination release checks
- [ ] Two distinct daily Shorts exist, each with its own topic, hook, storyboard, render, SRT and manifest; neither is a duplicate or a simple unedited cut of the other.
- [ ] Each Short is independently validated as 9:16, 1080x1920, H.264/AAC, constant 30 fps and strictly under 160 seconds.
- [ ] One complete long-form episode exists, with an editorially earned target of approximately 10 minutes (normally 8–12 minutes where supported; no padding).
- [ ] The YouTube episode master is horizontal 16:9; the Instagram master is fully recomposed 9:16 and retains the complete episode's substantive narration, examples and conclusion.
- [ ] Both episode masters have independently verified full duration, expected dimensions/aspect ratio, H.264/AAC, full decode, chapter timestamps, synced burned captions and SRT, thumbnail where applicable, motion, audio and source/rights evidence.
- [ ] Every one of the four platform masters has its own manifest and passing critical checks; no aggregate score can hide a failed export.
- [ ] Buffer duplicate checks and final status verification are completed separately for all six destinations: Short 1 on YouTube and Instagram; Short 2 on YouTube and Instagram; complete episode on YouTube and Instagram.
- [ ] A destination is counted as published only when Buffer reports sent and a verified public URL is available. Scheduled, sending, error, missing, ambiguous or HOLD states are not published.
- [ ] When compute, a source, a credential, platform support or a required validation is unavailable, hold the affected asset/destination and record the exact blocker. Never lower a gate to meet the daily count.
