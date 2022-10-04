import os
from pathlib import Path

from h2cow.utils import configure


def new(project_directory: str, server_ip: str):
    os.makedirs(project_directory)
    os.makedirs(os.path.join(project_directory, "recordings"))

    cfg = configure.create_template_config()

    # project directory
    cfg["project_path"] = project_directory
    
    # rtsp url
    cfg["server_ip"] = server_ip
    cfg["port"] = "554"
    cfg["user_name"] = "admin"
    cfg["password"] = "admin"
    cfg["channels"] = list(range(1,7))

    # directories
    cfg["image_recordings"] = str(Path("recordings", "images"))
    cfg["logs"] = "logs"
    cfg["water_recordings"] = str(Path("recordings", "water_gauge"))

    configure.write_config(cfg, Path(project_directory, "config.yaml"))
    return cfg