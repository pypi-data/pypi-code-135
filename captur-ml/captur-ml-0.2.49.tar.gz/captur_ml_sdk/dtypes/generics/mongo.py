import pydantic

from captur_ml_sdk.dtypes.generics import ClassificationPrediction
from typing import List, Optional


class MongoImage(pydantic.BaseModel):
    id: Optional[str] = pydantic.Field(
        "",
        description='A unique identifier of the image.'
    )
    url: Optional[pydantic.AnyUrl] = pydantic.Field(
        "",
        description='An http[s]:// or gs:// URL pointing to the image resource. Required if `data` is not specified.'
    )
    label: Optional[str] = pydantic.Field(
        "",
        description='Ground truth label assigned to the image.'
    )
    audit_labels: Optional[List[str]] = pydantic.Field(
        "",
        description='Ground truth list of acceptable labels assigned to the image.'
    )
    predictions: Optional[List[ClassificationPrediction]] = pydantic.Field(
        "",
        description='ML Model predictions on the image.'
    )
