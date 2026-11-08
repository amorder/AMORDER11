# Open-source AI production and asset provenance

## Default policy

Use free/open-source tools and local inference first. Do not assume that a model is commercially reusable because its weights are downloadable or its source code is public. Do not use paid generation credits, paid subscriptions or hosted inference without explicit project-owner approval.

The existing AMORDER toolchain uses Blender, FFmpeg/ffprobe, Python/Pillow and an English narration path. Add optional models only when their value, licensing, hardware needs, maintenance burden and output quality are understood.

## Model review checklist

For every model or checkpoint, record:
- Name, publisher, exact revision/commit and source URL.
- Software and model licence, including commercial-use, attribution and redistribution terms.
- Hardware/runtime requirements and local storage footprint.
- Intended use and known limitations.
- Prompt, workflow/configuration, seed where available and generation date.
- Human review status and any content disclosure needed.

Review software, model weights, datasets, fonts, voices, music and output assets independently. Licences are not interchangeable.

## Remote inference and privacy

Do not send broker data, trade records, credentials, private research, personal data or unpublished material to an unapproved service. A model being open source does not make its hosted API private or free.

Use least privilege and isolated job directories. Never place tokens, API keys, cookies or private configuration in Git, logs, screenshots or generated media.

## Provenance for generated media

For every generated image, clip, voice or sound item, retain a manifest with model/revision, source, prompt/workflow, seed where available, generation timestamp, output checksum, licence review and human reviewer.

AI imagery may provide a labelled illustration, metaphor, reconstruction or scene that is clearly not documentary evidence. Never fabricate interviews, quotations, lip-sync, testimonials, historical footage, broker interfaces, trade executions, market data or real-world events. Label generated/reconstructed visuals whenever a reasonable viewer could mistake them for literal footage.

## Local quality review

Audition full narration for naturalness, pronunciation, timing and fatigue. Inspect generated visuals for anatomical/geometric errors, flicker, temporal instability, impossible objects, false text and misleading context. Reject assets that fail; do not rely on a model's own safety or quality score as release approval.
