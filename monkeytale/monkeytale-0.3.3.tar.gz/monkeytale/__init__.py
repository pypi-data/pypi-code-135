from pathlib import Path

import click
from eliot import start_task
from sh import pwd

from .file_management import initialize_build_directory, start_log

__version__ = "0.3.3"

cwd = Path(pwd().strip("\n"))


@click.command()
@click.version_option(version=__version__)
def cli():
    with start_task(action_type="MonkeytaleBuild") as task:
        start_log()
        initialize_build_directory()


if __name__ == "__main__":
    cli()  # pragma: no cover
