import sys
import os

import argparse

from smog.const import VERSION

from smogconvert.core import specloader
from smogconvert import convert, run_piped, normalize_args

"""
this script expects following parameters on cmd-line

param-1: spec-file.json describing the transformation
param-2: input-file
param-3: output-file
"""


def main_func():

    parser = argparse.ArgumentParser(
        prog="smogconvert",
        usage="python3 -m %(prog)s [options]",
        description="simple media organizer - converter",
        epilog="for more information refer to https://github.com/kr-g/smog",
    )
    parser.add_argument(
        "--version", "-v", action="version", version=f"%(prog)s {VERSION}"
    )

    parser.add_argument(
        "spec_file",
        type=str,
        action="store",
        help="spec-file.json describing the transformation",
    )

    parser.add_argument(
        "src",
        type=str,
        action="store",
        help="input-file",
    )

    parser.add_argument(
        "dest",
        type=str,
        action="store",
        default="-",
        help="output-file, or - for stdout (default: '%(default)s')",
    )

    parsed_args = parser.parse_args()

    procs = specloader(parsed_args.spec_file)

    args = [sys.argv[0], parsed_args.src, parsed_args.dest]

    nargs = normalize_args(args)

    rc = run_piped(procs, nargs)
    if rc:
        # write raw bytes to stdout
        os.write(sys.stdout.fileno(), rc)


if __name__ == "__main__":
    main_func()
