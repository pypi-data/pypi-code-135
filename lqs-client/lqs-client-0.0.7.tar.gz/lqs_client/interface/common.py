import json
from enum import Enum

import requests


class ProcessStatus(str, Enum):
    ready = "ready"
    pre_processing = "pre-processing"
    pre_processed = "pre-processed"
    processing = "processing"
    processed = "processed"
    post_processing = "post-processing"
    complete = "complete"


class UserRole(str, Enum):
    viewer = "viewer"
    editor = "editor"
    owner = "owner"


class LogFormat(str, Enum):
    ros = "ros"
    mls = "mls"


class RESTInterface:
    def __init__(self, api_url, headers):
        self._api_url = api_url
        self._headers = headers

    def _get_url_param_string(self, args, exclude=[]):
        url_params = ""
        for key, value in args.items():
            if value is not None and key not in ["self"] + exclude:
                url_params += f"&{key}={value}"
        if len(url_params) > 0:
            url_params = "?" + url_params[1:]
        return url_params

    def _get_payload_data(self, args, exclude=[]):
        payload = {}
        for key, value in args.items():
            if value is not None and key not in ["self"] + exclude:
                payload[key] = value
        return payload

    def _get_resource(self, resource_path):
        r = requests.get(f"{self._api_url}/{resource_path}", headers=self._headers)
        results = r.json()
        return results

    def _create_resource(self, resource_path, data):
        r = requests.post(
            f"{self._api_url}/{resource_path}",
            data=json.dumps(data),
            headers=self._headers,
        )
        response_data = r.json()
        return response_data

    def _update_resource(self, resource_path, data):
        r = requests.patch(
            f"{self._api_url}/{resource_path}",
            data=json.dumps(data),
            headers=self._headers,
        )
        response_data = r.json()
        return response_data

    def _delete_resource(self, resource_path):
        r = requests.delete(f"{self._api_url}/{resource_path}", headers=self._headers)
        results = r.json()
        return results
