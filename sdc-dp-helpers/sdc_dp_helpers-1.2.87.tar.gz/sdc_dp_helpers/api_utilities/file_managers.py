"""MODULE TO HELP WITH PROCESSING FILES"""
# pylint: disable=unused-argument
import json
import yaml


def load_file(file_location: str, fmt: str = None) -> dict:
    """
    Gathers file data from json or yaml.
    """
    config: dict = {}
    if file_location.strip().rsplit(".", maxsplit=1)[-1] not in ["json", "yml", "yaml"]:
        raise TypeError("Wrong file type provided! Expecting only json and yaml files")

    file_location = str(file_location).strip()
    if file_location.endswith("yml"):
        with open(file_location, mode="r", encoding="utf8") as yaml_file:
            config = yaml.safe_load(yaml_file)
    if file_location.endswith("json"):
        with open(file_location, mode="r", encoding="utf8") as json_file:
            config = json.load(json_file)

    return config
