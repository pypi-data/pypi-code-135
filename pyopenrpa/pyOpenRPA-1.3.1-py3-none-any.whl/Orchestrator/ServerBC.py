import inspect
from pyOpenRPA.Tools import CrossOS
import urllib.parse # decode URL in string
import os #for path operations
from . import __Orchestrator__
import mimetypes
mimetypes.add_type("font/woff2",".woff2")
mimetypes.add_type("application/javascript",".js")

# объявление import
from fastapi import FastAPI, Form, Request, HTTPException, Depends, Header, Response, Body

gCacheDict = {}


# Tool to merge complex dictionaries
def __ComplexDictMerge2to1__(in1Dict, in2Dict):
    lPathList=None
    if lPathList is None: lPathList = []
    for lKeyStr in in2Dict:
        if lKeyStr in in1Dict:
            if isinstance(in1Dict[lKeyStr], dict) and isinstance(in2Dict[lKeyStr], dict):
                __ComplexDictMerge2to1__(in1Dict[lKeyStr], in2Dict[lKeyStr])
            elif in1Dict[lKeyStr] == in2Dict[lKeyStr]:
                pass  # same leaf value
            else:
                raise Exception('Conflict at %s' % '.'.join(lPathList + [str(lKeyStr)]))
        else:
            in1Dict[lKeyStr] = in2Dict[lKeyStr]
    return in1Dict

# Tool to merge complex dictionaries - no exceptions, just overwrite dict 2 in dict 1
def __ComplexDictMerge2to1Overwrite__(in1Dict, in2Dict):
    """
    Merge in2Dict in in1Dict. In conflict override and get value from dict 2

    :param in1Dict: Source dict. Save the link (structure)
    :param in2Dict: New data dict
    :return: Merged dict 1
    """
    lPathList=None
    if lPathList is None: lPathList = []
    for lKeyStr in in2Dict:
        if lKeyStr in in1Dict:
            if isinstance(in1Dict[lKeyStr], dict) and isinstance(in2Dict[lKeyStr], dict):
                __ComplexDictMerge2to1Overwrite__(in1Dict[lKeyStr], in2Dict[lKeyStr])
            else:
                in1Dict[lKeyStr] = in2Dict[lKeyStr]
        else:
            in1Dict[lKeyStr] = in2Dict[lKeyStr]
    return in1Dict


def AuthenticateBlock(inRequest):
    raise HTTPException(status_code=401, detail="here is the details", headers={'Content-type':'text/html', 'WWW-Authenticate':'Basic'})

