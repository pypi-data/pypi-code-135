from typing import Literal

NUMBER_KEY = Literal[1, 2, 3, 4, 5, 6, 7]
NAMED_KEY = Literal[
    "coin", "robot_error", "error", "ping", "ready", "success", "wilhelm"
]
from beepy import beep as _beep  # type: ignore


def beep(*, sound: NUMBER_KEY | NAMED_KEY) -> None:
    _beep(sound=sound)  # type: ignore
