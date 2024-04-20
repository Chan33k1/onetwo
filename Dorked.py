import sys
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import webbrowser

if len(sys.argv) < 2:
    print("Usage: python search_social_media.py <search_term> [time_period]")
    sys.exit()

search_term = sys.argv[1]
social_media_sites = [
    "twitter.com", 
    "facebook.com", 
    "instagram.com", 
    "rumble.com", 
    "reddit.com", 
    "telegram.org",
    "discord.com",
    "quora.com",
    "Pinterest"
]

time_period = sys.argv[2] if len(sys.argv) == 3 else "d"

if time_period == "h":
    time_range = "&tbs=qdr:h"
elif time_period == "w":
    time_range = "&tbs=qdr:w"
elif time_period == "m":
    time_range = "&tbs=qdr:m"
else:
    time_range = "&tbs=qdr:d"

for site in social_media_sites:
    url = f"https://www.google.com/search?q={site} {search_term}{time_range}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.find_all("a")
    for link in links:
        href = link.get("href")
        if site in href:
            try:
                response = requests.get(href)
                if response.status_code == 200:
                    print(link.text)
                    webbrowser.open(href)
            except:
                pass