#Check access before execute the action
#return bool True - go execute, False - dont execute
def UserAccessCheckBefore(inMethod, inRequest):
    # Help def - Get access flag from dict
    #pdb.set_trace()
    def HelpGetFlag(inAccessRuleItem, inRequest, inGlobalDict, inAuthenticateDict):
        if "FlagAccess" in inAccessRuleItem:
            return inAccessRuleItem["FlagAccess"]
        elif "FlagAccessDefRequestGlobalAuthenticate" in inAccessRuleItem:
            return inAccessRuleItem["FlagAccessDefRequestGlobalAuthenticate"](inRequest, inGlobalDict,
                                                                              inAuthenticateDict)
    ##########################################
    inMethod=inMethod.upper()
    #Prepare result false
    lResult = False
    lAuthToken = inRequest.OpenRPA["AuthToken"]
    #go next if user is identified
    lUserDict = None
    #print(f"lAuthToken: {lAuthToken}")
    if lAuthToken:
        lUserDict = __Orchestrator__.GSettingsGet()["ServerDict"]["AccessUsers"]["AuthTokensDict"][lAuthToken]
    #print(f"lUserDict: {lUserDict}")
    #pdb.set_trace()
    ########################################
    ########################################
    #Check general before rule (without User domain)
    #Check rules
    inRuleMatchURLList = __Orchestrator__.GSettingsGet().get("ServerDict", {}).get("AccessUsers", {}).get("RuleMethodMatchURLBeforeList", [])
    for lAccessRuleItem in inRuleMatchURLList:
        #Go next execution if flag is false
        if not lResult:
            #Check if Method is identical
            if lAccessRuleItem["Method"].upper() == inMethod:
                #check Match type variant: BeginWith
                if lAccessRuleItem["MatchType"].upper() == "BEGINWITH":
                    lURLPath = inRequest.path
                    lURLPath = lURLPath.upper()
                    if lURLPath.startswith(lAccessRuleItem["URL"].upper()):
                        lResult = HelpGetFlag(lAccessRuleItem, inRequest, __Orchestrator__.GSettingsGet(), lUserDict)
                # check Match type variant: Contains
                elif lAccessRuleItem["MatchType"].upper() == "CONTAINS":
                    lURLPath = inRequest.path
                    lURLPath = lURLPath.upper()
                    if lURLPath.contains(lAccessRuleItem["URL"].upper()):
                        lResult = HelpGetFlag(lAccessRuleItem, inRequest, __Orchestrator__.GSettingsGet(), lUserDict)
                # check Match type variant: Equal
                elif lAccessRuleItem["MatchType"].upper() == "EQUAL":
                    if lAccessRuleItem["URL"].upper() == inRequest.path.upper():
                        lResult = HelpGetFlag(lAccessRuleItem, inRequest, __Orchestrator__.GSettingsGet(), lUserDict)
                # check Match type variant: EqualCase
                elif lAccessRuleItem["MatchType"].upper() == "EQUALCASE":
                    if lAccessRuleItem["URL"] == inRequest.path:
                        lResult = HelpGetFlag(lAccessRuleItem, inRequest, __Orchestrator__.GSettingsGet(), lUserDict)
    #########################################
    #########################################
    #Do check if lResult is false
    if not lResult:
        #Check access by User Domain
        #Check rules to find first appicable
        #Check rules
        lMethodMatchURLList = __Orchestrator__.GSettingsGet().get("ServerDict", {}).get("AccessUsers", {}).get("RuleDomainUserDict", {}).get((lUserDict["Domain"].upper(), lUserDict["User"].upper()), {}).get("MethodMatchURLBeforeList", [])
        if len(lMethodMatchURLList) > 0:
            for lAccessRuleItem in lMethodMatchURLList:
                #Go next execution if flag is false
                if not lResult:
                    #Check if Method is identical
                    if lAccessRuleItem["Method"].upper() == inMethod:
                        #check Match type variant: BeginWith
                        if lAccessRuleItem["MatchType"].upper() == "BEGINWITH":
                            lURLPath = inRequest.path
                            lURLPath = lURLPath.upper()
                            if lURLPath.startswith(lAccessRuleItem["URL"].upper()):
                                lResult = HelpGetFlag(lAccessRuleItem, inRequest, __Orchestrator__.GSettingsGet(), lUserDict)
                        #check Match type variant: Contains
                        elif lAccessRuleItem["MatchType"].upper() == "CONTAINS":
                            lURLPath = inRequest.path
                            lURLPath = lURLPath.upper()
                            if lURLPath.contains(lAccessRuleItem["URL"].upper()):
                                lResult = HelpGetFlag(lAccessRuleItem, inRequest, __Orchestrator__.GSettingsGet(), lUserDict)
                        # check Match type variant: Equal
                        elif lAccessRuleItem["MatchType"].upper() == "EQUAL":
                            if lAccessRuleItem["URL"].upper() == inRequest.path.upper():
                                lResult = HelpGetFlag(lAccessRuleItem, inRequest, __Orchestrator__.GSettingsGet(), lUserDict)
                        # check Match type variant: EqualCase
                        elif lAccessRuleItem["MatchType"].upper() == "EQUALCASE":
                            if lAccessRuleItem["URL"] == inRequest.path:
                                lResult = HelpGetFlag(lAccessRuleItem, inRequest, __Orchestrator__.GSettingsGet(), lUserDict)
        else:
            return True
    #####################################
    #####################################
    #Return lResult
    return lResult

