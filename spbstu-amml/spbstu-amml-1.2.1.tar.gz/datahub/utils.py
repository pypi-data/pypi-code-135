import os

from pathlib import Path

def cli_configure():
    credentials = {}
    credentials["aws_access_key_id"] = input("Enter Access Key ID:")
    credentials["aws_secret_access_key"] = input("Enter Secret Access key:")

    config = {}
    config["region"] = input("Enter Region:")

    configure(credentials, config)

def configure(credentials: dict, config: dict):
    """
    """
    cfg_path = get_cfg_path()
    os.makedirs(cfg_path, exist_ok=True)

    write_cfg_file(cfg_path / "credentials", credentials)
    write_cfg_file(cfg_path / "config", config)

def get_cfg_path():
    return Path.home() / ".aws"

def write_cfg_file(cfg_path: str, content: dict):
    cfgd = open(cfg_path, "w")
    cfgd.write("[default]\n")
    
    for key, val in content.items():
        cfgd.write(f"   {key}={val}\n")
    
    cfgd.close()
    
