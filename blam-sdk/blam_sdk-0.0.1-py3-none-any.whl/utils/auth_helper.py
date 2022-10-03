from email.policy import default
import os
import yaml


DEFAULT_FILE_PATH = f"{os.environ['HOME']}/.blam/creds.yml"


def get_creds_from_env():
    if os.path.exists(DEFAULT_FILE_PATH):
        with open(DEFAULT_FILE_PATH, "r") as f:
            creds = yaml.safe_load(f)
        return creds["user"], creds["password"]
    elif os.environ.get("BLAM_USER") and os.environ.get("BLAM_PASSWORD"):
        return os.environ.get("BLAM_USER"), os.environ.get("BLAM_PASSWORD")
    else:
        raise Exception("No credentials found")


def add_cred_args(parser):
    parser.add_argument("-u", "--user", help="Blam user", default=None)
    parser.add_argument("-p", "--password", help="Blam password", default=None)
