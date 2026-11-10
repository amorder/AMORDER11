#!/usr/bin/env python3
"""Static regression checks for AMORDER public render and asset publishing contracts."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
episode = (root / "tools" / "render_public_episode.py").read_text(encoding="utf-8")
short = (root / "tools" / "render_public_short.py").read_text(encoding="utf-8")
short_workflow = (root / ".github" / "workflows" / "render-public-short.yml").read_text(encoding="utf-8")
episode_workflow = (root / ".github" / "workflows" / "render-public-episode.yml").read_text(encoding="utf-8")
blender_scenes = (root / "tools" / "blender_scenes.py").read_text(encoding="utf-8")

checks = {
    "long-form SRT generation": "subtitles_for_scenes(scenes, durations, subtitle_path)" in episode,
    "long-form burned captions": "subtitles=filename=" in episode and "captions_burned" in episode,
    "long-form chapter timing": "scene_durations_seconds" in episode and '"chapters": chapters' in episode,
    "YouTube thumbnail generation": "def create_thumbnail(" in episode and '"thumbnail": str(thumbnail_path)' in episode,
    "short-form SRT generation": "subtitles_for_scenes(scenes,durations,subtitle)" in short,
    "short-form burned captions": "subtitles=filename=" in short and '"captions_burned":True' in short,
    "Blender camera and object keyframes": (
        "def animate_scene(" in blender_scenes
        and 'camera.keyframe_insert(data_path="location"' in blender_scenes
        and 'obj.keyframe_insert(data_path="location"' in blender_scenes
        and "bpy.ops.render.render(animation=True)" in blender_scenes
    ),
    "Blender H.264 animation export": (
        'scene.render.image_settings.file_format = "FFMPEG"' in blender_scenes
        and 'scene.render.ffmpeg.format = "MPEG4"' in blender_scenes
        and 'scene.render.ffmpeg.codec = "H264"' in blender_scenes
    ),
    "Short renderer uses animated Blender clips": (
        '"--duration",f"{duration:.3f}"' in short
        and '"--fps",str(blender_fps)' in short
        and "minterpolate=fps=" in short
    ),
    "Episode renderer uses animated Blender clips": (
        '"--duration", f"{duration:.3f}"' in episode
        and '"--fps", str(blender_fps)' in episode
        and "minterpolate=fps=" in episode
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
checks["episode workflow cancels superseded renders"] = "cancel-in-progress: true" in episode_workflow

compile(episode, str(root / "tools" / "render_public_episode.py"), "exec")
compile(short, str(root / "tools" / "render_public_short.py"), "exec")
compile(blender_scenes, str(root / "tools" / "blender_scenes.py"), "exec")
print("PASS: both renderer scripts compile")

failed = [name for name, passed in checks.items() if not passed]
for name, passed in checks.items():
    print(("PASS" if passed else "FAIL") + ": " + name)
if failed:
    raise SystemExit("Public video render contract regression: " + ", ".join(failed))
print("PASS: all public render, Blender animation, caption, thumbnail and binary-commit contract checks")
