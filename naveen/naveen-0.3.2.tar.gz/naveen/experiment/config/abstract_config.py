from abc import ABC
from dataclasses import dataclass
from typing import List


@dataclass
class AbstractConfig(ABC):
    name: str
    reshaper: List[str]
    plotter: List[str]
    filename: str
    experiment_class = None  # type: ignore
    experiment_module: str
