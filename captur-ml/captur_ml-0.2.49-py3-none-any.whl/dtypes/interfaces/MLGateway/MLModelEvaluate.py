import pydantic
from pydantic import HttpUrl

from captur_ml_sdk.dtypes.generics.mongo import MongoImage
from typing import List, Optional


class Meta(pydantic.BaseModel):
    webhooks: Optional[List[HttpUrl]] = pydantic.Field(
        None,
        description="Webhooks to which the evaluation should be sent."
    )
    request_id: Optional[str] = pydantic.Field(
        "",
        description="Unique identifier for the request."
    )
    metrics: Optional[List[str]] = pydantic.Field(
        None,
        description="List of metrics to be calculated."
    )
    is_external: Optional[bool] = pydantic.Field(
        True,
        description="Whether the evaluation request is for external or internal purposes."
    )


class MongoModelEvaluateRequest(pydantic.BaseModel):
    data: List[MongoImage] = pydantic.Field(
        ...,
        description="Data to be used for evaluation."
    )
    meta: Optional[Meta] = pydantic.Field(
        None,
        description="Additional information included in the request."
    )
