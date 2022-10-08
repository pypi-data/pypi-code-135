from typing import Iterable, Mapping, Any

import requests

from repotea.args import ArgumentParser
from repotea.utils import eprint


def get_data_from_keys(keys: Iterable[str], args: ArgumentParser) -> Mapping[str, Any]:
    data = {}
    for key in keys:
        attr = getattr(args, key, None)
        if attr is None or (isinstance(attr, str) and attr == ""):
            continue
        data[key] = attr
    return data


def eprint_message(resp: requests.Response):
    try:
        eprint(resp.json()["message"])
    except Exception:
        return
