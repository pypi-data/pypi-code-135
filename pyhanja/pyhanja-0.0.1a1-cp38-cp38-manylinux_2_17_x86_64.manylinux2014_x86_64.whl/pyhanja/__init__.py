from ._pyhanja import Dictionary, DictionaryItem, Convert, MatchPosition

from importlib import resources as _resources

_dict_file = None

with _resources.path("pyhanja.data", "hanja.txt") as p:
    _dict_file = str(p)


def default_dict():
    ret = Dictionary()
    ret.add_data(_dict_file)
    return ret
