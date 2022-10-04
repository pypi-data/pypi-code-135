import random


def generate_key(inp):
    key = ""
    for i in inp:
        key += chr(random.choice(range(32, 176)))
    return key

