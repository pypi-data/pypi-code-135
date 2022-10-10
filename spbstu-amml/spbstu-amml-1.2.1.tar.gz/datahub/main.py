import argparse

from datahub import utils

comands = {
    "configure": utils.cli_configure
}

def arg_parser():
    parser = argparse.ArgumentParser(description="""
    Datahub utils to manage the data repository
    """)
    parser.add_argument("comand", type=str, choices=comands.keys())

    return parser

def main(argv: str):
    parser = arg_parser()
    args = parser.parse_args(argv[1:])
    comands[args.comand]()