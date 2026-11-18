# Tuesday 17 November 2026 — The World in One Picture

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/reren-dev/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/reren-dev/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

## Dense 35-Story Broadsheet Front Page

This entry presents a dense, comprehensive broadsheet front page summing up the world's news of **Tuesday 17 November 2026** across 6 continents and 35 verified stories:

- **Top Section (3 Large Illustrated Stories):** Ukraine strikes Crimean Bridge, Tanker explosions near Hormuz, and Trump-Xi-Putin Shenzhen summit. Each illustrated scene features distinct, recognisable visual elements drawn via PIL.
- **Middle Grid (8 Medium Illustrated Stories):** Japan jet scrambles, US intel on Iran dirty bomb, Estonia border closure, COP31 final week, Microsoft global outage, UK settlement sanctions, Argentina 5-goal rout, and Depardieu guilty plea.
- **Bottom Strip:**
  - **Left:** "Where It Happened" world map generated from simplified Natural Earth land outlines (equirectangular projection with land in pale green on pale blue sea) with numbered coordinate dots for stories 1–11.
  - **Right:** Numbered list of stories 12–35 covering global politics, conflicts, UN treaties, climate pledges, sports, and economic data ("ALSO ON TUESDAY 17 NOVEMBER").

## Design Fixes in This Version
1. **No Truncation:** All headlines and summaries (including Headline #5: "US intel: Iran weighing 'dirty bomb'") are rendered using strict programmatic word wrapping and boundary checks that raise on overflow instead of silently dropping words.
2. **Real World Map:** Replaced abstract blobs with a verified land outline from Natural Earth data, accurately positioning numbered coordinate dots for global events.
3. **Recognisable Mini-Scenes:** All 11 illustrated story cards feature multi-element mini-scenes drawn in PIL (bridges, tankers, flags, jets, Capitol dome, border checkpoint, COP31 stage, monitors, Big Ben, football pitch, and courthouse).

## How `main.py` Works

`main.py` is written in Python 3.13 using standard library modules only (`os`, `shutil`). It:
1. Determines the target output directory from the `MAKEFUN_OUTPUT_DIR` environment variable (falling back to `/output`).
2. Resolves the source path of `entry.png` relative to the script directory.
3. Copies `entry.png` byte-identically to the output directory (`/output/entry.png`).
4. Validates that the file size is within limits ($\le 1$ MiB, exactly 1024x1024 pixels).
