import boto3
import json
import logging
import requests

from blam_sdk.utils.auth_helper import get_creds_from_env


BASE_URL = "https://api.blam.jaguar-ai.com"
CLIENT_ID = "3m3jp0ri9vpfs8oh3jlngijb7k"


class BlamBaseService:
    def __init__(self, api_path, user=None, password=None):
        if user and password:
            self._user = user
            self._password = password
        else:
            self._user, self._password = get_creds_from_env()
        self._headers = {"Authorization": None}
        self.base_url = f"{BASE_URL}/{api_path}"
        self.refresh_auth()

    def _check_res(self, res, msg):
        if res.status_code > 299:
            res_body = res.json()
            logging.error(msg)
            logging.error(res_body)
            raise Exception(res_body)

    def _get_url(self, path=""):
        return f"{self.base_url}/{path}"

    def _get(self, path=""):
        res = requests.get(self._get_url(path), headers=self._headers)
        self._check_res(res, f"Get failed")
        return res.json()

    def _put(self, path="", body={}):
        res = requests.put(
            self._get_url(path), data=json.dumps(body), headers=self._headers
        )
        self._check_res(res, f"Put failed")
        return res.json()

    def _post(self, path="", body={}):
        res = requests.post(
            self._get_url(path), data=json.dumps(body), headers=self._headers
        )
        self._check_res(res, f"Post failed")
        return res.json()

    def _delete(self, path=""):
        res = requests.delete(self._get_url(path), headers=self._headers)
        self._check_res(res, f"Delete failed")
        return res.json()

    def refresh_auth(self):
        cidp = boto3.client("cognito-idp")
        try:
            self.auth_info = cidp.initiate_auth(
                AuthFlow="USER_PASSWORD_AUTH",
                AuthParameters={
                    "USERNAME": self._user,
                    "PASSWORD": self._password,
                },
                ClientId=CLIENT_ID,
            )["AuthenticationResult"]
            self._headers["Authorization"] = self.auth_info["IdToken"]
        except Exception as e:
            logging.error(e)
            raise Exception("Failed to get auth tokens")
