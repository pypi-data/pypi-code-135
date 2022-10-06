import logging
import os, os.path
from typing import Optional


def snake_case_to_title_case(snake_case: str) -> str:
    return snake_case.replace("_", " ").capitalize()


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        style="{",
        format="[{levelname}({name}):{filename}:{funcName}] {message}",
    )


def find_file_upwards(filename: str, dir: str = ".") -> Optional[str]:
    dir = os.path.abspath(dir)
    for entry in os.scandir(dir):
        if entry.is_file() and entry.name == filename:
            return entry.path
    if dir == "/":
        return None
    parent_dir = os.path.dirname(dir)
    return find_file_upwards(filename, parent_dir)
