from utils.preprocessing import preprocess
from utils.extract_keyphrases import extract_keyphrases
from utils.print_keyphrases import print_results


def extract(text: str, do_print: bool = False) -> list[list[str]]:
    text = preprocess(text)
    keyphrases = extract_keyphrases(text)

    if do_print:
        print_results(keyphrases)

    return keyphrases
