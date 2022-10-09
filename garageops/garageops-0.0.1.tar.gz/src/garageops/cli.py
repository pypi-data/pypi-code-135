# SPDX-FileCopyrightText: 2022 Chris Wilson <christopher.david.wilson@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Optional

import typer

from .__about__ import __app_name__, __version__

app = typer.Typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(  # noqa: B008
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return
