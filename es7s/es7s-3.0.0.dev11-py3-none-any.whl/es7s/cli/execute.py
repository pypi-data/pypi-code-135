# ------------------------------------------------------------------------------
#  es7s [setup/configuration/commons]
#  (c) 2021-2022 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------

from __future__ import annotations

import re
from typing import Tuple

import click
from pytermor import Style, Colors, SgrRenderer

from es7s.cli._cmd import logexec, Es7sCommand, CliCommand, SubprocessError, CliGroup
from es7s.core import PrefixedNumericsFormatter


@click.group(cls=CliGroup, short_help="run standalone helper or embed component")
@click.pass_context
def group(ctx: click.Context):
    pass


class ListDirCommand(Es7sCommand):
    LS_PATH = "/usr/bin/ls"
    LS_ARGS = [
        "-l",
        "--quoting-style=shell-escape",
        "--no-group",
        "--classify",
        "--almost-all",
        "--si",
        "--group-directories-first",
        "--time-style=+%e-%b  %Y\n%e-%b %R",
        "--",
    ]
    SPLIT_REGEXP = re.compile(r"(\S+)")
    NO_SIZE_ATTR_REGEXP = re.compile("^[dl]")
    INACTIVE_ATTR_REGEXP = re.compile("(-+)")
    FILE_CLASS_REGEXP = re.compile(r"\x1b[\[\]](?:0?m|K)(.)$")  # there will be \e[m SGR or \e]K
    OUTPUT_SEPARATOR = ""

    INACTIVE_ENCLOSURE = Style(fg=Colors.GREY).render("\x00").split("\x00")  # pre-render for better performance

    def __init__(self, ctx: click.Context, file: Tuple[str], **kwargs):
        super().__init__(ctx, **kwargs)
        self._run(file)

    @logexec
    def _run(self, file: Tuple[str]):
        color = SgrRenderer.is_sgr_usage_allowed()
        args = [
            self.LS_PATH,
            "--color=" + ("always" if color else "never"),
            *self.LS_ARGS,
            *file,
        ]

        try:
            skipped_total = False
            for r in self._stream_subprocess(*args):
                if not skipped_total:
                    skipped_total = True
                    continue
                line = self._process_ls_output(r.rstrip())
                if line:
                    print(line)
        except SubprocessError as e:
            if e.code == 0 or e.code == 1:  # subdirectory permission error
                return
            raise e

    def _process_ls_output(self, line: str) -> str:
        def split_ls_line(s: str) -> tuple[str, ...]:
            splitted = self.SPLIT_REGEXP.split(s, 7)
            pairs = [iter(splitted)] * 2
            for value in zip(*pairs, strict=False):
                yield "".join(value)  # value ex.: (' ', '461')
            yield splitted[-1]

        splitted = list(split_ls_line(line))
        if len(splitted) != 8:
            return line

        attrs, hlinks, user, size, date, time, filename, rightover = splitted
        fc = " "

        if self.NO_SIZE_ATTR_REGEXP.match(attrs):
            size = self._render_inactive("".rjust(len(size)))
        else:
            size = PrefixedNumericsFormatter.format(size)

        filename += rightover
        if fcmatch := self.FILE_CLASS_REGEXP.search(filename):
            fc = fcmatch.group(1)
            filename = filename.removesuffix(fc)
        fc = f" {fc}"

        if attrs.startswith("-"):
            attrs = " " + attrs[1:]
        attrs = re.sub(self.INACTIVE_ATTR_REGEXP, self._render_inactive(r"\1"), attrs)
        hlinks = " " * len(hlinks)

        return self.OUTPUT_SEPARATOR.join([attrs, hlinks, user, size, date, time, fc, filename])

    def _render_inactive(self, s: str) -> str:
        return self.INACTIVE_ENCLOSURE[0] + s + self.INACTIVE_ENCLOSURE[1]


@group.command(
    name="list-dir",
    cls=CliCommand,
    short_help="ls with bells and whistes",
    help="Wrapper around GNU `ls` with preset settings for 'one-button' usage. FILE is directory "
    "to list information about and can be used multiple times. Default is current directory.\n\n"
    "Runs and formats output of:\n\n"
    f"{ListDirCommand.LS_PATH} {' '.join(ListDirCommand.LS_ARGS)} [FILE]...",
)
@click.argument("file", type=str, required=False, nargs=-1)
@click.pass_context
def list_dir(ctx: click.Context, **kwargs):
    ListDirCommand(ctx, **kwargs)
