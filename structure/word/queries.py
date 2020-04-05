import graphene

from structure.word.types import Word

class WordQuery(graphene.ObjectType):
    word = graphene.Field(Word, search=graphene.String(required=True))

    def resolve_word(self, info, **kwargs):
        return Word(text="Feature In Development")