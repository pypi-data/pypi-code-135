from logging import exception
from saleStorePredictor.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from saleStorePredictor.entity.config_entity import ModelPusherConfig
from saleStorePredictor.utils import read_yaml, create_directories, load_json
from saleStorePredictor.entity import DataIngestionConfig, ModelTrainerConfig,ModelTrainerArtifact,ModelEvaluationConfig
from saleStorePredictor.entity import DataValidationConfig, DataTransformationConfig,DataTransformationArtifact,DataIngestionArtifact

from pathlib import Path
import os
import datetime
from saleStorePredictor import logging

class ConfigurationManager:
    def __init__(
        self, 
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
            ingested_train_dir=config.ingested_train_dir,
            ingested_test_dir=config.ingested_test_dir 
        )

        return data_ingestion_config

    def get_pusher_config(self) -> ModelPusherConfig:

        config = self.config.model_pusher_config


        pusher_config = ModelPusherConfig(
            model_pusher_file_path = config.model_export_dir
        )

        return pusher_config




    def get_data_ingestion_artifact(self) -> DataIngestionArtifact:

        config = self.config.data_ingestion        

        training_dataset = os.path.join(config.ingested_train_dir,config.train_file_name)
        testing_dataset = os.path.join(config.ingested_test_dir,config.test_file_name)

        data_ingestion_artifact = DataIngestionArtifact(
            train_file_path= training_dataset,
            test_file_path= testing_dataset
        )
        return data_ingestion_artifact



    def get_data_validation_config(self) -> DataValidationConfig:
    
        config = self.config.data_validation_config
        ingestion_config = self.config.data_ingestion

        create_directories([config.validated_train_dir,config.validated_test_dir])
        

        training_dataset = os.path.join(config.validated_train_dir,ingestion_config.train_file_name)
        testing_dataset = os.path.join(config.validated_test_dir,ingestion_config.test_file_name)
        dataValidationConfig = DataValidationConfig(
            training_dataset=training_dataset,
            test_dataset=testing_dataset,
            schema_path=SCHEMA_FILE_PATH
            )
        
        return  dataValidationConfig  


    def get_data_transformation_config(self) -> DataTransformationConfig:
    
        config = self.config.data_ingestion
        trans_config = self.config.data_transformation_config
        

        training_dataset = os.path.join(config.ingested_train_dir,config.train_file_name)
        testing_dataset = os.path.join(config.ingested_test_dir,config.test_file_name)
        transformed_training_dataset = os.path.join(trans_config.transformed_dir,trans_config.transformed_train_dir)
        transformed_test_dataset = os.path.join(trans_config.transformed_dir,trans_config.transformed_test_dir)
        preprocessed_object_path_file  = os.path.join(trans_config.preprocessing_dir,trans_config.preprocessed_object_file_name)
       
        dataTransformationConfig = DataTransformationConfig(
            training_dataset=training_dataset,
            test_dataset=testing_dataset,
            schema_path=SCHEMA_FILE_PATH,
            transformed_train_path_file=transformed_training_dataset,
            transformed_test_path_file=transformed_test_dataset,
            preprocessed_object_path_file=preprocessed_object_path_file
             )
        
        return  dataTransformationConfig  


    def get_data_transformation_artifact(self) -> DataTransformationArtifact:


            trans_config = self.config.data_transformation_config
            transformed_training_dataset = Path(os.path.join(trans_config.transformed_dir,trans_config.transformed_train_dir,trans_config.transformed_train_file_name))
            transformed_test_dataset = Path(os.path.join(trans_config.transformed_dir,trans_config.transformed_test_dir,trans_config.transformed_test_file_name))
            preprocessed_object_path_file  = Path(os.path.join(trans_config.preprocessing_dir,trans_config.preprocessed_object_file_name))


            data_transformation_artifact = DataTransformationArtifact(
                transformed_train_file_path = transformed_training_dataset,
                transformed_test_file_path = transformed_test_dataset,
                preprocessed_object_file_path = preprocessed_object_path_file

                )

            return data_transformation_artifact


    """   model_evaluation_config: ModelEvaluationConfig,
                 data_ingestion_artifact: DataIngestionArtifact,
                 model_trainer_artifact: ModelTrainerArtifact   """ 


    def get_model_trainer_artifact(self) -> ModelTrainerArtifact:
        model_config = self.config.model_trainer_config
        model_report_file_path = Path(os.path.join(model_config.trained_model_dir,model_config.model_report_file_name))

        data = load_json(model_report_file_path)
       
        model_trainer_artifact = ModelTrainerArtifact(
        is_trained=data.is_trained,
        trained_model_file_path=data.trained_model_file_path,
        train_rmse=data.train_rmse,
        test_rmse=data.test_rmse,
        train_accuracy=data.train_accuracy,
        test_accuracy=data.test_accuracy,
        model_accuracy=data.model_accuracy  )


        return model_trainer_artifact

        


        

            


    def get_model_evaluation_config(self) -> ModelEvaluationConfig:

            model_evaluation_config = self.config.model_evaluation_config

            logging.info("Model evaluation config: {}".format(model_evaluation_config))

            create_directories([os.path.dirname(model_evaluation_config.model_evaluation_file_name)])
            model_evaluation_config = ModelEvaluationConfig(
                model_evaluation_file_path =model_evaluation_config.model_evaluation_file_name,
                best_model=model_evaluation_config.best_model,
                time_stamp=datetime.datetime.now())
            
            return model_evaluation_config








    def get_data_model_trainer_config(self) -> ModelTrainerConfig:

        model_config = self.config.model_trainer_config
        trained_model_file_path =   Path(os.path.join(model_config.trained_model_dir,model_config.model_file_name))
        model_config_file_path =   Path(os.path.join(model_config.model_config_dir,model_config.model_config_file_name))
        model_report_file_path = Path(os.path.join(model_config.trained_model_dir,model_config.model_report_file_name))
        model_trainer_config = ModelTrainerConfig(
            trained_model_file_path=trained_model_file_path,
            base_accuracy=model_config.base_accuracy ,
            model_config_file_path=model_config_file_path,
            model_report_file_path=model_report_file_path)


        return model_trainer_config    


        
     


        

        