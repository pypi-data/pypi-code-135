"""Login CLI command definition."""
import click
from rich.console import Console
from rich.style import Style

from dapla_team_cli.auth.services.get_token import get_token


console = Console()

styles = {
    "normal": Style(blink=True, bold=True),
    "warning": Style(color="dark_orange3", blink=True, bold=True),
}


@click.command()
def list_token() -> None:
    """Retrieves keycloak token from local machine or informs user that no such token exists."""
    keycloak_token = get_token()

    if keycloak_token:
        console.print(f"Your token: {keycloak_token}", style=styles["normal"])
    else:
        console.print(
            "You do not have a keycloak token set. Please run dpteam auth login --with-token <your_token> in order to add it.",
            style=styles["normal"],
        )
