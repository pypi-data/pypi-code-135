# Example PyPI (Python Package Index) Package
import time
import requests
from .config import config


class AuthArmorSDK(object):

    def __init__(self, client_id: str, client_secret: str, webauthn_client_id: str):
        self.client_id = client_id
        self.client_secret = client_secret

        if self.client_id is None:
            raise ValueError(
                "Please specify a valid Client ID, you can generate a Client ID from the AuthArmor Dashboard (https://dashboard.autharmor.com/)")

        if self.client_secret is None:
            raise ValueError(
                "Please specify a valid Client Secret, you can generate a Client Secret from the AuthArmor Dashboard (https://dashboard.autharmor.com/)")

        if webauthn_client_id is not None:
            self.webauthn_client_id = webauthn_client_id

    def __extend_token__(self):
        update_threshold = time.time() + (2 * 60)

        if self.token_expiration <= update_threshold:
            response = requests.get(config["login_url"] + "/connect/token", params={
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "grant_type": "client_credentials"
            })
            data = response.json()
            self.token = data["access_token"]
            self.token_expiration = time.time() + 8 * 60

    def start_enroll_credential(self, user_id: str, timeout_in_seconds: int, username: str):
        self.__extend_token__()

        if self.webauthn_client_id is None:
            raise ValueError(
                "Please initialize the Auth Armor SDK with a valid WebAuthn Client ID, you can generate one from the AuthArmor Dashboard (https://dashboard.autharmor.com/)")

        response = requests.post("{}/users/{}/webauthn/register/start".format(config["api_url_v3"], user_id), json={
            "webauthn_client_id": self.webauthn_client_id,
            "timeout_in_seconds": timeout_in_seconds,
        }, headers={
            "Authorization": "Bearer {}".format(self.token),
            "Content-Type": "application/json",
            "X-AuthArmor-UsernameValue": username,
        })
        data = response.json()

        return data

    def verify_enroll_credential(self, user_id: str, signed_response: str, username: str):
        self.__extend_token__()

        if self.webauthn_client_id is None:
            raise ValueError(
                "Please initialize the Auth Armor SDK with a valid WebAuthn Client ID, you can generate one from the AuthArmor Dashboard (https://dashboard.autharmor.com/)")

        response = requests.post("{}/users/{}/webauthn/register/finish".format(config["api_url_v3"], user_id), json={
            "webauthn_client_id": self.webauthn_client_id,
            "response": signed_response,
        }, headers={
            "Authorization": "Bearer {}".format(self.token),
            "Content-Type": "application/json",
            "X-AuthArmor-UsernameValue": username,
        })
        data = response.json()

        return data

    def verify_auth_request(self, auth_method: str, auth_validation_token: str, auth_request_id: str):
        self.__extend_token__()

        if auth_method not in ["authenticator", "magiclink", "webauthn"]:
            raise ValueError(
                "Please specify a valid auth_method ('authenticator', 'magiclink', 'webauthn')")

        try:
            response = requests.post("{}/auth/{}/validate".format(config["api_url_v3"], auth_method), json={
                "auth_validation_token": auth_validation_token,
                "auth_request_id": auth_request_id,
            }, headers={
                "Authorization": "Bearer {}".format(self.token),
                "Content-Type": "application/json",
            })
            data = response.json()

            if data["validate_auth_response_details"]["is_replay"]:
                raise ValueError("Replayed request detected!")

            if not data["validate_auth_response_details"]["authorized"]:
                raise ValueError("Unauthorized user")

            request_details = data["validate_auth_response_details"]["auth_details"]["request_details"]["auth_profile_details"]

            return {
                "verified": True,
                "request_details": request_details,
            }
        except requests.exceptions.HTTPError as e:
            return {
                "verified": False,
                "error": e
            }
        except ValueError as e:
            raise e

    def verify_register_request(self, auth_method: str, registration_validation_token: str, auth_request_id: str):
        self.__extend_token__()

        if auth_method not in ["authenticator", "magiclink", "webauthn"]:
            raise ValueError(
                "Please specify a valid auth_method ('authenticator', 'magiclink', 'webauthn')")

        try:
            response = requests.post("{}/users/register/{}/validate".format(config["api_url_v3"], auth_method), data={
                "registration_validation_token": registration_validation_token,
                "auth_request_id": auth_request_id,
            }, headers={
                "Authorization": "Bearer {}".format(self.token),
                "Content-Type": "application/json",
            })
            data = response.json()

            return {
                "verified": True,
                "request_details": data,
            }
        except requests.exceptions.HTTPError as e:
            return {
                "verified": False,
                "error": e
            }

    def get_user_by_id(self, user_id: str):
        self.__extend_token__()

        if user_id is None or len(user_id) == 0:
            raise ValueError("Please specify a valid user_id")

        response = requests.get("{}/users/{}/validate".format(config["api_url_v3"], user_id), headers={
            "Authorization": "Bearer {}".format(self.token),
            "Content-Type": "application/json",
        })
        data = response.json()

        return data
