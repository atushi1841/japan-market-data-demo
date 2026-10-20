#!/usr/bin/env python3
"""2. Yahoo Auctions Japan keyword search — export to CSV."""
import csv, os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_API_TOKEN"])
run = client.actor("atushi1841/yahoo-auctions-japan-scraper").call(
    run_input={"keyword": "Nintendo Switch", "maxResults": 30}
)
with open("yahoo_sample.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["title", "price", "bid_count", "end_time"])
    for i in run["data"]["items"]:
        w.writerow([i["title"], i["price"], i["bids"], i["endTime"]])