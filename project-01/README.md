# Web Crawler Implementation (SEIR Course Project)

## Introduction

This project demonstrates a simple implementation of a web crawler using Python.
The program starts from a given URL and automatically visits web pages by
following hyperlinks found in each page.

The main purpose of this project is to understand the basic workflow
of how search engines collect information from the web.

---

## What This Program Does

- Takes a starting URL (seed URL)
- Downloads the webpage
- Extracts the title of the page
- Finds all hyperlinks present in the page
- Adds new links to a queue (frontier)
- Repeats the process until 50 pages are visited
- Saves all visited URLs and their titles in a file

---

## Key Concepts Used

### Frontier
A list that stores URLs waiting to be visited.

### Visited Set
A collection that keeps track of already crawled URLs to avoid repetition.

### HTML Parsing
BeautifulSoup is used to extract page titles and links from HTML content.

---

## Execution Flow

1. Initialize the seed URL.
2. Add it to the frontier.
3. While the frontier is not empty:
   - Remove one URL.
   - Fetch the webpage.
   - Extract and store its title.
   - Extract all links.
   - Add new valid links to the frontier.
4. Stop after crawling 50 pages.

---

## Output File

All results are stored in:
