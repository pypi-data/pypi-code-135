"""Common services for groups CLI commands."""
import os
import re

import questionary as q
import tfvars
from rich.console import Console
from rich.style import Style

from dapla_team_cli.team import TeamInfo


console = Console()

styles = {
    "normal": Style(blink=True, bold=True),
    "warning": Style(color="dark_orange3", blink=True, bold=True),
}


def deduce_team_info() -> TeamInfo:
    """Inspect the current directory and deduce team name from the residing ´terraform.tfvars` file.

    Returns:
        Team information deduced from the iac repo

    Raises:
        ValueError: If team info could not be deduced from the current directory
    """
    try:
        team_info = parse_team_info()
    except (TypeError, ValueError) as err:
        print(err)
        raise ValueError("Could not run because current directory is not a IAC repo: ") from None

    if not team_info:
        raise ValueError("Failed to deduce team info")

    return team_info


def parse_team_info() -> TeamInfo:
    """Retrieve team info and organization number from .tfvars file.

    Returns:
        The team info retrieved from file.
    """
    path_to_tfvars = "terraform.tfvars"
    if not os.path.isfile(path_to_tfvars):
        iac_repo_path = os.path.abspath(
            q.path(
                "Path to the team iac repo",
                only_directories=True,
            ).ask()
        )

        path_to_tfvars = iac_repo_path + "/terraform.tfvars"

        if not os.path.isfile(path_to_tfvars):
            console.print(
                "No terraform.tfvars file found in the provided repo. Please provide a valid IAC repo path", style=styles["warning"]
            )
            exit(1)

    tf_vars_content = open(path_to_tfvars, encoding="UTF-8")
    match = re.search(r"organizations\/(\w{12})\/roles", tf_vars_content.read())
    assert match is not None
    org_nr = match.group(1)
    tfv = tfvars.LoadSecrets(path_to_tfvars)
    return TeamInfo(name=tfv["team_name"], org_nr=org_nr)
