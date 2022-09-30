import requests
import pandas as pd
from .logger import Logger

def predict(endpoint_url,data):
    logger = Logger.get_instance()
    try:
        response = requests.post(endpoint_url, headers={"Content-Type": "application/json"}, json=data)

        if response.status_code==200:
            return pd.DataFrame(data=response.json(),columns=['prediction_result'])
        elif response.status_code==413:
            raise Exception("Inference data passed is too large. This might be due to mlflow docker image's nginx configuration limiting inferencing data size to 5 MiB.",response.text)
        else:
            raise Exception("Inferencing endpoint failed.",response.text)
    except Exception as e:
        logger.error(e)
        raise