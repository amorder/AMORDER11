# A Trailing Stop Is Not a Price Promise

- **Publication date:** 2026-11-12
- **Language / audience:** English / global
- **Channels:** Instagram Reels, YouTube Shorts
- **Topic:** Why a trailing-stop trigger is not a guaranteed execution price

## Story and production
A concise explanation of the high-water mark, the one-way trailing rule, market-order execution, gaps and regular-hours limitations. No stock-specific call, trade result, account information or performance claim is used.

- **Opening hook:** "A trailing stop can trigger and still fill at a different price."
- **Scene design:** six distinct Blender Eevee PBR setups: idea, timestamp, source, gaps, stand-down and brand.
- **Motion:** keyframed camera and object animation in every Blender scene; FFmpeg motion-compensated delivery at 30 fps.
- **Target runtime:** 105-145 seconds; hard maximum strictly below 159 seconds (2:39).
- **Delivery:** 1080x1920, 9:16, 30 fps, H.264 MP4, AAC English narration, burned captions and SRT sidecar.
- **Voice:** Kokoro-82M ONNX, af_heart; restrained original sound design only.
- **Editorial note:** this explainer distinguishes a trigger condition from an execution price and includes the broker-specific regular-hours caveat without implying that every broker follows the same rules.

## YouTube
**Title:** A Trailing Stop Is Not a Price Promise | AMORDER #Shorts

A trailing stop can trigger and still fill at a different price. This short explains the high-water mark, why the stop can ratchet upward but not downward, and why gaps, market hours and execution rules matter.

Sources:
SEC Investor Bulletin: https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-15
Alpaca order documentation: https://docs.alpaca.markets/us/docs/orders-at-alpaca

Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns.

#AMORDER #RiskEducation #Shorts

## Instagram
A trailing stop is an order rule, not a guaranteed execution price. Learn what the high-water mark does, why the stop can ratchet upward, and how gaps or market hours can change the result.

Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns.

#AMORDER #RiskEducation

**Alt text:** Six cinematic graphite-studio 3D scenes use glass, metal, a clock-like high-water marker and a broken signal line to explain how a trailing stop moves, triggers and may fill at a different price.

## Sources
- [SEC Investor Bulletin: Stop, Stop-Limit, and Trailing Stop Orders](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-15)
- [Alpaca: Placing Orders](https://docs.alpaca.markets/us/docs/orders-at-alpaca)

## Disclosure
Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns.

## Assets
- Storyboard: `posts/2026-11-12-trailing-stop-not-a-promise.short.json`
- Expected MP4: `assets/amorder-trailing-stop-not-a-promise-2026-11-12.mp4` (pending render)
- Expected SRT: `subtitles/amorder-trailing-stop-not-a-promise-2026-11-12.srt`
- Expected manifest: `assets/amorder-trailing-stop-not-a-promise-manifest-2026-11-12.json`

## Release gates
- [ ] Blender keyframed render completed; at least five distinct visual setups
- [ ] 1080x1920, 30 fps, H.264/AAC; runtime below 159 seconds
- [ ] Public HTTPS MP4 fetch returns non-empty MP4 bytes
- [ ] Full FFmpeg decode; representative-frame variation; no black/frozen sections
- [ ] Safe-zone and subtitle readability checks; SRT text/timing matches narration
- [ ] Audio stream, loudness and clipping checks pass
- [ ] Sources, rights, privacy and disclosure checks pass
- [ ] Automated quality score at least 85/100; no critical gate failed

## Publishing record
| Destination | Buffer post ID | Public URL | Status |
|---|---|---|---|
| Instagram Reel | pending | pending | pending_render |
| YouTube Short | pending | pending | pending_render |

No destination is reported as published until its provider status is confirmed as `sent`.
