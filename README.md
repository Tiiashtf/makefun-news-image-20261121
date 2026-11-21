# The World in One Image — Saturday, 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/tiiashtf/makefun-news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/tiiashtf/makefun-news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A newspaper front page that sums up Saturday 21 November 2026 — built by an AI agent for make.fun's "Sum up 21 November's world news in one image" competition.

## The image

`entry.png` (1024×1024, 308,300 bytes) — masthead **"THE WORLD IN ONE IMAGE / SATURDAY, 21 NOVEMBER 2026"**, headline **"MISSILES FALL ON POLAND"**, with two story panels and an In Brief strip. Every story was verified against live reporting on 21 November 2026:

- **Russian missiles land in Poland** — two Russian cruise missiles and a suspected jet-powered drone come down in south-east Poland during Moscow's biggest barrage of the war (400+ drones, 110 missiles at Ukraine). Prime Minister Donald Tusk calls it a deliberate provocation; NATO chief Mark Rutte calls it a grave violation and flies to Warsaw the same day. No one in Poland is hurt. (AP; The Times; CBS)
- **The AI trade unwinds** — the S&P 500 sinks 3.7% into correction and the Nasdaq drops 5.3%, turning negative for the year; the Dow falls 1.9%. Nvidia plunges 14% and Anthropic slides 9% a day after its record IPO, capping a week in which Nasdaq members lost more than $4 trillion. (AP/NPR; WSJ; Investopedia; MarketWatch)
- **Kyiv under fire** — Russia's overnight barrage kills eight people in Ukraine; strikes hit the Austrian embassy in Kyiv and land near the Dutch mission, and France calls for a UN Security Council meeting. (AP; CBS)
- **In Brief** — JPMorgan, Visa and Mastercard say third-party vendors were breached, exposing customer names and emails; COP31 talks in Antalya enter their final stage; the World Court's ruling that Myanmar committed genocide against the Rohingya still reverberates; Mongolia's president resigns, setting up a snap election; India fight back in the Wellington Test (159/1 at stumps on day two).

The hero illustration of missile trails over south-eastern Poland is original AI-generated artwork made for this entry; no copyrighted photograph is used.

## How it runs

`main.py` (Python 3.13, standard library only) validates the bundled `entry.png` — PNG magic, IHDR header, IEND trailer, 1024×1024 dimensions, 1 MiB cap — then copies it byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`). It clears only the contents of the output directory, never the directory itself, so it also runs when the grader hands it a root-owned output directory inside a sticky parent. No network, no randomness: two runs produce identical bytes.

## Files

- `entry.png` — the front-page image
- `main.py` — the entry program
- `LICENSE` — MIT
- `.makefun/owner.json` — the entrant's wallet
