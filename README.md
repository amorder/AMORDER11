# AMORDER11 — Daily content library

This public repository is the source of truth for content drafts and reusable creative assets intended for publishing through Buffer.

## Daily publishing workflow

1. Add one Markdown file per post under `posts/`, using `YYYY-MM-DD-short-title.md`.
2. Store shared image or video assets under `assets/` and reference their public raw GitHub URLs in the post file.
3. Keep platform-specific copy in the same post file (currently Instagram and X).
4. Review the copy and asset, then publish or schedule each channel through Buffer.
5. Update the post file with the Buffer post IDs, public post links (when available), and final status.

## First workflow test

- Post record: [2026-11-06-workflow-test.md](2026-11-06-workflow-test.md)
- Creative asset: [AMORDER11-workflow-test.jpg](https://github.com/amorder/AMORDER11/blob/daily-content/AMORDER11-workflow-test.jpg)
- Asset branch: `daily-content`
- The first creative is a 320×168 JPEG for a publishing smoke test; use a full-resolution asset for normal posts.

## Current setup

- Public repository: https://github.com/amorder/AMORDER11
- Buffer workspace: My organization
- Connected destinations: Instagram professional account `amorder11` and X profile `amorder11`
- Time zone: Asia/Kolkata

**Note:** The repository currently stores source content and assets; a scheduled GitHub-to-Buffer automation has not been configured. Posts can be published through the connected Buffer account.
