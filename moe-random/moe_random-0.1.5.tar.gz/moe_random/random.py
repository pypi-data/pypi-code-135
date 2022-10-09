"""Outputs a random item in the library."""

import argparse
from collections import OrderedDict
from typing import Any

import moe
import moe.cli
from moe import config
from moe.library import Album, Extra, LibItem, Track
from moe.util.cli import cli_query, query_parser

__all__: list[str] = []


@moe.hookimpl
def plugin_registration():
    """Depend on the cli plugin."""
    if not config.CONFIG.pm.has_plugin("cli"):
        config.CONFIG.pm.set_blocked("random")
        log.warning("The 'random' plugin requires the 'cli' plugin to be enabled.")


@moe.hookimpl
def add_command(cmd_parsers: argparse._SubParsersAction):
    """Adds the ``list`` command to Moe's CLI."""
    random_parser = cmd_parsers.add_parser(
        "random",
        aliases=["rand"],
        description="Outputs a random item from the library.",
        help="output a random library item",
    )
    item_type_group = random_parser.add_mutually_exclusive_group(required=True)
    item_type_group.add_argument(
        "-a",
        "--album",
        action="store_true",
        help="output a random album",
    )
    item_type_group.add_argument(
        "-e",
        "--extra",
        action="store_true",
        help="output a random extra",
    )
    item_type_group.add_argument(
        "-t",
        "--track",
        action="store_true",
        help="output a random track",
    )
    random_parser.set_defaults(func=_parse_args)


def _parse_args(args: argparse.Namespace):
    """Parses the given commandline arguments.

    Args:
        args: Commandline arguments to parse.

    Raises:
        SystemExit: Invalid query or no items found.
    """
    if args.album:
        items = cli_query("*", "album")
    elif args.extra:
        items = cli_query("*", "extra")
    else:
        items = cli_query("*", "track")

    print(items[random.randint(0, len(items) - 1)])
