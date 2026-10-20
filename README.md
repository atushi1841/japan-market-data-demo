# Japan Market Data Demo

**Real Japanese e-commerce data in 5 lines of Python — no scraping, no proxies.**

This repo is a runnable demo for the [Apify Store Japan Market Actors](https://apify.com/store/actors/japan-market-mcp) directory. Every CSV sample below came from a single Apify Actor run; every script below runs with `pip install apify-client` + a free [Apify token](https://apify.com).

## What is this?

Japan market data — real scraped market data from Japan's e-commerce marketplaces (Mercari, Yahoo Auctions, Rakuten, SUUMO, Kakaku.com) as ready-to-use sample CSV files plus 3 runnable Python web scraping snippets. No scraping infrastructure needed: the data comes from Apify Actors, and you can point the same scripts at the live marketplaces in under 10 lines.

## Why this exists

Japan is the world's third-largest economy and its secondhand markets (Mercari 5M+ daily listings, Yahoo Auctions 15M+ items, Rakuten ¥2T GMV) are invisible to most English-language data tooling. These 86 Apify Actors close that gap — and this repo proves they work.

## Sample CSVs (5 files, 5 rows each)

| Marketplace | File | Actor | Rows |
|---|---|---|---|
| Mercari Japan | [`data/samples/mercari_sample.csv`](data/samples/mercari_sample.csv) | [mercari-japan-search-scraper](https://apify.com/store/actors/mercari-japan-search-scraper) | 5 |
| Yahoo Auctions JP | [`data/samples/yahoo_sample.csv`](data/samples/yahoo_sample.csv) | [yahoo-auctions-japan-scraper](https://apify.com/store/actors/yahoo-auctions-japan-scraper) | 5 |
| Rakuten Ichiba | [`data/samples/rakuten_sample.csv`](data/samples/rakuten_sample.csv) | [rakuten-market-scraper](https://apify.com/store/actors/rakuten-market-scraper) | 5 |
| SUUMO (Real Estate) | [`data/samples/suumo_sample.csv`](data/samples/suumo_sample.csv) | [suumo-japan-real-estate-scraper](https://apify.com/store/actors/suumo-japan-real-estate-scraper) | 5 |
| Kakaku.com (Price Search) | [`data/samples/kakaku_sample.csv`](data/samples/kakaku_sample.csv) | [japan-kakaku-price-search](https://apify.com/store/actors/japan-kakaku-price-search) | 5 |

Schema notes: `price_jpy` is the listed price in Japanese yen; `status` is `On Sale` / `Sold` / `Bidding` / `Leased` / `In Stock` / `Out of Stock`.

## Python snippets (3, ≤10 lines each)

All three need only `pip install apify-client` and `export APIFY_API_TOKEN=...` (free tier: 1M credits/month).

### 1. Mercari Japan — search & print
[`scripts/01_mercari_search.py`](scripts/01_mercari_search.py)
```python
from apify_client import ApifyClient
import os
client = ApifyClient(os.environ["APIFY_API_TOKEN"])
run = client.actor("atushi1841/mercari-japan-search-scraper").call(
    run_input={"searchQuery": "anime figure", "maxResults": 50})
for item in run["data"]["items"][:5]:
    print(item["name"], item["price"])
```

### 2. Yahoo Auctions Japan — export to CSV
[`scripts/02_yahoo_auctions.py`](scripts/02_yahoo_auctions.py)
```python
import csv, os
from apify_client import ApifyClient
client = ApifyClient(os.environ["APIFY_API_TOKEN"])
run = client.actor("atushi1841/yahoo-auctions-japan-scraper").call(
    run_input={"keyword": "Nintendo Switch", "maxResults": 30})
with open("yahoo_sample.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["title", "price", "bid_count", "end_time"])
    for i in run["data"]["items"]:
        w.writerow([i["title"], i["price"], i["bids"], i["endTime"]])
```

### 3. SUUMO real estate — lowest rent
[`scripts/03_suumo_search.py`](scripts/03_suumo_search.py)
```python
import os
from apify_client import ApifyClient
client = ApifyClient(os.environ["APIFY_API_TOKEN"])
run = client.actor("atushi1841/suumo-japan-real-estate-scraper").call(
    run_input={"searchText": "1LDK 新宿", "maxResults": 20})
lowest = min(run["data"]["items"], key=lambda x: x["rent"])
print(lowest["name"], lowest["rent"], lowest["address"])
```

## Full Actor Directory

86 production-grade Actors across every Japanese marketplace — [browse the Apify Store catalog](https://apify.com/store/actors/japan-market-mcp).

## Buy the data pipeline (Gumroad)

The Actors above are free to run, but the curated weekly datasets built on top of them are sold on Gumroad:

- **FREE Sample** — [gumroad.com/l/kutuxe](https://atushi5.gumroad.com/l/kutuxe) ($0)
- **Weekly CSV Dataset** — [gumroad.com/l/agyhq](https://atushi5.gumroad.com/l/agyhq) ($3,999)
- **Weekly Report** — [gumroad.com/l/qdyyyi](https://atushi5.gumroad.com/l/qdyyyi) ($10)

## License

Samples are synthetic demo data generated for illustration. Scripts are MIT — see the [parent project](https://github.com/atushi1841/japan-market-data).