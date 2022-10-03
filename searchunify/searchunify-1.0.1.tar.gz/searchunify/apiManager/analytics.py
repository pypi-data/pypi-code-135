from searchunify.utils.RequestManager import RequestManager
import json
import glob
import searchunify.utils.globals

with open(glob.glob(searchunify.utils.globals.baseDir+"/apis/apis.json")[0]) as config_file:
    constants = json.load(config_file)
    analyicsApi = constants["analytics"]


def getTilesDataApi(**payload):
    url = searchunify.utils.globals.baseUrl + analyicsApi['tileData']
    payload = json.dumps(payload)
    response = RequestManager.httpRequest(
        "POST", url, headers=searchunify.utils.globals.headers, data=payload)
    return response


def getSearchSummaryChartApi(**payload):
    url = searchunify.utils.globals.baseUrl + analyicsApi['searchSummaryChart']
    payload = json.dumps(payload)
    response = RequestManager.httpRequest(
        "POST", url, headers=searchunify.utils.globals.headers, data=payload)
    return response


def getAllSearchQueryApi(**payload):
    url = searchunify.utils.globals.baseUrl + analyicsApi['searchQueryAll']
    response = RequestManager.httpRequest(
        "GET", url, headers=searchunify.utils.globals.headers, params=payload)
    return response


def searchQueryWithResultApi(**payload):
    url = searchunify.utils.globals.baseUrl + analyicsApi['searchQueryWithResults']
    response = RequestManager.httpRequest(
        "GET", url, headers=searchunify.utils.globals.headers, params=payload)
    return response


def searchQueryWithNoClicksApi(**payload):
    url = searchunify.utils.globals.baseUrl + analyicsApi['searchQueryWithNoClicks']
    response = RequestManager.httpRequest(
        "GET", url, headers=searchunify.utils.globals.headers, params=payload)
    return response


def searchQueryWithoutResultsApi(**payload):
    url = searchunify.utils.globals.baseUrl + analyicsApi['searchQueryWithoutResult']
    response = RequestManager.httpRequest(
        "GET", url, headers=searchunify.utils.globals.headers, params=payload)
    return response


def searchQueryHistogramApi(**payload):
    url = searchunify.utils.globals.baseUrl + analyicsApi['searchQueryHistogram']
    payload = json.dumps(payload)
    response = RequestManager.httpRequest(
        "POST", url, headers=searchunify.utils.globals.headers, data=payload)
    return response


def missedQueryHistogramApi(**payload):
    url = searchunify.utils.globals.baseUrl + analyicsApi['missedQueryHistogram']
    payload = json.dumps(payload)
    response = RequestManager.httpRequest(
        "POST", url, headers=searchunify.utils.globals.headers, data=payload)
    return response


def searchSessionByCaseUidAuthApi(**payload):
    url = searchunify.utils.globals.baseUrl + analyicsApi['searchSessionByCaseUidAuth']
    payload = json.dumps(payload)
    response = RequestManager.httpRequest(
        "POST", url, headers=searchunify.utils.globals.headers, data=payload)
    return response


def getAllSearchConversionApi(**payload):
    url = searchunify.utils.globals.baseUrl + analyicsApi['allSearchConversion']
    response = RequestManager.httpRequest(
        "GET", url, headers=searchunify.utils.globals.headers, params=payload)
    return response


def searchConversionNotOnFirstPageApi(**payload):
    url = searchunify.utils.globals.baseUrl + analyicsApi['searchConversionNotOnFirstPage']
    response = RequestManager.httpRequest(
        "GET", url, headers=searchunify.utils.globals.headers, params=payload)
    return response


def searchConversionWithFiltersApi(**payload):
    url = searchunify.utils.globals.baseUrl + analyicsApi['searchConversionWithFilters']
    response = RequestManager.httpRequest(
        "GET", url, headers=searchunify.utils.globals.headers, params=payload)
    return response


def searchConversionBySessionIdApi(**payload):
    url = searchunify.utils.globals.baseUrl + analyicsApi['searchConversionBySessionId']
    url = url.replace("<searchSessionId>", str(payload['sessionId']), 1)
    response = RequestManager.httpRequest(
        "GET", url, headers=searchunify.utils.globals.headers, params=payload)
    return response


def discussionsReadyToBecomeArticlesApi(**payload):
    url = searchunify.utils.globals.baseUrl + \
        analyicsApi['discussionsReadyToBecomeArticles']
    payload = json.dumps(payload)
    response = RequestManager.httpRequest(
        "POST", url, headers=searchunify.utils.globals.headers, data=payload)
    return response


def searchSessionAllsearchQueryApi(**payload):
    url = searchunify.utils.globals.baseUrl + analyicsApi['searchSessionAllsearchQuery']
    response = RequestManager.httpRequest(
        "GET", url, headers=searchunify.utils.globals.headers, params=payload)
    return response


def getKcsSupportSearchQueryApi(**payload):
    url = searchunify.utils.globals.baseUrl + analyicsApi['kcsSupport']
    payload = json.dumps(payload)
    response = RequestManager.httpRequest(
        "POST", url, headers=searchunify.utils.globals.headers, data=payload)
    return response


def getSearchSessionByCaseUidApi(**payload):
    url = searchunify.utils.globals.baseUrl + analyicsApi['searchSessionByCaseUid']
    payload = json.dumps(payload)
    response = RequestManager.httpRequest(
        "POST", url, headers=searchunify.utils.globals.headers, data=payload)
    return response


def getSearchSessionBySearchSessionIdApi(**payload):
    url = searchunify.utils.globals.baseUrl + analyicsApi['searchSessionBySearchSessionId']
    url = url.replace("<searchSessionId>", str(payload['sessionId']), 1)
    response = RequestManager.httpRequest(
        "GET", url, headers=searchunify.utils.globals.headers, params=payload)
    return response


def getCaseCreatedArticlesApi(**payload):
    url = searchunify.utils.globals.baseUrl + analyicsApi['articlesCreatedCases']
    payload = reModifyKeys(**payload)
    payload = json.dumps(payload)
    response = RequestManager.httpRequest(
        "POST", url, headers=searchunify.utils.globals.headers, data=payload)
    return response


def getCaseDeflectedArticlesApi(**payload):
    url = searchunify.utils.globals.baseUrl + analyicsApi['articlesDeflectedCase']
    payload = reModifyKeys(**payload)
    payload = json.dumps(payload)
    response = RequestManager.httpRequest(
        "POST", url, headers=searchunify.utils.globals.headers, data=payload)
    return response


def getAttachedArticlesApi(**payload):
    url = searchunify.utils.globals.baseUrl + analyicsApi['attachedArticles']
    payload = reModifyKeys(**payload)
    payload = json.dumps(payload)
    response = RequestManager.httpRequest(
        "POST", url, headers=searchunify.utils.globals.headers, data=payload)
    return response


def getAttachedOnCaseApi(**payload):
    url = searchunify.utils.globals.baseUrl + analyicsApi['attachedOnCase']
    payload = reModifyKeys(**payload)
    payload = json.dumps(payload)
    response = RequestManager.httpRequest(
        "POST", url, headers=searchunify.utils.globals.headers, data=payload)
    return response


def reModifyKeys(**payload):
    payload["from"] = payload['startDate']
    payload["to"] = payload['endDate']
    payload["uid"] = payload['searchClientId']
    payload["limit"] = payload['count']
    del payload['startDate'],  payload['endDate'], payload['searchClientId'], payload['count']
    return payload
