import pprint
import requests

from bs4 import BeautifulSoup as BS
from bs4.element import NavigableString

from scrape.util import word_serp as ws

_JISHO_API_URL = "https://jisho.org/api/v1/search/words?keyword={word}"

def search_word(query: str):
    """
    This is the basic search function for a given word.
    Equivalent to Jisho's <query> #words
    By design, appending #words means this is a single word query search.
    """
    return ws.search(query)
