from requests import Response


def parse(key: str, response: Response):
    return response.json()[key]