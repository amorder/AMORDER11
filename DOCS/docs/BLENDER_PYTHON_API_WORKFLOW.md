# Blender Python workflow for AMORDER

## Role of Blender

Use Blender's Python API (bpy) to create original 3D environments, procedural subjects, cameras, lighting, materials, object animation and compositing. Treat Blender as a specialised media worker, not as a replacement for the existing AMORDER pipeline.

The current AMORDER scene generator is \`tools/blender_scenes.py\`. The short and episode renderers remain the active entry points. Review those implementations before adding new dependencies or changing output contracts.

## Deterministic scene construction

- Start from a known scene state.
- Use stable names for scenes, objects, collections, materials and output paths.
- Prefer direct datablock APIs for reproducibility. Use context-sensitive bpy.ops operators deliberately and check poll() when applicable.
- Pass explicit frame count, FPS, resolution, engine, camera, colour-management and output settings.
- Separate scene construction, image-sequence rendering and final edit/encoding.
- Save editable .blend source and, where practical, lossless PNG/OpenEXR image sequences before delivery encoding.
- Keep all outputs inside the job-specific output directory.
- Record Blender version, script revision/hash, render engine, resolution, FPS, frame range and checksums.

## Motion and camera standards

- Give every camera move a story purpose: establish, follow, reveal, inspect or transition.
- Use coherent lens language and physical camera movement.
- Animate object transforms, camera paths, material properties or procedural elements when the story needs them.
- Use easing and believable inertia; avoid constant drift, arbitrary zooms and repetitive orbit shots.
- Check contact shadows, scale, reflections, geometry, normals, focus, clipping and temporal continuity.
- Do not treat a still frame plus a digital zoom as genuine moving-shot coverage.

## Example headless render pattern

The exact script and arguments vary by project. A typical local Blender command is:

~~~bash
blender --background --factory-startup --python tools/blender_scenes.py -- --output-dir output/example --render
~~~

Use the actual script-supported arguments; do not assume the example options above are present without checking --help or the script.

After rendering, use FFmpeg/ffprobe to inspect and encode the approved image sequence. Do not treat a successful process exit as creative approval.

## Worker contract

A worker should receive a validated job manifest, a restricted input directory, an output directory and explicit render limits. It should return job ID, Blender version, scene/output paths, frame range, warnings, elapsed time, checksums and a terminal state.

Reject path traversal, unexpected external paths, excessive frame counts/resolution, unbounded render time and uncontrolled output size. Return a non-zero exit on failure and clean only the worker's own temporary files.

## Vertical Shorts/Reels render contract

The current public short renderer invokes Blender with a scene duration and a 12 fps render rate. The camera and scene objects must be keyframed for the scene duration. FFmpeg motion-compensates those scene frames to a 30 fps portrait export. A static PNG plate does not satisfy the production motion requirement. The final short is 1080x1920, H.264/AAC, with burned English captions and an SRT sidecar, and its encoded duration must be strictly below 160 seconds (2:40). The render manifest must mark genuine Blender keyframed animation and provide the visual-coverage percentage.

## Validation

Smoke-test on the exact installed Blender version. Reopen the saved .blend file, inspect frames at full size, play the sequence at real speed and decode the final video. Check for missing/frozen/black frames, flicker, material artifacts, camera jumps, bad typography and audio-sync errors. A human must review the complete export before release.
