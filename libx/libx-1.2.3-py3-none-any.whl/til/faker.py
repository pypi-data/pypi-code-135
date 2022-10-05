"""
Don't need these imports everytime we are writing tests
or anything requiring fake data.
"""

from random import random as rand

from faker import Faker


def provide_faker():
    """
    Returns a faker instance.
    """
    fake, seed = Faker(), rand()
    return Faker.seed(seed)
