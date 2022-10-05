
import argparse

from .modules.directory_parser import parse
from .modules.function_finder import find_all_functions
from .modules.function_search import iterate_and_search


def main():
    """ Return a list of functions within a directory """

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--language", type=str, help="Programming language",
                        choices=['python', 'php'], default='python')
    parser.add_argument(
        "-p", "--path", help="Path to directory", required=True)
    parser.add_argument(
        "-x", "--exclude", help="Exclude a file or directory pattern, (comma separated")
    args = parser.parse_args()

    # List filenames
    all_files = [x for x in parse(args.path, args.language, args.exclude)]

    # Search all functions by filenames
    functions_by_file = find_all_functions(all_files, args.language)
    functions_count = sum(len(v) for v in functions_by_file.values())
    print(' * Found {} functions in {} files.'.format("{:,.0f}".format(functions_count),
                                                      "{:,.0f}".format(len(functions_by_file))))

    # Search all functions in all files
    count = 0
    for file_path in functions_by_file:
        # All functions in file
        functions = functions_by_file[file_path]

        # Loop through all functions
        for function in functions:
            res = iterate_and_search(function, all_files, args.language)

            if not res:
                count += 1
                print(
                    '   -> Function `{}` from `{}` not found in any file.'.format(function, file_path))

    print(' * Found {} dead functions.'.format("{:,.0f}".format(count)))

    return None


if __name__ == '__main__':
    main()
