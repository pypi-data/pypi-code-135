'''
File:          context.py
File Created:  2022-10-06 14:09:10
Author:        callmexss (callmexss@126.com)
Description:   handy context manager.
'''

import os


def load_set(filename):
    if not os.path.exists(filename):
        return set()

    with open(filename, 'r') as f:
        li = f.readlines()
    
    return {x.strip() for x in li}

    
def save_set(filename, hash_set):
    with open(filename, 'w') as f:
        f.writelines([x + "\n" for x in hash_set])


class Checker:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.set = load_set(filename)

    def __enter__(self):
        return self

    def insert(self, value):
        if value in self.set:
            print(f"{value} already exists.")
        else:
            self.set.add(value)

    def __exit__(self, exc_type, exc_value, traceback):
        save_set(self.filename, self.set)
        if exc_type:
            print(exc_value)
            print(traceback)
