# ------------------------------------------------------------------------------
#  es7s [setup/configuration/commons]
#  (c) 2021-2022 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------

import sys

import click

from es7s.cli._cmd import CommandOption, CliCommand, Es7sCommand, logexec, CliGroup


@click.group(cls=CliGroup, short_help="manage es7s system components")
@click.pass_context
def group(ctx: click.Context):
    pass


class InstallCommand(Es7sCommand):
    def __init__(self, ctx: click.Context, dry_run: bool, **kwargs):
        super().__init__(ctx, **kwargs)
        self._run(dry_run)

    @logexec
    def _run(self, dry_run: bool):
        raise NotImplementedError("OH NOES")

    def __copy_core(self):
        pass

    def __inject_bashrc(self):
        pass

    def __inject_gitconfig(self):
        pass

    def __copy_bin(self):
        pass

    def __apt_install(self):
        pass

    def __install_es7s_exts(self):
        # colors
        # fonts
        # prompt
        # tmux
        # kolombos
        # leo
        # watson
        # nalog
        pass


class ConfigCommand(Es7sCommand):
    def z__init__(self, ctx: click.Context, dry_run: bool, **kwargs):
        super().__init__(ctx, **kwargs)
        self._run(dry_run)

    @logexec
    def _run(self):
        print("MMMM YES")


@group.command(name="install", cls=CliCommand, short_help="install es7s system")
@click.option(
    "-n",
    "--dry-run",
    cls=CommandOption,
    is_flag=True,
    default=None,
    help="Don't actually do anything, just pretend to.",
)
@click.pass_context
def install(ctx: click.Context, **kwargs):
    """
    <FILLME>
    """
    InstallCommand(ctx, **kwargs)


@group.command(name="config", cls=CliCommand, short_help="get or update es7s-system settings")
@click.pass_context
def config(ctx: click.Context, **kwargs):
    """
    <FILLME>
    """
    ConfigCommand(ctx, **kwargs)
