"""Auth related commands.

Commands invoked by dpteam auth <some-command> is defined here.
"""

import click

from dapla_team_cli.auth.list_token.cmd import list_token
from dapla_team_cli.auth.login.cmd import login


@click.group()
def auth() -> None:
    """Auth command group."""
    pass


auth.add_command(login)
auth.add_command(list_token)
