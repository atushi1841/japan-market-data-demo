# t_3c3c1048 — japan-market-data-demo GitHub 検索発見性向上 / verification evidence

**Task ID:** t_3c3c1048
**Date:** 2026-10-20
**Owner:** atushi1841

---

## verification_evidence

### 1. Topics set (>=5)

```bash
$ curl -s https://api.github.com/repos/atushi1841/japan-market-data-demo | python3 -c "import json,sys;d=json.load(sys.stdin);print('topics:',d.get('topics'))"
topics: ['apify', 'japan', 'japan-market-data', 'kakaku', 'mercari', 'python', 'suumo', 'web-scraping', 'yahoo-auctions']
```

Count = 9 (threshold: 5) → PASS

Note: The raw `curl` PATCH `/repos/...` silently returned `topics: []` despite HTTP 200. The `gh repo edit --add-topic` path succeeded. Final state confirmed via GET.

### 2. README search keywords (>=3 match lines)

```bash
$ curl -s https://raw.githubusercontent.com/atushi1841/japan-market-data-demo/main/README.md | grep -icE "japan market data|sample csv|scraping"
4
```

New section added at line 7–9 (between intro paragraph and "## Why this exists"):
```markdown
## What is this?

Japan market data — real scraped market data from Japan's e-commerce marketplaces (Mercari, Yahoo Auctions, Rakuten, SUUMO, Kakaku.com) as ready-to-use sample CSV files plus 3 runnable Python web scraping snippets. No scraping infrastructure needed: the data comes from Apify Actors, and you can point the same scripts at the live marketplaces in under 10 lines.
```

Existing Gumroad / Apify links (lines 70–76) unchanged.

### 3. GitHub search rank check

```bash
$ curl -s "https://api.github.com/search/repositories?q=japan+market+data+csv&per_page=5" | python3 -c "import json,sys;d=json.load(sys.stdin);print('total_count:',d.get('total_count'));[print(' ',r['full_name'],r.get('stargazers_count')) for r in d.get('items',[])]"
total_count: 3
  atushi1841/japan-market-data-demo 0
  atushi1841/japanese-hobby-price-dataset 0
  jettbrains/-L- 164
```

Repo ranks **#1** for "japan market data csv" query (minutes after push).

### 4. Git history

```bash
$ git log --oneline -3
572fef3 t_3c3c1048: add What is this? section + search keywords for GitHub search discoverability
1f33e5e fix: remove bullet prefix from command citations
608430f Move verification report to reports/ (guard naming)
```

Pushed to `main` at `2026-10-20T00:40` (JST). Commit `1901000` adds this evidence report.
