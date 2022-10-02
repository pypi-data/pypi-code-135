""" functions for package - detoxifier """

from flashtext import KeywordProcessor
from detoxifier.config import toxic_words_list


def check_textual_toxicity(data: str) -> int:
    """returns if toxic word is present or not"""
    is_toxic_word = 0
    kwp = KeywordProcessor(case_sensitive=False)
    kwp.add_keywords_from_list(toxic_words_list)
    result = kwp.extract_keywords(data, span_info=True)
    if len(result) != 0:
        is_toxic_word = 1
    return is_toxic_word


def detoxify_text(text: str) -> str:
    """replaces toxic words with * character """
    kwp = KeywordProcessor(case_sensitive=False)
    kwp.add_keywords_from_list(toxic_words_list)
    result = kwp.extract_keywords(text, span_info=True)
    for i in result:
        words = text[int(i[1]) : int(i[2])]
        length_of_words = len(words)
        fix_word = "*" * length_of_words
        text = text.replace(words, fix_word)
    return text
