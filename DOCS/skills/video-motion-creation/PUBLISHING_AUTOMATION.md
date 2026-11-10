# AMORDER publishing automation standard

This document defines safe publishing requirements. It does not create credentials, enable new platform APIs or prove that any account is currently connected. The account owner has granted standing authorization for automatic publication of public-safe AMORDER educational content to the already-connected channels; per-asset human approval is not required while that authorization is active.

## Core rule

Use the existing authorized AMORDER daily automation and connected Buffer integration. Do not create a competing publisher or duplicate schedules. Never store Buffer, Meta, YouTube, X, Hugging Face or personal credentials in this public repository.

Publishing is downstream of creative approval; it is not part of video rendering.

## Fail-closed publishing states

Use a separate state per destination:

DRAFT → VALIDATED → RENDERED → TECH_QA_PASSED → AUTOMATED_RELEASE_GATE_PASSED → QUEUED → PUBLISHING → PUBLISHED_VERIFIED

Failure states include HOLD, PUBLISH_FAILED, UNKNOWN_REMOTE_STATUS and CANCELLED.

Only an export with confirmed rights, fact-checks, required disclosures, technical validation and passed automated editorial/release checks may enter the queue under the owner's standing authorization. If an account, destination, asset URL, permission, source, rights status or file integrity is unclear, HOLD.

## Duplicate and retry protection

- Create a stable content/job ID and destination-specific idempotency key.
- Check for an existing queued or published item before retrying.
- If an upload times out, status is unknown until the provider is queried.
- Never blindly retry an ambiguous upload.
- Keep successful and failed destination states independent. A failed Instagram publish does not mean that YouTube also failed.
- Record the provider post ID, permalink when available, schedule/publish time and final response.
- Never call a draft, scheduled item or processing upload “published.”

## Platform-specific metadata

Prepare distinct metadata for each destination. YouTube long-form, YouTube Shorts, Instagram Reels and X have different format and copy expectations. Do not assume one file, caption or upload result is accepted everywhere.

The export must be checked for its intended aspect ratio, duration, codec, captions, thumbnail and audio. Do not blindly crop a landscape master to create a vertical cut; reframe scenes for the vertical safe area.

## Privacy, rights and audit

Do not post private trading material, internal dashboards, credentials, account IDs, raw broker data, unpublished research or private logs. Confirm music, footage, fonts, voice and generated asset rights for each intended use.

Record the approving person, approval timestamp, content version, source/rights references, destination and verified publish receipt. Keep logs free of tokens and secret-bearing request headers.

## Stop conditions

Do not publish when:
- required factual sources or disclosures are missing;
- any media rights are unknown or unsuitable;
- technical validation fails;
- the owner standing auto-publishing authorization is absent or revoked;
- the destination/account differs from the intended one;
- a duplicate may already exist;
- upload status is ambiguous;
- the platform reports a warning or policy rejection.

Automation may report errors and recommend corrections. It must not override a stop condition or claim human approval. It may mark only the documented automated release checks as passed.
