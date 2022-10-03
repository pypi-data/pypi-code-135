"""
fstring_to_format terminal client
"""

from __future__ import absolute_import
import sys

from .core import formatify


def main(args):
    """Main function"""
    formatify(args[1])


if __name__ == "__main__":
    main(sys.argv)
