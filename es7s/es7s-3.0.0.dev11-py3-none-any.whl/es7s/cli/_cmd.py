# ------------------------------------------------------------------------------
#  es7s [setup/configuration/commons]
#  (c) 2021-2022 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------

import json
import re
import subprocess
from abc import ABCMeta
from subprocess import CalledProcessError, CompletedProcess
from typing import Any

import click
from click import Command, Context, Option, HelpFormatter, Group
from pytermor import RendererManager, SgrRenderer

from ..log import setup

# ------------------------------------------------------------------------------
# `click` command overrides/injections

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])
HELP_HINT = "Use COMMAND with '--help' option to get the detailed description."


def _wh_imposter(origin):
    def wrapper(heading):
        # heading = Style(bold=True).render(heading.upper())
        return origin(heading.upper())

    return wrapper


class CommandOption(Option):
    group_title = "Options"


class CliCommand(Command):
    def __init__(self, **kwargs):
        kwargs["params"] = kwargs.get("params", []) + [
            Option(
                param_decls=["-q", "--quiet"],
                is_flag=True,
                default=False,
                help="Don't print anything to standard error stream, which is used for errors, warnings and debug "
                "messages.",
            ),
            Option(
                param_decls=["-v", "--verbose"],
                count=True,
                type=click.IntRange(0, 2, clamp=True),
                default=0,
                help="Increase the amount of details of execution process. '-v' for more info and exception "
                "tracing, '-vv' for debugging.",
            ),
            Option(
                param_decls=["-c", "--color"],
                is_flag=True,
                default=None,
                help="Explicitly enable using of ANSI escape sequences to format the output.",
            ),
            Option(
                param_decls=["-C", "--no-color"],
                is_flag=True,
                default=None,
                help="Explicitly disable output formatting.",
            ),
        ]
        kwargs["epilog"] = (
            kwargs.get("epilog", "")
            + "\n\n"
            + "If neither of `--color` and `--no-color` is set, the option will be determined by the app itself "
            "depending on detection of interactive terminal."
        )
        super().__init__(**kwargs)

    def format_help(self, ctx: Context, formatter: HelpFormatter) -> None:
        formatter.write_heading = _wh_imposter(origin=formatter.write_heading)
        super().format_help(ctx, formatter)

    def format_options(self, ctx: Context, formatter: HelpFormatter) -> None:
        opt_groups = {k: [] for k in [CommandOption, Option]}
        for param in self.get_params(ctx):
            rv = param.get_help_record(ctx)
            if rv is not None and type(param) in opt_groups.keys():
                opt_groups[type(param)].append(rv)

        for opt_class, opts in opt_groups.items():
            if opts:
                if not hasattr(opt_class, "group_title"):
                    group_title = "Common options"
                    # opts.reverse()
                else:
                    group_title = getattr(opt_class, "group_title")
                with formatter.section(group_title.upper()):
                    formatter.write_dl(opts)


class CliGroup(Group):
    def __init__(self, **kwargs):
        # context_settings = {**CONTEXT_SETTINGS, 'color': None}
        kwargs["epilog"] = kwargs.get("epilog", "") + "\n\n" + HELP_HINT
        super().__init__(context_settings=CONTEXT_SETTINGS, **kwargs)

    def format_help(self, ctx: Context, formatter: HelpFormatter) -> None:
        formatter.write_heading = _wh_imposter(origin=formatter.write_heading)
        super().format_help(ctx, formatter)


# ------------------------------------------------------------------------------
# actual command runners


def logexec(fn):
    def wrapper(self, *args, **kwargs):
        try:
            self.logger.info("Starting command execution")
            fn(self, *args, **kwargs)
        except Exception as e:
            self.logger.exception(e)
            self.logger.info("Terminating due to exception")
            raise SystemExit(1) from e
        self.logger.info("Terminating normally")
        return fn

    return wrapper


class SubprocessError(Exception):
    def __init__(self, code: int):
        self.code = code
        self.msg = f"Subprocess terminated with code {code}"

    def __str__(self):
        return self.msg


class Es7sCommand(metaclass=ABCMeta):
    def __init__(self, ctx: click.Context, quiet: bool, verbose: bool, color: bool, no_color: bool):
        self.ctx = ctx
        module_path = self.__module__.split(".")
        ident = module_path[1] if len(module_path) > 1 else module_path[0]

        self.logger = setup(ident, self.__class__.__qualname__, quiet, verbose)
        RendererManager.set_up(SgrRenderer)
        if color:
            SgrRenderer.set_up(force_styles=True)
            self.logger.debug(f"Force-enabled {SgrRenderer.__qualname__} formatting")
        elif no_color:
            SgrRenderer.set_up(force_styles=None)
            self.logger.debug(f"Force-disabled {SgrRenderer.__qualname__} formatting")
        self.logger.debug(f"Initialized command with {self._print_args(ctx.params)}")

    def _print_args(self, *params: dict[str, Any]) -> str:
        results: list[dict[str, Any]] = []
        for param_chunk in params:
            results.append({k: str(v) for k, v in param_chunk.items()})
        joined = " ".join(json.dumps(result, separators=(" ", "=")) for result in results)
        return re.sub("[\"']", "", joined).translate({ord("{"): "(", ord("}"): ")"})

    def _run_subprocess(self, *args: Any, require_success: bool) -> CompletedProcess:
        def log_streams_dump(out: Any, err: Any):
            for name, stream in {"stdout": out, "stderr": err}.items():
                if not stream:
                    self.logger.debug(f"Subprocess {name} stream is empty")
                else:
                    self.logger.debug(f"Subprocess {name} stream dump:\n{stream}\n============")

        self.logger.info(f'Running subprocess: {" ".join(args)}')
        try:
            cp = subprocess.run(args, capture_output=True, encoding="utf8", check=require_success)
        except CalledProcessError as e:
            log_streams_dump(e.stdout.strip(), e.stdout.strip())
            raise e

        cp.stdout, cp.stderr = cp.stdout.strip(), cp.stderr.strip()
        log_streams_dump(cp.stdout, cp.stderr)
        return cp

    def _stream_subprocess(self, *args: Any) -> str:
        for r in self._read_stream(*args):
            if isinstance(r, int):
                raise SubprocessError(r)
            yield r

    def _read_stream(self, *args: Any) -> str:
        self.logger.info(f'Running subprocess in stream mode: {" ".join(args)}')
        process = subprocess.Popen(args, stdout=subprocess.PIPE, encoding="utf8")

        self.logger.debug(f"Subprocess stdout stream:")
        for line in iter(process.stdout.readline, ""):
            self.logger.debug(line.rstrip())
            yield line
