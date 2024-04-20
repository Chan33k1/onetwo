import sys
import requests
from bs4 import BeautifulSoup

def search_google(keyword):
    url = f"https://www.google.com/search?q={keyword}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.find_all("a")
    social_media_sites = [
        "twitter.com", 
        "facebook.com", 
        "instagram.com", 
        "rumble.com", 
        "reddit.com", 
        "telegram.org",
        "discord.com"
    ]
    live_links = []
    for link in links:
        href = link.get("href")
        for site in social_media_sites:
            if site in href:
                if "http" in href or "https" in href:
                    live_links.append(href)
                else:
                    live_links.append("https://" + href)
    return live_links

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python search_google.py <keyword>")
        sys.exit()
    keyword = sys.argv[1]
    live_links = search_google(keyword)
    print(live_links)