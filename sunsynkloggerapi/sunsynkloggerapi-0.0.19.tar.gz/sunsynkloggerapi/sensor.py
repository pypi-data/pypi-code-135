""" SunSynk Logger API Sensor Classes"""
import copy
from typing import Any, Iterator, List, Optional, Union

import attr

from .const import (
    _LOGGER
)


@attr.s(slots=True)
class Sensor:
    """SunSynk Sensor"""

    key: str = attr.ib()
    name: str = attr.ib()
    unit: str = attr.ib(default="")
    value: Any = attr.ib(default=None)
    enabled: bool = attr.ib(default=True)

    def __attrs_post_init__(self) -> None:
        """Post init Sensor."""
        key = str(self.key)

class Sensors:
    """SunSynk Inverter Sensors."""

    def __init__(self, sensors: Union[Sensor, List[Sensor], None] = None):
        self.__s: List[Sensor] = []
        if sensors:
            self.add(sensors)

    def __len__(self) -> int:
        return len(self.__s)

    def __contains__(self, key: str) -> bool:
        try:
            if self[key]:
                return True
        except KeyError:
            pass
        return False

    def __getitem__(self, key: str) -> Sensor:
        for sen in self.__s:
            if key in (sen.name, sen.key):
                return sen
        raise KeyError(key)

    def __iter__(self) -> Iterator[Sensor]:
        return self.__s.__iter__()

    def add(self, sensor: Union[Sensor, List[Sensor]]) -> None:
        if isinstance(sensor, (list, tuple)):
            for sss in sensor:
                self.add(sss)
            return

        if isinstance(sensor, Sensor):
            sensor = copy.copy(sensor)
        else:
            raise TypeError("Sensor Object Expected")

        if sensor.name in self:
            old = self[sensor.name]
            self.__s.remove(old)
            _LOGGER.warning("Replacing sensor %s with %s", old, sensor)

        self.__s.append(sensor)