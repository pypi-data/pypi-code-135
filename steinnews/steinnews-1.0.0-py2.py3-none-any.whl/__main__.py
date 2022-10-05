#! /usr/bin/env python
# encoding: utf-8


import click
import sys
import colorama

from . import write_next_version


@click.command()
@click.argument("input_file")
@click.argument("output_file")
@click.option("-v", "--verbose", is_flag=True)
def cli(input_file, output_file, verbose):
    try:
        write_next_version(input_file, output_file)
    except Exception as e:

        if verbose:
            # We just propagate the exception out
            raise

        colorama.init()
        print(colorama.Fore.RED + str(e))
        sys.exit(1)
