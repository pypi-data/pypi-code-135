import requests


class Client:
    
    """_summary_"""
    
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        username: str,
        password: str,
        scope: list[str] = ["read_station"],
    ) -> None:

        self.response = requests.post(
            "https://api.netatmo.com/oauth2/token",
            data={
                "grant_type": "password",
                "client_id": client_id,
                "client_secret": client_secret,
                "username": username,
                "password": password,
                "scope": scope,
            },
        )
        self.json = self.response.json()
        self.access_token = self.json["access_token"]
        self.refresh_token = self.json["refresh_token"]
        self.expires_in = self.json["expires_in"]
