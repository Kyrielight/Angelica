"""
Utils for extracting data from Jisho All/Word SERP
Fortunately, words can be extracted directly through the JSON API.
"""

import json
import pprint
import requests

from bs4.element import NavigableString
from deprecated import deprecated
from graphql import GraphQLError

from structure.word.types import Word, WordSense, WordLink, WordJapanese
from typing import List

_JISHO_API_URL = "https://jisho.org/api/v1/search/words?keyword={word}"

def _create_wordjapanese(words):
    """Converts the word's Japanese entries into GraphQL WordJapanese objects"""
    ret = list()
    for word in words:
        try:
            ret.append(WordJapanese(word=word['word'], reading=word['reading']))
        except:
            ret.append(WordJapanese(reading=word['reading']))
    return ret

def _create_wordlink(links):
    """Converst the word's links to GraphQL WordLink objects"""
    ret = list()
    for link in links:
        try:
            ret.append(WordLink(text=link['text'], url=link['url']))
        except:
            ret.append(WordLink(url=link['url']))
    return ret

def _create_wordsense(senses):
    """Converts the word's senses into GraphQL WordSense objects"""
    ret = list()
    for sense in senses:
        antonyms = sense['antonyms']       
        english_definitions = sense['english_definitions']
        links = _create_wordlink(sense['links'])
        parts_of_speech = sense['parts_of_speech']
        see_also = sense['see_also']
        tags = sense['tags']

        ret.append(WordSense(
            english_definitions=english_definitions,
            parts_of_speech=parts_of_speech,
            links=links,
            tags=tags,
            see_also=see_also,
            antonyms=antonyms
        ))
    return ret

def search(query: str) -> List[Word]:
    request = requests.get(_JISHO_API_URL.format(word=query))

    if request.status_code != 200:
        # Error in connecting - Is Jisho Down?
        raise GraphQLError("Unable to connect to Jisho's API, is Jisho down?")

    data = request.json()
    if data['meta']['status'] != 200:
        return list() # Empty response
    
    words = list() # Store all words in a list to return

    for word in data['data']:

        # Common Word Entries
        is_common = bool(word['is_common'])
        japanese = _create_wordjapanese(word['japanese'])
        jlpt = word['jlpt']
        senses = _create_wordsense(word['senses'])
        slug = word['slug']
        tags = word['tags']

        words.append(Word(
            is_common=is_common,
            japanese=japanese,
            jlpt=jlpt,
            senses=senses,
            slug=slug,
            tags=tags
        ))

    return words

"""Temporarily deprecated methods"""

@deprecated
def fetch_text(soup):
    """Scrape the Japanese text of the word"""
    return soup.find("span", class_="text").contents[0].strip()

@deprecated
def fetch_meanings(soup):
    """Fetch meanings for each word"""
    #meanings = [meaning.contents[0].strip() for meaning in result.find_all("span", class_="meaning-meaning")]
    meanings_root = soup.find("div", class_="meanings-wrapper")

    for child in meanings_root.find_all("div", recursive=False):
        print(child)

    return "meaning"

@deprecated
def fetch_labels(soup):
    """Fetches labels from each word, like JLPT level"""
    labels = list()
    for label in soup.find_all("span", class_="label"):
        for descendant in label.descendants:
            if isinstance(descendant, NavigableString):
                labels.append(descendant.string.strip())
    return labels
