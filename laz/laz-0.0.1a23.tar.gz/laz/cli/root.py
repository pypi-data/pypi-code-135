# std

# internal
from laz.cli.parser import parser
from laz.utils.load import load
from laz.utils.logging import get_logger
from laz.model.runner import Runner
from laz.utils.utils import split_args


def root():
    parser.add_argument(
        "--reverse",
        "-r",
        action="store_true",
        default=False,
        help="Run targets in reverse order.",
    )

    cli_args, laz_args = split_args()
    if len(laz_args) == 0:
        from laz.cli.subcommands.help import help

        help()
        exit(1)

    cli_args = parser.parse_args(cli_args)
    get_logger(verbosity=cli_args.verbose)
    root_node = load()
    runner = Runner(root_node, cli_args, laz_args)
    runner.run()
