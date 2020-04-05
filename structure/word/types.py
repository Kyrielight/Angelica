import graphene

class WordMeaning(graphene.ObjectType):
    meaning = graphene.String(description="The word's meaning", required=True)

    supplemental_info = graphene.String(
        default_value="None",
        description="This meaning's supplemental info")

class Word(graphene.ObjectType):
    text = graphene.String(description="The word's text", required=True)
    meaning = graphene.List(WordMeaning, description="The world's meaning(s)", required=True)
    tags = graphene.List(graphene.String, description="The word's tags")
    other_forms = graphene.String(description="The word's other forms")
    notes = graphene.String(description="The word's notes")