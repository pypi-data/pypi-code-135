from ._pyhanja import Dictionary, DictionaryItem, Convert, MatchPosition

from importlib import resources as _resources

_dict_file = None

with _resources.path("pyhanja.data", "hanja.txt") as p:
    _dict_file = str(p)

default_dict = Dictionary()

default_dict.add_data(_dict_file)


def default_convert(query: str):
    return Convert(query, default_dict)
