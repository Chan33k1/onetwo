import requests

def search_for_results(keyword):
    urls = [
        "https://www.facebook.com", 
        "https://t.me", 
        "https://www.google.com/search?q="
        "https://instagram.com"
        
    ]
    found_results = []
    for url in urls:
        if url == "https://www.google.com/search?q=":
            full_url = url + keyword.replace(" ", "+")
        else:
            full_url = url
        try:
            response = requests.get(full_url)
        except requests.exceptions.RequestException as e:
            print(f"Error accessing {full_url}: {e}")
            continue
        if response.status_code == 200:
            content = response.text
            if keyword in content:
                found_results.append(full_url)
                print(f"Keyword '{keyword}' found in {full_url}")
            else:
                print(f"Keyword '{keyword}' not found in {full_url}")
        else:
            print(f"Error accessing {full_url}. Status code: {response.status_code}")
    if found_results:
        print(f"Results found at: {', '.join(found_results)}")
    else:
        print("No results found.")

search_for_results("Giovanni")