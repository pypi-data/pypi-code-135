import os
import toml
from cli import login

from typing import List


class CinnarollAPIKeyMissingError(Exception):
    ...


# class WrongAPIKey(Exception): ...
# class DisallowedWriteError(Exception): ...
class CinnarollEnvironmentConfigurationError(Exception):
    ...


API_KEY_ENV_VAR_NAME = "CINNAROLL_API_KEY"


# def write_in_project_dir_is_disallowed() -> bool:
#     return False
#

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


# def api_key_is_wrong() -> bool:
#     # fire a /ping request to backend with X-API-KEY header, 200 -> False, 401 -> True
#     return False
#
def check_environment() -> None:
    errors: List[Exception] = []

    #     if write_in_project_dir_is_disallowed():
    #         raise DisallowedWriteError("Can’t save files in project folder. Check project folder's permissions.")
    #

    try:
        _ = get_api_key()
    except Exception as e:
        errors.append(e)
    #
    #     if api_key_is_wrong():
    #         raise WrongAPIKey("Cinnaroll API Key is wrong, perhaps pasted incorrectly. ")
    #
    if len(errors):
        print("The following errors were found. Correct them and import the package again.\n")
        for err in errors:
            print(f"{err}\n")
        raise CinnarollEnvironmentConfigurationError


check_environment()
