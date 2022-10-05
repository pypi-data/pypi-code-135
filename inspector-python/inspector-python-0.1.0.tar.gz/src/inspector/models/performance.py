from __future__ import annotations
from abc import abstractmethod
import time
from typing import Union
from src.inspector.models import HasContext


class Performance(HasContext):
    _timestamp: Union[None, float] = None
    _duration: Union[None, float] = None

    # Start the timer.
    # type: None|float
    # param: timestamp
    # return: Performance
    @abstractmethod
    def start(self, timestamp: Union[None, float] = None) -> Performance:
        self._timestamp = timestamp if timestamp else round(time.time() * 1000)
        print('\n\nself._timestamp: ', self._timestamp)
        return self

    # Stop the timer and calculate duration.
    # type: None|float
    # param: duration
    # return: Performance
    @abstractmethod
    def end(self, duration: Union[None, float] = None) -> Performance:
        """

        :type: object
        """
        self._duration = duration if duration else (round(time.time() * 1000) - self._timestamp)
        return self

    def get_timestamp(self):
        return self._timestamp

    def get_duration(self):
        return self._duration
