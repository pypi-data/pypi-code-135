"""IAM Bindings CLI command definition."""
import os
import shutil
import sys
import time
from io import TextIOWrapper
from typing import Any
from typing import List

import click
import git
import questionary as q
from rich.console import Console
from rich.style import Style
from rich.tree import Tree

from dapla_team_cli import github
from dapla_team_cli.config import get_config_folder_path
from dapla_team_cli.team import TeamInfo
from dapla_team_cli.tf.iam_bindings import IAMBindingConfig
from dapla_team_cli.tf.iam_bindings import MissingUserSuppliedInfoError
from dapla_team_cli.tf.iam_bindings import jinja_env
from dapla_team_cli.tf.iam_bindings.auth_groups import AuthGroup
from dapla_team_cli.tf.iam_bindings.auth_groups import ask_for_auth_group_name
from dapla_team_cli.tf.iam_bindings.buckets import ask_for_buckets
from dapla_team_cli.tf.iam_bindings.environments import ask_for_environments
from dapla_team_cli.tf.iam_bindings.expiry import ask_for_expiry
from dapla_team_cli.tf.iam_bindings.project_roles import ask_for_project_roles
from dapla_team_cli.tf.iam_bindings.terraform import parse_team_info
from dapla_team_cli.tf.iam_bindings.terraform import write_tf_files


console = Console()

styles = {
    "normal": Style(blink=True, bold=True),
    "warning": Style(color="dark_orange3", blink=True, bold=True),
    "success": Style(color="green", blink=True, bold=True),
}


@click.command()
@click.option(
    "team_repo_path",
    "--team-repo",
    default=os.path.abspath("."),
    type=click.Path(exists=True),
    help="Path to your local team iac repo. Default: current dir.",
)
@click.option(
    "auth_group",
    "--auth-group",
    "-g",
    help='Name of "auth group", such as demo-enhjoern-a-support',
)
@click.option(
    "push_to_github",
    "--github/--no-github",
    default=True,
    help="True if the changes should be be pushed as a branch to GitHub",
)
@click.option(
    "source_config_file",
    "--source-config",
    type=click.File("rb"),
    help="Read config from json instead of prompting interactively",
)
@click.option(
    "target_config_file",
    "--target-config",
    type=click.File("w"),
    help="Name of target config json file (if you later want to replay without interactive prompting)",
)
def iam_bindings(
    team_repo_path: str, auth_group: str, push_to_github: bool, source_config_file: Any, target_config_file: Any
) -> None:
    """Create IAM Binding Terraform files that assign roles and permissions to a group of Dapla users.

    You are prompted to supply information such as name of the group, environments, project roles, bucket roles
    and also a timeframe that the IAM binding should be constrained by. Terraform files are then created, one for each
    environment and auth group, keeping configuration neatly grouped and separated.

    \b
    Example:
        Let's say you want the support group of a team (e.g. `demo-enhjoern-a`) to be able to administer Secret Manager
        for a limited amount of time in both `staging` and `prod` environments. The output from this command would then
        be two files: `iam-support-staging.tf` and `iam-support-prod.tf`.

    Note that the command is strictly working with _one_ auth group. You need to run the command multiple times if you
    want to create IAM bindings for multiple groups. Alternatively, you can record the config and re-run in
    non-interactive mode, only changing the name of the auth group between executions.
    """
    team_repo_path = ask_for_iac_repo()

    if source_config_file:
        config_json = source_config_file.read()
        config = IAMBindingConfig.parse_raw(config_json)
    else:
        try:
            config = ask_for_config(team_repo_path, auth_group)
        except MissingUserSuppliedInfoError as e:
            bail_out(str(e), 1)

    config_folder_path = get_config_folder_path(tmp=True)

    if not os.path.exists(f"{team_repo_path}/.git"):
        console.print("The provided IAC repo does not seem to be a git repository (missing .git folder)", style=styles["warning"])
        console.print(
            "We need this to create a pull request. Please provide a IAC repo that is pulled using git.", style=styles["warning"]
        )
        exit(1)
    else:

        g = git.cmd.Git(team_repo_path)
        iac_repo_remote_url = str(g.execute(["git", "remote", "get-url", "origin"]))

    g = git.cmd.Git(config_folder_path)

    iac_repo_clone_folder = f"{int(time.time())}-{config.team_name}"
    iac_repo_clone_path = f"{config_folder_path}/{iac_repo_clone_folder}"

    console.print(
        f"Cloning a copy of {config.team_name} from {iac_repo_remote_url} into temporary folder...", style=styles["normal"]
    )

    g.execute(["git", "clone", f"{iac_repo_remote_url}", f"{iac_repo_clone_path}"])

    console.print(
        "Cloning complete. Temporary files will automatically be removed after this command has finished running.",
        style=styles["normal"],
    )

    target_tf_files = write_tf_files(config, target_path=iac_repo_clone_path)

    print_summary(config, target_tf_files)

    if target_config_file:
        target_config_file.write(config.json())

    if push_to_github:
        rationale = ask_for_rationale()
        create_git_branch(repo_path=iac_repo_clone_path, config=config, files=target_tf_files, rationale=rationale)

    cleanup_iac_temp_folder(iac_repo_clone_path)


