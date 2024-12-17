from nlp_rake import Rake
from nltk.corpus import stopwords


def extract_keyphrases(text: str) -> list[list[str]]:
    stops = list(set(stopwords.words('russian')))

    keyphrases = []
    for word_number in range (5, 0, -1):
        rake = Rake(stopwords=stops, max_words=word_number, language_code='ru')
        res = rake.apply(text)[:2]
        for r in res:
            keyphrases.append(r[0].split())

    return keyphrases
