import requests
from bs4 import BeautifulSoup

def search(query):
    url = f"https://www.google.com/search?q={query}&num=10"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    search_results = []
    for result in soup.select(".tF2Cxc"):
        link = result.select_one(".yuRUbf a")["href"]
        title = result.select_one(".yuRUbf").get_text()
        description = result.select_one(".IsZvec").get_text()
        search_results.append({"title": title, "link": link, "description": description})
    return search_results

query = input("Enter your search query: ")
results = search(query)
for result in results:
    print(result["title"])
    print(result["link"])
    print(result["description"])
    print()