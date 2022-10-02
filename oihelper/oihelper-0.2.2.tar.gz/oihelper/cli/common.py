import os
import pathlib
import re
import click

CONFIG_DIR = os.path.expanduser(f"{pathlib.Path.home()}/oi-helper/")

CONFIG_FILE = pathlib.Path(f"{CONFIG_DIR}/config.json")

STATUS_COLORS = {
    "AC": "green",
    "WA": "red",
    "RE": "magenta",
    "TLE": "cyan",
    "MLE": "yellow",
    "UKE": "blue",
}


class OIHelperRuntimeError(Exception):
    def __init__(self, message=None) -> None:
        if message:
            self.message = message
        self.message = "An unexpected error happened during execution. There should be more expansions above."
        super().__init__(self.message)


def get_testcase_no(testcase: str) -> int:
    testcase_no = 0
    custom_testcase_tester = re.compile("\w+\d+-\d+.\w+")
    if custom_testcase_tester.match(testcase):
        return int(testcase.split("-", 1)[-1].split(".")[0])

    for char in testcase:
        if char.isdigit():
            testcase_no = testcase_no * 10 + int(char)
    return testcase_no


def abort_with_error(msg: str) -> None:
    click.echo(click.style(f"Error: {msg}", bold=True, fg="red"))
    raise click.Abort(msg)


def warn(msg: str) -> None:
    click.echo(click.style(f"Warning: {msg}", bold=True, fg="yellow"))
