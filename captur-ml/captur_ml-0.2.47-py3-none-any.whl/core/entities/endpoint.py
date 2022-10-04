from typing import List

from pydantic import Field
from pydantic.dataclasses import dataclass

from google.cloud.aiplatform import Endpoint
from google.cloud.aiplatform_v1beta1.types import DeployedModel

from google.api_core import exceptions as google_exceptions


@dataclass
class VertexAIEndpoint:
    #: A unique identifier for the VertexAI Endpoint.
    id: str
    #: The GCP project name.
    project: str
    #: The global location of the VertexAI Endpoint.
    location: str

    def __post_init__(self):
        self.endpoint = Endpoint(
            endpoint_name=self.id, project=self.project, location=self.location
        )

    @property
    def exists(self) -> bool:
        """Checks if the VertexAI Endpoint exists."""
        try:
            self.endpoint.list_models()
        except (google_exceptions.NotFound, google_exceptions.InvalidArgument):
            return False
        return True

    @property
    def is_active(self) -> bool:
        """Checks if the VertexAI Endpoint exists and has at least one model serving requests."""
        if not self.exists:
            return False

        return len(self.models) > 0

    @property
    def models(self) -> List[DeployedModel]:
        """Returns a list of models deployed to the VertexAI Endpoint."""
        return self.endpoint.list_models()
