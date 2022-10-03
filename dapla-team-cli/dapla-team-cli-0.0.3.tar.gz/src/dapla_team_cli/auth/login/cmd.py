"""Login CLI command definition. Sets credentials on local machine for CLI user."""
import click

from dapla_team_cli.auth.services.set_token import set_token


@click.command()
@click.option(
    "keycloak_token",
    "--with-token",
    "-wt",
    help="The keycloak token needed to access Dapla Team API´",
)
def login(keycloak_token: str) -> None:
    """Creates or updates a file with a keycloak token for access to Dapla Team API.

    Args:
        keycloak_token: The authorization token needed to access Dapla Team API
    """
    set_token(keycloak_token)
