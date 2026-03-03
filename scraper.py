import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class WebScraper:

    def __init__(self, address):

        if not address.startswith("http"):
            address = "https://" + address
        self.base_url = address

        print("Crawler initialized.")
        print("Website to crawl:", self.base_url)

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--blink-settings=imagesEnabled=false")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")

        self.browser = webdriver.Chrome(options=chrome_options)

    def load(self):
        print("\nConnecting to website...")
        self.browser.get(self.base_url)
        time.sleep(0.5)
        print("Website loaded.")

    def get_soup(self):
        print("\nExtracting HTML from page...")
        page = self.browser.page_source
        soup = BeautifulSoup(page, "html.parser")
        print("HTML extraction complete.")
        return soup

    def show_title(self, soup):
        print("\n--- TITLE ---")
        title_tag = soup.find("title")
        if title_tag:
            print(title_tag.text.strip())
        else:
            print("Title not available")

    def show_body(self, soup):
        print("\n--- BODY CONTENT ---\n")
        body_tag = soup.find("body")
        if body_tag:
            content = body_tag.get_text(separator=" ", strip=True)
            print(content)

    def show_outlinks(self, soup):

        print("\n--- OUTGOING LINKS ---\n")
        printed_links = set()
        for element in soup.find_all("a"):
            href = element.get("href")
            if href is None:
                continue

            current = urljoin(self.base_url, href)
            if current not in printed_links:
                print(current)
                printed_links.add(current)
        print("\nTotal links discovered:", len(printed_links))

    def start(self):

        self.load()
        soup = self.get_soup()
        self.show_title(soup)
        self.show_body(soup)
        self.show_outlinks(soup)
        print("\nScraping finished.")
        self.browser.quit()


if len(sys.argv) < 2:
    print("Please provide a URL")
    sys.exit()

scraper = WebScraper(sys.argv[1])
scraper.start()