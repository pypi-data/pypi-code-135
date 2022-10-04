import json
import requests
import datetime

import pkg_resources
from pkg_resources import DistributionNotFound

from types import ModuleType
from .constants import URL, HTTP_STATUS_CODE, ERROR_CODE

from . import resources
from .constants.api_list import API_NAMES


def capitalize_camel_case(string):
    return "".join(map(str.capitalize, string.split('_')))


# Create a dict of resource classes
RESOURCE_CLASSES = {}
for name, module in resources.__dict__.items():
    if isinstance(module, ModuleType) and \
            capitalize_camel_case(name) in module.__dict__:
        RESOURCE_CLASSES[capitalize_camel_case(name)] = module.__dict__[
            capitalize_camel_case(name)]


class Client:
    """PG Rewards SDK client class"""
    DEFAULTS = {
        'sandbox_base_url': URL.SANDBOX_BASE_URL,
        'production_base_url': URL.PRODUCTION_BASE_URL
    }

    def __init__(self,
                 session=None,
                 auth=None,
                 production_mode=False,
                 **options):
        """
        Initialize a Client object with session,
        optional auth handler, and options
        """
        self.session = session or requests.Session()
        self.token_res = {}
        self.token_current_time = None
        self.auth = auth
        self.production_mode = production_mode

        self.base_url = self._set_base_url(**options)
        # intializes each resource
        # injecting this client object into the constructor
        for name, Klass in RESOURCE_CLASSES.items():
            setattr(self, name, Klass(self))

    def get_version(self):
        version = ""
        try:
            version = pkg_resources.require("pgrwpy")[0].version
        except DistributionNotFound:
            print('DistributionNotFound')
        return version

    def _set_base_url(self, **options):
        if self.production_mode is False:
            base_url = self.DEFAULTS['sandbox_base_url']
        if self.production_mode is True:
            base_url = self.DEFAULTS['production_base_url']
        if 'base_url' in options:
            base_url = options['base_url']
            del (options['base_url'])
        return base_url

    def _check_token_exists(self):
        """ 
        Verify that the token response exists to avoid repeat calls within 59 seconds
        """
        if isinstance(self.token_current_time, datetime.datetime) and isinstance(self.token_res, dict) and 'token' in self.token_res:
            time_calculate = datetime.datetime.now() - self.token_current_time
            if time_calculate.total_seconds() < 59:
                return True
        return False

    def auth_header(self):
        userID = self.auth[0]
        secretKey = self.auth[1]
        if not userID or not secretKey:
            raise ValueError("MISSING REQUEST PARAMS for userID and secretKey")
        if self._check_token_exists():
            return self.token_res
        payload = json.dumps({
            "userID": userID,
            "secretKey": secretKey
        })
        url = self.base_url + URL.TOKEN
        response = requests.request("POST", url, headers={
            'Content-Type': 'application/json;charset=UTF-8'
        }, data=payload)
        if not 'token' in response:
            raise ValueError(ERROR_CODE.INCORECTKEY)
        self.token_current_time = datetime.datetime.now()
        self.token_res = response.json()
        return response.json()

    def request(self, method, path, auth_token, **options):
        """
        Dispatches a request to the PG Rewards SDK HTTP API
        """
        api_name = options['api_id']
        del options['api_id']
        url = "{}{}".format(self.base_url, path)
        if 'data' in options:
            payload = json.dumps(options['data'])
        else:
            payload = ""
        response = requests.request(method, url, headers={
            'Authorization': 'Bearer ' + auth_token,
            'Content-Type': 'application/json;charset=UTF-8'
        }, data=payload)
        # print(response.text)
        if ((response.status_code >= HTTP_STATUS_CODE.OK) and
                (response.status_code < HTTP_STATUS_CODE.REDIRECT)):
            return response.json()
        else:
            json_response = response.text
            resolve_url = "{}?search={}".format(
                URL.RESOLVE,
                api_name,)
            print("This link should help you to troubleshoot the error: " + resolve_url)
            return json_response

    def get(self, path, params, **options):
        """
        Parses GET request options and dispatches a request
        """
        method = "GET"
        auth_header = self.auth_header()
        return self.request("get",
                            path,
                            params=params,
                            auth_token=auth_header['token'],
                            **options)

    def post(self, path, data, **options):
        """
        Parses POST request options and dispatches a request
        """
        method = "POST"
        auth_header = self.auth_header()
        return self.request("post",
                            path,
                            data=data,
                            auth_token=auth_header['token'],
                            **options)

    def patch(self, path, data, **options):
        """
        Parses PATCH request options and dispatches a request
        """
        method = "PATCH"
        auth_header = self.auth_header()
        return self.request("patch",
                            path,
                            auth_token=auth_header['token'],
                            **options)

    def delete(self, path, data, **options):
        """
        Parses DELETE request options and dispatches a request
        """
        method = "DELETE"
        auth_header = self.auth_header()
        return self.request("delete",
                            path,
                            data=data,
                            auth_token=auth_header['token'],
                            **options)

    def put(self, path, data, **options):
        """
        Parses PUT request options and dispatches a request
        """
        method = "PUT"
        auth_header = self.auth_header()
        return self.request("put",
                            path,
                            data=data,
                            auth_token=auth_header['token'],
                            **options)
