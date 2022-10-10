# -*- coding: utf-8-*-
"""
###### ganerate randam datatype Collections #######
## Version 0.1 ##

# ---- List of fuctions -----
# dictsort = dict by keys and values are sorted
"""
import random
import logging
from faker import Faker
from pysuit.interface import PySuit


class DataTypeCollection(PySuit):
    """
    List of fake datatype generator collections
    """

    __name__ = "pysuit.DataTypeCollection()"

    def fake_random_datatype(self, data_type, size):
        """
        Sorting dict by keys or values
        """
        try:
            fake = Faker()
            random_list = [fake.word(), fake.pyfloat(), fake.random_int()]

            # genrate fake random dict
            if data_type is dict:
                fake_dict = {}
                for lenght in range(size):
                    value = random.choice(random_list)
                    key = fake.random_int()
                    fake_dict.update({key: value})
                return fake_dict

            # generate fake random list
            if data_type in [list, tuple]:
                fake_list = []
                for lenght in range(size):
                    item = random.choice(random_list)
                    fake_list.append(item)

                # generate fake random tuple
                if data_type is tuple:
                    return tuple(fake_list)

                return fake_list

            # generate fake random set
            if data_type is set:
                fake_set = set()
                for lenght in range(size):
                    item = fake.random_int()
                    fake_set.add(item)
                return fake_set

        except Exception as errors:
            logging.exception(f"error while accessing the dict: {errors}")
            raise errors
