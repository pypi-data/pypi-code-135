from pydantic import AnyUrl
from pydantic.dataclasses import dataclass as pd_dataclass

from captur_ml.core.dtypes.generics import ClassificationPrediction, AuditLabel
from typing import List, Optional


@pd_dataclass
class MongoImage:
    #: An http[s]:// or gs:// URL pointing to the image resource. Required if `data` is not specified.
    url: AnyUrl
    #: A unique identifier of the image.
    id: str = ""
    #: Ground truth label assigned to the image.
    label: str = ""
    #: Ground truth list of acceptable labels assigned to the image.
    audit_labels: List[AuditLabel] = ()
    #: ML Model predictions on the image.
    predictions: List[ClassificationPrediction] = ()
