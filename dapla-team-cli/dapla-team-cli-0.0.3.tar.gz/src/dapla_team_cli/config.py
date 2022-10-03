"""CLI-wide config variables."""
import os
from sys import platform


if platform in ("linux", "darwin"):
    import pwd

from rich.console import Console
from rich.style import Style


console = Console()

styles = {
    "normal": Style(blink=True, bold=True),
    "error": Style(color="red", blink=True, bold=True),
    "success": Style(color="green", blink=True, bold=True),
    "warning": Style(color="dark_orange3", blink=True, bold=True),
}


def get_config_folder_path(tmp: bool = False) -> str:
    """Gets the config folder path on current machine.

    Args:
        tmp: A true/false flag that determines whether function should return temporary folder or base folder.

    Raises:
        Exception: If the platform is not linux, darwin (macos) or windows.

    Returns:
        The config folder path, or temporary folder path inside config folder.
    """
    if platform in ("linux", "darwin"):
        username = pwd.getpwuid(os.getuid())[0]
    elif platform == "windows":
        username = os.getlogin()
    else:
        raise Exception("Unknown platform. The CLI only supports Unix and Windows based platforms.")

    if platform in ("darwin", "linux"):
        config_folder_path = rf"/Users/{username}/.config/dapla-team-cli"
    else:
        config_folder_path = rf"C:\Users\{username}\AppData\dapla-team-cli"

    if not os.path.exists(config_folder_path):
        os.makedirs(config_folder_path)

    if tmp:
        return str(config_folder_path + "/tmp")
    else:
        return str(config_folder_path)


DAPLA_TEAM_API_BASE = "https://team-api.dapla-staging.ssb.no/"
