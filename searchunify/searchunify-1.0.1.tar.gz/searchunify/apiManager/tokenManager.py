from searchunify.utils.RequestManager import RequestManager
import base64
import glob
import searchunify.utils.globals
import json

with open(glob.glob(searchunify.utils.globals.baseDir+"/apis/apis.json")[0]) as config_file:
    constants = json.load(config_file)
    tokensApi = constants["tokens"]


def generateAccessTokenApi(**args):
    searchunify.utils.globals.baseUrl = args['instance'].strip("/")
    url = searchunify.utils.globals.baseUrl + tokensApi['accessToken']
    del args['instance']
    result = base64Encode(**args)
    response = RequestManager.httpRequest(
        "POST", url, headers=result["headers"], data=result["playload"])
    # Make global variables.
    searchunify.utils.globals.clientId = args['clientId']
    searchunify.utils.globals.secrets = args['secrets']
    searchunify.utils.globals.accessToken = response['accessToken']
    searchunify.utils.globals.refreshToken = response['refreshToken']
    searchunify.utils.globals.headers = {
        'Authorization': 'Bearer ' + searchunify.utils.globals.accessToken,
        'Content-Type': 'application/json'
    }
    if(searchunify.utils.globals.accessToken and searchunify.utils.globals.baseUrl and searchunify.utils.globals.refreshToken):
        return "SearchUnify sdk initialized."
    else:
        return "SearchUnify sdk not initialized."


def base64Encode(username=None, password=None, clientId=None, secrets=None):
    message = clientId+":"+secrets
    message = message.encode('ascii')
    message = base64.b64encode(message)
    base64_message = message.decode('ascii')
    grantType = "password"
    playLoad = 'grant_type='+grantType+'&username='+username+'&password='+password
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic '+base64_message,
        'cache-contro': 'no-cache'
    }
    return {"playload": playLoad, "headers": headers}


def getAccessTokenFromRefreshTokenApi():
    grant_type = "refresh_token"
    url = searchunify.utils.globals.baseUrl + tokensApi['accessToken']
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'cache-contro': 'no-cache'
    }
    payload = 'grant_type='+grant_type+'&refresh_token='+searchunify.utils.globals.refreshToken + \
        '&client_id='+searchunify.utils.globals.clientId+'&client_secret='+searchunify.utils.globals.secrets
    response = RequestManager.httpRequest(
        "POST", url, headers=headers, data=payload)
    # Make global variables.
    searchunify.utils.globals.accessToken = response['accessToken']
    searchunify.utils.globals.refreshToken = response['refreshToken']
    searchunify.utils.globals.headers = {
        'Authorization': 'Bearer ' + searchunify.utils.globals.accessToken,
        'Content-Type': 'application/json'
    }
    if(response['accessToken'] and response['refreshToken']):
        return 'Token refreshed successfully'
    else:
        return 'Token not refreshed.'
