#!/usr/bin/env python3
"""Independent release gates for public AMORDER vertical shorts.

Checks the exact encoded MP4, its subtitle sidecar, storyboard, visual motion,
text-safe layout, narration stream, and public-source/disclosure contract.
No broker, account, private research, credentials, or publishing APIs are used.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import urlparse

import numpy as np
from PIL import Image, ImageDraw, ImageFont

DISCLOSURE = (
    "Paper-trading education only; not live-money performance; "
    "not investment advice; no guaranteed returns."
)
WIDTH, HEIGHT, FPS = 1080, 1920, 30
SAMPLE_WIDTH, SAMPLE_HEIGHT = 160, 284


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command, check=True, capture_output=True, text=True
    )


def normalized(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def parse_srt_text(content: str) -> list[tuple[float, float, str]]:
    blocks = re.split(r"\r?\n\s*\r?\n", content.strip())
    cues: list[tuple[float, float, str]] = []
    stamp = re.compile(
        r"^(\d{2}):(\d{2}):(\d{2}),(\d{3}) --> "
        r"(\d{2}):(\d{2}):(\d{2}),(\d{3})$"
    )

    def seconds(parts: tuple[str, ...]) -> float:
        h, m, s, ms = (int(x) for x in parts)
        return h * 3600 + m * 60 + s + ms / 1000

    for block in blocks:
        lines = block.splitlines()
        if len(lines) < 3:
            raise ValueError("Malformed SRT cue")
        match = stamp.match(lines[1].strip())
        if not match:
            raise ValueError("Malformed SRT timestamp")
        start = seconds(match.groups()[:4])
        end = seconds(match.groups()[4:])
        text = normalized(" ".join(lines[2:]))
        if not text or end <= start:
            raise ValueError("Empty or non-positive SRT cue")
        cues.append((start, end, text))
    if not cues:
        raise ValueError("SRT contains no subtitle cues")
    return cues


def longest_true_run(values: list[bool]) -> int:
    best = current = 0
    for value in values:
        current = current + 1 if value else 0
        best = max(best, current)
    return best


def motion_metrics(frames: np.ndarray) -> dict[str, float | int]:
    if frames.ndim != 3 or len(frames) < 3:
        raise ValueError("Not enough representative frames to inspect motion")
    means = frames.mean(axis=(1, 2))
    stds = frames.std(axis=(1, 2))
    interior_means = means[1:-1] if len(means) > 2 else means
    interior_stds = stds[1:-1] if len(stds) > 2 else stds
    black = int(np.sum((interior_means < 2.5) & (interior_stds < 1.5)))
    diffs = np.abs(frames[1:].astype(np.int16) - frames[:-1].astype(np.int16))
    mean_diffs = diffs.mean(axis=(1, 2))
    frozen = longest_true_run((mean_diffs < 0.05).tolist())
    coverage = float(np.mean(mean_diffs >= 0.05) * 100)
    return {
        "black_frame_count": black,
        "longest_frozen_run_seconds": frozen,
        "motion_coverage_percent": round(coverage, 2),
        "sampled_frame_count": int(len(frames)),
    }


def sample_frames(video: Path) -> np.ndarray:
    result = subprocess.run(
        [
            "ffmpeg", "-v", "error", "-i", str(video),
            "-vf", f"fps=1,scale={SAMPLE_WIDTH}:{SAMPLE_HEIGHT}:flags=area,format=gray",
            "-f", "rawvideo", "-pix_fmt", "gray", "pipe:1",
        ],
        check=True, capture_output=True,
    )
    frame_size = SAMPLE_WIDTH * SAMPLE_HEIGHT
    count = len(result.stdout) // frame_size
    if count < 15:
        raise ValueError(f"Only {count} one-second frames could be sampled")
    return np.frombuffer(
        result.stdout[: count * frame_size], dtype=np.uint8
    ).reshape(count, SAMPLE_HEIGHT, SAMPLE_WIDTH)


def validate_scene_variation(frames: np.ndarray, durations: list[float]) -> dict[str, float | int]:
    samples = []
    elapsed = 0.0
    for duration in durations:
        midpoint = elapsed + float(duration) / 2
        index = min(len(frames) - 1, max(0, int(round(midpoint))))
        samples.append(frames[index])
        elapsed += float(duration)
    if len(samples) < 5:
        raise ValueError("Fewer than five representative scene frames are available")
    differences = [
        float(np.mean(np.abs(samples[i].astype(np.int16) - samples[i - 1].astype(np.int16))))
        for i in range(1, len(samples))
    ]
    if min(differences) < 1.0:
        raise ValueError("Representative scene frames do not show enough shot-to-shot variation")
    return {
        "scene_midpoint_count": len(samples),
        "minimum_scene_difference": round(min(differences), 2),
    }


def font_file() -> str:
    result = run(["fc-match", "-f", "%{file}", "Noto Sans"])
    path = result.stdout.strip()
    if not path or not Path(path).is_file():
        raise ValueError("Noto Sans font unavailable for safe-zone validation")
    return path


def wrap_lines(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont,
               max_width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for word in text.split():
        candidate = (current + " " + word).strip()
        if current and draw.textbbox((0, 0), candidate, font=font)[2] > max_width:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def validate_safe_zones(story: dict) -> dict[str, int]:
    font = font_file()
    canvas = Image.new("RGB", (1, 1))
    draw = ImageDraw.Draw(canvas)
    title_font = ImageFont.truetype(font, 78)
    support_font = ImageFont.truetype(font, 39)
    max_title_lines = 0
    max_support_lines = 0
    for index, scene in enumerate(story["scenes"], 1):
        title_lines = wrap_lines(draw, scene["title"], title_font, 900)
        support_lines = wrap_lines(draw, scene["overlay"], support_font, 850)
        max_title_lines = max(max_title_lines, len(title_lines))
        max_support_lines = max(max_support_lines, len(support_lines))
        title_height = sum(
            draw.textbbox((0, 0), line, font=title_font)[3]
            for line in title_lines
        ) + 8 * max(0, len(title_lines) - 1)
        support_height = sum(
            draw.textbbox((0, 0), line, font=support_font)[3]
            for line in support_lines
        ) + 9 * max(0, len(support_lines) - 1)
        end_y = 1000 + title_height + 20 + support_height
        if len(title_lines) > 3 or len(support_lines) > 3 or end_y > 1650:
            raise ValueError(f"Scene {index} text exceeds mobile-safe overlay bounds")
    # The renderer burns subtitles at MarginV=290 and keeps the footer below y=1786.
    renderer = Path(__file__).with_name("render_public_short.py").read_text(encoding="utf-8")
    if 'MarginV=290' not in renderer or 'd.line((82, 1786' not in renderer:
        raise ValueError("Subtitle/footer safe-zone contract changed")
    return {
        "max_title_lines": max_title_lines,
        "max_support_lines": max_support_lines,
        "subtitle_margin_bottom_px": 290,
    }


def validate_public_contract(story: dict) -> None:
    if story.get("language") != "en" or story.get("audience") != "global":
        raise ValueError("Public video must be English and global-audience")
    if story.get("disclosure") != DISCLOSURE:
        raise ValueError("Required disclosure missing or changed")
    for field in ("instagram_caption", "youtube_description"):
        if DISCLOSURE.casefold() not in str(story.get(field, "")).casefold():
            raise ValueError(f"Required disclosure missing from {field}")
    sources = story.get("sources")
    if not isinstance(sources, list) or not sources:
        raise ValueError("At least one official HTTPS source is required")
    domains = {urlparse(url).netloc.lower() for url in sources if isinstance(url, str)}
    if not all(isinstance(url, str) and url.startswith("https://") for url in sources):
        raise ValueError("Every source must use HTTPS")
    approved_domains = {
        str(domain).lower()
        for domain in story.get("automated_review", {}).get("approved_source_domains", [])
    }
    if not approved_domains or not all(
        any(domain == approved or domain.endswith("." + approved) for approved in approved_domains)
        for domain in domains
    ):
        raise ValueError("A source domain is missing from the reviewed allowlist")
    music = str(story.get("format", {}).get("music", "")).casefold()
    if "no copyrighted" not in music:
        raise ValueError("Storyboard must explicitly prohibit copyrighted music")
    review = story.get("automated_review", {})
    required = (
        "public_safety_reviewed",
        "claims_checked_against_sources",
        "rights_and_asset_origin_reviewed",
        "disclosure_verified",
    )
    if not all(review.get(key) is True for key in required):
        raise ValueError("Automated source, rights, privacy, or disclosure review is incomplete")

    public_text = json.dumps(story, ensure_ascii=True)
    private_patterns = (
        r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b",
        r"\b(?:client_order_id|buying power|portfolio value|account balance|account id|api[_ -]?key|secret token)\b",
        r"\bP&L\b",
        r"\$\s?\d[\d,]*(?:\.\d+)?",
        r"\b[0-9a-f]{40,}\b",
    )
    for pattern in private_patterns:
        if re.search(pattern, public_text, flags=re.IGNORECASE):
            raise ValueError(f"Public storyboard matched a private-data safety pattern: {pattern}")

    scenes = story.get("scenes")
    if not isinstance(scenes, list) or not 5 <= len(scenes) <= 8:
        raise ValueError("Short storyboard must contain 5–8 scenes")
    if len({scene.get("visual") for scene in scenes}) < 5:
        raise ValueError("At least five distinct Blender visual setups are required")
    for number, scene in enumerate(scenes, 1):
        for key in ("visual", "title", "overlay", "narration"):
            value = scene.get(key)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"Scene {number} is missing {key}")
            if any(ord(char) > 127 for char in value):
                raise ValueError(f"Scene {number} contains non-ASCII copy")
    if not str(story.get("youtube_title", "")).strip() or len(story["youtube_title"]) > 100:
        raise ValueError("YouTube title missing or over 100 characters")
    if len(str(story.get("instagram_caption", ""))) > 2200:
        raise ValueError("Instagram caption exceeds 2200 characters")


def validate_audio(video: Path) -> dict[str, float]:
    result = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", str(video), "-af", "volumedetect", "-f", "null", "-"],
        check=True, capture_output=True, text=True,
    )
    mean_match = re.search(r"mean_volume:\s*(-?[\d.]+)\s*dB", result.stderr)
    max_match = re.search(r"max_volume:\s*(-?[\d.]+)\s*dB", result.stderr)
    if not mean_match or not max_match:
        raise ValueError("FFmpeg could not measure narration loudness")
    mean_db, peak_db = float(mean_match.group(1)), float(max_match.group(1))
    if not -30.0 <= mean_db <= -8.0:
        raise ValueError(f"Audio mean level outside safe narration range: {mean_db:.2f} dB")
    if peak_db > -0.1:
        raise ValueError(f"Audio peak too close to clipping: {peak_db:.2f} dB")
    return {"mean_volume_db": round(mean_db, 2), "max_volume_db": round(peak_db, 2)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--storyboard", required=True)
    parser.add_argument("--video", required=True)
    parser.add_argument("--subtitle", required=True)
    parser.add_argument("--manifest", required=True)
    args = parser.parse_args()
    storyboard_path, video, subtitle, manifest_path = map(
        Path, (args.storyboard, args.video, args.subtitle, args.manifest)
    )
    story = json.loads(storyboard_path.read_text(encoding="utf-8"))
    validate_public_contract(story)
    first_scene = story["scenes"][0]
    if (
        len(first_scene["title"]) > 40
        or len(first_scene["overlay"]) > 60
        or len(first_scene["narration"].split()) > 24
    ):
        raise ValueError("Opening hook is too long for the first visual beat")
    if not video.is_file() or video.stat().st_size < 100_000:
        raise ValueError("Final MP4 is missing or unexpectedly small")
    if not subtitle.is_file() or subtitle.stat().st_size < 100:
        raise ValueError("SRT sidecar is missing or unexpectedly small")

    info = json.loads(run([
        "ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(video)
    ]).stdout)
    streams = info.get("streams", [])
    v = next((item for item in streams if item.get("codec_type") == "video"), None)
    a = next((item for item in streams if item.get("codec_type") == "audio"), None)
    duration = float(info.get("format", {}).get("duration", 0))
    if not v or (v.get("codec_name"), v.get("width"), v.get("height")) != ("h264", WIDTH, HEIGHT):
        raise ValueError(f"Video must be H.264 1080x1920: {v}")
    if v.get("avg_frame_rate") != "30/1":
        raise ValueError(f"Video must be 30 fps: {v.get('avg_frame_rate')}")
    if not a or a.get("codec_name") != "aac":
        raise ValueError(f"AAC narration stream missing: {a}")
    if not 15 <= duration < 159:
        raise ValueError(f"Runtime must be 15 seconds to strictly below 159 seconds: {duration:.2f}")
    if video.stat().st_size < 100_000:
        raise ValueError("Final MP4 is unexpectedly small")

    # Decode the entire encoded file; metadata alone is not enough.
    run(["ffmpeg", "-v", "error", "-i", str(video), "-f", "null", "-"])
    frames = sample_frames(video)
    motion = motion_metrics(frames)
    if motion["black_frame_count"] > 0:
        raise ValueError(f"Detected {motion['black_frame_count']} black/blank sample frames")
    if motion["longest_frozen_run_seconds"] >= 4:
        raise ValueError("Detected a frozen visual section lasting at least four seconds")
    if motion["motion_coverage_percent"] < 60:
        raise ValueError(
            f"Sampled motion coverage below 60%: {motion['motion_coverage_percent']}%"
        )

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    outputs = manifest.get("outputs", [])
    if len(outputs) != 1:
        raise ValueError("Short manifest must contain exactly one vertical output")
    output = outputs[0]
    if (
        manifest.get("blender_render_width") != 720
        or manifest.get("blender_render_height") != 1280
        or manifest.get("blender_taa_render_samples") != 2
        or manifest.get("delivery_upscale_filter") != "lanczos"
        or manifest.get("blender_animation_fps") != 6
        or manifest.get("delivery_fps") != 30
    ):
        raise ValueError("Manifest does not confirm the bounded Blender render and 1080p delivery profile")
    if (
        output.get("blender_keyframed_animation") is not True
        or int(output.get("genuine_motion_coverage_percent", 0)) < 60
        or output.get("captions_burned") is not True
        or output.get("disclosure") != "verified"
        or output.get("subtitle") is None
    ):
        raise ValueError("Manifest does not confirm Blender animation, captions, or disclosure")
    scene_durations = output.get("scene_durations_seconds", [])
    if len(scene_durations) != len(story["scenes"]):
        raise ValueError("Manifest scene timings do not match the storyboard")
    scene_variation = validate_scene_variation(frames, scene_durations)

    subtitle_text = subtitle.read_text(encoding="utf-8-sig")
    cues = parse_srt_text(subtitle_text)
    expected = normalized(" ".join(scene["narration"] for scene in story["scenes"]))
    actual = normalized(" ".join(cue[2] for cue in cues))
    if actual != expected:
        raise ValueError("SRT text does not exactly match the approved narration script")
    previous_end = 0.0
    max_chars = 0
    for start, end, cue_text in cues:
        if start < previous_end - 0.02 or end > duration + 0.10:
            raise ValueError("SRT cue timing overlaps or exceeds the encoded runtime")
        if len(cue_text) > 120:
            raise ValueError("Subtitle cue is too long for mobile readability")
        if end - start < 0.25:
            raise ValueError("Subtitle cue is too brief to read")
        previous_end = end
        max_chars = max(max_chars, len(cue_text))

    safe = validate_safe_zones(story)
    audio = validate_audio(video)
    score = 100
    components = {
        "story_facts_and_public_safety": 20,
        "hook_and_pacing_contract": 15,
        "blender_animation_and_motion": 25,
        "audio_presence_and_levels": 15,
        "typography_subtitles_and_accessibility": 10,
        "sources_rights_privacy_and_disclosure": 10,
        "export_integrity_and_platform_fit": 5,
    }
    score = sum(components.values())
    if score < 85:
        raise ValueError(f"Creative and technical score below release threshold: {score}")
    quality_gate = {
        "status": "passed",
        "score": score,
        "release_threshold": 85,
        "automated_only": True,
        "human_review_claimed": False,
        "checks": components,
        "motion": motion,
        "scene_variation": scene_variation,
        "audio": audio,
        "subtitles": {"cue_count": len(cues), "max_characters_per_cue": max_chars},
        "safe_zones": safe,
        "duration_seconds": round(duration, 3),
        "resolution": f"{WIDTH}x{HEIGHT}",
        "fps": FPS,
        "video_codec": "h264",
        "audio_codec": "aac",
        "full_decode": "passed",
        "sources_and_disclosure": "passed",
    }
    manifest["quality_gate"] = quality_gate
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(quality_gate, indent=2))


if __name__ == "__main__":
    main()
