import requests
from bs4 import BeautifulSoup

def search_google(Opera):
    url = "https://www.google.com/search"
    params = {
        "q": opera
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, params=params, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    search_results = soup.select(".g")
    for result in search_results:
        title = result.select_one(".rc > .r > a")
        if title:
            print(title.text)
            print(title["href"])