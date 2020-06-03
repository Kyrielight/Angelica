import graphene

class WordJapanese(graphene.ObjectType):
    word = graphene.String() # This could be blank for kana-only words
    reading = graphene.String(required=True)

class WordLink(graphene.ObjectType):
    text = graphene.String()
    url = graphene.String()

class WordSense(graphene.ObjectType):
    # TODO
    english_definitions = graphene.List(graphene.String)
    parts_of_speech = graphene.List(graphene.String)
    links = graphene.List(WordLink)
    tags = graphene.List(graphene.String, description="The meaning's tags, e.g. kana only")
    #restrictions = graphene.List(graphene.String)
    see_also = graphene.List(graphene.String)
    antonyms = graphene.List(graphene.String)
    #source = graphene.List(graphene.String)
    #info = graphene.List(graphene.String)

class Word(graphene.ObjectType):
    is_common = graphene.Boolean(description="The word's commonality")
    japanese = graphene.List(WordJapanese)
    jlpt = graphene.List(graphene.String, description="The word's JLPT level, if applicable.")
    senses = graphene.List(WordSense, description="The word's meaning(s)")
    slug = graphene.String(description="The word's slug")
    tags = graphene.List(graphene.String, description="The word's tags, e.g. WaniKani level")
