#!/usr/bin/env python3
"""3. SUUMO real-estate search — lowest rent per city."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_API_TOKEN"])
run = client.actor("atushi1841/suumo-japan-real-estate-scraper").call(
    run_input={"searchText": "1LDK 新宿", "maxResults": 20}
)
lowest = min(run["data"]["items"], key=lambda x: x["rent"])
print(lowest["name"], lowest["rent"], lowest["address"])