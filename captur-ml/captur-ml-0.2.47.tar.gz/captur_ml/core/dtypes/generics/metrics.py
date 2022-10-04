# from pydantic.dataclasses import dataclass as pd_dataclass

# from typing import Optional, Dict, List, Union


# @dataclass
# class ClassificationStandardMetrics:
#     #: The precision of the classification model
#     accuracy: Optional[float] = pydantic.Field("", description="Overall model accuracy")
#     confusion_matrix: Optional[List[str]] = pydantic.Field(
#         "",
#         description="Confusion matrix showing numbers of correct predictions and confusion between classes",
#     )
#     f1_score: Optional[float] = pydantic.Field("", description="Overall model f1 score")
#     f1_score_per_class: Optional[Dict[str, Union[float, None]]] = pydantic.Field(
#         "", description="F1 score calculated separately for each class in the dataset"
#     )
#     precision: Optional[float] = pydantic.Field(
#         "", description="Overall model precision score"
#     )
#     precision_per_class: Optional[Dict[str, Union[float, None]]] = pydantic.Field(
#         "", description="Precision calculated separately for each class in the dataset"
#     )
#     recall: Optional[float] = pydantic.Field(
#         "", description="Overall model recall score"
#     )
#     recall_per_class: Optional[Dict[str, Union[float, None]]] = pydantic.Field(
#         "", description="Recall calculated separately for each class in the dataset"
#     )


# class ClassificationAuditMetrics:
#     accuracy: Optional[float] = pydantic.Field("", description="Overall model accuracy")
#     precision_per_class: Optional[Dict[str, Union[float, None]]] = pydantic.Field(
#         "", description="Precision calculated separately for each class in the dataset"
#     )
