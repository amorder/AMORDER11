# AMORDER11 — Content automation only

AMORDER11 is the public content operations repository for AMORDER. It stores approved post drafts, platform-specific copy, public creative assets, source links, and publishing records for Buffer.

It is **not** the trading system, research database, paper-trading ledger, or application-code repository. Those functions remain in a separate private repository.

## Daily content workflow

1. Create or update one Markdown post record under `posts/`, named `YYYY-MM-DD-short-title.md`.
2. Keep the post title, publication date, factual source links, platform-specific copy for X and Instagram, disclosure, approved asset references, and publishing record in that file.
3. Store only approved public creative assets under `assets/`. Reference stable raw GitHub URLs. Use full-resolution, platform-compatible media for normal posts; the original 320×168 JPEG is only a smoke-test asset.
4. Review every factual statement and ensure the copy contains no private trading data, trade-specific calls, unverified claims, or performance promises.
5. Publish or queue each connected channel through the existing AMORDER daily automation and connected Buffer integration. X and Instagram are handled as separate channel actions.
6. Update the same Markdown file with each Buffer post ID, public URL (when available), and confirmed status: `sent`, `scheduled`, `draft`, or `error`. Never label a failed post as published, and check for duplicates before retrying.

## Repository boundary

**Allowed here:** reviewed post copy, captions, editorial notes, approved public images/videos, public source URLs, content calendar metadata, and Buffer publishing IDs/URLs/statuses.

**Never store here:** trading or strategy source code, candidate scans, symbol-specific research, raw market/broker data, private journals, account/order IDs, balances, positions, fills, trade-by-trade details, P&L/performance statistics, broker payloads, credentials, tokens, `.env` files, or internal logs.

Content may explain general research, data-quality, paper-trading, and risk-management concepts. Any paper-trading disclosure must clearly say it is simulated activity, not live-money performance, not investment advice, and not a promise of returns. Do not publish buy/sell calls, price targets, or fabricated metrics.

## Publishing and security

- Buffer workspace: My organization
- Connected destinations: Instagram professional account `amorder11` and X profile `amorder11`
- Time zone: Asia/Kolkata
- The existing daily AMORDER automation orchestrates content using the connected Buffer integration.
- The repository's GitHub Actions workflow is a read-only secret-pattern guard. There is no GitHub Actions publisher in this repository.
- Do not add Buffer, Alpaca, Hugging Face, or GitHub credentials to this public repo or create a workflow that publishes by embedding credentials in source files.

## Initial workflow test

- Post record: [2026-11-06 workflow test](posts/2026-11-06-workflow-test.md)
- Smoke-test creative: [AMORDER11-workflow-test.jpg](https://github.com/amorder/AMORDER11/blob/daily-content/AMORDER11-workflow-test.jpg)
- Asset branch: `daily-content`

