import argparse

from argparse import ArgumentParser

from races_report.custom_exceptions import OpenFileException
from races_report.races_report import Report


def argument_parser() -> ArgumentParser:
    """Parses command line arguments"""
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-p', '--path', required=True, type=str, help="path to start and end data files")
    arg_parser.add_argument('-d', '--driver', type=str, help="driver's full name")
    group = arg_parser.add_mutually_exclusive_group(required=False)
    group.add_argument('--asc', dest='ordering', action='store_const', const='asc',
                       help="shows list of drivers in asc order")
    group.add_argument('--desc', dest='ordering', action='store_const', const='desc',
                       help="shows list of drivers in desc order")
    return arg_parser


def print_report(report):
    """Print a races_report to the console"""
    print(report)


def main():
    """ """
    try:
        args_dict = vars(argument_parser().parse_args())
        report = Report(**args_dict).build_report()
        print_report(report)
    except OpenFileException as e:
        print('Oops!', e)


if __name__ == '__main__':
    main()
