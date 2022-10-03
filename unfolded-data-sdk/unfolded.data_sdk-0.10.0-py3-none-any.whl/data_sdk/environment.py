from enum import Enum

from pydantic import BaseModel


class EnvironmentConfig(BaseModel):
    """EnvironmentConfig specifies request and authentication endpoints for a given environment"""

    base_url: str = "https://api.unfolded.ai"
    studio_url: str = "https://studio.unfolded.ai"


class AuthEnvironment(str, Enum):
    """Enum for the different Unfolded environments"""

    PRODUCTION = "production"


class AuthConfig(BaseModel):
    client_id: str
    auth_url: str = "https://auth.unfolded.ai"
    audience: str = "unfolded-api"
    scope: str = "offline_access"


AUTH_CONFIGS = {
    AuthEnvironment.PRODUCTION: AuthConfig(
        client_id="v970dpbcqmRtr3y9XwlAB3dycpsvNRZF",
    ),
}

PRODUCTION_ENV = EnvironmentConfig()
