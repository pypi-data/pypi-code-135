from abc import ABC

from loko_client.utils.requests_utils import URLRequest

GATEWAY = 'http://localhost:9999/routes/'

class OrchestratorClient(ABC):
    """
        An abstract base orchestrator client
    """

    def __init__(self, gateway=GATEWAY):
        self.u = URLRequest(gateway).orchestrator
