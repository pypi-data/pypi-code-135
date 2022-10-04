import json

from pydantic import ValidationError

from .exceptions.authenticator_exc import ConfigLoadException, ConfigLoadValidationException
from .login_provider import LoginProvider
from .models.config import ConfigData

DEFAULT_CONFIG_FNAME = 'data/config.json'

class Config(object):
    fname = DEFAULT_CONFIG_FNAME
    data: ConfigData
    
    def __init__(self, fname = DEFAULT_CONFIG_FNAME):
        self.fname = fname
        self.load()

    def load(self):
        try:
            with open(self.fname, 'r') as out:
                config = json.loads(out.read())
            
            self.data = ConfigData(**config)

        except ValidationError:
            raise ConfigLoadValidationException(self.fname)

        except Exception:
            raise ConfigLoadException(self.fname)

class Authenticator:
    config: Config
    config_fname = DEFAULT_CONFIG_FNAME
    provider: LoginProvider

    def __init__(self, config_fname=DEFAULT_CONFIG_FNAME, provider=LoginProvider()): 
        self.config_fname = config_fname
        self.config = Config(config_fname)
        self.provider = provider
    
    def login(self):
        email = self.config.data.lisensi.email
        password = self.config.data.lisensi.pwd
        return self.provider.login(email, password)