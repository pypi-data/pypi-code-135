import sys
from typing import cast

import click
from click import Command

from dovi_helpers.cli import commands
from dovi_helpers.helpers import check_prerequisites_ok
from dovi_helpers.initializers import init_system


@click.group()
def main() -> None:
    """
    Command line interface for collection of scripts to convert MKV container into
    Dolby Vision 8.1 compatible MP4.
    """

    if "--help" not in sys.argv:
        init_system()

        if check_prerequisites_ok() is False:
            raise click.exceptions.Abort(
                "Some commands are missing. Unable to continue."
            )


main.add_command(cast(Command, commands.demux))
main.add_command(cast(Command, commands.info))
main.add_command(cast(Command, commands.mux))
main.add_command(cast(Command, commands.pipeline))

if __name__ == "__main__":
    main()
