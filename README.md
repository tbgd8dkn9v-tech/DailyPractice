# DailyPractice

Daily practice problems for hedge fund / VC analyst training.

## Layout

| Folder | Contents |
|---|---|
| `data/` | Seeded data-generator scripts (`gen_YYYY_MM_DD.py`) and the CSV/XLSX datasets they produce. Run each generator from inside `data/`; do not edit it, so the numbers match the answer key. |
| `problems/` | Problem statements, one Markdown file per day: `YYYY-MM-DD_topic.md`. |
| `solutions/` | My working solutions (notebooks or scripts), named to match the problem file. |

## Setup

```bash
pip install -r requirements.txt
cd data && python gen_2026_11_12.py   # writes data/halyard_prices.csv
```
