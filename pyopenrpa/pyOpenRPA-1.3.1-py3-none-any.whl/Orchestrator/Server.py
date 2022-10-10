#     inRequest.OpenRPA = {}
#     inRequest.OpenRPA["AuthToken"] = None
#     inRequest.OpenRPA["Domain"] = None
#     inRequest.OpenRPA["User"] = None

# lResponseDict = {"Headers": {}, "SetCookies": {}, "Body": b"", "StatusCode": None}
# self.OpenRPAResponseDict = lResponseDict

#from http.client import HTTPException
import threading

from pyOpenRPA.Tools import CrossOS


from http import cookies
from . import ServerBC

# объявление import
from fastapi import FastAPI, Form, Request, HTTPException, Depends, Header, Response, Body
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn
import io
from starlette.responses import StreamingResponse
from typing import Union
from pyOpenRPA import __version__

import base64
import uuid
import datetime

# ИНИЦИАЛИЗАЦИЯ FASTAPI!
app = FastAPI(
        title = "pyOpenRPA (ORPA) Orchestrator",
        description = "Сервер оркестратора pyOpenRPA Orchestrator",
        version = __version__,
        openapi_url="/orpa/fastapi/openapi.json", 
        docs_url = "/orpa/fastapi/docs",
        redoc_url = "/orpa/fastapi/redoc",
        swagger_ui_oauth2_redirect_url = "/orpa/fastapi/docs/oauth2-redirect",
    )      

def IdentifyAuthorize(inRequest:Request, inResponse:Response,
    inCookiesStr: Union[str, None] = Header(default=None,alias="Cookie"), 
    inAuthorizationStr: Union[str, None] = Header(default="",alias="Authorization")):
    if __Orchestrator__.GSettingsGet().get("ServerDict", {}).get("AccessUsers", {}).get("FlagCredentialsAsk", False)==True:
        lResult={"Domain": "", "User": ""}
        ######################################
        #Way 1 - try to find AuthToken
        lCookies = cookies.SimpleCookie(inCookiesStr) # inRequest.headers.get("Cookie", "")
        __Orchestrator__.GSettingsGet()
        lHeaderAuthorization = inAuthorizationStr.split(" ")
        if "AuthToken" in lCookies:
            lCookieAuthToken = lCookies.get("AuthToken", "").value
            if lCookieAuthToken:
                #Find AuthToken in GlobalDict
                if lCookieAuthToken in __Orchestrator__.GSettingsGet().get("ServerDict", {}).get("AccessUsers", {}).get("AuthTokensDict", {}):
                    #Auth Token Has Been Founded
                    lResult["Domain"] = __Orchestrator__.GSettingsGet()["ServerDict"]["AccessUsers"]["AuthTokensDict"][lCookieAuthToken]["Domain"]
                    lResult["User"] = __Orchestrator__.GSettingsGet()["ServerDict"]["AccessUsers"]["AuthTokensDict"][lCookieAuthToken]["User"]
                    #Set auth token
                    mOpenRPA={}
                    mOpenRPA["AuthToken"] = lCookieAuthToken
                    mOpenRPA["Domain"] = lResult["Domain"]
                    mOpenRPA["User"] = lResult["User"]
                    mOpenRPA["IsSuperToken"] = __Orchestrator__.GSettingsGet().get("ServerDict", {}).get("AccessUsers", {}).get("AuthTokensDict", {}).get(mOpenRPA["AuthToken"], {}).get("FlagDoNotExpire", False)
                    return lCookieAuthToken
        ######################################
        #Way 2 - try to logon
        if len(lHeaderAuthorization) == 2:
            llHeaderAuthorizationDecodedUserPasswordList = base64.b64decode(lHeaderAuthorization[1]).decode("utf-8").split(
                ":")
            lUser = llHeaderAuthorizationDecodedUserPasswordList[0]
            lPassword = llHeaderAuthorizationDecodedUserPasswordList[1]
            lDomain = ""
            if "\\" in lUser:
                lDomain = lUser.split("\\")[0]
                lUser = lUser.split("\\")[1]
            lLogonBool = __Orchestrator__.OSCredentialsVerify(inUserStr=lUser, inPasswordStr=lPassword, inDomainStr=lDomain)
            #Check result
            if lLogonBool:
                lResult["Domain"] = lDomain
                lResult["User"] = lUser
                #Create token
                lAuthToken=str(uuid.uuid1())
                __Orchestrator__.GSettingsGet()["ServerDict"]["AccessUsers"]["AuthTokensDict"][lAuthToken] = {}
                __Orchestrator__.GSettingsGet()["ServerDict"]["AccessUsers"]["AuthTokensDict"][lAuthToken]["Domain"] = lResult["Domain"]
                __Orchestrator__.GSettingsGet()["ServerDict"]["AccessUsers"]["AuthTokensDict"][lAuthToken]["User"] = lResult["User"]
                __Orchestrator__.GSettingsGet()["ServerDict"]["AccessUsers"]["AuthTokensDict"][lAuthToken]["FlagDoNotExpire"] = False
                __Orchestrator__.GSettingsGet()["ServerDict"]["AccessUsers"]["AuthTokensDict"][lAuthToken]["TokenDatetime"] = datetime.datetime.now()
                #Set-cookie
                inResponse.set_cookie(key="AuthToken",value=lAuthToken)
                mOpenRPA={}
                mOpenRPA["AuthToken"] = lAuthToken
                mOpenRPA["Domain"] = lResult["Domain"]
                mOpenRPA["User"] = lResult["User"]
                mOpenRPA["IsSuperToken"] = __Orchestrator__.GSettingsGet().get("ServerDict", {}).get("AccessUsers", {}).get("AuthTokensDict", {}).get(mOpenRPA["AuthToken"], {}).get("FlagDoNotExpire", False)
                return lAuthToken
                #inRequest.OpenRPASetCookie = {}
                #New engine of server
                #inRequest.OpenRPAResponseDict["SetCookies"]["AuthToken"] = lAuthToken
            else:
                raise HTTPException(status_code=401, detail="Попытка авторизации не прошла успешно (неверная пара логин / пароль)", headers={})
        ######################################
        else:
            raise HTTPException(status_code=401, detail="Попытка авторизации не прошла успешно (неполная пара логин / пароль)", headers={'Content-type':'text/html', 'WWW-Authenticate':'Basic'})
    else: return None # Credentials are not required - return none



