""" Logger configuration"""
import os
import logging
import logging.config
import sys
import yaml


def setup_logger(default_path='log.yaml', default_level=logging.INFO, env_key='LOG_CFG'):
    """
    Sets up the logger and loads the logger's configuration yaml file
    :param default_path: Log config file, defaults to "log.yaml"
    :param default_level: Default log level, defaults to INFO
    :param env_key: Environment variable for log config paths, defaults to "LOG_CFG"
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt', encoding="utf-8") as file:
            try:
                config = yaml.safe_load(file.read())
                logging.config.dictConfig(config)
            except BaseException as exception:
                print('Error in Logging Configuration. Using default configuration. ', exception)
                logging.basicConfig(level=default_level, stream=sys.stdout)
    else:
        logging.basicConfig(level=default_level, stream=sys.stdout)
        print('Failed to load log configuration file. Using default configuration.')
