from src.inspector.transports import Transport
from abc import ABC, abstractmethod
from src.inspector import Configuration
import http.client
import ssl
import time


class CurlTransport(Transport):
    PORT = 80
    TIMEOUT = 10

    def __init__(self, configuration: Configuration):
        Transport.__init__(configuration)

    def send_chunk(self, data):
        headers = self._get_api_headers()
        connection = http.client.HTTPSConnection(self._config.get_url(), self.PORT, timeout=self.TIMEOUT,
                                                 context=ssl._create_unverified_context())
        connection.request('POST', "/", data, headers)
        response = connection.getresponse()
        print(response.read().decode())
