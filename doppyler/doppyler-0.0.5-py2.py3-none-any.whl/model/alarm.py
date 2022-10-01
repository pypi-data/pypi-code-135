"""Models for alarm."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import time
from enum import Enum, IntEnum
from typing import TypedDict

from ..const import ATTR_COLOR, ATTR_ID, ATTR_NAME, ATTR_REPEAT, ATTR_SOUND, ATTR_VOLUME
from .color import Color, ColorDict


class RepeatDayOfWeek(str, Enum):
    """Day of the week to repeat alarm enum."""

    MONDAY = "Mo"
    TUESDAY = "Tu"
    WEDNESDAY = "We"
    THURSDAY = "Th"
    FRIDAY = "Fr"
    SATURDAY = "Sa"
    SUNDAY = "Su"


class AlarmSource(IntEnum):
    """Alarm source enum."""

    SYSTEM = 0
    APP = 1
    ALEXA = 2


class AlarmDict(TypedDict):
    """Representation of an alarm."""

    id: int
    name: str
    time_hr: int
    time_min: int
    repeat: str
    color: ColorDict
    volume: int
    status: int
    src: int
    sound: str


@dataclass
class Alarm:
    """Alarm class."""

    id: int
    name: str
    alarm_time: time
    repeat: list[RepeatDayOfWeek]
    color: Color
    volume: int
    status: bool
    src: AlarmSource
    sound: str

    def to_dict(self) -> AlarmDict:
        """Convert Alarm to AlarmDict."""
        return {
            ATTR_ID: self.id,
            ATTR_NAME: self.name,
            "time_hr": self.alarm_time.hour,
            "time_min": self.alarm_time.minute,
            ATTR_REPEAT: "".join([day_of_week.value for day_of_week in self.repeat]),
            ATTR_COLOR: {
                "red": self.color.red,
                "green": self.color.green,
                "blue": self.color.blue,
            },
            ATTR_VOLUME: self.volume,
            "status": int(self.status),
            "src": self.src.value,
            ATTR_SOUND: self.sound,
        }

    @staticmethod
    def from_dict(alarm_dict: AlarmDict) -> "Alarm":
        """Create Alarm from dict."""
        alarm_dict["repeat"] = alarm_dict["repeat"].replace("0", "")
        return Alarm(
            alarm_dict[ATTR_ID],
            alarm_dict[ATTR_NAME],
            time(hour=alarm_dict["time_hr"], minute=alarm_dict["time_min"]),
            [
                RepeatDayOfWeek(day)
                for day in [
                    alarm_dict[ATTR_REPEAT][i : i + 2]
                    for i in range(0, len(alarm_dict["repeat"]), 2)
                    if alarm_dict[ATTR_REPEAT][i : i + 2]
                ]
            ],
            Color.from_dict(alarm_dict[ATTR_COLOR]),
            alarm_dict[ATTR_VOLUME],
            bool(alarm_dict["status"]),
            AlarmSource(alarm_dict["src"]),
            alarm_dict[ATTR_SOUND],
        )
