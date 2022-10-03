import requests
from requests.exceptions import HTTPError
import json


class RequestManager:
    def httpRequest(method, url, **args):
        try:
            result = requests.request(method, url, **args)
            response = json.loads(result.text)
            return response
        except HTTPError as httpError:
            return httpError
        except Exception as error:
            return error
