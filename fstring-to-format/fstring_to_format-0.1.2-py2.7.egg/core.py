"""
Module bundling all functions needed to convert f-strings to .format()
"""
from __future__ import print_function
from __future__ import unicode_literals
import re
import glob
import shutil
import io
import os

MAINPATTERN = re.compile(r"f['\"].*\{[^\{\s}]+\}+.*['\"]")
PARTPATTERN = re.compile(r"\{[^\{\}\s]+\}")


def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


def formatify(path):
    files = glob.glob(path)
    files = [file for file in files if os.path.isfile(file)]
    if not files:
        print("No files are found")
    else:
        for file in files:
            print("Backing up {0}".format(file))
            shutil.copy(file, "{0}.temp".format(file))
            with io.open(file, "r+", encoding="utf-8") as f:
                print("Opening {0}".format(file))
                content = f.read()
                matches = MAINPATTERN.findall(content)
                for match in matches:
                    parts = unique(PARTPATTERN.findall(match))
                    toreplace = match
                    for ind, part in enumerate(parts):
                        toreplace = toreplace.replace(part, "{" + str(ind) + "}").lstrip("f")
                    toreplace += ".format("
                    for part in parts:
                        toreplace += "{0}, ".format(part.strip("{").strip("}"))
                    toreplace = toreplace.rstrip(", ") + ")"
                    content = content.replace(match, toreplace)
                f.seek(0)
                f.truncate(0)
                print("Writing {0}".format(file))
                f.write(content)
                f.close()
        print("All files are converted")
