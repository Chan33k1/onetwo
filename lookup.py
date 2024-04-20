```python
import re
import requests

def lookup_email(email):
    url = f"https://www.spokeo.com/email-search/search?email={email}"
    response = requests.get(url)
    if response.status_code == 200:
        results = re.findall(r'<a href="/[^"]+" class="name-link">([^<]+)</a>', response.text)
        return results
    else:
        return []

def lookup_phone(phone):
    url = f"https://www.spokeo.com/reverse-phone-lookup/search?q={phone}"
    response = requests.get(url)
    if response.status_code == 200:
        results = re.findall(r'<a href="/[^"]+" class="name-link">([^<]+)</a>', response.text)
        return results
    else:
        return []

email = "example@example.com"
phone = "1234567890"

email_results = lookup_email(email)
phone_results = lookup_phone(phone)

print("Email Results:")
for result in email_results:
    print(result)

print("\nPhone Results:")
for result in phone_results:
    print(result)
```
Note: This code uses the `requests` library to send HTTP requests and the `re` module for regular expression matching.