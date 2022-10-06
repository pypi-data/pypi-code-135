import argparse
import os
from argparse import Namespace
from typing import Optional, Type

from unique_character.count_unique_character import count_letter


class NameSpace(argparse.Namespace, Type):
    filename: str
    word: str


def validate_file(filename: str) -> str:
    if not os.path.isfile(filename):
        raise FileNotFoundError('File not found')
    return filename


def read_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def run_parser(args=None) -> Optional[Namespace]:
    parser = argparse.ArgumentParser(description="Count uniq chars")
    parser.add_argument('--string', dest='word', help='Input str')
    parser.add_argument('--file', dest="filename", help="Input file")
    return parser.parse_args(args, namespace=None)


def main() -> int:
    args = run_parser()
    if args.filename:
        file_path = validate_file(args.filename)
        text = read_file(file_path)
        return count_letter(text)
    elif args.word:
        return count_letter(args.word)
    raise ValueError('Please select --string or --file')


if __name__ == '__main__':
    main()
