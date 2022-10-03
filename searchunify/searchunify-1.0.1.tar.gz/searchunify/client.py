"""This library developed by searchunify. This library has various capabilities data pulling and pushing. This library gives the simple way to integrate SearchUnify API's"""
__author__ = "Mohan Rana"
__copyright__ = "Copyright 2021, SearchUnify"
__version__ = "1.0.1"
__maintainer__ = "SearchUnify"
__email__ = "mohanr@grazitti.com"

import os
import searchunify.utils.globals
searchunify.utils.globals.baseUrl = None
searchunify.utils.globals.accessToken = None 
searchunify.utils.globals.refreshToken = None
searchunify.utils.globals.headers = None 
searchunify.utils.globals.clientId = None
searchunify.utils.globals.secrets = None 
searchunify.utils.globals.baseDir = os.path.dirname(__file__)

from searchunify.utils.schema import *
from schema import Schema
from searchunify.apiManager.search import getSearchResultsApi
from searchunify.apiManager.contents import *
from searchunify.apiManager.analytics import *
from searchunify.apiManager.tokenManager import *

def validation(schema, **args):
    if(schema and args and searchunify.utils.globals.baseUrl and searchunify.utils.globals.accessToken):
        schema.validate(args)
    else:
        raise Exception("SDK not initialized yet.")


def startClient(**args):
    """
    Used to initialize SearchUnify client. 
    Pass instance url, username, password, clientId and secrets.
    """
    try:
        schema = Schema(getAccessTokenSchema())
        schema.validate(args)
        response = generateAccessTokenApi(**args)
        return response
    except Exception as error:
        return error


def refreshToken():
    """
    Used to refresh accessToken from refresh token.
    """
    try:
        schema = Schema(getAccessTokenFromRefreshTokenSchema())
        validation(schema, refresh_token=searchunify.utils.globals.refreshToken, clientId=searchunify.utils.globals.clientId, secrets=searchunify.utils.globals.secrets)
        response = getAccessTokenFromRefreshTokenApi()
        return response
    except Exception as error:
        return error


def getTilesData(**args):
    """
    Used to get information about visitors, search users, clicks, results, cases, and other essential search behavior.
    """
    try:
        schema = Schema(getTilesDataSchema())
        validation(schema, **args)
        response = getTilesDataApi(**args)
        return response
    except Exception as error:
        return error


def getSearchSummaryChart(**args):
    """
    Return Searches with Results, and All Searches with Clicks (conversions) have changed over the period between startDate and endDate.
    """
    try:
        schema = Schema(getSearchSummaryChartSchema())
        validation(schema, **args)
        response = getSearchSummaryChartApi(**args)
        return response
    except Exception as error:
        return error


def getAllSearchQuery(**args):
    """
    Returns the most popular search queries over the period from startDate to endDate.
    """
    try:
        schema = Schema(getAllSearchQuerySchema())
        validation(schema, **args)
        response = getAllSearchQueryApi(**args)
        return response
    except Exception as error:
        return error


def getSearchQueryWithResult(**args):
    """
    Returns the most popular search queries for which results were found.
    """
    try:
        schema = Schema(searchQueryWithResultSchema())
        validation(schema, **args)
        response = searchQueryWithResultApi(**args)
        return response
    except Exception as error:
        return error


def searchQueryWithNoClicks(**args):
    """
    Returns the most popular search queries for which results were found but users didn't click on any of them.
    """
    try:
        schema = Schema(searchQueryWithNoClicksSchema())
        validation(schema, **args)
        response = searchQueryWithNoClicksApi(**args)
        return response
    except Exception as error:
        return error


def searchQueryWithoutResults(**args):
    """
    Returns the most popular search queries for which no results were found.
    """
    try:
        schema = Schema(searchQueryWithoutResultsSchema())
        validation(schema, **args)
        response = searchQueryWithoutResultsApi(**args)
        return response
    except Exception as error:
        return error


def searchQueryHistogram(**args):
    """
    Returns search and conversion data over the period between startDate and endDate.
    """
    try:
        schema = Schema(searchQueryHistogramSchema())
        validation(schema, **args)
        response = searchQueryHistogramApi(**args)
        return response
    except Exception as error:
        return error


