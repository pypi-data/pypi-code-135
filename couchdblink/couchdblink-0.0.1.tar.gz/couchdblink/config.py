import json

try:
    from .nogit import extra_config

    # print("config loading with nogit.extra_config")
except ImportError:
    # print("config loading without nogit.extra_config")
    extra_config = None

if not extra_config:
    CRED_URL = ""
    CRED_JSON_FILE_PATH = ""
else:
    CRED_JSON_FILE_PATH = extra_config.DEFAULT_CRED_JSON_FILE_PATH

if CRED_JSON_FILE_PATH:
    with open(CRED_JSON_FILE_PATH) as f:
        data = json.load(f)
    CRED_URL = data["url"]
