from pydantic import confloat
from pydantic.dataclasses import dataclass as pd_dataclass

from typing import List


@pd_dataclass
class ClassificationPrediction:
    #: A human-readable name of the Prediction.
    name: str
    #: The statistical confidence of the Prediction.
    confidence: float
    #: A unique identifier of the Prediction.
    id: str = ""


@pd_dataclass
class ClassificationPredictionSet:
    #: A list of predictions
    predictions: List[ClassificationPrediction]
