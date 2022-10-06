import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class ModelProvider(str, Enum):
    """Supported model providers."""

    openai = "OpenAI"
    mock = "Mock"


class ModelEndpoint(str, Enum):
    """Supported model provider endpoints."""

    complete = "Complete"
    edit = "Edit"


class ProjectModelConfigResponse(BaseModel):
    id: str
    display_name: str
    model_name: str
    prompt_template: Optional[str]
    parameters: Optional[dict]
    provider: Optional[ModelProvider]
    endpoint: Optional[ModelEndpoint]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: Optional[str]
    last_used: datetime.datetime
