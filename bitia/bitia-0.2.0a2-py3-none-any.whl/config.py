import os
import typing as T
from pathlib import Path
import tempfile

BITIA_MAIN_SCRIPT_NAME: T.Final[str] = "__main__.bitia.sh"

g_server = "https://public.bitia.link/api/v1"


def bitia_dir() -> Path:
    """CLI cache directory"""
    bdir = Path(tempfile.gettempdir()) / "bitia"
    bdir.mkdir(parents=True, exist_ok=True)
    return bdir


def get_server(use_env: bool = True) -> str:
    """Server to use"""
    if use_env and os.environ.get("BITIA_SERVER") is not None:
        return os.environ["BITIA_SERVER"]
    return g_server


def set_server(server: str):
    """set bitia server"""
    global g_server
    g_server = server
