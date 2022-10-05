from flask.wrappers import Request


class HTTPTrigger:
    def __init__(self, request: Request):
        self.request = request

    def get_request(self) -> Request:
        return self.request
