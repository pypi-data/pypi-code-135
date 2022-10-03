import os
import toml


class CinnarollCredentialsSaveError(Exception):
    ...


USER_HOME_DIR = os.path.join(os.path.expanduser('~'))
CREDENTIALS_DIR_PATH = os.path.join(USER_HOME_DIR, ".cinnaroll")
CREDENTIALS_FILE_PATH = os.path.join(CREDENTIALS_DIR_PATH, "credentials")
CREDENTIALS_FILE_API_KEY_KEY = "API Key"


def login() -> None:
    try:
        os.makedirs(os.path.dirname(CREDENTIALS_FILE_PATH), exist_ok=True)
    except PermissionError:
        raise CinnarollCredentialsSaveError(
            f"Couldn't create directory {CREDENTIALS_DIR_PATH}."
            f" Ensure you have write permissions to {USER_HOME_DIR} directory, and re-run this command again."
        )
    try:
        with open(CREDENTIALS_FILE_PATH, "w") as credentials_file:
            api_key = input("Paste your personal cinnaroll API Key here: ")
            credentials = {
                "default": {
                    CREDENTIALS_FILE_API_KEY_KEY: api_key
                }
            }
            toml.dump(credentials, credentials_file)
            print(f"Your API Key was saved at {CREDENTIALS_FILE_PATH}.")
    except PermissionError:
        raise CinnarollCredentialsSaveError(
            f"Couldn't create or open file {CREDENTIALS_FILE_PATH}."
            f" Ensure you have write permissions to {CREDENTIALS_DIR_PATH} directory, and to {CREDENTIALS_FILE_PATH}"
            f" if it exists, and re-run this command again."
        )


def main() -> None:
    try:
        login()
    except Exception as e:
        print(e)
