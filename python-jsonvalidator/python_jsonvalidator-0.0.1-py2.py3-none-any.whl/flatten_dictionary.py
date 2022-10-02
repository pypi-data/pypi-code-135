"""
Flatten a dictionary
"""
from typing import Generator


class FlattenDictionary:
    def _get_dictionary_values(self, dictionary: dict) -> Generator:
        """
        get nested dictionary values
        """
        for key, value in dictionary.items():
            if type(value) == dict:
                yield from self._get_dictionary_values(value)
            elif type(value) == list:
                if len(value) > 0 and type(value[0]) == dict:
                    for item in value:
                        if type(item) == dict:
                            yield from self._get_dictionary_values(item)
                else:
                    yield (key, value)
            else:
                yield (key, value)

    def flatten_dictionary(self, dictionary: dict) -> dict:
        """
        return a simple {key : value} object from a nested dictionary
        """
        if not isinstance(dictionary, dict):
            return {
                "valid": False,
                "error": (
                    f"expected an object type 'dict'"
                    f" but received type {type(dictionary)} as argument"
                ),
            }

        res = {}
        for key, value in self._get_dictionary_values(dictionary):
            if key not in res:
                res[key] = value
        return res
