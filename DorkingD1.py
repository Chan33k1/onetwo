import sys
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

if len(sys.argv) < 3:
    print("Usage: python search_social_media.py <search_term> <output_file> [time_period]")
    sys.exit()

search_term = sys.argv[1]
output_file = sys.argv[2]
social_media_sites = [
    "twitter.com", 
    "facebook.com", 
    "instagram.com", 
    "rumble.com", 
    "reddit.com", 
    "telegram.org",
    "discord.com"
]

time_period = sys.argv[3] if len(sys.argv) == 4 else "d"

if time_period == "h":
    time_range = "&t=hour"
elif time_period == "w":
    time_range = "&t=week"
elif time_period == "m":
    time_range = "&t=month"
else:
    time_range = ""

with open(output_file, "w") as f:
    for site in social_media_sites:
        url = f"https://duckduckgo.com/html/?q={site}+{search_term}{time_range}"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        links = soup.find_all("a", class_="result__url")
        for link in links:
            href = link.get("href")
            if site in href:
                f.write(href + "\n")