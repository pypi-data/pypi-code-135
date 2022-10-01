from fastapi.exceptions import HTTPException as FastAPIHTTPException


# KnownException
class OpenApiServiceException(Exception):
    def __init__(self, returnReasonCode, returnAuthMsg, errMsg, **kwargs):
        self.errMsg = errMsg
        self.returnReasonCode = returnReasonCode
        self.returnAuthMsg = returnAuthMsg

    def __str__(self):
        return f"{self.errMsg} [{self.returnReasonCode}] {self.returnAuthMsg}"


# Wrong Request
class DataGoKrException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f"check, {self.msg}"


# DataGoKr Base Exception
class DataGoKrUnknownException(Exception):
    def __init__(self, response):
        self.response = response

    def __str__(self):
        request = self.response.request_info.dict()
        response = {k: v for k, v in self.response.dict().items() if k != "request_info"}
        return f"unknown exception, request: {request}, response: {response}"


# KnownException
class DataGoKrResponseException(Exception):
    def __init__(self, resultCode, resultMsg):
        self.resultCode = resultCode
        self.resultMsg = resultMsg

    def __str__(self):
        return f"server sent error [{self.resultCode}] {self.resultMsg}"


# 00    NORMAL_SERVICE
# Error 아님


# 01	APPLICATION_ERROR	어플리케이션 에러
class ApplicationError(DataGoKrException):
    status_code: int = 500


# 02	DB_ERROR	데이터베이스 에러
class HttpError(DataGoKrException):
    status_code: int = 500


# 03	NODATA_ERROR	데이터없음 에러
# Error 아님


# 04	HTTP_ERROR	HTTP 에러
class HttpError(DataGoKrException):
    status_code: int = 400


# 05	SERVICETIME_OUT	서비스 연결실패 에러
class ServiceTimeOutError(DataGoKrException):
    status_code: int = 408


# 10	INVALID_REQUEST_PARAMETER_ERROR	잘못된 요청 파라메터 에러
class InvalidRequestParametersError(DataGoKrException):
    status_code: int = 400


# 11	NO_MANDATORY_REQUEST_PARAMETERS_ERROR	필수요청 파라메터가 없음
class NoMandatoryRequestParametersError(DataGoKrException):
    status_code: int = 400


# 12	NO_OPENAPI_SERVICE_ERROR	해당 오픈API서비스가 없거나 폐기됨
class LimitedNumberOfServiceRequestExccedsError(DataGoKrException):
    status_code: int = 403


# 20	SERVICE_ACCESS_DENIED_ERROR	서비스 접근거부
class ServiceAccessDeniedError(DataGoKrException):
    status_code: int = 401


# 21	TEMPORARILY_DISABLE_THE_SERVICEKEY_ERROR	일시적으로 사용할 수 없는 서비스 키
class TemporarilyDisableTheServiceKeyError(DataGoKrException):
    status_code: int = 403


# 22	LIMITED_NUMBER_OF_SERVICE_REQUESTS_EXCEEDS_ERROR	서비스 요청제한횟수 초과에러
class LimitedNumberOfServiceRequestExccedsError(DataGoKrException):
    status_code: int = 403


# 30	SERVICE_KEY_IS_NOT_REGISTERED_ERROR	등록되지 않은 서비스키
class ServiceKeyIsNotRegisteredError(DataGoKrException):
    status_code: int = 401


# 31	DEADLINE_HAS_EXPIRED_ERROR	기한만료된 서비스키
class DeadlineHasExpiredError(DataGoKrException):
    status_code: int = 403


# 32	UNREGISTERED_IP_ERROR	등록되지 않은 IP
class UnregisteredIpError(DataGoKrException):
    status_code: int = 401


# 33	UNSIGNED_CALL_ERROR	서명되지 않은 호출
class UnsignedCallError(DataGoKrException):
    status_code: int = 401


# 99	UNKNOWN_ERROR	기타에러
class UnknownError(DataGoKrException):
    status_code: int = 503


DataGoKrError = {
    "00": None,
    "01": ApplicationError,
    "02": HttpError,
    "03": None,
    "04": HttpError,
    "05": ServiceTimeOutError,
    "10": InvalidRequestParametersError,
    "11": NoMandatoryRequestParametersError,
    "12": LimitedNumberOfServiceRequestExccedsError,
    "20": ServiceAccessDeniedError,
    "21": TemporarilyDisableTheServiceKeyError,
    "22": LimitedNumberOfServiceRequestExccedsError,
    "30": ServiceKeyIsNotRegisteredError,
    "31": DeadlineHasExpiredError,
    "32": UnregisteredIpError,
    "33": UnsignedCallError,
    "99": UnknownError,
}
