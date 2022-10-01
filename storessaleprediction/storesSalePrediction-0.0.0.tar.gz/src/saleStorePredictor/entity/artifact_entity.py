from dataclasses import dataclass
from pathlib import Path



@dataclass(frozen=True)
class DataIngestionArtifact:
    train_file_path: Path
    test_file_path: Path

  

@dataclass(frozen=True)
class DataTransformationArtifact:
    transformed_train_file_path: str
    transformed_test_file_path: str
    preprocessed_object_file_path: str


@dataclass(frozen=True)
class ModelTrainerArtifact:
    is_trained: bool
    trained_model_file_path: str
    train_rmse: float
    test_rmse: float
    train_accuracy: float
    test_accuracy: float
    model_accuracy: float

@dataclass(frozen=True)
class ModelEvaluationArtifact:
    is_model_accepted: bool
    evaluated_model_path: str







   