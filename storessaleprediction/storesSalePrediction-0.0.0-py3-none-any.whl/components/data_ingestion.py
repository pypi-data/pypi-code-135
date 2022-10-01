import os
import urllib.request as request
from zipfile import ZipFile
from saleStorePredictor.entity import DataIngestionConfig, DataIngestionArtifact
from saleStorePredictor import logger
from saleStorePredictor.utils import get_size
from tqdm import tqdm
from pathlib import Path
from sklearn.model_selection import train_test_split
import pandas as pd


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        logger.info("Trying to download file...")
        if not os.path.exists(self.config.local_data_file):
            logger.info("Download started...")
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file,
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")        

    def _get_updated_list_of_files(self, list_of_files):
        return [f for f in list_of_files]

    def _preprocess(self, zf: ZipFile, f: str, working_dir: str):
        target_filepath = os.path.join(working_dir, f)
        if not os.path.exists(target_filepath):
            zf.extract(f, working_dir)
        
        if os.path.getsize(target_filepath) == 0:
            logger.info(f"removing file:{target_filepath} of size: {get_size(Path(target_filepath))}")
            os.remove(target_filepath)

    def unzip_and_clean(self):
        logger.info(f"unzipping file and removing unawanted files")
        with ZipFile(file=self.config.local_data_file, mode="r") as zf:
            list_of_files = zf.namelist()
            updated_list_of_files = self._get_updated_list_of_files(list_of_files)
            for f in tqdm(updated_list_of_files):
                self._preprocess(zf, f, self.config.unzip_dir)


    def split_data_as_train_test(self) -> DataIngestionArtifact:
        try:
            train_file_path = self.config.root_dir + "/raw"

            train_file_name = "Train.csv" 
            test_file_name = "Test.csv" 

            train_file_path = os.path.join(train_file_path,train_file_name)


            logger.info(f"Reading csv file: [{train_file_path}]")
            sale_df = pd.read_csv(train_file_path)

            

            logger.info(f"Splitting data into train and test")
            
            X_train, X_test, y_train, y_test = train_test_split(sale_df[sale_df.columns[:-1]],sale_df[sale_df.columns[-1]],test_size=0.33,random_state=0)
            
            train = pd.concat([X_train, y_train],axis=1)
            test = pd.concat([X_test, y_test],axis=1)

            train_file_path = os.path.join(self.config.ingested_train_dir,
                                            train_file_name)

            test_file_path = os.path.join(self.config.ingested_test_dir,
                                        test_file_name)
            
            if train is not None:
                os.makedirs(self.config.ingested_train_dir,exist_ok=True)
                logger.info(f"Exporting training datset to file: [{train_file_path}]")
                train.to_csv(train_file_path,index=False)

            if test is not None:
                os.makedirs(self.config.ingested_test_dir, exist_ok= True)
                logger.info(f"Exporting test dataset to file: [{test_file_path}]")
                test.to_csv(test_file_path,index=False)
            

            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,
                                test_file_path=test_file_path)
            logger.info(f"Data Ingestion artifact:[{data_ingestion_artifact}]")
            return data_ingestion_artifact

        except Exception as e:
            raise e           


