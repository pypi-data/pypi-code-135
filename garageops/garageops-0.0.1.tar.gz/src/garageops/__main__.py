# SPDX-FileCopyrightText: 2022 Chris Wilson <christopher.david.wilson@gmail.com>
#
# SPDX-License-Identifier: MIT

from . import cli
from .__about__ import __app_name__


def main():
    cli.app(prog_name=__app_name__)


if __name__ == "__main__":
    main()
