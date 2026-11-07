# Data First. Decisions Second. — 2026-11-07

- **Publication date:** 2026-11-07
- **Intended channels:** Instagram Reels; YouTube Shorts
- **Audience and language:** Global audience; English only
- **Topic:** Data-quality checks before forming a market view
- **Format target:** 9:16 vertical, 1080×1920, 30 fps, H.264 MP4 with AAC narration, 15–45 seconds
- **Creative approach:** Cinematic Blender 3D scenes, spacious typography, concise overlays, smooth FFmpeg camera motion and a calm English narration.
- **Voiceover model:** Kokoro-82M ONNX, voice `af_heart`; no external TTS API or credential.
- **Open-source production stack:** Blender, Kokoro ONNX, FFmpeg/ffprobe, Pillow. Motion-design QA reference: [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft).
- **Sources:** [Kokoro ONNX model](https://huggingface.co/onnx-community/Kokoro-82M-v1.0-ONNX), [Kokoro ONNX runtime](https://github.com/thewh1teagle/kokoro-onnx), [Blender headless rendering](https://docs.blender.org/manual/en/latest/advanced/command_line/render.html), [FFmpeg documentation](https://ffmpeg.org/documentation.html).
- **Factual claim review:** General educational process statements only; no symbols, market data, broker data, trade examples, price targets, or performance claims.

## Voiceover script

> A chart can look perfect and still be wrong. Start with the timestamp. Is the data fresh? Check for missing bars and gaps. Know what your data source actually covers. If the information is stale, incomplete, or unclear, stop. No reliable data means no trade. AMORDER. Data first. Decisions second.

## On-screen story

| Scene | Headline | Supporting line | 3D visual |
|---|---|---|---|
| 1 | A CHART CAN LOOK RIGHT | And still be wrong. | Evidence lens and data tiles |
| 2 | CHECK THE TIMESTAMP | Is the data fresh? | Precision clock |
| 3 | LOOK FOR MISSING DATA | Gaps break context. | Modular data grid with a visible gap |
| 4 | KNOW YOUR SOURCE | Understand its coverage. | Source streams converging through a gateway |
| 5 | NO TRUST. NO TRADE. | Stale or incomplete? Stand aside. | Shield and pause mark |
| 6 | DATA FIRST. DECISIONS SECOND. | AMORDER / Paper-trading education. | Abstract orbital brand sculpture |

## Instagram Reel caption

A clean-looking chart is not proof of clean data.

Check the timestamp. Look for missing bars. Understand what your data source actually covers. When the information is stale or incomplete, step aside.

Data first. Decisions second.

Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns.

#AMORDER #DataQuality #PaperTrading #RiskDiscipline #TradingEducation

## YouTube Shorts metadata

- **Title:** Data First. Decisions Second. | AMORDER #Shorts
- **Description:** A practical reminder for anyone studying markets: check timestamps, look for missing data, understand your feed's coverage, and avoid acting on information you cannot trust.

  Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns.

  #AMORDER #DataQuality #PaperTrading #Shorts

## Disclosure

Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns.

## Asset and publishing record

- **Storyboard:** [2026-11-07-data-before-decisions.short.json](2026-11-07-data-before-decisions.short.json)
- **Renderer:** [tools/render_public_short.py](../tools/render_public_short.py)
- **Blender scene generator:** [tools/blender_scenes.py](../tools/blender_scenes.py)
- **Render workflow:** [.github/workflows/render-public-short.yml](../.github/workflows/render-public-short.yml)
- **Target asset:** `assets/amorder-data-first-2026-11-07.mp4`
- **Public asset URL:** https://raw.githubusercontent.com/amorder/AMORDER11/main/assets/amorder-data-first-2026-11-07.mp4
- **Render status:** pending_render — do not publish until GitHub Actions, ffprobe validation, and public HTTPS asset availability are confirmed.

### Instagram Reels
- **Buffer post ID:** not submitted
- **Status:** draft / pending approved MP4
- **Public URL:** not available

### YouTube Shorts
- **Buffer post ID:** not submitted
- **Status:** draft / pending approved MP4
- **Public URL:** not available
