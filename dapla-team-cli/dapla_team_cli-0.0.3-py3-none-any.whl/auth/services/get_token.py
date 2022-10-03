"""Get token helper function. Retrieves the keycloak token on local machine."""
import json
import os
from typing import Union

from rich.console import Console
from rich.style import Style

from dapla_team_cli.config import get_config_folder_path


console = Console()

styles = {
    "normal": Style(blink=True, bold=True),
    "warning": Style(color="dark_orange3", blink=True, bold=True),
}


def get_token() -> Union[str, None]:
    """Retrieves token if it exists or returns None if no token exists.

    Returns:
        Either the keycloak token, if it exists, or None if it does not exist.
    """
    config_folder_path = get_config_folder_path()
    config_file_path = config_folder_path + "/dapla-cli-keycloak-token.json"

    if os.path.isfile(config_file_path):
        with open(config_file_path, encoding="UTF-8") as f:
            data = json.loads(f.read())
            keycloak_token = data["keycloak_token"]
    else:
        console.print("No valid access token found. Please run 'dpteam auth login' first.", style=styles["warning"])
        exit(1)

    return str(keycloak_token)
