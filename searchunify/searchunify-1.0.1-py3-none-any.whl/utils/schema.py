from schema import And, Use, Optional


def getAccessTokenSchema():
    schema = {
        'instance': str,
        'username': str,
        'password': str,
        'clientId': str,
        'secrets': str
    }
    return schema


def getAccessTokenFromRefreshTokenSchema():
    schema = {
        'refresh_token': str,
        'clientId': str,
        'secrets': str
    }
    return schema


def getCaseCreatedArticlesSchema():
    schema = {
        'startDate': str,
        'endDate': str,
        'searchClientId': str,
        'internalUser': str,
        'searchType': str,
        Optional('offset'): int,
        Optional('count'): And(Use(int), lambda n: 0 < n <= 500, error="count should be 1-500")
    }
    return schema


def getCaseDeflectedArticlesSchema():
    schema = {
        'startDate': str,
        'endDate': str,
        'searchClientId': str,
        'internalUser': str,
        'searchType': str,
        Optional('offset'): int,
        Optional('count'): And(Use(int), lambda n: 0 < n <= 500, error="count should be 1-500")
    }
    return schema


def getAttachedArticlesSchema():
    schema = {
        'startDate': str,
        'endDate': str,
        'searchClientId': str,
        'internalUser': str,
        Optional('offset'): int,
        Optional('count'): And(Use(int), lambda n: 0 < n <= 500, error="count should be 1-500")
    }
    return schema


def getAttachedOnCaseSchema():
    schema = {
        'startDate': str,
        'endDate': str,
        'searchClientId': str,
        'url': str,
        Optional('offset'): int,
        Optional('count'): And(Use(int), lambda n: 0 < n <= 500, error="count should be 1-500")
    }
    return schema


def getTilesDataSchema():
    schema = {
        'startDate': str,
        'endDate': str,
        Optional('searchClientId'): str
    }
    return schema


def getSearchSummaryChartSchema():
    schema = {
        'startDate': str,
        'endDate': str,
        Optional('searchClientId'): str
    }
    return schema


def getAllSearchQuerySchema():
    schema = {
        'startDate': str,
        'endDate': str,
        'count': And(int, lambda n: 0 < n <= 500, error="count should an intiger value (1-500)"),
        Optional('searchClientId'): str
    }
    return schema


def searchQueryWithNoClicksSchema():
    schema = {
        'startDate': str,
        'endDate': str,
        'count': And(int, lambda n: 0 < n <= 500, error="count should an intiger value (1-500)"),
        Optional('searchClientId'): str
    }
    return schema


def searchQueryWithoutResultsSchema():
    schema = {
        'startDate': str,
        'endDate': str,
        'count': And(int, lambda n: 0 < n <= 500, error="count should an intiger value (1-500)"),
        Optional('searchClientId'): str
    }
    return schema


def searchQueryWithResultSchema():
    schema = {
        'startDate': str,
        'endDate': str,
        'count': And(int, lambda n: 0 < n <= 500, error="count should an intiger value (1-500)"),
        Optional('searchClientId'): str
    }
    return schema


def searchQueryHistogramSchema():
    schema = {
        'startDate': str,
        'endDate': str,
        'count': And(int, lambda n: 0 < n <= 500, error="count should an intiger value (1-500)"),
        Optional('searchClientId'): str
    }
    return schema


def missedQueryHistogramSchema():
    schema = {
        'startDate': str,
        'endDate': str,
        'count': And(int, lambda n: 0 < n <= 500, error="count should an intiger value (1-500)"),
        Optional('searchClientId'): str
    }
    return schema


def searchSessionByCaseUidAuthSchema():
    schema = {
        'startDate': str,
        'endDate': str,
        'count': And(int, lambda n: 0 < n <= 500, error="count should an intiger value (1-500)"),
        'caseUID': str
    }
    return schema


def getAllSearchConversionSchema():
    schema = {
        'startDate': str,
        'endDate': str,
        'count': And(int, lambda n: 0 < n <= 500, error="count should an intiger value (1-500)"),
        Optional('searchClientId'): str
    }
    return schema


def searchConversionNotOnFirstPageSchema():
    schema = {
        'startDate': str,
        'endDate': str,
        'count': And(int, lambda n: 0 < n <= 500, error="count should an intiger value (1-500)"),
        Optional('searchClientId'): str
    }
    return schema


def searchConversionWithFiltersSchema():
    schema = {
        'startDate': str,
        'endDate': str
    }
    return schema


def searchConversionBySessionIdSchema():
    schema = {
        'startDate': str,
        'endDate': str,
        'sessionId': str,
        'count': And(int, lambda n: 0 < n <= 500, error="count should an intiger value (1-500)"),
        Optional('searchClientId'): str
    }
    return schema


def discussionsReadyToBecomeArticlesSchema():
    schema = {
        'startDate': str,
        'endDate': str,
        Optional('internalUser'): str,
        'count': And(int, lambda n: 0 < n <= 500, error="count should an intiger value (1-500)"),
        Optional('searchClientId'): str
    }
    return schema


def searchSessionAllsearchQuerySchema():
    schema = {
        'startDate': str,
        'endDate': str,
        'count': And(int, lambda n: 0 < n <= 500, error="count should an intiger value (1-500)"),
        Optional('searchClientId'): str
    }
    return schema


def getKcsSupportSearchQuerySchema():
    schema = {
        'startDate': str,
        'endDate': str,
        'count': And(int, lambda n: 0 < n <= 500, error="count should an intiger value (1-500)"),
        Optional('searchClientId'): str
    }
    return schema


def getSearchSessionByCaseUidSchema():
    schema = {
        'startDate': str,
        'endDate': str,
        'caseUid': str
    }
    return schema


def getSearchSessionBySearchSessionIdSchema():
    schema = {
        'startDate': str,
        'endDate': str,
        Optional('pageNumber'): And(int, error="pageNumber should be a number"),
        'count': And(int, lambda n: 0 < n <= 500, error="count should an intiger value (1-500)"),
        'sessionId': str,
        Optional('searchClientId'): str
    }
    return schema


def getContentSourceByIdSchema():
    schema = {
        'contentSourceId': str
    }
    return schema


def getObjectSpecificDataSchema():
    schema = {
        'contentSourceId': str,
        'objectId': str,
        Optional('startFrom'): int,
        Optional('size'): int
    }
    return schema


def getObjectSpecificDataWithIdSchema():
    schema = {
        'contentSourceId': str,
        'objectId': str,
        'documentId': str
    }
    return schema


def updateDoucmentByIdSchema():
    schema = {
        'contentSourceId': str,
        'objectId': str,
        'documentId': str,
        'data': dict
    }
    return schema


def bulkUploadSchema():
    schema = {
        'contentSourceId': str,
        'objectId': str,
        'data': list
    }
    return schema


def getSearchResultsSchema():
    schema = {
        'uid': str,
        'searchString': str
    }
    return schema
