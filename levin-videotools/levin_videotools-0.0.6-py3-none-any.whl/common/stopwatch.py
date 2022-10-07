import math
import time


class Stopwatch:
    def __init__(self):
        self._start_time = time.time()
        self._end_time = None
        self._time_elapsed = 0

    def stop(self):
        if self._end_time:
            raise Exception('Already stopped')

        self._end_time = time.time()
        self._time_elapsed = self._end_time - self._start_time
        return self._elapse_format()

    def _elapse_format(self):
        millis = int(math.modf(self._time_elapsed)[0] * 1000)
        sec = int(self._time_elapsed % 60)
        mins = int((self._time_elapsed / 60) % 60)
        hours = int(self._time_elapsed / 3600)

        return f"{hours}:{mins}:{sec}.{millis}"
