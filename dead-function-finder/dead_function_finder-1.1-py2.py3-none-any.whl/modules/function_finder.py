
import re

from .directory_parser import parse
from .supported_languages import get_function_definition_pattern, get_magic_method_format


def find_functions(file_path, language='python'):
    """ Return a list of functions within a file """

    # Read file
    with open(file_path, 'r') as file:
        try:
            file_content = file.read()
        except UnicodeDecodeError:
            return []

    # Find all functions
    functions = re.findall(
        get_function_definition_pattern(language), file_content)

    # Remove magic methods
    functions = remove_magic_methods(functions, language)

    return list(set(functions))


def find_all_functions(files, language='python'):
    """ Return a list of functions within a directory """

    functions_by_file = {}
    for file_path in files:
        functions = find_functions(file_path, language)

        if functions:
            functions_by_file[file_path] = functions

    return functions_by_file


def remove_magic_methods(functions, language='python'):
    """ Remove magic methods from a list of functions """

    magic_method_format = get_magic_method_format(language)

    # Remove magic methods
    result = []
    for function in functions:

        if not re.match(magic_method_format, function):
            result.append(function)

    return result
