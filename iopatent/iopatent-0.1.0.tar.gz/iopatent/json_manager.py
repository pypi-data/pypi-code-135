"""_summary_
"""

import json
from iopatent.exceptions import JsonReadError, JsonWriteError


def read_json(file_path, *args, **kwargs) -> dict:
    """_summary_

    Args:
        file_path (str): _description_

    Returns:
        dict: _description_
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f, *args, **kwargs)
        return data
    except Exception as e:
        raise JsonReadError('Unable to read json file') from e


def to_json(data: dict, file_path: str, *args, **kwargs) -> None:
    """_summary_

    Args:
        data (dict): _description_
        file_path (str): _description_
    """
    try:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, *args, **kwargs)
    except Exception as e:
        raise JsonWriteError('Unable to save json file') from e