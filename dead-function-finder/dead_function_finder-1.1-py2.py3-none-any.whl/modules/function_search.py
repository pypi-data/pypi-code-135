import re

from .supported_languages import get_search_pattern


def search_function_in_file(function_name, file_path, language='python'):
    """ Return a list of functions within a file """

    # Read file
    with open(file_path, 'r') as file:
        try:
            file_content = file.read()
        except UnicodeDecodeError:
            return None

    start, end = get_search_pattern(language)

    # Find all functions
    found = re.search(start + function_name + end, file_content, re.MULTILINE)

    return True if found else False


def iterate_and_search(function_name, files, language):
    """ Return a list of functions within a directory """

    for file_path in files:
        found = search_function_in_file(function_name, file_path, language)

        if found:
            return True

    return False
