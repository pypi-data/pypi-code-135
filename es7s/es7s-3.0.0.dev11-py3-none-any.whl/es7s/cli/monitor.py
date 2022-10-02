# ------------------------------------------------------------------------------
#  es7s [setup/configuration/commons]
#  (c) 2021-2022 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
import re
import sys
from dataclasses import dataclass
from re import Pattern
from subprocess import CalledProcessError
from time import sleep

import click
from pytermor import Style, NOOP_STYLE, Colors, Styles, SgrRenderer
from pytermor.render import TmuxRenderer

from es7s.cli._cmd import CliGroup, Es7sCommand, logexec, CliCommand, CommandOption
from es7s.core.strings import StyleRegistry

POLLING_INTERVAL_SEC = 2.0


@click.group(
    cls=CliGroup,
    short_help="run system monitor (mostly used by tmux)",
    epilog="""\b
[&] is system-unique daemon that ~runs~ WILL RUN as a background service
[*] asterisk indicates persistent monitor launched by tmux when it starts
[ ] no mark means this is 'one-use' monitor invoked at every statusbar update
""",
)
@click.pass_context
def group(ctx: click.Context):
    pass


# ------------------------------------------------------------------------------
# docker


@dataclass
class DockerStatusConfig:
    name: str
    search_regexp: Pattern = None
    style_static: Style = NOOP_STYLE
    style_changed: Style = None
    align: str = ">"

    @property
    def enabled(self) -> bool:
        return self.search_regexp is not None

    def __hash__(self) -> int:
        return int.from_bytes(self.name.encode(), byteorder="big")


@dataclass
class StatusState:
    container_amount: int = None
    updated_ticks_ago: int = 0


class MonitorDockerCommand(Es7sCommand):
    """
    Format:   |s dd dd|
           running^  ^restarting

    Examples: |D  2  0|
              |D 23  0|
              |D  4 11|
    """

    DOCKER_PATH = "/usr/bin/docker"
    DOCKER_ARGS = ["ps", '--format="{{.Status}}"']
    STATUS_FILTER_TEMPLATE = "--filter=status={:s}"
    STATUSES_TO_MONITOR = [
        DockerStatusConfig(
            "running", re.compile('^"up', re.IGNORECASE), style_changed=Style(fg=Colors.GREEN, bold=True)
        ),
        DockerStatusConfig(
            "restarting",
            re.compile('^"restarting', re.IGNORECASE),
            style_static=Style(fg=Colors.YELLOW),
            style_changed=Style(fg=Colors.HI_YELLOW, bold=True),
        ),
        DockerStatusConfig("removing"),
        DockerStatusConfig("dead"),
        DockerStatusConfig("paused"),
        DockerStatusConfig("created"),
        DockerStatusConfig("exited"),
    ]
    AMOUNT_UPDATE_HIGHLIGHT_DELAY_TICKS = 3
    AMOUNT_FIELD_SIZE = 2

    def __init__(self, ctx: click.Context, tmux: bool, **kwargs):
        super().__init__(ctx, **kwargs)

        enabled_configs = [cfg for cfg in self.STATUSES_TO_MONITOR if cfg.enabled]
        self.status_map = {cfg: StatusState() for cfg in enabled_configs}
        self.renderer = TmuxRenderer if tmux else SgrRenderer
        self._run()

    @logexec
    def _run(self):
        self._print()

        while True:
            try:
                self._count_containers()
            except CalledProcessError as e:
                self.logger.exception(e)
                self._print(error=True)
            else:
                self._print()
            sleep(POLLING_INTERVAL_SEC)

    def _count_containers(self):
        filter_args = [self.STATUS_FILTER_TEMPLATE.format(cfg.name) for cfg in self.status_map.keys()]
        args = [self.DOCKER_PATH, *self.DOCKER_ARGS, *filter_args]
        cp = self._run_subprocess(*args, require_success=True)
        lines = cp.stdout.splitlines()

        for cfg in self.status_map.keys():
            status_match_amount = 0
            for line in lines:
                if cfg.search_regexp.match(line):
                    status_match_amount += 1

            self.status_map[cfg].updated_ticks_ago += 1
            if self.status_map[cfg].container_amount is None:
                self.status_map[cfg].updated_ticks_ago = self.AMOUNT_UPDATE_HIGHLIGHT_DELAY_TICKS
            elif self.status_map[cfg].container_amount != status_match_amount:
                self.status_map[cfg].updated_ticks_ago = 0
            self.status_map[cfg].container_amount = status_match_amount

        self.logger.debug(
            "Container status: {}".format({cfg.name: v.container_amount for cfg, v in self.status_map.items()})
        )
        self.logger.debug(
            "Updated ticks ago: {}".format({cfg.name: v.updated_ticks_ago for cfg, v in self.status_map.items()})
        )

    def _print(self, error: bool = False):
        label = self.renderer.render("D", StyleRegistry.LABEL)
        if error:
            output = self.renderer.render("ERROR", Styles.ERROR)
        else:
            output = " ".join(
                (self._render_val(cfg, state) if state.container_amount is not None else "-" * self.AMOUNT_FIELD_SIZE)
                for cfg, state in self.status_map.items()
            )
        print(f"{label} {output}")
        sys.stdout.flush()

    def _render_val(self, cfg: DockerStatusConfig, state: StatusState) -> str:
        style = cfg.style_static

        if state.container_amount == 0:
            style = StyleRegistry.DISABLED
        if state.updated_ticks_ago < self.AMOUNT_UPDATE_HIGHLIGHT_DELAY_TICKS:
            style = cfg.style_changed

        if len(str(state.container_amount)) <= self.AMOUNT_FIELD_SIZE:
            val = f"{state.container_amount:{cfg.align}{self.AMOUNT_FIELD_SIZE}d}"
        else:
            val = "H".ljust(self.AMOUNT_FIELD_SIZE, "+")
        return self.renderer.render(val, style)


# ------------------------------------------------------------------------------


@group.command(name="docker", cls=CliCommand, short_help="*  docker container status counters")
@click.option(
    "-t", "--tmux", cls=CommandOption, is_flag=True, default=False, help="Transform output SGRs to tmux markup."
)
@click.pass_context
def monitor_docker(ctx: click.Context, **kwargs):
    """
    <FILLME>
    """
    MonitorDockerCommand(ctx, **kwargs)
