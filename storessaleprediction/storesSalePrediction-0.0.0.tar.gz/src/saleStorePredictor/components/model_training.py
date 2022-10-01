from dataclasses import asdict
import datetime
import sys,os
from saleStorePredictor import logging
from typing import List
from pathlib import Path
from saleStorePredictor.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact
from saleStorePredictor.entity.config_entity import ModelTrainerConfig
from saleStorePredictor.utils import load_numpy_array_data,save_bin,load_bin,create_directories,save_json
from saleStorePredictor.entity.model_factory import MetricInfoArtifact, ModelFactory,GridSearchedBestModel
from saleStorePredictor.entity.model_factory import evaluate_regression_model




class SaleStorePredictorModel:
    def __init__(self, preprocessing_object, trained_model_object):
        """
        TrainedModel constructor
        preprocessing_object: preprocessing_object
        trained_model_object: trained_model_object
        """
        self.preprocessing_object = preprocessing_object
        self.trained_model_object = trained_model_object

    def predict(self, X):
        """
        function accepts raw inputs and then transformed raw input using preprocessing_object
        which gurantees that the inputs are in the same format as the training data
        At last it perform prediction on transformed features
        """
        transformed_feature = self.preprocessing_object.transform(X)
        return self.trained_model_object.predict(transformed_feature)

    def __repr__(self):
        return f"{type(self.trained_model_object).__name__}()"

    def __str__(self):
        return f"{type(self.trained_model_object).__name__}()"




class ModelTrainer:

    def __init__(self, model_trainer_config:ModelTrainerConfig, data_transformation_artifact: DataTransformationArtifact):
        try:
            logging.info(f"{'>>' * 30}Model trainer log started.{'<<' * 30} ")
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise e

    def initiate_model_trainer(self)->ModelTrainerArtifact:
        try:
            logging.info(f"Loading transformed training dataset")
            transformed_train_file_path = (self.data_transformation_artifact.transformed_train_file_path)
            train_array = load_numpy_array_data(file_path=transformed_train_file_path)

            logging.info(f"Loading transformed testing dataset")
            transformed_test_file_path = (self.data_transformation_artifact.transformed_test_file_path)
            test_array = load_numpy_array_data(file_path=transformed_test_file_path)

            logging.info(f"Splitting training and testing input and target feature")
            x_train,y_train,x_test,y_test = train_array[:,:-1],train_array[:,-1],test_array[:,:-1],test_array[:,-1]

            logging.info(f"X_train numpy array shape: {x_train.shape}")
            
            logging.info(f"Extracting model config file path")
            model_config_file_path = self.model_trainer_config.model_config_file_path

            logging.info(f"Initializing model factory class using above model config file: {model_config_file_path}")
            model_factory = ModelFactory(model_config_path=model_config_file_path)
            
            
            base_accuracy = self.model_trainer_config.base_accuracy
            logging.info(f"Expected accuracy: {base_accuracy}")

            logging.info(f"Initiating operation model selecttion")
            best_model = model_factory.get_best_model(X=x_train,y=y_train,base_accuracy=base_accuracy)
            
            logging.info(f"Best model found on training dataset: {best_model}")
            
            logging.info(f"Extracting trained model list.")
            grid_searched_best_model_list:List[GridSearchedBestModel]=model_factory.grid_searched_best_model_list
            
            model_list = [model.best_model for model in grid_searched_best_model_list ]
            logging.info(f"Evaluation all trained model on training and testing dataset both")
            metric_info:MetricInfoArtifact = evaluate_regression_model(model_list=model_list,X_train=x_train,y_train=y_train,X_test=x_test,y_test=y_test,base_accuracy=base_accuracy)

            logging.info(f"Best found model on both training and testing dataset.")
            
            

            preprocessing_obj=  load_bin(Path(self.data_transformation_artifact.preprocessed_object_file_path))
            model_object = metric_info.model_object


            trained_model_file_path=self.model_trainer_config.trained_model_file_path
            sale_model = SaleStorePredictorModel(preprocessing_object=preprocessing_obj,trained_model_object=model_object)
            logging.info(f"Saving model at path: {trained_model_file_path}")
            create_directories([os.path.dirname(trained_model_file_path)])
            save_bin(sale_model,trained_model_file_path)


            model_trainer_artifact =  ModelTrainerArtifact(is_trained=True,
            trained_model_file_path=trained_model_file_path,
            train_rmse=metric_info.train_rmse,
            test_rmse=metric_info.test_rmse,
            train_accuracy=metric_info.train_accuracy,
            test_accuracy=metric_info.test_accuracy,
            model_accuracy=metric_info.model_accuracy  
            )

            d = {
                 "is_trained":True,
            "trained_model_file_path":str(trained_model_file_path),
            "train_rmse":metric_info.train_rmse,
            "test_rmse":metric_info.test_rmse,
            "train_accuracy":metric_info.train_accuracy,
            "test_accuracy":metric_info.test_accuracy,
            "model_accuracy":metric_info.model_accuracy , 
            "time_stamp":datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            
            }

            model_report_file_path=Path(self.model_trainer_config.model_report_file_path)

            logging.info(f"report path for model: %s" % model_report_file_path)
            
            save_json(model_report_file_path,d)

            logging.info(f"Model Trainer Artifact: {model_trainer_artifact}")
            return model_trainer_artifact
        except Exception as e:
            raise  e

    def __del__(self):
        logging.info(f"{'>>' * 30}Model trainer log completed.{'<<' * 30} ")