# ------------------------------------------------------------------------------
#  es7s [setup/configuration/commons]
#  (c) 2021-2022 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------

from __future__ import annotations

import codecs
import os.path
from os.path import dirname
from typing import TextIO, IO

import click
from click import File
from pytermor import Style
from pytermor.util import ReplaceSGR

from es7s.cli._cmd import CliCommand, logexec, Es7sCommand, CliGroup
from es7s.core import PrefixedNumericsFormatter, SANITIZE_REGEX


@click.group(cls=CliGroup, short_help="run demo example(s) of es7s features")
@click.pass_context
def group(ctx: click.Context):
    """
    Commands for demonstration of work of some es7s modules, running on predefined examples.
    """
    pass


class FormatNumericsCommand(Es7sCommand):
    CHUNK_SIZE = 8096

    @property
    def _input_path(self) -> str:
        return os.path.join(dirname(__file__), "..", "..", "tests", "inputs", "format-numerics-demo.txt")

    def __init__(self, ctx: click.Context, file: File | None, **kwargs):
        super().__init__(ctx, **kwargs)

        preset_mode = False
        if file is None:
            preset_mode = True
            file = click.open_file(self._input_path, "r")
            self.logger.info("Replaced input stream with demo file")

        codecs.register_error("replace_with_qmark", lambda e: ("?", e.start + 1))
        self._line_num = 1
        self._offset = 0
        self._input: TextIO

        self._assign_input(file)
        self._run(preset_mode)

    @logexec
    def _run(self, preset_mode: bool):
        if preset_mode:
            self._run_preset()
        self._read_and_process_input()
        self._close_input()

    def _run_preset(self):
        headers = [Style(bold=True).render(s) for s in ["Input:", "Output:"]]
        click.echo(headers.pop(0))
        self._read_and_process_input(remove_sgr=True)
        self._reset_input()
        click.echo(headers.pop(0))

    def _read_and_process_input(self, remove_sgr: bool = False):
        try:
            while line := self._input.readline(self.CHUNK_SIZE):
                processed_line = self._process_decoded_line(line)
                if remove_sgr:
                    processed_line = ReplaceSGR("").apply(processed_line)
                print(processed_line)
            return
        except UnicodeDecodeError as e:
            self.logger.error(str(e))
            self.logger.warning("Switching to raw output")

        self._reset_input(self._offset)
        try:
            while line := self._input.buffer.readline(self.CHUNK_SIZE):
                click.echo(self._process_raw_line(line))
        except Exception as e:
            self.logger.error(str(e))

    def _process_decoded_line(self, line: str | None) -> str:
        if line is None:
            return ""
        self.logger.debug(f"Read line: {line}")
        line_len = len(line.encode())
        result = PrefixedNumericsFormatter.format(line.strip("\n"))

        self.logger.debug(f"Processed {line_len} bytes, line {self._line_num}, offset {self._offset}")
        self._line_num += 1
        self._offset += line_len
        return result

    def _process_raw_line(self, line: bytes | None) -> bytes:
        if line is None:
            return b""
        self.logger.debug(f"Read line: {line}")
        line_len = len(line)
        result = SANITIZE_REGEX.sub(b".", line)

        self.logger.debug(f"Processed {line_len} bytes, offset {self._offset}")
        self._line_num += 1
        self._offset += line_len
        return result

    def _assign_input(self, inp: TextIO | IO):
        self._input = inp
        self.logger.info(f"Current input stream is {self._input.name}")

    def _close_input(self):
        if not self._input.closed:
            self.logger.info(f"Closing input stream {self._input.name}")
            self._input.close()

    def _reset_input(self, offset: int = 0):
        if self._input.seekable():
            self.logger.info(f"Resetting input stream position to {offset}")
            self._input.seek(offset)


@group.command(name="format-numerics", cls=CliCommand, short_help="perform a test run of built-in number formatter")
@click.argument("file", type=File(mode="r"), required=False)
@click.pass_context
def format_numerics(ctx: click.Context, **kwargs):
    """
    Read preset text example and highlight all occurenceses of numbers with (prefixed) units with different
    color depending on value power.

    If FILE argument is set, read text from given FILE instead. If FILE is '-', read standard input.

    Is used by es7s list-dir.
    """
    FormatNumericsCommand(ctx, **kwargs)
