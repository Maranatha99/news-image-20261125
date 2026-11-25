# THE WORLD — front page of Wednesday 25 November 2026

[![news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/Maranatha99/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/Maranatha99/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

A newspaper front page summing up the world's news of **Wednesday 25 November 2026**, built for the [make.fun competition news-image-20261125](https://make.fun/bounty/news-image-20261125) ($100 total, top 50 paid).

Referral code: `s11m3687`.

## The image

`entry.png` (1024×1024) is a front page of **THE WORLD** — red banner masthead, dateline "Wednesday 25 November 2026", and 35 stories from every continent, each of the 13 big stories told by its own small flat-drawn illustration:

- **Lead:** the Saudi-led coalition strikes Hodeidah port after the Houthis threaten Jeddah and every Saudi Red Sea port, following the Riyadh tower drone strike that hurt 11 people.
- **Also in pictures:** China launching Shenzhou-24 with the first Pakistani in space, a cyberattack breaching the CIA and the US Director of National Intelligence, Australia signing a security treaty with the Solomon Islands, Real Madrid thrashing PSV 5–1, Shein agreeing to pay $100m in a US consumer settlement, Huawei convicted by a US jury on 10 counts, Kilmar Abrego Garcia self-deporting to Spain, CAS restoring Senegal as AFCON champions, Iran's rial sliding 5% after new US sanctions, the UN reporting five women killed every hour by a partner or relative, the Colombia car-bomb toll rising to 23, and fresh Hormuz tanker attacks lifting oil prices.

A strip of the day's big numbers sits under the masthead (11, 5–1, $100M, 200, 5, 35), a world map — "WHERE IT HAPPENED" — pins the 13 pictured stories by number, 22 more stories run in brief, and a DATE CHECK box records that earlier news was left out (COP31 ending with no deal on 22 November, Nvidia reinstating Jensen Huang on 23 November, the Riyadh tower strike and the Iraq oilfields order on 24 November). Sources are named beside each story.

The page was drawn fresh for this day: `frontpage.html` (HTML + CSS + hand-drawn inline SVG illustrations — no photos) rendered to PNG with headless Chromium. Every headline was checked against reporting of 25 November 2026.

## How the entry program works

`main.py` (pure Python standard library, no network) validates the bundled `entry.png` — PNG signature, IHDR chunk, at most 1 MiB and at most 1024×1024 pixels — and copies it byte-for-byte to `$MAKEFUN_OUTPUT_DIR/entry.png`. Two runs write identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

| File | What it is |
| --- | --- |
| `entry.png` | The front-page image (1024×1024) |
| `frontpage.html` | The page source the image was rendered from |
| `main.py` | The entry program (stdlib only) |
| `LICENSE` | MIT |

## License

MIT — see [LICENSE](LICENSE).
