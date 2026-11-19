# The World in One Day — 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/jojosinkonstanor-collab/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/jojosinkonstanor-collab/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Thursday, 19 November 2026, on a single newspaper front page — forty-one
stories, drawn entirely with Pillow in Python, so every headline, number
and caption is crisp, spelled exactly as written, and never smeared by
an image generator.

## What is on the page

- **Thirteen featured cards.** The lead three: the first Trump-Xi-Putin
  trilateral in Shenzhen; GTA VI's launch after a 13-year wait (15.9
  million pre-orders, $1.54bn); Anthropic's debut in the biggest IPO on
  record ($81.3bn at $83, trading as ANT). Then the World Court's
  Rohingya ruling, COP31's final 48 hours, Cyclone Akvan bearing down
  on Odisha, Ukraine watching Shenzhen from the sidelines, the APEC
  Shenzhen Declaration, flooded Florida, a Nature study explaining
  Earth's missing billion years, Mélenchon in Paris, a Houthi missile
  threat over Riyadh, and a drug bust in Derna.
- **Twenty-eight briefs** under "ALSO ON THURSDAY", one line each —
  Gaza, Crimea, the record Van Gogh sale, Banxico, Canberra, Mogadishu,
  Frankfurt, Washington, Ottawa, New Delhi, Tokyo, Sydney, Thimphu,
  Shenzhen, Antalya, Wellington, Caracas, Manama, Riyadh, Palo Alto,
  Sacramento, La Paz, Seoul, Chennai, Bengaluru, Mumbai, and the South
  Pacific.
- **A dotted world map** ("WHERE IT HAPPENED") with red numbers marking
  the thirteen featured stories and grey dots for the briefs, plus a
  region breakdown: Europe 8 · The Americas 10 · Asia-Pacific 11 ·
  Mideast 4 · Africa 2 · Oceania 4 · World 2.
- **A six-number stat strip** ($81.3bn, 15.9m, 200,000, $120bn,
  730,000, 300) and a **DATE CHECK** footer that names the big Wednesday
  stories the page deliberately leaves out — the EU's €45bn Ukraine
  loan, Voyager 1 crossing one light-day — so nothing dated is passed
  off as Thursday news.

The masthead reads "THE WORLD IN ONE DAY" above the date line
"THURSDAY, 19 NOVEMBER 2026". Each card gets a category tag, a
headline, one line of context, and a flat geometric scene drawn in PIL.

## The entry program

`main.py` (Python 3.13, standard library only) does one job: it reads
`asset/entry.png`, checks the PNG magic bytes and the 1024x1024 size
from the IHDR chunk, and writes those exact bytes to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). It touches no
network and re-checks the written file's size, so a short write fails
loudly instead of shipping a broken image.

Try it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
python3 -c "from PIL import Image; im = Image.open('out/entry.png'); print(im.size)"
```

Run it twice and compare checksums — the bytes come out identical
every time, because the input never changes.

## How the page was made

`draw2.py` (not part of the submission; kept in the repo for audit)
renders `asset/entry.png` from the story list. The audit that drove
this second edition — what the first entry lost on, and what changed —
is in `AUDIT-v2.md`.

---

Built for the [make.fun bounty: Sum up 19 November's world news in one image](https://make.fun/bounty/news-image-20261119).
