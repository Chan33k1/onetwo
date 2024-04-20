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
    url = f"https://duckduckgo.com/html/?q=site%3A{site}+{search_term}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.find_all("a", class_="result__url")
    for link in links:
        href = link.get("href")
        if site in href:
            print(href)