lRouteList =[]
for lItem in app.router.routes:
    lRouteList.append(lItem)
app.router.routes=[]
for lItem in lRouteList:
    app.add_api_route(
        path=lItem.path,
        endpoint=lItem.endpoint,
        methods=["GET"],
        dependencies=[Depends(IdentifyAuthorize)],
        tags=["FastAPI"]
    )


from . import ServerSettings  

def BackwardCompatibility(inRequest:Request, inResponse:Response, inBodyStr:str = Body(""), inAuthTokenStr = None):
    lHTTPRequest = ServerBC.HTTPRequestOld(inRequest=inRequest, inResponse=inResponse, inAuthTokenStr=inAuthTokenStr)
    lHTTPRequest.path = inRequest.url.path
    lHTTPRequest.body = inBodyStr
    lHTTPRequest.client_address = [inRequest.client.host]
    threading.current_thread().request = lHTTPRequest
    lResult = lHTTPRequest.do_GET(inBodyStr=inBodyStr)
    if lResult is None:
        lResult = lHTTPRequest.do_POST(inBodyStr=inBodyStr)
    if lHTTPRequest.OpenRPAResponseDict["Headers"]["Content-type"] != None:
        return StreamingResponse(io.BytesIO(lResult), media_type=lHTTPRequest.OpenRPAResponseDict["Headers"]["Content-type"])

#WRAPPERS!
def BackwardCompatibityWrapperAuth(inRequest:Request, inResponse:Response, inBodyStr:str = Body(""),
    inAuthTokenStr:str=Depends(ServerSettings.IdentifyAuthorize)): # Old from v1.3.1 (updated to FastAPI)
    return BackwardCompatibility(inRequest = inRequest, inResponse = inResponse, inBodyStr = inBodyStr, inAuthTokenStr=inAuthTokenStr)
def BackwardCompatibityWrapperNoAuth(inRequest:Request, inResponse:Response, inBodyStr:str = Body("")): # Old from v1.3.1 (updated to FastAPI)
    return BackwardCompatibility(inRequest = inRequest, inResponse = inResponse, inBodyStr = inBodyStr, inAuthTokenStr=None)
def BackwardCompatibityBeginWrapperAuth(inBeginTokenStr, inRequest:Request, inResponse:Response, inBodyStr:str = Body(""),
    inAuthTokenStr:str=Depends(ServerSettings.IdentifyAuthorize)): # Old from v1.3.1 (updated to FastAPI)
    return BackwardCompatibility(inRequest = inRequest, inResponse = inResponse, inBodyStr = inBodyStr, inAuthTokenStr=inAuthTokenStr)
