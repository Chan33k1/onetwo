import sys
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def search_google(keyword, time_range="d"):
    social_media_sites = [
        "twitter.com", 
        "facebook.com", 
        "instagram.com", 
        "rumble.com", 
        "reddit.com", 
        "telegram.org",
        "discord.com"
    ]
    if time_range == "live":
        time_range_str = "&tbs=qdr:n10"
    elif time_range == "h":
        time_range_str = "&tbs=qdr:h"
    elif time_range == "w":
        time_range_str = "&tbs=qdr:w"
    elif time_range == "m":
        time_range_str = "&tbs=qdr:m"
    else:
        time_range_str = "&tbs=qdr:d"
    url = f"https://www.google.com/search?q={keyword}{time_range_str}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.find_all("a")
    live_links = []
    recent_links = []
    for link in links:
        href = link.get("href")
        for site in social_media_sites:
            if site in href:
                if "http" in href or "https" in href:
                    live_links.append(href)
                else:
                    live_links.append("https://" + href)
                if time_range == "live":
                    recent_links.append(href)
                else:
                    date_str = link.find("span", {"class": "f"}).text
                    date_obj = datetime.strptime(date_str, "%b %d, %Y")
                    if (datetime.now() - date_obj).days <= {"h": 1, "w": 7, "m": 30, "d": 365}[time_range]:
                        recent_links.append(href)
    return live_links, recent_links

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python search_google.py <keyword> [time_range]")
        sys.exit()
    keyword = sys.argv[1]
    time_range = sys.argv[2] if len(sys.argv) == 3 else "d"
    live_links, recent_links = search_google(keyword, time_range)
    print(f"Live Links ({len(live_links)}):")
    print(live_links)
    print(f"Recent Links ({len(recent_links)}):")
    print(recent_links)