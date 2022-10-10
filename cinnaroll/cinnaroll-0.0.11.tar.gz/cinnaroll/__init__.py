import os
import toml
from cli import login

from typing import List

# imports for nicer calling of cinnaroll, cinnaroll.rollout() instead of cinnaroll.rollout.rollout()
# and cinnaroll.RolloutConfig instead of cinnaroll.rollout.RolloutConfig
from .rollout import rollout, RolloutConfig


class CinnarollAPIKeyMissingError(Exception):
    ...


class CinnarollEnvironmentConfigurationError(Exception):
    ...


API_KEY_ENV_VAR_NAME = "CINNAROLL_API_KEY"


def get_api_key_from_toml_file_content(credentials_file: str) -> str:
    try:
        api_key: str = toml.loads(credentials_file)['default']['API Key']
        return api_key
    except KeyError:
        return ""


def get_api_key() -> str:
    api_key = os.environ.get(API_KEY_ENV_VAR_NAME)
    if api_key:
        return api_key
    try:
        with open(login.CREDENTIALS_FILE_PATH, "r") as credentials_file:
            api_key = get_api_key_from_toml_file_content(credentials_file.read())
            if api_key:
                return api_key
    except FileNotFoundError:
        pass
    raise CinnarollAPIKeyMissingError(f"Cinnaroll API Key is missing. Use cinnaroll-login to configure the API Key, \
or set {API_KEY_ENV_VAR_NAME} environment variable.")


def check_environment() -> None:
    errors: List[Exception] = []

    try:
        _ = get_api_key()
    except Exception as e:
        errors.append(e)

    if len(errors):
        print("The following errors were found. Correct them and import the package again.\n")
        for err in errors:
            print(f"{err}\n")
        raise CinnarollEnvironmentConfigurationError


check_environment()