def BackwardCompatibityBeginWrapperNoAuth(inBeginTokenStr, inRequest:Request, inResponse:Response, inBodyStr:str = Body("")): # Old from v1.3.1 (updated to FastAPI)
    return BackwardCompatibility(inRequest = inRequest, inResponse = inResponse, inBodyStr = inBodyStr, inAuthTokenStr=None)



from . import __Orchestrator__
import mimetypes
mimetypes.add_type("font/woff2",".woff2")
mimetypes.add_type("text/javascript",".js")
from typing import Union

def InitFastAPI():
    global app
    lL = __Orchestrator__.OrchestratorLoggerGet()
    __Orchestrator__.GSettingsGet()["ServerDict"]["ServerThread"] = app
    ServerSettings.SettingsUpdate()
    BCURLUpdate()

def BCURLUpdate():
    for lConnectItemDict in __Orchestrator__.GSettingsGet()["ServerDict"]["URLList"]:
        if "BCBool" not in lConnectItemDict:
            if "ResponseFolderPath" in lConnectItemDict:
                app.mount(lConnectItemDict["URL"], 
            StaticFiles(directory=CrossOS.PathStr(lConnectItemDict["ResponseFolderPath"])), 
            name=lConnectItemDict["URL"].replace('/',"_"))
            else:
                if lConnectItemDict.get("MatchType") in ["EqualCase", "Equal","EqualNoParam"]:
                    if lConnectItemDict.get("UACBool",True):
                        app.add_api_route(
                            path=lConnectItemDict["URL"],
                            endpoint=BackwardCompatibityWrapperAuth,
                            response_class=PlainTextResponse,
                            methods=[lConnectItemDict["Method"]],
                            tags=["BackwardCompatibility"]
                        )
                    else:
                        app.add_api_route(
                            path=lConnectItemDict["URL"],
                            endpoint=BackwardCompatibityWrapperNoAuth,
                            response_class=PlainTextResponse,
                            methods=[lConnectItemDict["Method"]],
                            tags=["BackwardCompatibility"]
                        )
                elif lConnectItemDict.get("MatchType") in ["BeginWith", "Contains"]:
                    lURLStr = lConnectItemDict["URL"]
                    if lURLStr[-1]!="/": lURLStr+="/"
                    lURLStr+="{inBeginTokenStr}"
                    if lConnectItemDict.get("UACBool",True):
                        app.add_api_route(
                            path=lURLStr,
                            endpoint=BackwardCompatibityBeginWrapperAuth,
                            response_class=PlainTextResponse,
                            methods=[lConnectItemDict["Method"]],
                            tags=["BackwardCompatibility"]
                        )
                    else:
                        app.add_api_route(
                            path=lURLStr,
                            endpoint=BackwardCompatibityBeginWrapperNoAuth,
                            response_class=PlainTextResponse,
                            methods=[lConnectItemDict["Method"]],
                            tags=["BackwardCompatibility"]
                        )
        lConnectItemDict["BCBool"]=True
                
def InitUvicorn(inHostStr=None, inPortInt=None, inSSLCertPathStr=None, inSSLKeyPathStr=None, inSSLPasswordStr=None):
    if inHostStr is None: inHostStr="0.0.0.0"
    if inPortInt is None: inPortInt=1024
    if inSSLCertPathStr != None: inSSLCertPathStr=CrossOS.PathStr(inSSLCertPathStr)
    if inSSLKeyPathStr != None: inSSLKeyPathStr=CrossOS.PathStr(inSSLKeyPathStr)
    global app
    lL = __Orchestrator__.OrchestratorLoggerGet()
    #uvicorn.run('pyOpenRPA.Orchestrator.Server:app', host='0.0.0.0', port=1024)
    uvicorn.run(app, host=inHostStr, port=inPortInt,ssl_keyfile=inSSLKeyPathStr,ssl_certfile=inSSLCertPathStr,ssl_keyfile_password=inSSLPasswordStr)
    if lL and inSSLKeyPathStr != None: lL.info(f"Сервер инициализирован успешно (с поддержкой SSL):: Слушает URL: {inHostStr}, Слушает порт: {inPortInt}, Путь к файлу сертификата (.pem, base64): {inSSLCertPathStr}")
    if lL and inSSLKeyPathStr == None: lL.info(f"Сервер инициализирован успешно (без поддержки SSL):: Слушает URL: {inHostStr}, Слушает порт: {inPortInt}")