def create_git_branch(repo_path: str, config: IAMBindingConfig, files: List[TextIOWrapper], rationale: str) -> None:
    """Push a new branch with the generated IAM bindings files to GitHub.

    Create a git branch with a descriptive name and detailed commit message.

    Attributes:
        repo_path: path to a local clone of the iac git repo
        config: user preferences
        files: the Terraform IAM binding files that should be applied through a new PR
        rationale: Short user-supplied text that outlines why the IAM bindings are created. This is included in the
        commit message and serves as an audit log
    """
    environments = "-and-".join(config.environments)
    branch_name = f"iam-bindings-for-{config.auth_group.shortname}-in-{environments}-{int(time.time())}"
    template = jinja_env.get_template("iam-bindings-git-commit-msg.jinja")
    commit_msg = template.render(c=config, rationale=rationale)
    instruction_msg = f"""A new branch called {branch_name} has been pushed to GitHub.
    Create a pull request and issue an 'atlantis apply'-comment in order to effectuate the IAM bindings."""
    b = github.NewBranch(
        repo_path=repo_path,
        branch_name=branch_name,
        commit_msg=commit_msg,
        files=[f.name for f in files],
        instruction_msg=instruction_msg,
    )
    github.create_branch(b)


def ask_for_config(team_repo_path: str, auth_group_name: str) -> IAMBindingConfig:
    """Ask the user for configuration used to generate IAM binding Terraform files.

    Args:
        team_repo_path: Path to a clone of the team's iac repo residing on the local filesystem. If not specified, then
            the current directory is searched.
        auth_group_name: Name of an auth group. If not specified, then the user is prompted explicitly for this.

    Returns:
        User supplied config used to generate IAM Terraform files

    Raises:
        MissingUserSuppliedInfoError: if the user failed to specify enough information (such as at least one environment)
    """
    team = _deduce_team_info(team_repo_path)

    if not auth_group_name:
        auth_group_name = ask_for_auth_group_name(team.name)
    auth_group = AuthGroup(name=auth_group_name, shortname=auth_group_name.replace(f"{team.name}-", ""))

    project_roles = ask_for_project_roles(auth_group_name)
    buckets = ask_for_buckets(team.name, auth_group_name)

    if not project_roles and buckets:
        raise MissingUserSuppliedInfoError("No roles or buckets specified, nothing to do...")

    environments = ask_for_environments()
    if not environments:
        raise MissingUserSuppliedInfoError("No environments specified, nothing to do...")

    gcp_projects = [f"{env}-{team.name}" for env in environments]
    expiry = ask_for_expiry()

    return IAMBindingConfig(
        team_name=team.name,
        auth_group=auth_group,
        project_roles=project_roles,
        buckets=buckets,
        environments=environments,
        org_nr=team.org_nr,
        gcp_projects=gcp_projects,
        expiry=expiry,
    )


