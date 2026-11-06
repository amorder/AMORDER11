# AMORDER11 — Content automation only

AMORDER11 is the public content operations repository for AMORDER. It stores reviewed post copy, platform-specific captions, approved public creative assets, source links, video storyboards, and Buffer publishing records.

It is not the trading system, research database, paper-trading ledger, or application-code repository. Those functions remain in the separate private repository amorder/AMORDER.

## Daily content workflow

1. Create or update one Markdown post record under posts/, named YYYY-MM-DD-short-title.md.
2. Keep the post title, publication date, factual source links, platform-specific copy, disclosure, approved asset references, and publishing record in that file.
3. For daily video content, add a content-only storyboard at posts/YYYY-MM-DD-short-title.short.json. The secret-free workflow .github/workflows/render-public-short.yml turns that storyboard into a vertical MP4 in assets/.
4. The renderer creates educational motion graphics and narration only. It does not access broker accounts, trading records, or private research. It uses no Buffer, Alpaca, Hugging Face, or user-supplied secrets.
5. Publish or queue each connected destination through the existing AMORDER daily automation and connected Buffer integration. X remains text-first; Instagram uses Reels; YouTube uses vertical Shorts. The same approved MP4 may be adapted with separate platform metadata and captions.
6. Update the same Markdown file with each Buffer post ID, public URL (when available), and confirmed status: sent, scheduled, draft, or error. Never label a failed post as published, and check for duplicates before retrying.

## Repository boundary

Allowed here: reviewed post copy, captions, educational scripts/storyboards, approved public images/videos, public source URLs, content calendar metadata, and Buffer publishing IDs/URLs/statuses.

Never store here: trading or strategy source code, candidate scans, symbol-specific research, raw market/broker data, private journals, account/order IDs, balances, positions, fills, trade-by-trade details, P&L/performance statistics, broker payloads, credentials, tokens, .env files, or internal logs.

Content may explain general research, data-quality, paper-trading, and risk-management concepts. Any paper-trading disclosure must clearly say it is simulated activity, not live-money performance, not investment advice, and not a promise of returns. Do not publish buy/sell calls, price targets, or fabricated metrics.

## Publishing and security

- Buffer workspace: My organization
- Connected destinations: Instagram professional account amorder11, YouTube channel AMORDERS, and X profile amorder11
- Time zone: Asia/Kolkata
- The existing daily AMORDER automation orchestrates publishing using the connected Buffer integration.
- The GitHub Actions secret guard is read-only. The short-render workflow only creates public creative media; it does not publish content and does not use stored secrets.
- Do not add Buffer, Alpaca, Hugging Face, or personal credentials to this public repo. GitHub Actions uses its repository-scoped generated token only to commit the rendered content asset.

## Initial workflow test

- 2026-11-06 content workflow test: posts/2026-11-06-workflow-test.md
- 2026-11-06 AMORDER public workflow post: posts/2026-11-06-building-amorder-in-public.md
- AMORDER video renderer: tools/render_public_short.py
- Short render workflow: .github/workflows/render-public-short.yml
