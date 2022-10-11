import requests
import pandas as pd


class OnchainsAPI:

    def __init__(self, api_key: str):
        self.api_key = api_key


if __name__ == '__main__':
    api_key = ''
    api = OnchainsAPI(api_key)
    print(api)