def _deduce_team_info(team_repo_path: str) -> TeamInfo:
    """Inspect the `team_repo_path` and deduce team name from the residing ´terraform.tfvars` file.

    Args:
        team_repo_path: Path to a clone of the team's iac repo residing on the local filesystem.

    Returns:
        Team information deduced from the iac repo.

    Raises:
        ValueError: If team info could not be deduced from the `team_repo_path`
    """
    try:
        team_info = parse_team_info(team_repo_path)
    except (TypeError, ValueError) as err:
        print(err)

    if not team_info:
        raise ValueError("Failed to deduce team info")

    return team_info


def ask_for_iac_repo() -> str:
    """Asks for a path to valid IAC repo if no terraform.vars file is found in the current repository.

    Returns:
        IAC repo path in the form of a string
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
    else:
        iac_repo_path = os.getcwd()
        print(iac_repo_path)

    return str(iac_repo_path)


def cleanup_iac_temp_folder(iac_repo_clone_path: str) -> None:
    """Cleans up temporary files in the .config folder that were cloned from github.

    Args:
        iac_repo_clone_path: Path to the cloned IAC repo (i.e the temporary files).
    """
    console.print("Cleaning up temporary files...", style=styles["normal"])

    if os.path.exists(iac_repo_clone_path):
        shutil.rmtree(iac_repo_clone_path)
    else:
        console.print(
            f"Failed to remove temporary files at {iac_repo_clone_path}. File was not correctly created or has been moved.",
            style=styles["warning"],
        )
        exit(1)

    console.print("Succesfully removed temporary files", style=styles["success"])


def ask_for_rationale() -> Any:
    """Ask the user for a reason for adding the IAM bindings.

    This text is included in the commit message and serves as an audit log.

    Returns:
        User-supplied rationale for adding the IAM bindings
    """
    return q.text("Why is the access needed?").ask()


def bail_out(message: str, exit_code: int = 0) -> None:
    """Print an exit message and exit the command with a status code.

    Args:
        message: The message to print when exiting.
        exit_code: Exit code to use when exiting. 0 means ok.
    """
    q.print(message)
    sys.exit(exit_code)


def print_summary(config: IAMBindingConfig, target_tf_files: List[TextIOWrapper]) -> None:
    """Print a summary of the executed command, detailing the user's choices and the resulting files.

    Args:
        config: The user supplied configuration that was used.
        target_tf_files: The generated Terraform files.
    """
    console = Console(record=True, width=100)
    tree = Tree(f"📎 [bold reverse]IAM bindings for [italic]{config.auth_group.name}")
    tree.add(f"🔩 [bold bright_white]GCP Projects:[/] {', '.join(config.gcp_projects)}")
    tree.add(f"📅 [bold bright_white]Timeframe:[/] {config.expiry.name} [bright_black]({config.expiry.timestamp})")

    if config.project_roles:
        project_roles = tree.add("🧢 [bold bright_white]Project Roles")
        for r in config.project_roles:
            project_roles.add(f"{r.title} [bright_black]({r.name})")

    if config.buckets:
        buckets = tree.add("🪣 [bold bright_white]Buckets")
        for env in config.environments:
            for b in config.buckets:
                # TODO: Add method to deduce this in BucketAuth class instead
                buckets.add(f"ssb-{env}-{config.team_name}-{b.simple_name} [bright_black]({b.access_type})")

    if target_tf_files:
        tf_files = tree.add("📄 [bold bright_white]Terraform files")
        for tf_file in target_tf_files:
            tf_files.add(f"[link=file:///{tf_file.name}]{os.path.basename(tf_file.name)}[/link]")

    console.print(tree)
