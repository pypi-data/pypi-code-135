# SPDX-FileCopyrightText: 2022 Chris Wilson <christopher.david.wilson@gmail.com>
#
# SPDX-License-Identifier: MIT

from typer.testing import CliRunner

from garageops import __app_name__, __version__, cli

runner = CliRunner()


def test_version():
    """Ensure the version string is formatted correctly."""
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout
