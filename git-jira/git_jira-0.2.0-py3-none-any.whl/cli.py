import click

from git_jira.commands.branch import branch
from git_jira.commands.configure import configure
from git_jira.commands.status import status
from git_jira.commands.list import list


@click.group()
def cli():
    pass

cli.add_command(configure)
cli.add_command(branch)
cli.add_command(status)
cli.add_command(list)
