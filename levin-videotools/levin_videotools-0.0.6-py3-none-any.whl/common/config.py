import os
from pathlib import Path

import yaml
from yaml.loader import FullLoader


def _load_yaml_file(file_name):
    if not os.path.exists(file_name):
        return {}

    with open(file_name, 'r', encoding='UTF8') as f:
        return yaml.load(f, Loader=FullLoader)

class Config:
    def __init__(self):
        self._app_home = f"{os.environ['HOME']}/app/videotools"
        self._app_config_file = f"{self._app_home}/config.yaml"
        self._app_config = _load_yaml_file(self._app_config_file)
        
        self._default_config_file = Path(os.path.dirname(__file__)).parent\
            .joinpath("config/default_config.yaml")
        self._default_config = _load_yaml_file(self._default_config_file)

    @property
    def log_home(self):
        return self._get_config_value('log_home')
    
    @property
    def md5_store_file(self):
        return self._get_config_value('md5_store_file')
    
    @property
    def video_process_threads(self):
        return self._get_config_value('video_process_threads')
    
    @property
    def text_to_clip(self):
        return self._get_config_value('text_to_clip')

    def _get_config_value(self, key):
        result = self._app_config.get(key, None)
        if not result:
            result = self._default_config.get(key)

        if isinstance(result, str):
            result = result.format(**self._get_placeholder_kv())
        
        return result
    
    def _get_placeholder_kv(self):
        return {"app_home": self._app_home}
