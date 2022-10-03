from searchunify.utils.RequestManager import RequestManager
import json
import glob
import searchunify.utils.globals

with open(glob.glob(searchunify.utils.globals.baseDir+"/apis/apis.json")[0]) as config_file:
    constants = json.load(config_file)
    searchApi = constants["search"]


def getSearchResultsApi(**payload):
    url = searchunify.utils.globals.baseUrl + searchApi['searchResults']
    payload = json.dumps(payload)
    response = RequestManager.httpRequest(
        "POST", url, headers=searchunify.utils.globals.headers, data=payload)
    return response
