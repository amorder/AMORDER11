# AMORDER video factory architecture reference

This is an implementation guide for future work, not a claim that a new factory or background worker has already been deployed.

## Separation of responsibilities

1. **Brief and editorial layer:** defines audience, topic, script, evidence, disclosures, format and approval state.
2. **Job manifest:** versioned, validated description of inputs, assets, shots, timeline, output targets and rights metadata.
3. **Media workers:** Blender for procedural scenes, FFmpeg for media processing, approved local speech/graphics tools for their defined task.
4. **Quality gate:** checks file integrity, dimensions, duration, audio presence, caption files, asset coverage, repetition and metadata.
5. **Human editorial review:** evaluates story, factual context, picture, audio, readability, rights and disclosure.
6. **Publishing adapter:** uses the existing authorized AMORDER publishing workflow and confirms each destination result.

## Suggested state machine

DRAFT → BRIEF_APPROVED → RESEARCHED → SCRIPT_APPROVED → STORYBOARDED → ASSETS_CLEARED → RENDERED → TECH_QA_PASSED → HUMAN_APPROVED → QUEUED → PUBLISHED_VERIFIED

Failure states: BLOCKED, QC_FAILED, PUBLISH_FAILED, UNKNOWN_REMOTE_STATUS and CANCELLED.

Every transition should record job ID, timestamp, actor, previous state, new state and evidence. Rerunning a stage must not silently create duplicate media or duplicate posts.

## Job isolation

Each job receives its own input directory, output directory, manifest and audit log. Reject path traversal and writes outside the job's assigned output path. Apply explicit limits for resolution, frame count, duration, render time and output size. Preserve source inputs and failure diagnostics.

## Idempotency and recovery

Use stable job IDs and a destination-specific idempotency key. Retry only transient errors, with bounded backoff. A timeout after a remote upload creates UNKNOWN_REMOTE_STATUS; query the provider before retrying. Never assume that an interrupted request failed.

## AMORDER integration boundary

The active workflow is in the current AMORDER renderer scripts and GitHub Actions workflows. This reference document does not authorize:
- adding another scheduler or set of GitHub Actions workflows;
- enabling an always-on worker or new service;
- introducing new credentials, OAuth scopes or model API keys;
- publishing without the existing approval and receipt checks;
- accessing broker/trading systems or private research.

Before implementing any factory upgrade, inspect current code, tests, branch configuration, secrets policy, execution limits and rollback path. Make changes in a reviewable branch, run tests, inspect the diff and verify the resulting deployment separately.
