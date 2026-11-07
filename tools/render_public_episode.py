#!/usr/bin/env python3
"""Render cinematic AMORDER long-form episodes for YouTube and Instagram.

Consumes only a reviewed public episode storyboard. No broker, account, private
research, ledger, credentials or social APIs are accessed by this renderer.
"""
from __future__ import annotations
import argparse, json, re, shutil, subprocess, tempfile
from pathlib import Path

import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw, ImageFont
from kokoro_onnx import Kokoro

DISCLOSURE = "Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns."
FPS = 30


def run(cmd):
    subprocess.run(cmd, check=True)


def probe(path):
    raw = subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries",
        "stream=codec_type,codec_name,width,height", "-show_entries",
        "format=duration", "-of", "json", str(path)
    ], text=True)
    return json.loads(raw)


def font_path():
    for family in ("Noto Sans", "DejaVu Sans"):
        try:
            p = subprocess.check_output(
                ["fc-match", "-f", "%{file}", family],
                text=True, stderr=subprocess.DEVNULL
            ).strip()
            if p and Path(p).exists():
                return p
        except (FileNotFoundError, subprocess.CalledProcessError):
            pass
    raise RuntimeError("No sans-serif font installed")


def validate_story(story):
    if story.get("language") != "en" or story.get("audience") != "global":
        raise ValueError("Only English/global storyboards are accepted")
    if story.get("disclosure") != DISCLOSURE:
        raise ValueError("Required paper-trading disclosure missing")
    for key, low, high in (("youtube_scenes", 7, 10), ("instagram_scenes", 5, 7)):
        scenes = story.get(key)
        if not isinstance(scenes, list) or not low <= len(scenes) <= high:
            raise ValueError(f"{key} must contain {low}–{high} scenes")
        for n, scene in enumerate(scenes, 1):
            for field in ("visual", "title", "overlay", "narration"):
                value = scene.get(field)
                if not isinstance(value, str) or not value.strip():
                    raise ValueError(f"{key} scene {n} missing {field}")
            if any(ord(ch) > 127 for ch in scene["title"] + scene["overlay"] + scene["narration"]):
                raise ValueError(f"{key} scene {n} must use plain English copy")
    yt_words = sum(len(s["narration"].split()) for s in story["youtube_scenes"])
    ig_words = sum(len(s["narration"].split()) for s in story["instagram_scenes"])
    if yt_words < 560:
        raise ValueError(f"YouTube narration too short for long-form episode: {yt_words} words")
    if not 280 <= ig_words <= 430:
        raise ValueError(f"Instagram narration must be 280–430 words; found {ig_words}")


def wrap(draw, text, font, max_width):
    lines, current = [], ""
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


def draw_block(draw, text, x, y, font, fill, max_width, gap=8):
    for line in wrap(draw, text, font, max_width):
        draw.text((x, y), line, font=font, fill=fill)
        y += draw.textbbox((0, 0), line, font=font)[3] + gap
    return y


def overlay(scene, index, count, width, height, font_file, output, disclosure):
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    grad = Image.new("RGBA", (1, height), (0, 0, 0, 0))
    start = int(height * .56)
    for y in range(start, height):
        t = (y - start) / max(1, height - start)
        grad.putpixel((0, y), (3, 8, 14, int(14 + 207 * (t ** 1.25))))
    image.alpha_composite(grad.resize((width, height)))
    d = ImageDraw.Draw(image)

    scale = width / 1080
    micro = ImageFont.truetype(font_file, max(18, int(24 * scale)))
    title_font = ImageFont.truetype(font_file, max(38, int((62 if width > height else 74) * scale)))
    body_font = ImageFont.truetype(font_file, max(24, int((30 if width > height else 38) * scale)))
    small = ImageFont.truetype(font_file, max(14, int(19 * scale)))

    margin = int(width * .065)
    d.text((margin, int(height * .055)), "AMORDER", font=micro, fill=(239, 246, 250, 255))
    d.text((margin + int(150 * scale), int(height * .06)), "RESEARCH / RISK / DISCIPLINE",
           font=small, fill=(165, 190, 202, 245))
    page = f"{index:02d} / {count:02d}"
    bounds = d.textbbox((0, 0), page, font=small)
    d.text((width - margin - (bounds[2] - bounds[0]), int(height * .06)),
           page, font=small, fill=(190, 214, 225, 240))
    d.line((margin, int(height * .105), width - margin, int(height * .105)),
           fill=(190, 214, 225, 100), width=max(1, int(2 * scale)))
    d.line((margin, int(height * .105),
            margin + int((width - 2 * margin) * index / count), int(height * .105)),
           fill=(65, 183, 203, 235), width=max(2, int(3 * scale)))

    y = int(height * (.69 if width > height else .65))
    y = draw_block(d, scene["title"], margin, y, title_font,
                   (247, 250, 251, 255), width - 2 * margin, max(5, int(7 * scale)))
    y += int(13 * scale)
    draw_block(d, scene["overlay"], margin, y, body_font,
               (181, 214, 225, 255), width - 2 * margin, max(4, int(6 * scale)))

    footer_y = int(height * .94)
    d.line((margin, footer_y - int(16 * scale), width - margin, footer_y - int(16 * scale)),
           fill=(190, 214, 225, 90), width=1)
    if index == count:
        d.text((margin, footer_y), "PAPER-TRADING EDUCATION ONLY", font=small,
               fill=(116, 208, 220, 255))
        d.text((margin, footer_y + int(28 * scale)), disclosure, font=small,
               fill=(216, 226, 232, 245))
    else:
        d.text((margin, footer_y + int(4 * scale)), "PAPER SIMULATION  /  EDUCATION ONLY",
               font=small, fill=(167, 190, 201, 230))
    image.save(output)


