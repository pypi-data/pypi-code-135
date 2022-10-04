from enum import Enum

from ns.errors import Error


class ErrorCodes(str, Enum):
    UNKNOWN_SERVICE = 'UNKNOWN_SERVICE'
    UNKNOWN_SERVICE_METHOD = 'UNKNOWN_SERVICE_METHOD'
    NOT_A_METHOD = 'NOT_A_METHOD'
    INVALID_ARGUMENTS = 'INVALID_ARGUMENTS'

    VALIDATION_ERROR = 'VALIDATION_ERROR'
    UNKNOWN_ERROR = 'UNKNOWN_ERROR'


class AutoapiError(Error[ErrorCodes]):
    """
    Ошибки API
    """
