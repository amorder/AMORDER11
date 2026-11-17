#!/usr/bin/env python3
"""Static regression checks for AMORDER public render and asset publishing contracts."""
import json
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
    "Short subtitles split long narration into mobile-readable cues": (
        "MAX_SUBTITLE_CUE_CHARS = 96" in short
        and "def split_subtitle_sentence(" in short
        and r're.split(r"(?<=[.!?])\s+"' in short
        and r'f"{number}\n{srt_time(cursor)} --> {srt_time(end)}\n{segment}\n"' in short
        and r'output.write_text("\n".join(cues), encoding="utf-8")' in short
        and "split_subtitle_sentence(sentence)" in short
    ),
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
        and all(key in motion_graphics for key in ("timestamp", "idea", "source", "gaps", "stand_down", "brand", "risk_budget", "stop_distance", "unit_value", "position_size", "minimum_unit"))
        and "drawbox=" in motion_graphics
        and "mod(t*" in motion_graphics
    ),
    "Short delivery normalizes the concatenated master and caption burn to constant 30 fps": (
        short.count('"-fps_mode","cfr"') >= 2
        and short.count('"-r",str(FPS)') >= 3
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
checks["short workflow retriggers when its own configuration changes"] = "      - '.github/workflows/render-public-short.yml'" in short_workflow
checks["short workflow commit message uses an exported variable available to the commit step"] = (
    'git commit -m "content: render ${OUTPUT%.mp4} short with captions"' in short_workflow and "${BASE}" not in short_workflow
)
checks["daily short validator enforces shared Instagram and YouTube scope"] = (
    'channels != {"instagram_reels", "youtube_shorts"}' in validator
    and 'fmt.get("aspect_ratio") != "9:16"' in validator
)
checks["new position-sizing scene keys have Blender geometry, camera motion and animated overlays"] = all(
    key in blender_scenes and key in motion_graphics
    for key in ("risk_budget", "stop_distance", "unit_value", "position_size", "minimum_unit")
)
latest_short_path = sorted((root / "posts").glob("*.short.json"))[-1]
latest_short = json.loads(latest_short_path.read_text(encoding="utf-8"))
latest_visuals = {scene.get("visual") for scene in latest_short.get("scenes", [])}
supported_visuals = {"idea", "timestamp", "gaps", "source", "stand_down", "brand",
                     "risk_budget", "stop_distance", "unit_value", "position_size", "minimum_unit"}
scene_narration = [
    " ".join(scene.get("narration", "").split()).casefold()
    for scene in latest_short.get("scenes", [])
]
checks["daily storyboard does not repeat narration across scenes"] = (
    len(scene_narration) == len(set(scene_narration))
    and all(scene_narration)
)
checks["latest daily storyboard uses at least five supported visual keys"] = (
    len(latest_visuals) >= 5 and latest_visuals <= supported_visuals
)
def sec_stop_execution_caveat_is_scoped(scenes):
    """Enforce precise SEC stop-order wording only when a storyboard makes that claim."""
    for scene in scenes:
        narration = " ".join(scene.get("narration", "").split()).casefold()
        if "sec" in narration and any(
            term in narration
            for term in ("stop order", "stop-limit order", "stop execution", "execution price")
        ):
            if "standard stop order" not in narration or "stop-limit order" in narration:
                return False
    return True


checks["SEC stop execution caveat is scoped to standard stop orders when present"] = (
    sec_stop_execution_caveat_is_scoped(latest_short.get("scenes", []))
)
checks["topic rotation does not require an unrelated SEC stop-order caveat"] = (
    sec_stop_execution_caveat_is_scoped([
        {"narration": "A market scan starts with instrument identity and data quality."}
    ])
)
checks["an unscoped SEC stop-order caveat is rejected"] = (
    not sec_stop_execution_caveat_is_scoped([
        {"narration": "The SEC says a stop order becomes a market order and the execution price can differ."}
    ])
)
checks["a correctly scoped SEC standard-stop caveat is accepted"] = (
    sec_stop_execution_caveat_is_scoped([
        {"narration": "The SEC says a standard stop order becomes a market order when triggered; the execution price can differ."}
    ])
)
checks["Blender uses a bounded Eevee sample budget"] = (
    "def setup(width=1080, height=1920, samples=2)" in blender_scenes
    and "eevee.taa_render_samples = samples" in blender_scenes
    and "eevee.taa_samples = samples" in blender_scenes
)
checks["Blender post-render SIGSEGV is tolerated only with a non-empty scene MP4 and mandatory validation"] = (
    "def run_blender_scene(command, output):" in short
    and "exc.returncode not in (-11, 139)" in short
    and "not output.is_file()" in short
    and "output.stat().st_size < 1024" in short
    and "run_blender_scene([" in short
    and 'clip_meta=json.loads(subprocess.check_output([' in short
    and '["ffmpeg","-v","error","-i",str(animation),"-f","null","-"]' in short
)
checks["Short render uses 720p Blender scenes and 1080p Lanczos delivery"] = (
    "BLENDER_WIDTH, BLENDER_HEIGHT, BLENDER_TAA_SAMPLES = 720, 1280, 2" in short and "BLENDER_FPS = 12" in short
    and "default=12" in blender_scenes
    and 'manifest.get("blender_animation_fps") != 12' in validator
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
checks["30 fps validation tolerates rational MP4 duration rounding"] = (
    "from fractions import Fraction" in validator
    and "def is_nominal_30_fps(value: str) -> bool:" in validator
    and "abs(float(rate) - FPS) <= 0.05" in validator
    and "from fractions import Fraction" in short_workflow
    and "abs(float(fps_value) - 30.0) <= 0.05" in short_workflow
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
