from urllib.parse import urlparse
import json

from sklearn.linear_model import LinearRegression
from saleStorePredictor.config import ConfigurationManager
from saleStorePredictor.components import ModelEvaluationAndPusher, data_ingestion
from saleStorePredictor import logger
from saleStorePredictor.utils import load_bin,load_json
from pathlib import Path 
import mlflow
import mlflow.sklearn


STAGE_NAME = "Model evaluation stage"

def main():
    config = ConfigurationManager()
    model_evaluation_config = config.get_model_evaluation_config()
    data_ingestion_artifact = config.get_data_ingestion_artifact()
    model_trainer_artifact = config.get_model_trainer_artifact()
    model_pusher_config = config.get_pusher_config()
    model_trainer_config = config.get_data_model_trainer_config()

    model_traner = ModelEvaluationAndPusher(
        model_evaluation_config=model_evaluation_config,
        data_ingestion_artifact=data_ingestion_artifact,
        model_trainer_artifact=model_trainer_artifact,
        model_pusher_config=model_pusher_config
    )
    with mlflow.start_run():
        
        model_info = model_traner.initiate_model_evaluation()
        model = load_bin(Path(model_info.evaluated_model_path)) 
        report = load_json(Path(model_trainer_config.model_report_file_path))

        mlflow.log_metric("train_rmse",report.train_rmse)
        mlflow.log_metric("test_rmse",report.test_rmse)
        mlflow.log_metric("train_accuracy",report.train_accuracy)
        mlflow.log_metric("test_accuracy",report.test_accuracy)
        mlflow.log_metric("model_accuracy",report.model_accuracy)
        

        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        # Model registry does not work with file store
        if tracking_url_type_store != "file":

            # Register the model
            # There are other ways to use the Model Registry, which depends on the use case,
            # please refer to the doc for more information:
            # https://mlflow.org/docs/latest/model-registry.html#api-workflow
            mlflow.sklearn.log_model(model, "model", registered_model_name=model.__name__)
        else:
            mlflow.sklearn.log_model(model, "model")
    



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e