import pprint
import requests

from bs4 import BeautifulSoup as BS
from bs4.element import NavigableString

from scrape.util import word_serp as ws

def basic():
    page = requests.get("https://jisho.org/search/%E5%B8%82")
    soup = BS(page.text, 'html.parser')
    #print(soup.find(id="main_results"))
    #print(soup.find_all("div", class_="exact_block"))

    words = list()

    """ Exact Matches """

    # While it's a class, the actual "exact_block" is essentially an ID'd div
    exact_results = soup.find_all("div", class_="exact_block")[0].find_all("div", class_="concept_light clearfix")
    #pprint.pprint(exact_results)
    for result in exact_results:

        text = ws.fetch_text(result)

        meanings = [meaning.contents[0].strip() for meaning in result.find_all("span", class_="meaning-meaning")]

        labels = ws.fetch_labels(result)
        #furigana = result.find("span", class_="furigana").contents[0].strip()

        print(text)
        print(meanings)
        print(labels)
        print()