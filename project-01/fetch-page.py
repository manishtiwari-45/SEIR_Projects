import sys
import requests
from bs4 import BeautifulSoup

""" The program takes a URL from the command line,
sends an HTTP GET request using the requests library,
parses the HTML using BeautifulSoup, extracts the title and
body text using get_text(), and finds all anchor tags to print their
href links."""

if len(sys.argv) < 2:
    print("You did not provide a URL")
    sys.exit(1)

url = sys.argv[1]
print(f"Target URL found: {url}")
print(f"Fetching url {url} ...")

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

print("Page Title")
if soup.title:
    title_text = soup.title.get_text()
    print(title_text)
else:
    print("No Title")


print("Page Body")
if soup.body:
    body_text = soup.body.get_text()
    body_text = body_text.strip()
    print(body_text)
else:
    print("No Body")


print("All links")
links = soup.find_all("a")
for link in links:
    href = link.get("href")
    if href:
        print(href)


print("Fetching Done!")