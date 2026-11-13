#!/usr/bin/env python3
"""Static regression checks for AMORDER public render and asset publishing contracts."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
episode = (root / "tools" / "render_public_episode.py").read_text(encoding="utf-8")
short = (root / "tools" / "render_public_short.py").read_text(encoding="utf-8")
short_workflow = (root / ".github" / "workflows" / "render-public-short.yml").read_text(encoding="utf-8")
episode_workflow = (root / ".github" / "workflows" / "render-public-episode.yml").read_text(encoding="utf-8")
blender_scenes = (root / "tools" / "blender_scenes.py").read_text(encoding="utf-8")
motion_graphics = (root / "tools" / "motion_graphics.py").read_text(encoding="utf-8")
validator = (root / "tools" / "validate_public_short.py").read_text(encoding="utf-8")

checks = {
    "long-form SRT generation": "subtitles_for_scenes(scenes, durations, subtitle_path)" in episode,
    "long-form burned captions": "subtitles=filename=" in episode and "captions_burned" in episode,
    "long-form chapter timing": "scene_durations_seconds" in episode and '"chapters": chapters' in episode,
    "YouTube thumbnail generation": "def create_thumbnail(" in episode and '"thumbnail": str(thumbnail_path)' in episode,
    "short-form SRT generation": "subtitles_for_scenes(scenes,durations,subtitle)" in short,
    "short-form burned captions": "subtitles=filename=" in short and '"captions_burned":True' in short,
    "Blender creates the PBR studio stage and 3D hero scenes": (
        "def setup(" in blender_scenes
        and "Anodised circular presentation stage" in blender_scenes
        and "Top edge softbox" in blender_scenes
        and '"BLENDER_EEVEE_NEXT"' in blender_scenes
    ),
    "Blender renders genuine PNG frame sequences before FFmpeg scene encoding": (
        'image_settings.media_type = "IMAGE"' in blender_scenes
        and 'image_settings.file_format = "PNG"' in blender_scenes
        and 'scene.render.filepath = str(frame_dir / "frame_")' in blender_scenes
        and 'bpy.ops.render.render(animation=True)' in blender_scenes
        and '"-i", str(frame_dir / "frame_%04d.png")' in blender_scenes
        and '"-c:v", "libx264"' in blender_scenes
        and "len(frames) != expected_frames" in blender_scenes
    ),
    "Blender scene MP4 is fully decoded before use": (
        '["ffmpeg", "-v", "error", "-i", str(output), "-f", "null", "-"]' in blender_scenes
        and '"ffprobe"' in short
        and '["ffmpeg","-v","error","-i",str(animation),"-f","null","-"]' in short
    ),
    "Motion-graphics layer includes scene-specific animation": (
        "def build_motion_graphics_filter(" in motion_graphics
        and all(key in motion_graphics for key in ("timestamp", "idea", "source", "gaps", "stand_down", "brand"))
        and "drawbox=" in motion_graphics
        and "mod(t*" in motion_graphics
    ),
    "Short renderer uses real keyframed Blender scene animation": (
        "from motion_graphics import build_motion_graphics_filter" in short
        and '"--duration",f"{duration:.3f}"' in short
        and '"--fps",str(BLENDER_FPS)' in short
        and "minterpolate=fps=" in short
        and '"blender_keyframed_animation":True' in short
    ),
    "Short renderer enforces sub-2:40 runtime": (
        "MAX_RUNTIME_SECONDS = 159.0" in short
        and "duration<MAX_RUNTIME_SECONDS" in short
        and "duration<MAX_RUNTIME_SECONDS" in short
    ),
    "Episode renderer composites animated motion graphics over Blender plates": (
        "from motion_graphics import build_motion_graphics_filter" in episode
        and "motion = build_motion_graphics_filter(width, height, duration, scene[\"visual\"])" in episode
        and "[0:v]{motion}" in episode
    ),
    "No Ken Burns zoompan fallback in video renderers": (
        "zoompan=" not in short and "zoompan=" not in episode
    ),
}

def collision_safe_commit(workflow: str) -> bool:
    return (
        'git fetch origin "$GITHUB_REF_NAME"' in workflow
        and 'git reset --mixed "origin/$GITHUB_REF_NAME"' in workflow
        and 'git push origin "HEAD:$GITHUB_REF_NAME"' in workflow
        and "git pull --rebase" not in workflow
        and "for attempt in 1 2 3" in workflow
    )

checks["short workflow safely replaces same-path binary assets"] = collision_safe_commit(short_workflow)
checks["episode workflow safely replaces same-path binary assets"] = collision_safe_commit(episode_workflow)
checks["episode workflow stages only manifest-listed outputs"] = (
    'subprocess.run(["git", "add", "--", *[str(path) for path in paths]], check=True)' in episode_workflow
    and 'for field in ("file", "subtitle", "thumbnail")' in episode_workflow
    and "git add assets/*-youtube-*.mp4" not in episode_workflow
)
checks["short workflow cancels superseded renders"] = "cancel-in-progress: true" in short_workflow
checks["Blender uses a bounded Eevee sample budget"] = (
    "def setup(width=1080, height=1920, samples=4)" in blender_scenes
    and "eevee.taa_render_samples = samples" in blender_scenes
    and "eevee.taa_samples = 8" in blender_scenes
)
checks["Short render uses 720p Blender scenes and 1080p Lanczos delivery"] = (
    "BLENDER_WIDTH, BLENDER_HEIGHT, BLENDER_TAA_SAMPLES = 720, 1280, 4" in short
    and '"--samples",str(BLENDER_TAA_SAMPLES)' in short
    and "scale={WIDTH}:{HEIGHT}:flags=lanczos" in short
    and '"blender_render_width":BLENDER_WIDTH' in short
)
checks["Short workflow allows the six-scene Blender render to finish"] = "timeout-minutes: 180" in short_workflow
checks["Short validator requires render-profile evidence"] = (
    'manifest.get("blender_render_width") != 720' in validator
    and 'manifest.get("delivery_upscale_filter") != "lanczos"' in validator
)
checks["short workflow runs the independent release validator"] = (
    "validate_public_short.py" in short_workflow
    and 'echo "STORYBOARD=$STORYBOARD"' in short_workflow
)
checks["short validator checks motion, black/frozen frames, SRT, audio and safe zones"] = (
    all(key in validator for key in (
        "black_frame_count", "longest_frozen_run_seconds", "motion_coverage_percent",
        "parse_srt_text", "volumedetect", "validate_safe_zones", "validate_scene_variation"
    ))
)
checks["episode workflow cancels superseded renders"] = "cancel-in-progress: true" in episode_workflow

compile(episode, str(root / "tools" / "render_public_episode.py"), "exec")
compile(short, str(root / "tools" / "render_public_short.py"), "exec")
compile(blender_scenes, str(root / "tools" / "blender_scenes.py"), "exec")
compile(motion_graphics, str(root / "tools" / "motion_graphics.py"), "exec")
compile(validator, str(root / "tools" / "validate_public_short.py"), "exec")
print("PASS: both renderer scripts compile")

failed = [name for name, passed in checks.items() if not passed]
for name, passed in checks.items():
    print(("PASS" if passed else "FAIL") + ": " + name)
if failed:
    raise SystemExit("Public video render contract regression: " + ", ".join(failed))
print("PASS: public render, Blender animation, subtitle, audio, safe-zone, source and release-gate contracts")
