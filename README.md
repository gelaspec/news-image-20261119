# The World in One Day — Thursday 19 November 2026

[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/c/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/gelaspec/news-image-20261119/rank.svg)](https://make.fun/c/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/gelaspec/news-image-20261119/reward.svg)](https://make.fun/c/news-image-20261119)

One image summing up the world's news of **Thursday 19 November 2026**:
a dense newspaper front page with **38 verified stories from 6 continents**.

- **Lead:** Trump, Xi and Putin meet in Shenzhen — the first-ever
  three-way summit of the US, Chinese and Russian leaders, 90 minutes
  at a round table, ending in a joint declaration that a nuclear war
  cannot be won and must never be fought. No deal on Ukraine or Iran.
- **Photo stories:** the World Court finds Myanmar committed genocide
  against the Rohingya — the first state ever found guilty by the ICJ;
  Ukraine hits the Kerch Bridge a third time in four days, halting
  rail traffic; a Houthi missile damages Riyadh's PIF Tower, blowing
  out windows on 7–8 floors, with no one hurt.
- **Grid:** 15 more stories — Israel ends its Gaza tank raid, the
  record $81bn Anthropic IPO, a 1,101-point Dow plunge, Somalia
  expelling the UAE envoy, the Senate backing Trump on the Iran war,
  Denmark ratifying the Greenland deal, Mongolia's president quitting,
  Serbia's student-list speaker, Seoul's court overturning Han's
  sentence, a US–Venezuela military deal, Ethiopia–Eritrea on the
  brink, COP31 dropping fossil fuels, GTA VI launching, Trump's Iran
  weapons warning, and Cyclone Akvan nearing Odisha.
- **Inside:** 19 more one-line stories, from Berlin's €70bn Ukraine
  aid pledge to a US judge finding ICE officials in contempt.

Every story was reported on 19 November 2026 (Reuters, AP, WSJ, BBC,
Al Jazeera, IAEA, IEA and others — see `notes.md` for the source of
each story). Nothing is invented, hyped, or speculation shown as fact.
The live board on 20 Nov showed a top-50 cutoff near 98.90% across
more than 16,000 entries, so this page is built to be read at a glance:
the date and the lead are the biggest things on it.

## How it was built

The front page is composed with PIL: AI-generated scene photos (which
carry no text — the summit hall shows the Chinese, Russian and US
flags in front of a Great Wall painting, exactly as reported) plus
PIL-rendered captions, so every word is spelled exactly and the layout
is exact. `main.py` (Python 3, standard library only, no network)
copies the held image `news.jpg` to `/output/entry.png`,
deterministically — two runs write byte-identical files.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Licence

MIT — see `LICENSE`.
