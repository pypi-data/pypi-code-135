import requests

class Profile(object):
    def __init__(self, json):
        self.href = json['links'][0]['href']
        self.validity = json['validity']
        self.uuid = json['uuid']
        self.username = json['username']
        self.displayName = json['displayName']
        self.lastActive = json['lastActive']
        self.active = json['active']
        self.reregistrationRequired = json['reregistrationRequired']
        self.validInDirectory = json['validInDirectory']
        self.canRequestGroups = json['canRequestGroups']
        self.tokenPasswordEnabled = json['tokenPasswordEnabled']
        self.keyHubPasswordChangeRequired = json['keyHubPasswordChangeRequired']
        self.directoryPasswordChangeRequired = json['directoryPasswordChangeRequired']
        self.licenseRole = json['licenseRole']


class KeyHubProfile(object):
    def __init__(self, authentication):
        self._headers = authentication.headers
        self._uri = authentication.uri
    
    def get_profile_info(self):
        # response = self._session.get(self._uri + "/keyhub/rest/v1/account/me") 
        response = requests.get(self._uri + "/keyhub/rest/v1/account/me", headers=self._headers, verify=True)
        return response.text

    def get_rotating_password(self):
        # /keyhub/rest/v1/account/provisioning/tokenpwd
        response = requests.get(self._uri + "/keyhub/rest/v1/account/provisioning/tokenpwd", headers=self._headers, verify=True)
        # return Profile(response.json())
        return response.text


def profile(authentication):
    return KeyHubProfile(authentication=authentication)

