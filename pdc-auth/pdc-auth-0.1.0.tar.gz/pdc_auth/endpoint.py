DEFAULT_ENDPOINT_URL = 'http://localhost:4000'
DEFAULT_ENDPOINT_PATH = '/v2/login'

class EndpointConfig:
    url: str = DEFAULT_ENDPOINT_URL
    path: str = DEFAULT_ENDPOINT_PATH

    def get_host(self):
        return '{}{}'.format(self.url, self.path)

def configure_endpoint(url=DEFAULT_ENDPOINT_URL, path=DEFAULT_ENDPOINT_PATH):
    if url[-1] == '/':
        url = url[0:len(url) - 1]

    EndpointConfig.url = url
    EndpointConfig.path = path