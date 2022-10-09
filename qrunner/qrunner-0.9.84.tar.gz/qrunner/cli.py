import argparse
# import sys
from qrunner import __version__, __description__
from qrunner.scaffold import create_scaffold


def main():
    """ API test: parse command line options and run commands.
    """
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument(
        "-v", "--version", dest="version", action='store_true', help="show version",
    )
    parser.add_argument(
        "-p", "--project", dest="project", help="create demo project",
    )

    args = parser.parse_args()
    version = args.version
    project = args.project

    if version:
        print(__version__)
    if project:
        create_scaffold(project)


if __name__ == "__main__":
    main()
