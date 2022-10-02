import io
import json
import os

import requests
from requests import Response


class DirectusApi:

    def __init__(self, username, password, endpoint):
        self.username = username
        self.password = password
        self.endpoint = endpoint
        self.access_token, self.refresh_token = self.__get_jwt_token()

    def __get_jwt_token(self) -> tuple:
        """
        Make a POST-Request to /auth/login and return the access_token and refresh_token as tuple.
        """
        url = self.endpoint + '/auth/login'
        payload = {'email': self.username, 'password': self.password}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=payload, headers=headers)

        return response.json()['data']['access_token'], response.json()['data']['refresh_token']

    def list_items_of_collection(self, collection: str):
        """
        Make a GET-Request to /items/<collection_name> and return the response as JSON.
        """
        url = self.endpoint + '/items/' + collection
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = requests.get(url, headers=headers)
        return response.json()

    def create_items(self, items: list, collection: str) -> Response:
        """
        Make a POST-Request to /items/<collection_name> and return the response as JSON.
        """
        url = self.endpoint + '/items/' + collection
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = requests.post(url, json=items, headers=headers)
        return response

    def import_items_by_json_file(self, filename: str, collection: str) -> Response:
        files = {'file': (filename, open(filename, 'rb'), 'application/json')}
        url = self.endpoint + '/utils/import/' + collection
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Accept': 'application/json'
        }
        response = requests.post(url, files=files, headers=headers)

        return response

    def import_items_by_data(self, data: list, collection: str) -> Response:
        file = io.BytesIO(json.dumps(data).encode('utf-8'))
        files = {'file': ('example.json', file, 'application/json')}
        url = self.endpoint + '/utils/import/' + collection
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Accept': 'application/json'
        }
        response = requests.post(url, files=files, headers=headers)

        return response
