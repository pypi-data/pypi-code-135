'''
File:          hashtool.py
File Created:  2022-10-06 14:13:15
Author:        callmexss (callmexss@126.com)
Description:   handy hash tools.
'''

import hashlib
import os


def md5sum(input=""):
    if not os.path.exists(input):
        return hashlib.md5(input.encode()).hexdigest()

    md5 = hashlib.md5()
    with open(input, 'rb') as f:
        for line in f:
            md5.update(line)

    return md5.hexdigest()
