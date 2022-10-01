from distutils.log import Log
from re import L
from saleStorePredictor.utils import read_yaml,save_numpy_array_data,save_bin,create_directories
import os
from saleStorePredictor.entity import DataTransformationConfig
from saleStorePredictor.config import ConfigurationManager
from saleStorePredictor import logging
import os
import numpy as np
from sklearn.base import BaseEstimator,TransformerMixin
from sklearn.preprocessing import StandardScaler,LabelEncoder,OrdinalEncoder,PolynomialFeatures
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer,make_column_transformer
from sklearn.impute import SimpleImputer
import pandas as pd
from pathlib import Path





class FeatureGeneratorAndCorrector(BaseEstimator, TransformerMixin):

    def __init__(self, columns=None):
        """
        FeatureGeneratorAndCorrector Initialization
        
        """
        self.columns = columns
        

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        try:
            X.fillna(X.mode())
            X["Item_type_combined"] = X['Item_Identifier'].apply(lambda x:x[0:2])
            X['Item_Fat_Content'] = X['Item_Fat_Content'].map({'LF':'Low Fat','reg':'Regular','low fat':'Low Fat','Regular':'Regular','Low Fat':'Low Fat'})
            
            return X
        except Exception as e:
            logging.error(f"Error generating feature {e}.") 


class ModifiedLabelEncoder(LabelEncoder):

    def fit_transform(self, y, *args, **kwargs):
        return y.apply(super(ModifiedLabelEncoder, self).fit_transform, result_type='expand')

    def transform(self, y, *args, **kwargs):
        return y.apply(super(ModifiedLabelEncoder, self).fit_transform, result_type='expand')            




class DataTransformation:

    def __init__(self,data_transformation_config:DataTransformationConfig):
        self.data_transformation_config = data_transformation_config
        self.train = pd.read_csv(self.data_transformation_config.training_dataset,index_col=False)
        self.test = pd.read_csv(self.data_transformation_config.test_dataset,index_col=False)


    def get_data_transformer_object(self)->ColumnTransformer:
        try:
            schema_file_path = Path(self.data_transformation_config.schema_path)

            dataset_schema = read_yaml(schema_file_path)

            numerical_columns = dataset_schema.numerical_columns
            categorical_columns = dataset_schema.categorical_columns


            num_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy="mean")),
               # ('scaler', StandardScaler())
            ]
            )

            transformers = make_column_transformer((ModifiedLabelEncoder(), categorical_columns+["Item_type_combined"]),
                                       )

            cat_pipeline = Pipeline(steps=[

                 
               ('feature_generator', FeatureGeneratorAndCorrector(columns=categorical_columns)),
                
                ('transformer', transformers),
                # ('encoders',MultiColumnLabelEncoder(columns=categorical_columns+['Item_type_combined'])),
                #  ('scaler', StandardScaler(with_mean=False)),
                


            ]
            )

           


           






            logging.info(f"Categorical columns preprocess: {categorical_columns}")
            logging.info(f"Numerical columns preprocess: {numerical_columns}")



            preprocessing = ColumnTransformer([
                ('num_pipeline', num_pipeline, numerical_columns),
                ('cat_pipeline', cat_pipeline, categorical_columns),


                

            
            ])

            
            return preprocessing

        except Exception as e:
            raise e
            logging.error(f"Error in preprocessing: {e}") 


    def initiate_data_transformation(self):
        try:
            logging.info(f"Obtaining preprocessing object.")
            preprocessing_obj = self.get_data_transformer_object()




            logging.info(f"Obtaining training and test file path.")
            train_file_path = Path(self.data_transformation_config.training_dataset)
            test_file_path =  Path(self.data_transformation_config.test_dataset)
            

            schema_file_path = Path(self.data_transformation_config.schema_path)
            
            logging.info(f"Loading training and test data as pandas dataframe.")
            train_df = pd.read_csv(train_file_path)

           


            logging.info(f"Before preprocessing train shape: {train_df.shape}")
            
            test_df = pd.read_csv(test_file_path)

            schema = read_yaml(schema_file_path)

            target_column_name = schema.target_column


            logging.info(f"Splitting input and target feature from training and testing dataframe.")
            input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df = test_df[target_column_name]

            

            
            

            logging.info(f"Applying preprocessing object on training dataframe and testing dataframe")
            input_feature_train_arr= preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            X_train = pd.DataFrame(input_feature_train_arr)
            X_test = pd.DataFrame(input_feature_test_arr)
            logging.info(f"train data colunms after preprocessing {X_train.info()}")


           
            

            


            train_arr = np.c_[ input_feature_train_arr, np.array(target_feature_train_df)]

            logging.info(f"Train shape after preprocessing : {train_arr.shape}")



            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
            
            transformed_train_dir = Path(self.data_transformation_config.transformed_train_path_file)
            transformed_test_dir = Path(self.data_transformation_config.transformed_test_path_file)

            train_file_name = os.path.basename(train_file_path).replace(".csv",".npz")
            test_file_name = os.path.basename(test_file_path).replace(".csv",".npz")

            transformed_train_file_path = os.path.join(transformed_train_dir, train_file_name)
            transformed_test_file_path = os.path.join(transformed_test_dir, test_file_name)

            logging.info(f"Saving transformed training and testing array.")
            #pd.DataFrame(train_arr, columns=list(schema.columns)+['combined']).to_csv("help.csv")
            save_numpy_array_data(file_path=transformed_train_file_path,array=train_arr)
            save_numpy_array_data(file_path=transformed_test_file_path,array=test_arr)

            

            preprocessing_obj_file_path = Path(self.data_transformation_config.preprocessed_object_path_file)

            create_directories([os.path.dirname(preprocessing_obj_file_path)])


            logging.info(f"Saving preprocessing object at {preprocessing_obj_file_path} type {type(preprocessing_obj)}")
            save_bin(preprocessing_obj,preprocessing_obj_file_path)

            
            
            logging.info(f"Data transformationa completed successfully.")
            
        except Exception as e:
            raise e
            logging.error(f"Error Saving preprocessing object: {e.with_traceback}")
   

    def __del__(self):
        logging.info(f"{'>>'*30}Data Transformation log completed.{'<<'*30} \n\n")    
