from pydantic.dataclasses import dataclass as pd_dataclass

from .image import Image
from .label import ClassLabel
from .prediction import ClassificationPredictionSet

from typing import List


@pd_dataclass
class TrainingData:
    #: The list of images used for training
    images: List[Image]
    #: The list of class labels used for training
    labels: List[ClassLabel]


@pd_dataclass
class PredictionData:
    #: The list of images used for prediction
    images: List[Image]


@pd_dataclass
class EvaluationData:
    #: The list of images used for evaluation
    images: List[Image]
    #: The list of class labels used for evaluation
    labels: List[ClassLabel]
    #: The list of classification predictions used for evaluation
    predictions: List[ClassificationPredictionSet]
