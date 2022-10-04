from .module_imports import *


@headers({"Ocp-Apim-Subscription-Key": key})
class Sites(Consumer):
    """Inteface to Sites resource for the RockyRoad API."""

    def __init__(self, Resource, *args, **kw):
        self._base_url = Resource._base_url
        super().__init__(base_url=Resource._base_url, *args, **kw)

    @returns.json
    @http_get("sites")
    def list(
        self,
    ):
        """This call will return a list of sites."""
