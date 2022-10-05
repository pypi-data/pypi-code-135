from src.inspector import Configuration
from src.inspector.transports import TransportInterface


class Transport(TransportInterface):
    """
    Key to authenticate remote calls.
    :type _config: Configuration
    """
    _config: Configuration = None

    """
    Custom url of the proxy if needed.
    :type _proxy: str
    """
    _proxy: str = None

    """
    Queue of messages to send.
    :type _queue: list
    """
    _queue: list = []

    def __init__(self, configuration: Configuration) -> None:
        """
        AbstractApiTransport constructor.
        :type configuration: object
        :raise InspectorException
        """
        self._config = configuration
        # $this->verifyOptions($configuration->getOptions());

    def _get_api_headers(self):
        """
        Return header configuration
        :return: list
        """
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Inspector-Key": self._config.get_ingestion_key(),
            "X-Inspector-Version": self._config.get_version()
        }
        return headers
