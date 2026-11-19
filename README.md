# The World in One Picture — 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/jojosinkonstanor-collab/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/jojosinkonstanor-collab/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Thursday, 19 November 2026, on a single newspaper front page. The page
is drawn entirely with Pillow in Python, so every headline, date line
and caption is crisp, spelled exactly as written, and never smeared by
an image generator. Six stories made the front page — the ones a reader
who missed the day would most need to catch up on.

## What is on the page

- **Front page lead — a first in Shenzhen.** Trump, Xi and Putin sit
  down together for the first time, for one hour, to talk nuclear
  arms, Iran and Ukraine.
- **Culture — the 13-year wait ends.** GTA VI launches worldwide at
  midnight; 9.69 million pre-orders, worth $942 million, were already
  in before launch day.
- **War — fire in the Gulf.** Three oil tankers burn east of the
  Strait of Hormuz after hitting mines, as the US-Iran war widens.
- **Courts — verdict in The Hague.** The World Court rules on
  Myanmar's alleged Rohingya genocide, in The Gambia's case from
  seven years ago.
- **Europe — a €45 billion loan.** The EU proposes the loan for
  Ukraine in 2027, covering two-thirds of Kyiv's €70 billion gap.
- **Space — one light-day out.** NASA confirms Voyager 1, launched
  in 1977, is now 16 billion miles from Earth — farther than any
  human-made object has ever flown.

Each story gets a category tag, a headline and one line of context,
with a flat geometric icon drawn in PIL. The masthead reads
"THE WORLD IN ONE PICTURE" above the date line
"THURSDAY, 19 NOVEMBER 2026".

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

---

Built for the [make.fun bounty: Sum up 19 November's world news in one image](https://make.fun/bounty/news-image-20261119).
