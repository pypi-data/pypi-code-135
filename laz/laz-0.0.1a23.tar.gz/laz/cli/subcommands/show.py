# std
from argparse import Namespace
from typing import List

# internal
from laz.model.node import Node
from laz.utils.errors import LazRuntimeError
from laz.model.runner import Runner
from laz.model.target import Target
from laz.utils.load import load
from laz.utils.logging import get_logger
from laz.cli.parser import parser

# constants
from laz.utils.node import get_path, get_node_configuration

DESCRIPTION = """Show the effective configuration of a given node or target.
"""

subparsers = parser.add_subparsers(required=True)

parser_show = subparsers.add_parser("show", description=DESCRIPTION)
parser_show.add_argument("path", type=str)


def show():

    args = parser.parse_args()
    get_logger(verbosity=args.verbose)

    root_node = load()
    runner = Runner(root_node, Namespace(reverse=False), [args.path])
    nodes = runner.resolver.resolve_nodes()
    targets = runner.resolve()

    if len(targets) >= 1:
        _show_target(targets)
    elif len(nodes) >= 1:
        _show_node(nodes)
    else:
        msg = f"""Error during show command.
Given path did not resolve to any targets or nodes.
"""
        raise LazRuntimeError(msg)


def _show_target(targets: List[Target]):

    if len(targets) > 1:
        target_paths = [t.data.target.path for t in targets]
        msg = f"""Error during show command.
Given path should not resolve to more than 1 target. Got {len(targets)}.
Resolved targets: {target_paths}
"""
        raise LazRuntimeError(msg)

    target = targets[0]
    print(target.json())


def _show_node(nodes: List[Node]):

    if len(nodes) > 1:
        node_paths = [get_path(n) for n in nodes]
        msg = f"""Error during show command.
Given path should not resolve to more than 1 node. Got {len(nodes)}.
Resolved nodes: {node_paths}
"""
        raise LazRuntimeError(msg)

    node = nodes[0]
    print(get_node_configuration(node).json())
