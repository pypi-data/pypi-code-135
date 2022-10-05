import os
import json
import uuid
import time
import requests
import traceback
import numpy as np
import pandas as pd
from sys import exc_info
pd.options.mode.chained_assignment = None

BRU_MODELS_URL = os.environ["BRU_MODELS_URL"]
RETRIES = int(os.environ["RETRIES"])
ERR_SYS = "System error: "


def batch2batch(df_b2b, url, batch=500, delay_req=0.05, verbose=False):
    """
    This function sends the data in batches to the microservice,
    sends a batch receives the same response batch

    Parameters
    ----------
    df_b2b : TYPE dataframe
        DESCRIPTION. dataframe to send
    url : TYPE string
        DESCRIPTION. url microservice
    batch : TYPE, optional int
        DESCRIPTION. The default is 500. Number of rows to send
    delay_req : TYPE, optional float
        DESCRIPTION. The default is 0.05. delay between request and request in seconds
    verbose : TYPE, optional bool
        DESCRIPTION. The default is False. if you want to see the batches in the terminal

    Returns
    -------
    df_output : TYPE dataframe
        DESCRIPTION. microservice response

    """
    df_output = pd.DataFrame()
    len_df = len(df_b2b)
    last_index = 0
    seq = np.arange(0, len_df, batch)
    method_name = 'batch2batch'

    for index in seq:
        if index == 0:
            i_1 = index
            i_2 = (index + batch) - 1
            last_index = last_index + batch

        else:
            i_1 = index
            i_2 = (last_index + batch) - 1
            last_index = last_index + batch

        data = df_b2b[i_1:i_2 + 1]
        data["uuid"] = None
        data["uuid"] = data["uuid"].apply(lambda x: f"{uuid.uuid4()}")
        original_id = list(data["uuid"])
        data = data.to_dict(orient='records')
        data = json.dumps(data)
        url_send = f'{url}/?len_df={len_df}&last_index={last_index}'
        requests_id = 1
        try:
            # try to make the request RETRIES times if the identifiers do not correspond
            while requests_id < RETRIES:
                response = requests.post(url=url_send, data=data)
                time.sleep(delay_req)

                res_json = response.json()
                df_response = pd.DataFrame(res_json)
                validation_ids = original_id == list(df_response["uuid"])

                if validation_ids:
                    break

                print('Bad request')
                requests_id += 1

            df_output = pd.concat([df_output, df_response])
            df_output = df_output.reset_index(drop=True)

            if verbose:
                print(f'Send batch column: {i_1} to {i_2}')

        except ConnectionError as e_1:
            print(''.center(60, '='))
            print(e_1)
            print(''.center(60, '='))
            error_1 = exc_info()[0]
            print(ERR_SYS + str(error_1))
            print(f'\nMethod: {method_name}')
            print(''.center(60, '='))
            traceback.print_exc()
            df_output = pd.DataFrame(columns=df_b2b.columns)

        except Exception as e_2:
            print(''.center(60, '='))
            print(e_2)
            print(''.center(60, '='))
            error_1 = exc_info()[0]
            print(ERR_SYS + str(error_1))
            print(f'\nMethod: {method_name}')
            print(''.center(60, '='))
            traceback.print_exc()
            df_output = pd.DataFrame(columns=df_b2b.columns)

    return df_output


class emotSent():

    def __init__(self, df_p, batch=500):

        method_name = 'emotSent __init__'

        try:
            self.cols_f = ['_id', 'clean_text']
            self.cols_except = df_p.columns
            self.batch = batch
            self.df_org = df_p
            self.df_p = df_p[self.cols_f]
            self.df_p = self.df_p.rename(columns={'_id': 'id'})

        except KeyError as e_1:
            print(''.center(60, '='))
            print(e_1)
            print(''.center(60, '='))
            error_1 = exc_info()[0]
            print(ERR_SYS + str(error_1))
            print(f'\nMethod: {method_name}')
            print(''.center(60, '='))
            traceback.print_exc()
            self.df_p = pd.DataFrame(columns=self.cols_f)

    def sentiment_emotion(self):

        method_name = 'emotSent.sentiment_emotion()'
        df_p = self.df_p
        batch = self.batch

        url_features = f'{BRU_MODELS_URL}/request_sentiment_emotion'

        try:
            df_send = batch2batch(df_b2b=df_p,
                                  batch=batch,
                                  url=url_features,
                                  delay_req=0.05)

            df_send = df_send.drop(columns='uuid')
            # pydantic ignore '_' character
            df_send = df_send.rename(columns={'id': '_id'})

            df_out = pd.merge(df_send, self.df_org, how='outer', on='_id')

        except Exception as e_1:
            print(''.center(60, '='))
            print(e_1)
            print(''.center(60, '='))
            error_1 = exc_info()[0]
            print(ERR_SYS + str(error_1))
            print(f'\nMethod: {method_name}')
            print(''.center(60, '='))
            traceback.print_exc()
            df_out = pd.DataFrame(columns=list(self.cols_except) + ['emotion', 'sentiment'])

        return df_out