def srt_time(seconds):
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def subtitles_for_scenes(scenes, durations, output):
    cues = []
    current = 0.0
    number = 1
    for scene, duration in zip(scenes, durations):
        sentences = [x.strip() for x in re.split(r"(?<=[.!?])\s+", scene["narration"].strip()) if x.strip()]
        weights = [max(1, len(x.split())) for x in sentences]
        total = sum(weights) or 1
        cursor = current
        for sentence, weight in zip(sentences, weights):
            span = duration * weight / total
            end = cursor + span
            cues.append(f"{number}\n{srt_time(cursor)} --> {srt_time(end)}\n{sentence}\n")
            cursor = end
            number += 1
        current += duration
    output.write_text("\n".join(cues), encoding="utf-8")


def render_variant(scenes, width, height, minimum, maximum, output, subtitle_path,
                   story_path, blender, tts, voice, speed, font_file, temp_root):
    script = Path(__file__).with_name("blender_scenes.py").resolve()
    plates = temp_root / (output.stem + "-plates")
    clips_dir = temp_root / (output.stem + "-clips")
    plates.mkdir(parents=True, exist_ok=True)
    clips_dir.mkdir(parents=True, exist_ok=True)
    clips, durations = [], []

    for index, scene in enumerate(scenes, 1):
        plate = plates / f"{index:02d}.png"
        run([
            blender, "--background", "--python", str(script), "--",
            "--visual", scene["visual"], "--output", str(plate),
            "--width", str(width), "--height", str(height)
        ])
        if not plate.exists() or plate.stat().st_size < 12000:
            raise RuntimeError(f"Missing cinematic Blender plate: {plate}")

        samples, sample_rate = tts.create(scene["narration"].strip(), voice=voice,
                                          speed=speed, lang="en-us")
        audio = np.asarray(samples, dtype=np.float32).reshape(-1)
        if audio.size == 0 or float(np.max(np.abs(audio))) < .015:
            raise RuntimeError(f"Empty or near-silent narration in scene {index}")
        wav = temp_root / f"{output.stem}-voice-{index:02d}.wav"
        sf.write(wav, audio, sample_rate, subtype="PCM_16")
        spoken = audio.size / sample_rate
        duration = spoken + (.65 if index == len(scenes) else .35)
        durations.append(duration)

        overlay_path = temp_root / f"{output.stem}-overlay-{index:02d}.png"
        overlay(scene, index, len(scenes), width, height, font_file,
                overlay_path, DISCLOSURE)

        fade_out = max(duration - .5, .05)
        zoom = "min(zoom+0.000035,1.035)"
        video_filter = (
            f"[0:v]zoompan=z='{zoom}':"
            f"x='iw/2-(iw/zoom/2)+sin(on/197)*3':"
            f"y='ih/2-(ih/zoom/2)+sin(on/239)*2':"
            f"d=1:s={width}x{height}:fps={FPS},"
            f"fade=t=in:st=0:d=0.45,fade=t=out:st={fade_out:.3f}:d=0.45,"
            "setsar=1[base];[base][1:v]overlay=0:0:format=auto,format=yuv420p[v]"
        )
        clip = clips_dir / f"clip-{index:02d}.mp4"
        run([
            "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
            "-loop", "1", "-framerate", str(FPS), "-i", str(plate),
            "-loop", "1", "-framerate", str(FPS), "-i", str(overlay_path),
            "-i", str(wav), "-filter_complex", video_filter,
            "-map", "[v]", "-map", "2:a:0",
            "-af", "apad=pad_dur=0.7,afade=t=in:st=0:d=0.25,"
                   + f"afade=t=out:st={fade_out:.3f}:d=0.4,"
                   + "loudnorm=I=-16:TP=-1.5:LRA=11",
            "-t", f"{duration:.3f}", "-r", str(FPS),
            "-c:v", "libx264", "-preset", "medium", "-crf", "18",
            "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
            "-ar", "48000", "-movflags", "+faststart", str(clip)
        ])
        clips.append(clip)

    total = sum(durations)
    if not minimum <= total <= maximum:
        raise RuntimeError(f"{output.name} duration {total:.1f}s outside {minimum}–{maximum}s")

    concat = temp_root / f"{output.stem}-concat.txt"
    concat.write_text("".join(f"file '{p.as_posix()}'\n" for p in clips), encoding="utf-8")
    run([
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
        "-f", "concat", "-safe", "0", "-i", str(concat),
        "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
        "-ar", "48000", "-movflags", "+faststart", str(output)
    ])
    subtitles_for_scenes(scenes, durations, subtitle_path)

    metadata = probe(output)
    streams = metadata.get("streams", [])
    video = next((x for x in streams if x.get("codec_type") == "video"), None)
    audio = next((x for x in streams if x.get("codec_type") == "audio"), None)
    actual = float(metadata.get("format", {}).get("duration", 0))
    if not video or (video.get("codec_name"), video.get("width"), video.get("height")) != ("h264", width, height):
        raise RuntimeError(f"Invalid video stream: {video}")
    if not audio or audio.get("codec_name") != "aac":
        raise RuntimeError(f"Invalid audio stream: {audio}")
    if not minimum <= actual <= maximum:
        raise RuntimeError(f"Encoded duration {actual:.1f}s outside {minimum}–{maximum}s")
    if output.stat().st_size < 500000:
        raise RuntimeError("Encoded video unexpectedly small")
    if subtitle_path.stat().st_size < 500:
        raise RuntimeError("Subtitle sidecar unexpectedly small")
    return {
        "file": str(output), "subtitle": str(subtitle_path), "bytes": output.stat().st_size,
        "duration_seconds": round(actual, 2), "width": width, "height": height,
        "fps": FPS, "video_codec": "h264", "audio_codec": "aac",
        "voice": voice, "disclosure": "verified"
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--voices", required=True)
    parser.add_argument("--blender", default="blender")
    parser.add_argument("--voice", default="af_heart")
    parser.add_argument("--speed", type=float, default=.96)
    args = parser.parse_args()

    if not shutil.which(args.blender) or not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        raise RuntimeError("Blender, FFmpeg and ffprobe are required")
    story_path = Path(args.input).resolve()
    story = json.loads(story_path.read_text(encoding="utf-8"))
    validate_story(story)
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    date_tag = story["publication_date"]
    slug = story["render_slug"]
    if not re.fullmatch(r"[a-z0-9-]+", slug):
        raise ValueError("Invalid render_slug")
    title = story["youtube_title"]
    font_file = font_path()
    tts = Kokoro(args.model, args.voices)

    with tempfile.TemporaryDirectory(prefix="amorder-episode-") as temp_name:
        temp_root = Path(temp_name)
        youtube = output_dir / f"{slug}-youtube-{date_tag}.mp4"
        instagram = output_dir / f"{slug}-instagram-{date_tag}.mp4"
        subs_dir = output_dir.parent / "subtitles"
        subs_dir.mkdir(parents=True, exist_ok=True)
        youtube_srt = subs_dir / f"{slug}-youtube-{date_tag}.srt"
        instagram_srt = subs_dir / f"{slug}-instagram-{date_tag}.srt"

        results = []
        results.append(render_variant(
            story["youtube_scenes"], 1920, 1080, 240, 480,
            youtube, youtube_srt, story_path, args.blender, tts,
            args.voice, args.speed, font_file, temp_root
        ))
        results.append(render_variant(
            story["instagram_scenes"], 1080, 1920, 150, 180,
            instagram, instagram_srt, story_path, args.blender, tts,
            args.voice, args.speed, font_file, temp_root
        ))
        if instagram.stat().st_size > 300 * 1024 * 1024:
            raise RuntimeError("Instagram video exceeds 300 MB API upload limit")
        manifest = {
            "title": title, "publication_date": date_tag, "language": "English",
            "audience": "global", "visual_engine": "Blender Eevee PBR cinematic",
            "post_production": "FFmpeg", "narration": "Kokoro-82M ONNX",
            "outputs": results, "disclosure": DISCLOSURE
        }
        manifest_path = output_dir / f"{slug}-manifest-{date_tag}.json"
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
