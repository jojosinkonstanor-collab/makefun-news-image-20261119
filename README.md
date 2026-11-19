# The World in One Picture — 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/jojosinkonstanor-collab/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/jojosinkonstanor-collab/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

One image that sums up the world's news of **Thursday, 19 November 2026** —
a newspaper front page drawn entirely with Pillow (Python), so every word is
sharp and exactly as written. No AI-generated text anywhere in the image.

## The six stories

1. **Lead — Trilateral summit in Shenzhen:** Trump, Xi and Putin hold their
   first-ever three-way summit — one hour in Shenzhen on nuclear arms, Iran
   and Ukraine.
2. **Culture — GTA VI:** launches after a 13-year wait; pre-orders hit
   9.69 million units, worth $942 million, before launch day.
3. **War — Gulf:** three oil tankers catch fire in the Strait of Hormuz;
   Iran says they hit mines east of the strait as the US-Iran war widens.
4. **Courts — The Hague:** the World Court rules on Myanmar's alleged
   Rohingya genocide, in The Gambia's case lodged seven years ago.
5. **Europe — Ukraine:** the EU proposes a €45 billion loan for Ukraine in
   2027, covering two-thirds of Kyiv's €70 billion funding gap.
6. **Space — NASA:** Voyager 1 reaches one light-day from Earth — NASA
   confirms the 1977 probe is 16 billion miles out, the farthest any
   human-made object has ever flown.

## How it works

`main.py` (Python 3.13, standard library only) copies `asset/entry.png`
to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). The image is
1024×1024 px, PNG, well under the 1 MiB limit, and every run writes
byte-identical output. `draw.py` (kept out of the submitted snapshot's
critical path; the PNG it produces is the shipped asset) renders the page
with Pillow: masthead, date line, six panels with category tags, headlines,
one line of context each, and flat geometric icons drawn with PIL shapes.

## Verify locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
python3 -c "from PIL import Image; im = Image.open('out/entry.png'); print(im.size)"
```

Run it twice and compare checksums — the bytes are identical.

---

Built for the [make.fun bounty: Sum up 19 November's world news in one image](https://make.fun/bounty/news-image-20261119).
