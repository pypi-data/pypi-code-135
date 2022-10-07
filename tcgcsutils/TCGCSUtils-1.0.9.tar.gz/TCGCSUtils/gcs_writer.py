import os
import pandas as pd
import posixpath
import numpy as np
import json
from google.cloud.storage import Client

class GCSWriter():
    def __init__(self,gcp_project: str = None,service_account_info: str = None):
        """
            The parameters are optional, if are not using the parameters, make sure that the env variables exists:
            - GCP_PROJECT
            - GOOGLE_APPLICATION_CREDENTIALS
            
            Parameters
            ---------------
            gcp_project (optional): GCP Project
            service_account_info (optional): That should contain the service_account json string, not the path to it
        """
        self.GCP_PROJECT = gcp_project if gcp_project else os.getenv("GCP_PROJECT")
        self.GOOGLE_APPLICATION_CREDENTIALS = service_account_info \
            if service_account_info \
            else json.loads(os.getenv('GOOGLE_APPLICATION_CREDENTIALS','{}'))
        
        if self.GOOGLE_APPLICATION_CREDENTIALS:
            self.client = Client.from_service_account_info(self.GOOGLE_APPLICATION_CREDENTIALS)
        else:
            raise ConnectionError(
                "Make sure the env variable \"GOOGLE_APPLICATION_CREDENTIALS\" exists or send a value to the parameter service_account_info"
            )

    def write_parquet(
        self,
        data: pd.DataFrame,
        bucket_name: str,
        prefix: str = None,
        file_name: str = None,
    ):
        data.replace({np.NaN:None},inplace=True)
        bucket = self.client.bucket(bucket_name)
        blob_name = posixpath.join(prefix,file_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_string(data.to_parquet())

    def write_json(
        self,
        data: dict,
        bucket_name: str,
        prefix: str = None,
        file_name: str = None,
    ):
        bucket = self.client.bucket(bucket_name)
        blob_name = posixpath.join(prefix,file_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_string(json.dumps(data))
