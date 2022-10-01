# KnownException
class OpenApiServiceException(Exception):
    def __init__(self, returnReasonCode, returnAuthMsg, errMsg, **kwargs):
        self.errMsg = errMsg
        self.returnReasonCode = returnReasonCode
        self.returnAuthMsg = returnAuthMsg

    def __str__(self):
        return f"{self.errMsg} [{self.returnReasonCode}] {self.returnAuthMsg}"


# Wrong Request
class LocalDataException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f"check, {self.msg}"


# LocalData Base Exception
class LocalDataUnknownException(Exception):
    def __init__(self, response):
        self.response = response

    def __str__(self):
        request = self.response.request_info.dict()
        response = {k: v for k, v in self.response.dict().items() if k != "request_info"}
        return f"unknown exception, request: {request}, response: {response}"


# KnownException
class LocalDataResponseException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return f"server sent error [{self.code}] {self.message}"
