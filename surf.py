import requests

# Define the function to search for results in Facebook, Telegram, and webpages
def search_for_results(keyword):
    urls = [
        "https://www.facebook.com", 
        "https://t.me", 
        "https://www.google.com/search?q="
    ]
    for url in urls:
        if url == "https://www.google.com/search?q=":
            full_url = url + keyword.replace(" ", "+")
        else:
            full_url = url
        response = requests.get(full_url)
        if response.status_code == 200:
            content = response.text
            if keyword in content:
                print(f"Keyword '{keyword}' found in {full_url}")
            else:
                print(f"Keyword '{keyword}' not found in {full_url}")
        else:
            print(f"Error accessing {full_url}. Status code: {response.status_code}")

# Example usage of the function
search_for_results("Arvind")
