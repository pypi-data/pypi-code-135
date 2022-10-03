"""Main file for project build cli tools."""

import sys
import logging
import argparse

from traceback import print_tb

from ptask import __doc__, __version__
from ptask.process import build


def main():
    """Check user input and then process to build the project."""
    logging.basicConfig(level=logging.INFO, format='[PROJ] %(levelname)s: %(message)s')

    # CLI
    usage = 'ptask build_type [options]'
    parser = argparse.ArgumentParser(prog='ptask',
                                     usage=usage,
                                     description=__doc__,
                                     epilog='Happy building your project! :)')

    parser.add_argument('build_type',
                        type=str,
                        metavar='build_type',
                        help='set the build type based on your task setup')
    parser.add_argument('-v',
                        '--version',
                        action='version',
                        version='%(prog)s -- {version}'.format(version=__version__))
    parser.add_argument('-i',
                        '--info',
                        dest='info',
                        default=False,
                        action='store_true',
                        required=False,
                        help='print the current build\'s information')
    parser.add_argument('-f',
                        '--file',
                        dest='file',
                        default='',
                        type=str,
                        required=False,
                        help='custom file task configuration')
    parser.add_argument('-p',
                        '--path',
                        dest='path',
                        default='',
                        type=str,
                        required=False,
                        help='custom build path for the project')

    args = parser.parse_args()

    try:
        build(args.build_type, args.file, args.path, args.info)
    except Exception as e:
        logging.error('ERROR - %s', e)
        print_tb(e.__traceback__)
        sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    main()
