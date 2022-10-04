from pydantic.dataclasses import dataclass as pd_dataclass
from typing import List


@pd_dataclass
class ClassLabel:
    #: A human-readable name of the class label
    name: str


@pd_dataclass
class AuditLabel:
    #: A list of human readable audit labels
    names: List[str]


@pd_dataclass
class BoundingBox:
    #: The x-coordinate of the top-left corner of the bounding box
    x: float
    #: The y-coordinate of the top-left corner of the bounding box
    y: float
    #: The width of the bounding box
    width: float
    #: The height of the bounding box
    height: float
