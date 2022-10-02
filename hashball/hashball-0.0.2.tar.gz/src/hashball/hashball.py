# MIT License
#
# Copyright (c) 2021 Kevin L.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from copy import deepcopy
from chash import CircularHash
from .chash_exceptions import *
from .chash_visualize import visualize_hashball


class hashball:
    def __init__(self):
        self.__circlehash = dict()

    # PUBLIC METHODS =============================================================================
    def add(self, key, value):
        hashb = CircularHash(key, value)
        cirhashkey = self.__generate_circular_key(key)
        self.__circlehash[cirhashkey] = hashb

    def get(self, key):
        cirhashkey = self.__generate_circular_key(key)
        try:
            value = self.__circlehash[cirhashkey]
        except KeyError as ex:
            return None
        return value

    def has_key(self, key):
        cirhashkey = self.__generate_circular_key(key)
        return self.__circlehash.__contains__(cirhashkey)

    def remove(self, key=None, value=None, all_values=False):
        if key == None and value == None:
            return
        if key != None and value != None:
            raise CHashException("Remove should only take in 1 parameter but 2 were given. Either key or value. ")
        
        if key != None:
            cirhashkey = self.__generate_circular_key(key)  # generate circular hash key
            value = self.__get_with_cirhashkey(cirhashkey)  # ensure key exist in 
            del self.__circlehash[cirhashkey]

        if value != None:
            for k, v in self.items():
                print(f"{v} vs {value}")
                if v == value:
                    del self.__circlehash[self.__generate_circular_key(k)]
                if not all_values:
                    return

    def items(self):
        return [[v.key, v.value] for v in self.__circlehash.values()]

    def keys(self, circular_key=False):
        if circular_key:
            return [k for k in self.__circlehash.keys()]
        else:
            return [v.key for v in self.__circlehash.values()]

    def values(self):
        return [v.value for v in self.__circlehash.values()]

    def copy(self):
        return deepcopy(self)

    def visualize(self):
        visualize_hashball(self.keys(circular_key=True))

    # PRIVATE METHODS =============================================================================
    def __generate_circular_key(self, key):
        def shift_decimal(number, shift, base=10):
            return number * base ** shift

        try:
            h = hash(key)
            if h > 0:
                h = shift_decimal(h, -len(str(h)))
            else:
                h = shift_decimal(h, -len(str(h)) + 1)
            cirhashkey = h * 360
        except TypeError as ex:
            raise CHashHashException(str(ex))
        return cirhashkey

    def __get_with_cirhashkey(self, cirhashkey):
        try:
            value = self.__circlehash[cirhashkey]
        except KeyError as ex:
            raise CHashKeyExeption(str(ex))
        return value

    def print_all(self):
        print("Circular Hash Table")
        for k, v in self.__circlehash.items():
            print(f"{k} :\t{v.__str__()}")
        print("")


if __name__ == "__main__":
    cdict = hashball()
    for i in range(100):
        cdict.add(f"thisisakey{i}", "thisisthevalue")

    print(cdict.visualize())