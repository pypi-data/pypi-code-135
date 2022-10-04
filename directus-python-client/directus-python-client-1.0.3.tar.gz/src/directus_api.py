import io
import json
import math
import uuid

import requests
from requests import Response
from tqdm import tqdm


class DirectusApi:
    def __init__(self, username, password, endpoint):
        self.username = username
        self.password = password
        self.endpoint = endpoint
        self.access_token, self.refresh_token = self.__get_jwt_token()
        self.request_headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

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
        response = requests.get(url, headers=self.request_headers)
        return response.json()

    def create_items(self, items: list, collection: str) -> Response:
        """
        Create multiple items in a collection.
        Make a POST-Request to /items/<collection_name> and return the response as JSON.
        """
        url = self.endpoint + '/items/' + collection
        response = requests.post(url, json=items, headers=self.request_headers)
        return response

    def updates_items(self, items: list, collection: str) -> Response:
        """
        Update multiple items in a collection. The items must have an id (primary key) field.
        Make a PATCH-Request to /items/<collection_name> and return the response as JSON.
        """
        url = self.endpoint + '/items/' + collection
        response = requests.patch(url, json=items, headers=self.request_headers)
        return response

    def import_items_by_json_file(self, filename: str, collection: str) -> Response:
        files = {'file': (filename, open(filename, 'rb'), 'application/json')}
        url = self.endpoint + '/utils/import/' + collection
        headers = {
            # Do not add Content-Type header here. Request lib will handle by itself for files.
            'Authorization': 'Bearer ' + self.access_token,
            'Accept': 'application/json'
        }
        response = requests.post(url, files=files, headers=headers)

        return response

    def import_items_by_data(self, data: list, collection: str) -> Response:
        file = io.BytesIO(json.dumps(data).encode('utf-8'))
        files = {'file': (str(uuid.uuid4()) + '.json', file, 'application/json')}
        url = self.endpoint + '/utils/import/' + collection
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Accept': 'application/json'
        }
        response = requests.post(url, files=files, headers=headers)

        return response

    def get_items(self, collection: str, limit: int = None, page_size: int = 25000,
                  filter_dict: dict = None, show_progress: bool = False) -> list:
        """
        Get all items from a collection and return them as list.
        :param show_progress: Show progress bar.
        :param filter_dict: A dict with the filter parameters.
                            See https://docs.directus.io/reference/introduction.html#search-http-method
        :param collection: The name of the collection.
        :param limit: The limit of items to return. If None all items will be returned.
        :param page_size: The number of items to return per request. Set this value depending of the RAM of your machine.
        :return: A list of items. Each item is a dictionary with the fields of the collection.
        """

        def __helper(page_size: int, page: int, filter_dict: dict = None):
            if filter_dict is not None:
                # Build url with query-parameters (e.g. ?filter[match_id][_eq]=wzi6xmt37)
                url_query = '?filter' + ''.join(
                    [f'[{k}][{k2}]={v2}' for k, v in filter_dict.items() for k2, v2 in v.items()])
            else:
                url_query = ''

            url = self.endpoint + '/items/' + collection + url_query
            headers = {
                'Authorization': 'Bearer ' + self.access_token,
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
            return requests.get(
                url, headers=headers,
                params={'limit': page_size, 'meta': '*', 'page': page})

        # Set page_size to limit if limit is smaller than page_size
        if limit is not None and limit < page_size:
            page_size = limit

        response = __helper(page_size=page_size, page=1, filter_dict=filter_dict)
        items = response.json()['data']
        total = response.json()['meta']['filter_count']

        if limit is None:
            number_of_pages = math.ceil(total / page_size)
        else:
            number_of_pages = math.ceil(limit / page_size)

        for page in tqdm(range(2, number_of_pages + 1), disable=not show_progress):
            response = __helper(page_size=page_size, page=page)
            items.extend(response.json()['data'])

        return items[:limit]

    def delete_item_by_id(self, collection: str, id: int) -> Response:
        """
        Delete an item by id.
        Make a DELETE-Request to /items/<collection_name>/<id> and return the response as JSON.
        """
        url = self.endpoint + '/items/' + collection + '/' + str(id)
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = requests.delete(url, headers=headers)
        return response

    def delete_items_by_id(self, collection: str, ids: list) -> Response:
        """
        Delete multiple items by id.
        Make a DELETE-Request to /items/<collection_name> and return the response as JSON.
        """
        url = self.endpoint + '/items/' + collection
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = requests.delete(url, json=ids, headers=headers)
        return response

    def delete_all_items_from_collection(self, collection: str):
        """
        Delete all items from a collection.
        Make a DELETE-Request to /items/<collection_name> and return the response as JSON.
        Returns status_code 204 on success.
        """
        url = self.endpoint + '/items/' + collection
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = requests.delete(url, headers=headers, json={'query': {'limit': -1}})

        return response
