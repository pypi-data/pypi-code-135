""" Application that takes a string and returns the number of unique characters in the string """
from collections import Counter
from functools import lru_cache


class ValueException(Exception):
    pass


@lru_cache(maxsize=128)
def count_letter(word: str) -> int:
    if not isinstance(word, str):
        raise ValueException("Please pass only str")
    number_chars = Counter(word)
    return sum([number_chars[symbol] == 1 for symbol in number_chars])
