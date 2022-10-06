"""
File:          rand.py
File Created:  2022-10-05 20:34:12
Author:        callmexss (callmexss@126.com)
Description:   handy random tools.
"""

import random
import string


class RandomHandy:
    """A worker who generates random things."""

    def __init__(self, _rand=None):
        """Construct a RandomHandy.
        
        Arguments:
            rand (random.Random) -- an instance of random.Random class
        """
        if _rand and not isinstance(_rand, random.Random):
            raise TypeError("Not a random.Random instance.")

        self.rand = _rand if _rand else random.Random()

    def generate_num_list(
        self, size=10, scope=(-100, 100), duplicated=False, element_type=int
    ):
        """Generate a random list.
        
        Keyword Arguments:
            size (int) -- the length of the list (default: 10)
            scope (tuple) -- the scope of the elements (default: (-100, 100))
            duplicated (bool) -- unique or not (default: False)
            element_type (type) -- the type of elements, int or float (default: int)
        
        Returns:
            list -- a random generated list
        """
        start, end = scope
        if size > (end - start) and not duplicated:
            raise ValueError(
                f"The size `{size}` is larger than the given scope `{scope}` "
                "to generate a unique random list."
            )

        if duplicated:
            ret = [self.rand.randint(start, end) for _ in range(size)]
        else:
            ret = self.rand.sample(range(start, end), size)

        if element_type is float:
            return [self.rand.random() * x for x in ret]

        return ret

    def generate_int_array(self, n=100, range_l=0, range_r=100):
        """Generate a random integer array
        
        Arguments:
            n (int) -- size of the array
            range_l (int) -- left boundary
            range_r (int) -- right boundary
        
        Returns:
            list -- a list of random integers
        """
        assert range_l < range_r
        return [random.randint(range_l, range_r) for _ in range(n)]

    def generate_nearly_ordered_array(self, n=100, swap_times=10):
        """Generate a nearly ordered array
        
        Arguments:
            n (int) -- size of the array
            swap_times (int) -- swap times
        
        Returns:
            list -- a nearly ordered array
        """
        li = [i for i in range(n)]
        for _ in range(swap_times):
            pos_x = random.randint(0, n - 1)
            pos_y = random.randint(0, n - 1)
            li[pos_x], li[pos_y] = li[pos_y], li[pos_x]
        return li

    def generate_string(self, size=10, unique=False, provider=None):
        """Generate a random string.

        Args:
            size (int, optional): length of string. Defaults to 10.
            unique (bool, optional): unique or not. Defaults to False.
            provider (str, optional): a string as provider. Defaults to None.

        Raises:
            ValueError: when need unique and not enough strings are provided

        Returns:
            str: a random string with given length
        """
        if not provider:
            provider = string.ascii_letters + string.digits

        if unique and size > len(provider):
            raise ValueError("not enough provider to generate unique random string")

        buffer = []
        while len(buffer) < size:
            c = random.choice(provider)
            if unique and c in buffer:
                continue

            buffer.append(c)

        return ''.join(buffer)