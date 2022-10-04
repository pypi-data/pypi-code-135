"""CLI entrypoint of the module."""

import argparse
import os
import sys
from typing import List, Optional

from graphenum.main import introspect
from graphenum.utils import dump_schema


def parse_args(args: List[str]) -> argparse.Namespace:
    """Parse the arguments."""

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-u',
        '--url',
        dest='url',
        type=str,
        help='The URL of the GraphQL endpoint.',
        default=None,
    )
    parser.add_argument(
        '-v',
        '--verbose',
        dest='verbose_mode',
        type=bool,
        help='Verbose',
        default=bool(os.getenv('DEBUG')),
    )
    parser.add_argument(
        '-s',
        '--schema-path',
        dest='schema_path',
        type=str,
        help='Output schema path',
        default=None,
    )
    parser.add_argument(
        '-o',
        '--output-schema',
        dest='output_schema',
        type=str,
        help='GraphQL schema path',
        default=None,
    )
    return parser.parse_args(args)


def cli(argv: Optional[List[str]] = None) -> None:
    """CLI entrypoint."""

    args = parse_args(argv or sys.argv[1:])
    assert args.url, 'Url is required'
    assert args.output_schema or args.verbose_mode or os.getenv('DEBUG'), 'Either schema_path or verbose_mode is required to output the schema'

    result = introspect(
        url=args.url,
        verbose_mode=args.verbose_mode,
        schema_path=args.schema_path,
    )

    schema = result[0]
    if args.output_schema:
        dump_schema(args.output_schema, schema)
