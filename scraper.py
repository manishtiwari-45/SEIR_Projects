import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


if len(sys.argv) != 2:
    print("Invalid URL givel, Try Again!")
    sys.exit()

url = sys.argv[1]

if not url.startswith("http"):
    url = "https://" + url

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

try:
    response = requests.get(url, headers=headers)
except:
    print("Failed to fetch webpage")
    sys.exit()

soup = BeautifulSoup(response.text, "html.parser")

# Extract Title
print("Title : ")
if soup.title:
    print(soup.title.get_text().strip())
else:
    print("No Title Found")
print()

# Extract Body Text
print("Body Text: ")
if soup.body:
    body_text = soup.body.get_text(" ", strip=True)
    print(body_text)
print()

# All links
print("Links: ")
links = soup.find_all("a")
seen = set()
for link in links:
    href = link.get("href")
    if href:
        full_link = urljoin(url, href)
        if full_link not in seen:
            print(full_link)
            seen.add(full_link)