def missedQueryHistogram(**args):
    """
    Returns the total number of queries that didn't produce even one result. The data is for the period between startDate and endDate.
    """
    try:
        schema = Schema(missedQueryHistogramSchema())
        validation(schema, **args)
        response = missedQueryHistogramApi(**args)
        return response
    except Exception as error:
        return error


def searchSessionByCaseUidAuth(**args):
    """
    Return the activity on a case. 
    """
    try:
        schema = Schema(searchSessionByCaseUidAuthSchema())
        validation(schema, **args)
        response = searchSessionByCaseUidAuthApi(**args)
        return response
    except Exception as error:
        return error


def getAllSearchConversion(**args):
    """
    Return a list of the count most popular documents. The data is from between startDate and endDate on a search client whose ID is searchClientID. 
    If the searchClientID is not specified, then the call fetches data from all the search clients.
    """
    try:
        schema = Schema(getAllSearchConversionSchema())
        validation(schema, **args)
        response = getAllSearchConversionApi(**args)
        return response
    except Exception as error:
        return error


def searchConversionNotOnFirstPage(**args):
    """
    Return a list of the count documents that are not on the first page. These documents can be boosted to enhance search experience. 
    The data is from between startDate and endDate on a search client whose ID is searchClientID. If the searchClientID is not specified, then the call fetches data from all the search clients.
    """
    try:
        schema = Schema(searchConversionNotOnFirstPageSchema())
        validation(schema, **args)
        response = searchConversionNotOnFirstPageApi(**args)
        return response
    except Exception as error:
        return error


def searchConversionWithFilters(**args):
    """
    Return a chart of the popularity of all your content sources. 
    The data is presented in an alphabetical order and includes: 
    objectName, objectData, filterName, filterData, facetName, and facetName. 
    An objectName is a content type and a filter is a high-level facet. 
    The data is from between startDate and endDate.
    """
    try:
        schema = Schema(searchConversionWithFiltersSchema())
        validation(schema, **args)
        response = searchConversionWithFiltersApi(**args)
        return response
    except Exception as error:
        return error


def searchConversionBySessionId(**args):
    """
    Return a list of the count most popular searches in a session. 
    The data is from between startDate and endDate on a search client whose ID is searchClientID. 
    If the searchClientID is not specified, then the call fetches data from all the search clients.
    """
    try:
        schema = Schema(searchConversionBySessionIdSchema())
        validation(schema, **args)
        response = searchConversionBySessionIdApi(**args)
        return response
    except Exception as error:
        return error


def getSearchSessionBySearchSessionId(**args):
    """
    Return a list of the count queries in a search session and the documents accessed during that session. 
    The data is from between startDate and endDate on a search client whose ID is searchClientID. 
    If the searchClientID is not specified, then the call fetches data from all the search clients.
    """
    try:
        schema = Schema(getSearchSessionBySearchSessionIdSchema())
        validation(schema, **args)
        response = getSearchSessionBySearchSessionIdApi(**args)
        return response
    except Exception as error:
        return error


def discussionsReadyToBecomeArticles(**args):
    """
    Return count discussions that have been accessed the most and can be converted into articles. 
    The data is from between startDate and endDate. 
    """
    try:
        schema = Schema(discussionsReadyToBecomeArticlesSchema())
        validation(schema, **args)
        response = discussionsReadyToBecomeArticlesApi(**args)
        return response
    except Exception as error:
        return error


def getSearchQueryInSessions(**args):
    """
    Return a list of the count search sessions and the searches conducted in each session. 
    The data is from between startDate and endDate on a search client whose ID is searchClientID. 
    If the searchClientID is not specified, then the call fetches data from all the search clients.
    """
    try:
        schema = Schema(searchSessionAllsearchQuerySchema())
        validation(schema, **args)
        response = searchSessionAllsearchQueryApi(**args)
        return response
    except Exception as error:
        return error


