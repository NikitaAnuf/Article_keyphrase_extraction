from pymorphy3 import MorphAnalyzer

import re

from variables import CHARACTER_ASCII_CODES


def preprocess(text: str) -> str:
    def clean_text(text: str) -> str:
        text = re.sub(r'[ ]*((рис.\s*((\d+)|(\d+–\d+)))|(табл.\s*((\d+)|(\d+–\d+)))|(таблица\s*\d+))', '', text)
        text = re.sub(r'[ ]*((\([\d\s]\))|\[.+\])', '', text)
        text = text.replace('-\n', '')
        text = re.sub(r'[\t\n]', ' ', text)

        return text

    def lemmatize(text: str) -> str:
        morph = MorphAnalyzer()

        words = text.split()

        for i in range(len(words)):
            if ord(words[i][-1]) in CHARACTER_ASCII_CODES:
                words[i] = morph.parse(words[i])[0].normal_form
            else:
                character = words[i][-1]
                words[i] = morph.parse(words[i][:-1])[0].normal_form + character

        text = ' '.join(words)
        return text

    text = clean_text(text)
    text = lemmatize(text)
    return text