class HTTPRequestOld():
    mRequest:Request = None
    mResponse:Response = None
    OpenRPA: dict = {}
    headers={}

    def __init__(self,inRequest,inResponse,inAuthTokenStr):
        self.mRequest = inRequest
        self.mResponse = inResponse
        if inAuthTokenStr != None:
            self.OpenRPA = {}
            self.OpenRPA["IsSuperToken"] = __Orchestrator__.WebUserIsSuperToken(inAuthTokenStr=inAuthTokenStr)
            self.OpenRPA["AuthToken"] = inAuthTokenStr
            self.OpenRPA["Domain"] = __Orchestrator__.WebUserDomainGet(inAuthTokenStr=inAuthTokenStr)
            self.OpenRPA["User"] = __Orchestrator__.WebUserLoginGet(inAuthTokenStr=inAuthTokenStr)
        else: self.OpenRPA = {"IsSuperToken":False, "AuthToken":None, "Domain":None, "User":None}
        self.headers=inRequest.headers

    # Def to check User Role access grants
    def UACClientCheck(self, inRoleKeyList): # Alias
        return self.UserRoleAccessAsk(inRoleKeyList=inRoleKeyList)
    def UserRoleAccessAsk(self, inRoleKeyList):
        lResult = True # Init flag
        lRoleHierarchyDict = self.UserRoleHierarchyGet() # get the Hierarchy
        # Try to get value from key list
        lKeyValue = lRoleHierarchyDict # Init the base
        for lItem in inRoleKeyList:
            if type(lKeyValue) is dict:
                if lItem in lKeyValue: # Has key
                    lKeyValue = lKeyValue[lItem] # Get the value and go to the next loop iteration
                else: # Else branch - true or false
                    if len(lKeyValue)>0: # False - if Dict has some elements
                        lResult = False # Set the False Flag
                    else:
                        lResult = True # Set the True flag
                    break # Stop the loop
            else: # Has element with no detalization - return True
                lResult = True # Set the flag
                break # Close the loop
        return lResult # Return the result

    # Def to get hierarchy of the current user roles
    # if return {} - all is available
    def UserRoleHierarchyGet(self):
        try:
            lDomainUpperStr = self.OpenRPA["Domain"].upper()
            lUserUpperStr = self.OpenRPA["User"].upper()
            return __Orchestrator__.GSettingsGet().get("ServerDict", {}).get("AccessUsers", {}).get("RuleDomainUserDict", {}).get((lDomainUpperStr, lUserUpperStr), {}).get("RoleHierarchyAllowedDict", {})
        except Exception as e:
            return {}
    #Tech def
    #return {"headers":[],"body":"","statuscode":111}
    def URLItemCheckDo(self, inURLItem, inMethod, inOnlyFlagUACBool = False):
        ###############################
        #Tech sub def - do item
        ################################
        def URLItemDo(inURLItem,inRequest,inGlobalDict):
            global gCacheDict
            inResponseDict = inRequest.OpenRPAResponseDict
            inResponseDict["Headers"]["Content-type"]= None
            #Set status code 200
            inResponseDict["StatusCode"] = 200
            #Content-type
            if "ResponseContentType" in inURLItem:
                inResponseDict["Headers"]["Content-type"] = inURLItem["ResponseContentType"]
            #If file path is set
            if "ResponseFilePath" in inURLItem:
                # Check cache
                if inURLItem.get("UseCacheBool",False) == True:
                    if inURLItem["ResponseFilePath"] in gCacheDict:
                        # Write content as utf-8 data
                        inResponseDict["Body"] = gCacheDict[inURLItem["ResponseFilePath"]]
                    else:
                        if os.path.exists(inURLItem["ResponseFilePath"]) and os.path.isfile(inURLItem["ResponseFilePath"]):
                            lFileObject = open(CrossOS.PathStr(inURLItem["ResponseFilePath"]), "rb")
                            # Write content as utf-8 data
                            gCacheDict[inURLItem["ResponseFilePath"]] = lFileObject.read()
                            inResponseDict["Body"] = gCacheDict[inURLItem["ResponseFilePath"]]
                            # Закрыть файловый объект
                            lFileObject.close()
                        else: inResponseDict["Headers"]["Content-type"]= "application/x-empty"; inResponseDict["StatusCode"] = 204 # NOCONTENT
                else:
                    if os.path.exists(inURLItem["ResponseFilePath"]) and os.path.isfile(inURLItem["ResponseFilePath"]):
                        lFileObject = open(CrossOS.PathStr(inURLItem["ResponseFilePath"]), "rb")
                        # Write content as utf-8 data
                        inResponseDict["Body"] = lFileObject.read()
                        # Закрыть файловый объект
                        lFileObject.close()
                    else: inResponseDict["Headers"]["Content-type"]= "application/x-empty"; inResponseDict["StatusCode"] = 204 # NOCONTENT
                # detect MIME type if none
                if inResponseDict["Headers"]["Content-type"] is None:
                    inResponseDict["Headers"]["Content-type"]= mimetypes.guess_type(inURLItem["ResponseFilePath"])[0]
            #If function is set
            if "ResponseDefRequestGlobal" in inURLItem:
                lDef = inURLItem["ResponseDefRequestGlobal"]
                lDefSignature = inspect.signature(lDef)
                if len(lDefSignature.parameters) == 2:
                    inURLItem["ResponseDefRequestGlobal"](inRequest, inGlobalDict)
                elif len(lDefSignature.parameters) == 1:
                    inURLItem["ResponseDefRequestGlobal"](inRequest)
                else:
                    inURLItem["ResponseDefRequestGlobal"]()                
            if "ResponseFolderPath" in inURLItem:
                #lRequestPath = inRequest.path
                lRequestPath = urllib.parse.unquote(inRequest.path)
                if inURLItem["URL"][-1]!="/": inURLItem["URL"]+= "/" # Fix for settings
                lFilePathSecondPart = lRequestPath.replace(inURLItem["URL"],"")
                lFilePathSecondPart = lFilePathSecondPart.split("?")[0]
                lFilePath = CrossOS.PathStr(os.path.join(inURLItem["ResponseFolderPath"],lFilePathSecondPart))
                #print(f"File full path {lFilePath}")
                #Check if file exist
                if os.path.exists(lFilePath) and os.path.isfile(lFilePath):
                    # Check cache
                    if inURLItem.get("UseCacheBool",False) == True:
                        if lFilePath in gCacheDict:
                            # Write content as utf-8 data
                            inResponseDict["Body"] = gCacheDict[lFilePath]
                        else:
                            lFileObject = open(lFilePath, "rb")
                            # Write content as utf-8 data
                            gCacheDict[lFilePath] = lFileObject.read()
                            inResponseDict["Body"] = gCacheDict[lFilePath]
                            # Закрыть файловый объект
                            lFileObject.close()
                    else:
                        lFileObject = open(lFilePath, "rb")
                        # Write content as utf-8 data
                        inResponseDict["Body"] = lFileObject.read()
                        # Закрыть файловый объект
                        lFileObject.close()
                    # detect MIME type if none
                    if inResponseDict["Headers"]["Content-type"] is None:
                        inResponseDict["Headers"]["Content-type"]= mimetypes.guess_type(lFilePath)[0]
                else:
                    inResponseDict["Headers"]["Content-type"]= "application/x-empty"; inResponseDict["StatusCode"] = 204 # NOCONTENT
            # If No content-type
            if inResponseDict["Headers"]["Content-type"] is None:
                inResponseDict["Headers"]["Content-type"]= "application/octet-stream"
        ##############################################
        # UAC Check 
        if inOnlyFlagUACBool == True and inURLItem.get("UACBool",None) in [None, True]:
            return False
        if inURLItem["Method"].upper() == inMethod.upper():
            # check Match type variant: BeginWith
            if inURLItem["MatchType"].upper() == "BEGINWITH":
                lURLPath = urllib.parse.unquote(self.path)
                lURLPath = lURLPath.upper()
                if lURLPath.startswith(inURLItem["URL"].upper()):
                    URLItemDo(inURLItem, self, __Orchestrator__.GSettingsGet())
                    return True
            # check Match type variant: Contains
            elif inURLItem["MatchType"].upper() == "CONTAINS":
                lURLPath = urllib.parse.unquote(self.path)
                lURLPath = lURLPath.upper()
                if lURLPath.contains(inURLItem["URL"].upper()):
                    URLItemDo(inURLItem, self, __Orchestrator__.GSettingsGet())
                    return True
            # check Match type variant: Equal
            elif inURLItem["MatchType"].upper() == "EQUAL":
                if inURLItem["URL"].upper() == urllib.parse.unquote(self.path).upper():
                    URLItemDo(inURLItem, self, __Orchestrator__.GSettingsGet())
                    return True
            # check Match type variant: EqualNoParam
            elif inURLItem["MatchType"].upper() == "EQUALNOPARAM":
                if inURLItem["URL"].upper() == urllib.parse.unquote(self.path).upper().split("?")[0]:
                    URLItemDo(inURLItem, self, __Orchestrator__.GSettingsGet())
                    return True
            # check Match type variant: EqualCase
            elif inURLItem["MatchType"].upper() == "EQUALCASE":
                if inURLItem["URL"] == urllib.parse.unquote(self.path):
                    URLItemDo(inURLItem, self, __Orchestrator__.GSettingsGet())
                    return True
        return False
    #ResponseContentTypeFile
    def SendResponseContentTypeFile(self, inContentType, inFilePath):
        inResponseDict = self.OpenRPAResponseDict
        self.mResponse.status_code = 200
        # Send headers
        self.mResponse.headers["Content-type"]=inContentType
        #Check if var exist
        if hasattr(self, "OpenRPASetCookie"):
            self.mResponse.set_cookie(key='AuthToken',value=self.OpenRPA['AuthToken'])
        lFileObject = open(inFilePath, "rb") 
        # Write content as utf-8 data
        lFileBytes = lFileObject.read()
        #Закрыть файловый объект
        lFileObject.close()
        return lFileBytes
    # ResponseContentTypeFile
    def ResponseDictSend(self):
        inResponseDict = self.OpenRPAResponseDict
        self.mResponse.status_code = inResponseDict["StatusCode"]
        # Send headers
        for lItemKey, lItemValue in inResponseDict["Headers"].items():
            self.mResponse.headers[lItemKey]=lItemValue
       # Send headers: Set-Cookie
        for lItemKey, lItemValue in inResponseDict["SetCookies"].items():
            self.mResponse.set_cookie(key=lItemKey,value=lItemValue)
            self.send_header("Set-Cookie", f"{lItemKey}={lItemValue}")
        return inResponseDict["Body"]

    def do_GET(self, inBodyStr):
        try:
            try:
                self.OpenRPA["DefUserRoleAccessAsk"]=self.UserRoleAccessAsk # Alias for def
                self.OpenRPA["DefUserRoleHierarchyGet"]=self.UserRoleHierarchyGet # Alias for def
            except Exception as e:
                pass
            # Prepare result dict
            lResponseDict = {"Headers": {}, "SetCookies": {}, "Body": b"", "StatusCode": None, "BodyIsText":True}
            self.OpenRPAResponseDict = lResponseDict
            #Check the user access (if flag, UAC)
            ####################################
            lFlagUserAccess = True
            #If need user authentication
            if __Orchestrator__.GSettingsGet().get("ServerDict", {}).get("AccessUsers", {}).get("FlagCredentialsAsk", False):
                if self.OpenRPA["AuthToken"] != None:
                    lFlagUserAccess = UserAccessCheckBefore("GET", self)
            ######################################
            if lFlagUserAccess:
                if CrossOS.IS_WINDOWS_BOOL: lOrchestratorFolder = "\\".join(__file__.split("\\")[:-1])
                if CrossOS.IS_LINUX_BOOL: lOrchestratorFolder = "/".join(__file__.split("/")[:-1])
                ############################
                #New server engine (url from global dict (URLList))
                ############################
                for lURLItem in __Orchestrator__.GSettingsGet()["ServerDict"]["URLList"]:
                    #Check if all condition are applied
                    lFlagURLIsApplied=False
                    lFlagURLIsApplied=self.URLItemCheckDo(lURLItem, "GET")
                    if lFlagURLIsApplied:
                        return  self.ResponseDictSend()
            else:
                raise HTTPException(status_code=403, detail="here is the details", headers={})
        except Exception as e:
            lL = __Orchestrator__.OrchestratorLoggerGet()
            if lL: lL.exception(f"Сервер (do_GET): Неопознанная ошибка сети - см. текст ошибки. Сервер продолжает работу")
    # POST
    def do_POST(self, inBodyStr):
        try:
            lL = __Orchestrator__.OrchestratorLoggerGet()
            try:
                self.OpenRPA["DefUserRoleAccessAsk"]=self.UserRoleAccessAsk # Alias for def
                self.OpenRPA["DefUserRoleHierarchyGet"]=self.UserRoleHierarchyGet # Alias for def
            except Exception as e:
                pass
            # Prepare result dict
            #pdb.set_trace()
            lResponseDict = {"Headers": {}, "SetCookies": {}, "Body": b"", "StatusCode": None, "BodyIsText":True}
            self.OpenRPAResponseDict = lResponseDict
            #Check the user access (if flag)
            ####################################
            lFlagUserAccess = True
            #If need user authentication
            if __Orchestrator__.GSettingsGet().get("ServerDict", {}).get("AccessUsers", {}).get("FlagCredentialsAsk", False):
                if self.OpenRPA["AuthToken"] != None:
                    lFlagUserAccess = UserAccessCheckBefore("POST", self)
            ######################################
            if lFlagUserAccess:
                lOrchestratorFolder = "\\".join(__file__.split("\\")[:-1])
                ############################
                #New server engine (url from global dict (URLList))
                ############################
                for lURLItem in __Orchestrator__.GSettingsGet()["ServerDict"]["URLList"]:
                    #Check if all condition are applied
                    lFlagURLIsApplied=False
                    lFlagURLIsApplied=self.URLItemCheckDo(lURLItem, "POST")
                    if lFlagURLIsApplied:
                        return self.ResponseDictSend()
            else:
                raise HTTPException(status_code=403, detail="here is the details", headers={})
        except Exception as e:
            lL = __Orchestrator__.OrchestratorLoggerGet()
            if lL: lL.exception(f"Сервер, обратная совместимость (do_POST): Неопознанная ошибка сети - см. текст ошибки. Сервер продолжает работу")

