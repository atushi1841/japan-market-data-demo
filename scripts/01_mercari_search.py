#!/usr/bin/env python3
"""1. Mercari Japan search via Apify — print first 5 listings."""
import json, os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_API_TOKEN"])
run = client.actor("atushi1841/mercari-japan-search-scraper").call(
    run_input={"searchQuery": "anime figure", "maxResults": 50}
)
for item in run["data"]["items"][:5]:
    print(item["name"], item["price"])