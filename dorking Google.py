import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print("Usage: python search_social_media.py <search_term>")
    sys.exit()

search_term = sys.argv[1]
social_media_sites = [
    "twitter.com", 
    "facebook.com", 
    "instagram.com", 
    "rumble.com", 
    "reddit.com", 
    "telegram.org",
    "discord.com"
]

for site in social_media_sites:
    url = f"https://www.google.com/search?q={site} {search_term}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.find_all("a")
    for link in links:
        href = link.get("href")
        if site in href:
            print(href)