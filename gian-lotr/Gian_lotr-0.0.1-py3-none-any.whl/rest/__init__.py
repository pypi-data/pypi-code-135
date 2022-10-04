from urllib.parse import urlencode
import requests
import io
from importlib import resources


def create_params(**kwargs):
    '''
    Used to create url parameters for API call
    '''
    url = kwargs.get("url")
    params = kwargs.get("params")
    if params:
        query_string = urlencode(eval(params))
    return f'{url}?{query_string}'


class PathBuilder:
    '''
    Used to build the correct API path that includes
    parameters & filters if necessary
    '''

    def __init__(self, **kwargs):
        self.base_url = kwargs.get('base_url')
        self.params = kwargs.get('params')
        self.obj_id = kwargs.get('object_id')
        self.obj_type = kwargs.get('object_type')

    # construct endpoints
    def build(self):

        if self.obj_type == "book":
            path = "/book"

        if self.obj_type == "movie":
            path = "/movie"

        if self.obj_type == "character":
            path = "/character"

        if self.obj_type == "quote":
            path = "/quote"

        if self.obj_id:
            path = f'{path}/{self.obj_id}'

        url = f'{self.base_url}{path}'
        print("Path Builder: ", url)

        return [path, url]


class APIRequester:
    '''
    Used to make the request
    '''

    def __init__(self, **kwargs):

        self.url = kwargs.get("url")
        self.headers = kwargs.get("headers")

    def get(self):
        response = requests.get(
            self.url,
            headers=self.headers,

        )
        return response


class TestingClient(object):

    def __init__(
        self,

        location=None,
    ):

        self.location = location

        # add multiple urls if necessary
        base_url = {

            "lotr": "https://the-one-api.dev/v2"
        }
        print("Base Url: **** ", base_url[self.location.strip().lower()])

        try:
            self.base_url = base_url[self.location.strip().lower()]
        except AttributeError:
            raise Exception("Use lotr")

        # Domains
        self._book = None
        self._movie = None
        self._character = None
        self._quote = None

    def request(self, method, base_url, object_type=None, object_id=None, profile_id=None,
                domain_id=None, domain_action=None, params=None, data=None, headers=None, auth=None):

        headers = headers or {}
        params = params or {}
        method = method.upper()

        path, url = PathBuilder(
            base_url=base_url, object_type=object_type, object_id=object_id, params=params).build()

        print(f'Endpoint (url): \n{url}\n\n')
        # add you your token here
        # auth = None #'Bearer tb2UM$%fW6_d5PweZ5G-s'
        auth = 'Bearer tb2UMXdfW6_d5P3Z5G-s'
        api = APIRequester(url=url, headers={'Authorization': auth})

        response = api.get()

        print(
            f'Response:\nStatus:\n{response.status_code}\nJson Response:\n{response.json()}\n\n'
        )
        json_response = response.json()
        return {
            "status": response.status_code,
            "json": json_response
        }

    @property
    def book(self):
        """
        Access the did_sdk Account API
        """
        if self._book is None:
            from Gian_lotr.rest.book import Book
            self._book = Book(self, self.base_url, 'book')
        return self._book

    @property
    def movie(self):
        """
        Access the did_sdk Account API
        """
        if self._movie is None:
            from Gian_lotr.rest.movie import Movie
            self._movie = Movie(self, self.base_url, 'movie')
        return self._movie

    @property
    def character(self):
        """
        Access the did_sdk Account API
        """
        if self._character is None:
            from Gian_lotr.rest.character import Character
            self._character = Character(self, self.base_url, 'character')
        return self._character

    @property
    def quote(self):
        """
        Access the did_sdk Account API
        """
        if self._quote is None:
            from Gian_lotr.rest.quote import Quote
            self._quote = Quote(self, self.base_url, 'quote')
        return self._quote