def getKcsSupportSearchQuery(**args):
    """
    Return the number of articles generated on your cases between startDate and endDate on a search client whose ID is searchClientID. 
    If the searchClientID is not specified, then the call fetches data from all the search clients.
    """
    try:
        schema = Schema(getKcsSupportSearchQuerySchema())
        validation(schema, **args)
        response = getKcsSupportSearchQueryApi(**args)
        return response
    except Exception as error:
        return error


def getSearchSessionByCaseUid(**args):
    """
    Return search, conversion, page views, case deflection, and case creation data for the argument caseUid.
    """
    try:
        schema = Schema(getSearchSessionByCaseUidSchema())
        validation(schema, **args)
        response = getSearchSessionByCaseUidApi(**args)
        return response
    except Exception as error:
        return error


def getCaseCreatedArticles(**args):
    """
    Return the list of articles that were consulted before a user created a case. 
    """
    try:
        schema = Schema(getCaseCreatedArticlesSchema())
        validation(schema, **args)
        response = getCaseCreatedArticlesApi(**args)
        return response
    except Exception as error:
        return error


def getCaseDeflectedArticles(**args):
    """
    Returns the articles that were consulted by users who didn't create a case.
    """
    try:
        schema = Schema(getCaseDeflectedArticlesSchema())
        validation(schema, **args)
        response = getCaseDeflectedArticlesApi(**args)
        return response
    except Exception as error:
        return error


def getAttachedArticles(**args):
    """
    Return how many articles have been attached to cases. 
    """
    try:
        schema = Schema(getAttachedArticlesSchema())
        validation(schema, **args)
        response = getAttachedArticlesApi(**args)
        return response
    except Exception as error:
        return error


def getAttachedOnCase(**args):
    """
    From the article URL, find out which cases it has been attached to. 
    """
    try:
        schema = Schema(getAttachedOnCaseSchema())
        validation(schema, **args)
        response = getAttachedOnCaseApi(**args)
        return response
    except Exception as error:
        return error

# content source methods.


def getContentSources():
    """
    Used to list all added content sources in SearchUnify instance.
    """
    try:
        response = getContentSourcesApi()
        return response
    except Exception as error:
        return error


def getContentSourceById(**args):
    """
    Used to get particular content source.
    You need pass contentSourceId as a parameter particular content source.
    """
    try:
        schema = Schema(getContentSourceByIdSchema())
        validation(schema, **args)
        response = getContentSourceByIdApi(**args)
        return response
    except Exception as error:
        return error


def getObjectAndFields(**args):
    """
    Used to get content source objects and fileds. 
    """
    try:
        schema = Schema(getContentSourceByIdSchema())
        validation(schema, **args)
        response = getObjectAndFieldsApi(**args)
        return response
    except Exception as error:
        return error


def getObjectSpecificData(**args):
    """
    If you have multiple objects type. You can get data from particular object by this method. 
    """
    try:
        schema = Schema(getObjectSpecificDataSchema())
        validation(schema, **args)
        response = getObjectSpecificDataApi(**args)
        return response
    except Exception as error:
        return error


def getObjectSpecificDataWithId(**args):
    """
    Used to get data from a specific object type and specific document id.
    """
    try:
        schema = Schema(getObjectSpecificDataWithIdSchema())
        validation(schema, **args)
        response = getObjectSpecificDataWithIdApi(**args)
        return response
    except Exception as error:
        return error


def updateDoucmentById(**args):
    """
    Used to update particular document in SearchUnify index. 
    """
    try:
        schema = Schema(updateDoucmentByIdSchema())
        validation(schema, **args)
        response = updateDoucmentByIdApi(**args)
        return response
    except Exception as error:
        return error


def bulkUpload(**args):
    """
    Used to index multiple document at a time. 
    """
    try:
        schema = Schema(bulkUploadSchema())
        validation(schema, **args)
        response = bulkUploadApi(**args)
        return response
    except Exception as error:
        return error


# Search methods
def getSearchResults(**args):
    """
    Used to search content from a particular plateform. 
    Pass uid, searchString and other optional parameters as per requirement.
    """
    try:
        schema = Schema(getSearchResultsSchema(), ignore_extra_keys=True)
        validation(schema, **args)
        response = getSearchResultsApi(**args)
        return response
    except Exception as error:
        return error
