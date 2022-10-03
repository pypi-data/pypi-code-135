import requests

class Client(object):
    def __init__(self, json):
        self.href = json['links'][0]['href']
        self.uuid = json['uuid']
        self.clientId = json['clientId']
        self.type = json['type']
        self.name = json['name']
        self.ssoApplication = json['ssoApplication']
        self.confidential = json['confidential']
        self.showLandingPage = json['showLandingPage']
        self.useClientCredentials = json['useClientCredentials']


class KeyHubClient(object):
    def __init__(self, authentication):
        self._session = authentication.session
        self._uri = authentication.uri
        self._client_id = authentication.client_id
        self._client_secret = authentication.client_secret
        self._session_password = authentication.session.access_token

    def get_client_info(self):
        response = self._session.get(self._uri + "/keyhub/rest/v1/client/me")
        return Client(response.json())

    def post_client_vault(self):
        content = { '$type': 'vault.VaultUnlock', 'password': self._session_password }
        response = requests.post(self._uri + "/keyhub/rest/v1/client/vault/unlock", data=content, verify=True, allow_redirects=False, auth=(self._client_id, self._client_secret))
        return response

def client(authentication):
    return KeyHubClient(authentication=authentication)
