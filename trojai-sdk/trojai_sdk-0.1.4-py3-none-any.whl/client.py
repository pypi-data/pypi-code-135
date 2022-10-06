import requests
from typing import Optional, List
import json
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from requests import Session

retry_strategy = Retry(
    total=2,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["HEAD", "GET", "PUT", "POST", "DELETE", "OPTIONS", "TRACE"],
)

retry_adapter = HTTPAdapter(max_retries=retry_strategy)
requests_retry = Session()
requests_retry.mount("https://", retry_adapter)
requests_retry.mount("http://", retry_adapter)

"""
Troj Client class handls all requests made to a passed endpoint
"""
class TrojClient:
    def __init__(
        self,
        *,
        api_endpoint: str = "http://localhost:8080/api/v1",
        api_key: str,
        **kwargs,
    ):
        self._creds_refresh_token = None
        self._creds_api_key = None
        self.api_endpoint = api_endpoint
        self.refresh_url = "https://troj.auth.ca-central-1.amazoncognito.com/oauth2/token"
        

        requests_retry.hooks["response"].append(
            self.reauth
        )  # https://github.com/psf/requests/issues/4747 - Important for Retry vs urllib3

    

    def _get_creds_headers(self):
        """
        Get appropriate request headers for the currently set credentials.

        Raises:
            Exception: No credentials set.
        """
        if self._creds_id_token:
            return {
                "Authorization": f"Bearer {self._creds_id_token}",
                "x-api-key": f"{self._creds_api_key}",
            }
        else:
            raise Exception("No credentials set.")

    def set_credentials(
        self,
        *,
        id_token: Optional[str] = None,
        refresh_token: Optional[str] = None,
        api_key: Optional[str] = None,
    ):
        """
        Set credentials for the client.

        :param id_token (str, optional): Used by the client to authenticate the user.
        :param refresh_token (str, optional): Used to refresh the ID Token.
        :param api_key (str, optional): Used to gain access to API.

        Raises:
            Exception: Invalid credential combination provided.
        """

        # TODO: Change to require id_token and api_key together
        if id_token is not None:
            self._creds_id_token = id_token

        if refresh_token is not None:
            self._creds_refresh_token = refresh_token

        if api_key is not None:
            self._creds_api_key = api_key


    """
    This function is not called in all the pytest tests
    """

    def reauth(self, res, *args, **kwargs):
        """Hook to re-authenticate whenever authentication expires."""
        if res.status_code == requests.codes.forbidden:
            if res.request.headers.get("REATTEMPT"):
                res.raise_for_status()
            self.refresh_tokens()
            req = res.request
            req.headers["REATTEMPT"] = 1
            req = self.auth_inside_hook(req)
            res = requests_retry.send(req)
            return res

    """
    This function is not called in all the pytest tests
    """

    def auth_inside_hook(self, req):
        """Set the authentication token for the premade request during reauth attempts inside the retry hook."""
        req.headers["Authorization"] = f"Bearer {self._creds_id_token}"
        return req

    def refresh_tokens(self):
        payload = f"grant_type=refresh_token&client_id={self.cognito_client_id}&refresh_token={self._creds_refresh_token}"
        requests.utils.quote(payload)
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
        }

        response = requests.request("POST", self.refresh_url, headers=headers, data=payload)
        self._creds_id_token = json.loads(response.text)["id_token"]

        return response

    def get_jobs(self):
        r = requests_retry.get(
            f"{self.api_endpoint}/jobs",
        )

    def post_job(self, config_json, docker_metadata):
        data = {"job_config": {"body": config_json}, "docker_metadata": docker_metadata}
        r = requests_retry.post(
            f"{self.api_endpoint}/jobs",
            headers=self._get_creds_headers(),
            json=data
        )
        self.raise_resp_exception_error(r)
    
        print("POST /jobs response:", r.json())

        return {"status_code": r.status_code, "data": r.json()}

    def get_job_status(self, job_id):
        r = requests_retry.get(
                    f"{self.api_endpoint}/jobs/{job_id}",
                    headers=self._get_creds_headers(),
                )

        print("GET /jobs/job_id response:", r.json())
        self.raise_resp_exception_error(r)

        return {"status_code": r.status_code, "data": r.json()}

    
    def raise_resp_exception_error(self, resp):
        if not resp.ok:
            message = None
            try:
                r_body = resp.json()
                message = r_body.get("message") or r_body.get("msg")
            except:
                # If we failed for whatever reason (parsing body, etc.)
                # Just return the code
                if resp.status_code == 500:
                    raise Exception(
                        f"HTTP Error received: {resp.reason}: {str(resp.status_code)}"
                    )
                else:
                    raise Exception(
                        f"HTTP Error received: {resp.reason}: {str(resp.status_code)} | {resp.json()['detail']}"
                    )
            if message:
                raise Exception(f"Error: {message}")
            else:
                if resp.status_code == 500:
                    raise Exception(
                        f"HTTP Error received: {resp.reason}: {str(resp.status_code)}"
                    )
                else:
                    raise Exception(
                        f"HTTP Error received: {resp.reason}: {str(resp.status_code)} | {resp.json()['detail']}"
                    )



