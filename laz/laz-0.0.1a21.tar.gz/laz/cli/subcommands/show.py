# std
from argparse import Namespace

# internal
from laz.utils.errors import LazRuntimeError
from laz.model.runner import Runner
from laz.utils.load import load
from laz.utils.logging import get_logger
from laz.cli.parser import parser

# constants
DESCRIPTION = """Show the effective configuration of a given target.
"""

subparsers = parser.add_subparsers(required=True)

parser_show = subparsers.add_parser('show', description=DESCRIPTION)
parser_show.add_argument('path', type=str)


def show():

    args = parser.parse_args()
    get_logger(verbosity=args.verbose)

    root_node = load()
    runner = Runner(root_node, Namespace(reverse=False), [args.path])
    targets = runner.resolve()

    if len(targets) != 1:
        target_paths = [t.id for t in targets]
        msg = f'''Error during show command.
During show command, number of targets should resolve to 1. Got {len(targets)}.
Resolved targets: {target_paths}
'''
        raise LazRuntimeError(msg)

    target = targets[0]
    print(target.json())
