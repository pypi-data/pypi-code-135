from mlflow.exceptions import RestException
from mlflow.utils.rest_utils import MlflowHostCreds, http_request

from mlfoundry.tracking.entities import AuthServerInfo


class AuthService:
    def __init__(self, auth_server_info: AuthServerInfo):
        self.host_creds = MlflowHostCreds(host=auth_server_info.auth_server_url)

    def get_token(self, api_key: str) -> str:
        response = http_request(
            host_creds=self.host_creds,
            endpoint="/api/v1/oauth/api-keys/token",
            method="post",
            json={"apiKey": api_key},
        )
        if response.status_code not in (200, 201):
            raise RestException(f"Failed to get token. {response.text}")
        response = response.json()
        token = response["accessToken"]
        return token
