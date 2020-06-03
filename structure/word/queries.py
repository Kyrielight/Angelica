import graphene
import pprint

from scrape import search
from structure.word.types import Word

class WordQuery(graphene.ObjectType):
    word = graphene.List(Word, search=graphene.String(required=True))

    def resolve_word(self, info, **kwargs):
        return search.search_word(kwargs['search'])