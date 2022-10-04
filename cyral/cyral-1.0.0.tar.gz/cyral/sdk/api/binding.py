"""Resource client to obtain information on sidecar bindings"""

from typing import Any, Dict

from ..client import Client
from .resource import ResourceClient


class BindingClient(ResourceClient):
    """BindingClient can be used to get information about the binding of a
    repo to a sidecar.
    """

    def __init__(
        self,
        cyral_client: Client,
        sidecar_id: str,
        repo_id: str,
    ) -> None:
        super().__init__(cyral_client)
        self.sidecar_id = sidecar_id
        self.repo_id = repo_id

    def get(self) -> Dict[str, Any]:
        """fetch information related to the binding"""
        uri = f"/v1/sidecars/{self.sidecar_id}/repos/{self.repo_id}"
        return self.do_get(uri)

    @staticmethod
    def port(binding_info: Dict[str, Any]) -> int:
        """port returns the sidecar listener port for the binding."""
        return binding_info["listener"]["port"]
