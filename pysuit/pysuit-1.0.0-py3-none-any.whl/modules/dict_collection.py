# -*- coding: utf-8-*-
"""
###### Dict Collections #######
## Version 0.1 ##

# ---- List of fuctions -----
# dictsort = dict by keys and values are sorted
"""

import logging
from pysuit.interface import PySuit


class DictCollections(PySuit):
    """
    List of dict collections
    """

    __name__ = "pysuit.DictCollections()"

    def dictsort(self, dictionary, flag='keys'):
        """
        Sorting dict by keys or values
        """
        try:
            final_dict = {}
            # Sorting dict by values
            if flag.lower() == "values":
                sorted_dict = sorted(
                    list(dictionary.values()),
                    key=lambda x: (len(str(x)), str(x))
                )
                for value in sorted_dict:
                    key_result = [
                        key for key in dictionary if dictionary[key] == value
                    ]
                    final_dict[key_result[0]] = value
            # Sorting dict by keys
            else:
                sorted_dict = sorted(
                    list(dictionary.keys()),
                    key=lambda x: (len(str(x)), str(x))
                )
                final_dict = {key: dictionary[key] for key in sorted_dict}

            return final_dict

        except Exception as errors:
            logging.exception(f"error while accessing the dict: {errors}")
            raise errors
