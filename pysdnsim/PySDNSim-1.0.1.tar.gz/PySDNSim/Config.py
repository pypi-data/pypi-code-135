from typing import Any


class Config:
    """
    Simulation configurations.
    """
    _interval: float
    _step_size: float
    _seed: Any

    def __init__(self, seed: Any, interval: float = 1.0, step_size: float = 0.001):
        """
        Simulation configurations with a given seed, interval and step size.

        :param seed: random number generator seed.
        :param interval: scheduler interval.
        :param step_size: simulation step size.
        """
        self._interval = interval
        self._step_size = step_size
        self._seed = seed

    @property
    def interval(self):
        return self._interval

    @property
    def step_size(self):
        return self._step_size

    @property
    def seed(self):
        return self._seed
