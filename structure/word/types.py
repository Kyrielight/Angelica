import graphene

class WordMeaning(graphene.ObjectType):
    meaning = graphene.String(description="The word's meaning", required=True)
    meaning_tags = graphene.String(description="The word's meaning tags")
    meaning_abstract = graphene.String(description="The word's abstract")

    supplemental_info = graphene.String(
        default_value="None",
        description="This meaning's supplemental info")

class Word(graphene.ObjectType):
    text = graphene.String(description="The word's text", required=True)
    meaning = graphene.List(WordMeaning, description="The world's meaning(s)")
    labels = graphene.List(graphene.String, description="The word's labels")
    other_forms = graphene.String(description="The word's other forms")
    notes = graphene.String(description="The word's notes")
    exact_match = graphene.Boolean(description="If this word is an exact match with the search")