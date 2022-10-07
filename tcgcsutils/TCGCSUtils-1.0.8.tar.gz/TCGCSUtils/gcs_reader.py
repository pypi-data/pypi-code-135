import os
import ndjson
import json
import numpy as np
import pandas as pd
from typing import List
from dateutil import tz
from datetime import datetime
from dateutil.relativedelta import relativedelta
from gcsfs import GCSFileSystem
from google.cloud.storage import Client
from google.cloud.storage.blob import Blob

class GCSReader():
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

    def _return_blobs(
        self,
        bucket_name: str,
        prefix: str = None,
        max_results: int = None,
        delta_time_kwargs: dict = None
    ) -> List[Blob]:
        bucket = self.client.bucket(bucket_name)
        blobs = bucket.list_blobs(prefix=prefix,max_results=max_results)
        utc_time = datetime.utcnow()
        
        if delta_time_kwargs:
            delta_time = utc_time - relativedelta(**delta_time_kwargs)
            delta_time_utc = delta_time.replace(tzinfo=tz.tzutc())
                
            return [blob for blob in blobs if blob.updated > delta_time_utc]
        else:
            return blobs

    def read_from_json(
        self,
        bucket_name: str,
        prefix: str = None,
        max_results: int = None,
        delta_time_kwargs: dict = None,
        return_dataframe: bool = False
    ):
        blobs = self._return_blobs(
            bucket_name,
            prefix,
            max_results,
            delta_time_kwargs
        )
        data = []
        for blob in blobs:    
            data.extend(ndjson.loads(blob.download_as_string()))
        if return_dataframe:
            return pd.DataFrame.from_records(data)
        return data
        
    def read_from_parquet(
        self,
        bucket_name: str,
        prefix: str = None,
        max_results: int = None,
        delta_time_kwargs: dict = None
    ):
        blobs = self._return_blobs(
            bucket_name,
            prefix,
            max_results,
            delta_time_kwargs
        )
        fs = GCSFileSystem(self.GCP_PROJECT,token=self.GOOGLE_APPLICATION_CREDENTIALS)

        dataframe = pd.Series(dtype='str')
        for blob in blobs:
            blob_name = os.path.join(bucket_name,blob.name) 
            df = pd.read_parquet(fs.open(blob_name))
            if dataframe.empty:
                dataframe = df
            else:
                dataframe = pd.concat([dataframe,df],ignore_index=True)
            
        dataframe.replace({np.NaN:None},inplace=True)
        return dataframe
