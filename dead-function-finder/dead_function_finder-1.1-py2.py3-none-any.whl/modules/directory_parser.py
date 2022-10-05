import glob
import re
import os

from .supported_languages import get_extension


def parse(path, language='python', exclude=None):
    """ Return a recursive list of files within a directory """

    # Add optional /
    if not path.endswith('/'):
        path += '/'

    # Resolve home path
    path = resolve_home_path(path)

    # Check if dir exists
    if not os.path.isdir(path):
        raise FileNotFoundError

    # absolute path to search all text files inside a specific folder
    path = path + r'**/*' + get_extension(language)
    files = glob.glob(path, recursive=True)

    exclusions = (exclude).split(',') if exclude else []

    result = []
    for file in files:
        # Skip directories with extensions
        if not os.path.isfile(file):
            continue

        # Skip excluded files
        if is_excluded(file, exclusions):
            continue

        result.append(file)

    return result


def resolve_home_path(path):
    """ Resolve home directory """

    if path.startswith('~'):
        path = os.path.expanduser(path)

    return path


def is_excluded(file, exclusions):
    """ Check if file contains an excluded pattern """

    for exclusion in exclusions:
        if exclusion and exclusion.strip() in file:
            return True

    return False
