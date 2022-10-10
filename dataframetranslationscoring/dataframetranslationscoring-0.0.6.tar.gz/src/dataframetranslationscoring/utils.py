from nltk.tokenize import word_tokenize
from collections import Counter
import numpy as np
import pandas as pd
import glob

def pd_read_pattern(pattern):
    files = glob.glob(pattern)

    df = pd.DataFrame()
    for f in files:
        df = df.append(pd.read_csv(f))

    return df.reset_index(drop=True)

df = pd_read_pattern('somefile*.csv')

def remove_punc(string):
    punc = """!()-[]{};:'"\, <>./?@#$%^&*_~1234567890"""
    for ele in string:
        if ele in punc:
            string = string.replace(ele, "")
    return string


def diff(text1, text2):
    text1 = text1.replace(" ", "")
    text2 = text2.replace(" ", "")
    return sum(c1 != c2 for c1, c2 in zip(text1, text2)) / len(text1)


def translation_quality_scores(original_text, translated_text):
    """
    This function takes two strings as input and returns three translation quality score.
    The score is calculated by comparing the original text to the translated text.
    The score is a float between 0 and 1.

    Args:
          original_text (str): The original text.
          translated_text (str): The translated text.

      Returns:
          characters_translated_vs_available: The percentage of characters translated vs characters available.
          words_translated_vs_available: The percentage of words translated vs words available.
          characters_to_translate: The number of characters to be translated.
    """
    # tokenize the strings
    original_token = word_tokenize(original_text)
    translated_token = word_tokenize(translated_text)
    # remove punctuation
    original_token = [remove_punc(i) for i in original_token]
    # remove empty strings
    original_token = list(filter(None, original_token))
    # lowercase
    original_token = [x.lower() for x in original_token]
    translated_token = [x.lower() for x in translated_token]
    # list of translated words
    translated_words = list(
        (Counter(original_token) - Counter(translated_token)).elements()
    )
    # calculate the scores

    characters_translated_vs_available = sum([len(i) for i in translated_words]) / sum(
        [len(i) for i in original_token]
    )

    sum_words_translated = len(translated_words)

    sum_words_original = len(original_token)

    sum_characters_translated = sum([len(i) for i in translated_words])

    sum_characters_original = sum([len(i) for i in original_token])

    words_translated_vs_available = len(translated_words) / len(original_token)

    characters_to_translate = sum(len(x) for x in original_text.split())

    return (
        characters_translated_vs_available,
        words_translated_vs_available,
        characters_to_translate,
        sum_words_translated,
        sum_words_original,
        sum_characters_translated,
        sum_characters_original
    )
