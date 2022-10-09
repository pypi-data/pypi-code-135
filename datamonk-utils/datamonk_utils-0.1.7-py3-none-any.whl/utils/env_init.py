
from dotenv import dotenv_values,find_dotenv,load_dotenv
from logging import config
import time
import os
def get_env_vars(FLOW_NAME):
    env_location=find_dotenv(filename=f".env.{FLOW_NAME}",
                             raise_error_if_not_found=True,
                             usecwd=True
                             )

    load_dotenv(env_location)

    CONFIG=dotenv_values(env_location)
    os.environ["run_timestamp"],CONFIG["run_timestamp"] = time.strftime("%Y-%m-%dT%H:%M:%S"),time.strftime("%Y-%m-%dT%H:%M:%S")
    return CONFIG


config.fileConfig('logging.conf', disable_existing_loggers=False)