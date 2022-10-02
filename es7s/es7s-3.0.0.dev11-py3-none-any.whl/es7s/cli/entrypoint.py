# ------------------------------------------------------------------------------
#  es7s [setup/configuration/commons]
#  (c) 2021-2022 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
import sys

import click

from es7s import APP_VERSION
from es7s.cli import manage, demo, execute, monitor
from es7s.cli._cmd import CliGroup


@click.group(cls=CliGroup)
@click.version_option(APP_VERSION, "-V", "--version")
@click.pass_context
def es7s(ctx: click.Context, **kwargs):
    """
    Entrypoint of es7s system CLI.
    """
    pass


es7s.add_command(manage.group, "manage")
es7s.add_command(execute.group, "exec")
es7s.add_command(demo.group, "demo")
es7s.add_command(monitor.group, "monitor")


def extcall():
    es7s()


def extcall_list_dir():
    es7s(["exec", "list-dir", *sys.argv[1:]])
