import pydantic
from typing import List


class ClassLabel(pydantic.BaseModel):
    name: str = pydantic.Field(
        ...,
        description='A human-readable name of the class label'
    )


class AuditLabel(pydantic.BaseModel):
    names: List[str] = pydantic.Field(
        ...,
        description="A list of classes with human-readable names"
    )


class BoundingBox(pydantic.BaseModel):
    x: float
    y: float
    width: float
    height: float


class SemSegRunLengthEncoding(pydantic.BaseModel):
    pass


class SegmentationMask(pydantic.BaseModel):
    pass


class BoundingPolygon(pydantic.BaseModel):
    pass
