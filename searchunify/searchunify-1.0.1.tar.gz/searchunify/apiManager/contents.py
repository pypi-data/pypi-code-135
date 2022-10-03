from searchunify.utils.RequestManager import RequestManager
import json
import glob
import searchunify.utils.globals
import re

with open(glob.glob(searchunify.utils.globals.baseDir+"/apis/apis.json")[0]) as config_file:
    constants = json.load(config_file)
    contentApi = constants["content"]


def replace_all(url, replacedObject):
    rep = dict((re.escape(k), v) for k, v in replacedObject.items())
    pattern = re.compile("|".join(rep.keys()))
    url = pattern.sub(lambda m: rep[re.escape(m.group(0))], url)
    return url


def getContentSourcesApi():
    url = searchunify.utils.globals.baseUrl + contentApi['contentSources']
    response = RequestManager.httpRequest(
        "GET", url, headers=searchunify.utils.globals.headers)
    return response


def getContentSourceByIdApi(**payload):
    url = searchunify.utils.globals.baseUrl + \
        contentApi['contentSourceByID'] + "/" + str(payload['contentSourceId'])
    response = RequestManager.httpRequest(
        "GET", url, headers=searchunify.utils.globals.headers)
    return response


def getObjectAndFieldsApi(**payload):
    url = searchunify.utils.globals.baseUrl + contentApi['objectAndFields']
    url = url.replace("<contentSourceId>", str(payload['contentSourceId']), 1)
    response = RequestManager.httpRequest(
        "GET", url, headers=searchunify.utils.globals.headers)
    return response


def getObjectSpecificDataApi(**payload):
    url = searchunify.utils.globals.baseUrl + contentApi['objectData']
    replacedObject = {"<contentSourceId>": str(
        payload['contentSourceId']), "<objectId>": str(payload['objectId'])}
    url = replace_all(url, replacedObject)
    payload["from"] = payload["startFrom"]
    del payload["contentSourceId"], payload["objectId"], payload["startFrom"]
    response = RequestManager.httpRequest(
        "GET", url, headers=searchunify.utils.globals.headers, params=payload)
    return response


def getObjectSpecificDataWithIdApi(**payload):
    url = searchunify.utils.globals.baseUrl + contentApi['objectDataWithId']
    replacedObject = {"<contentSourceId>": str(payload['contentSourceId']), "<objectId>": str(
        payload['objectId']), "<documentId>": str(payload['documentId'])}
    url = replace_all(url, replacedObject)
    response = RequestManager.httpRequest(
        "GET", url, headers=searchunify.utils.globals.headers, params=payload)
    return response


def updateDoucmentByIdApi(**payload):
    url = searchunify.utils.globals.baseUrl + contentApi['updateDoucmentById']
    replacedObject = {"<contentSourceId>": str(payload['contentSourceId']), "<objectId>": str(
        payload['objectId']), "<documentId>": str(payload['documentId'])}
    url = replace_all(url, replacedObject)
    payload = json.dumps(payload['data'])
    response = RequestManager.httpRequest(
        "POST", url, headers=searchunify.utils.globals.headers, data=payload)
    return response


def bulkUploadApi(**payload):
    url = searchunify.utils.globals.baseUrl + contentApi['bulkUpload']
    replacedObject = {"<contentSourceId>": str(
        payload['contentSourceId']), "<objectId>": str(payload['objectId'])}
    url = replace_all(url, replacedObject)
    payload = {
        "bulkData": payload['data']
    }
    payload = json.dumps(payload)
    response = RequestManager.httpRequest(
        "POST", url, headers=searchunify.utils.globals.headers, data=payload)
    return response
