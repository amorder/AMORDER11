#!/usr/bin/env python3
"""Static regression checks for public AMORDER caption and thumbnail exports."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
episode = (root / "tools" / "render_public_episode.py").read_text(encoding="utf-8")
short = (root / "tools" / "render_public_short.py").read_text(encoding="utf-8")

checks = {
    "long-form SRT generation": "subtitles_for_scenes(scenes, durations, subtitle_path)" in episode,
    "long-form burned captions": "subtitles=filename=" in episode and "captions_burned" in episode,
    "long-form chapter timing": "scene_durations_seconds" in episode and '"chapters": chapters' in episode,
    "YouTube thumbnail generation": "def create_thumbnail(" in episode and '"thumbnail": str(thumbnail_path)' in episode,
    "short-form SRT generation": "subtitles_for_scenes(scenes,durations,subtitle)" in short,
    "short-form burned captions": "subtitles=filename=" in short and '"captions_burned":True' in short,
}
compile(episode, str(root / "tools" / "render_public_episode.py"), "exec")
compile(short, str(root / "tools" / "render_public_short.py"), "exec")
print("PASS: both renderer scripts compile")

failed = [name for name, passed in checks.items() if not passed]
for name, passed in checks.items():
    print(("PASS" if passed else "FAIL") + ": " + name)
if failed:
    raise SystemExit("Caption/thumbnail contract regression: " + ", ".join(failed))
print("PASS: all public video caption and thumbnail contract checks")

short_workflow = (root / ".github" / "workflows" / "render-public-short.yml").read_text(encoding="utf-8")
episode_workflow = (root / ".github" / "workflows" / "render-public-episode.yml").read_text(encoding="utf-8")

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
