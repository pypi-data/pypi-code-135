from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    ingested_train_dir: Path
    ingested_test_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    """Data Validation Config"""
    training_dataset: Path 
    test_dataset: Path
    schema_path: Path

@dataclass(frozen=True)
class DataTransformationConfig:
    """
    Data Transformation Config
    """
    training_dataset: Path 
    test_dataset: Path
    schema_path: Path
    transformed_train_path_file: Path
    transformed_test_path_file: Path
    preprocessed_object_path_file: Path



@dataclass(frozen=True)
class ModelTrainerConfig:
    trained_model_file_path: str
    base_accuracy: float
    model_config_file_path: str  
    model_report_file_path: str


@dataclass
class ModelEvaluationConfig:
    model_evaluation_file_path: str 
    best_model: str
    time_stamp: float      


@dataclass(frozen=True)
class ModelPusherConfig:
    model_pusher_file_path: str
    

