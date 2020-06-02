"""
Utils for extracting data from Jisho All/Word SERP
"""

from bs4.element import NavigableString

def fetch_text(soup):
    """Scrape the Japanese text of the word"""
    return soup.find("span", class_="text").contents[0].strip()

#def fetch_meanings(soup):
#    """Fetch the raw meanings of the word"""

def fetch_labels(soup):
    labels = list()
    for label in soup.find_all("span", class_="label"):
        for descendant in label.descendants:
            if isinstance(descendant, NavigableString):
                labels.append(descendant.string.strip())
    return labels
