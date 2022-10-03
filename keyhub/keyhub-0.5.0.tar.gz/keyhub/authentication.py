from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import requests, json

class KeyHubClientAuthentication(object):
    def __init__(self, uri, client_id, client_secret):
        self.uri = uri
        self.client_id = client_id
        self.client_secret = client_secret

        client = BackendApplicationClient(client_id=client_id)
        oauth = OAuth2Session(client=client)
        token = oauth.fetch_token(token_url=uri+'/login/oauth2/token?authVault=access', client_id=client_id, client_secret=client_secret)

        session = OAuth2Session(client_id, token=token)
        session.headers.update({'Accept': 'application/vnd.topicus.keyhub+json;version=latest'})
        session.headers.update({'topicus-Vault-session': token['vaultSession']})
        self.session = session
    
    def info(self):
        # TODO: return info object instead of json
        response = self.session.get(self.uri + "/keyhub/rest/v1/info")
        return response.json()

    def docs(self):
        response = requests.get(self.uri + "/keyhub/rest/v1/openapi.json")
        return response.json()

class KeyHubAccountAuthentication(object):
    def __init__(self, uri, client_id, client_secret, callback_uri):
        # https://keyhub-instance/login/code?usercode=CODE-HERE
        # "authorizationCode" : {
        #   "authorizationUrl" : "https://keyhub-instance/login/oauth2/authorize",
        #    "tokenUrl" : "https://keyhub-instance/login/oauth2/token",
        #    "refreshUrl" : "https://keyhub-instance/login/oauth2/token",
        self.uri = uri
        authorize_url = self.uri + "/login/oauth2/authorize"
        token_url = self.uri + "/login/oauth2/token"
        
        authorization_redirect_url = authorize_url + '?response_type=code&client_id=' + client_id + '&redirect_uri=' + callback_uri + '&scope=openid'

        print("go to the following url on the browser and enter the code from the returned url: ")
        print("---  " + authorization_redirect_url + "  ---")
        authorization_code = input('code: ')

        # step I, J - turn the authorization code into a access token, etc
        data = {'grant_type': 'authorization_code', 'code': authorization_code, 'redirect_uri': callback_uri}
        print("requesting access token")
        access_token_response = requests.post(token_url, data=data, verify=True, allow_redirects=False, auth=(client_id, client_secret))
        
        # we can now use the access_token as much as we want to access protected resources.
        tokens = json.loads(access_token_response.text)
        access_token = tokens['access_token']
        headers = {'Authorization': 'Bearer ' + access_token}
        self.headers = headers
        

def client_auth(uri, client_id, client_secret):
    return KeyHubClientAuthentication(uri=uri, client_id=client_id, client_secret=client_secret)

def account_auth(uri, client_id, client_secret, callback_uri):
    return KeyHubAccountAuthentication(uri=uri, client_id=client_id, client_secret=client_secret, callback_uri=callback_uri)
