# -*- coding: utf-8-*-

"""
Nested Collections
"""
# ---- List of fuctions -----

from pysuit.interface import PySuit


class NestedCollections(PySuit):
    """
        Nested to single Sort
    """
    __name__ = "pysuit.NestedCollections()"
    """
        created function ===> removNested
    """
    output = []

    def nested_iterator(self, nested_element):

        """
        function used for removing nested
        """
        try:

            if len(nested_element) == 0:
                self.output = []

            if type(nested_element) == set:
                for element in nested_element:
                    if type(element) in [tuple, frozenset]:

                        self.nested_iterator(element)
                    else:
                        self.output.append(element)

            else:
                for element in nested_element:
                    if type(element) in [list, tuple, set]:
                        self.nested_iterator(element)

                    else:
                        self.output.append(element)

        except Exception as e:

            raise e

        if type(nested_element) is tuple:
            return tuple(self.output)
        elif type(nested_element) is set:
            return set(self.output)
        else:
            return self.output
