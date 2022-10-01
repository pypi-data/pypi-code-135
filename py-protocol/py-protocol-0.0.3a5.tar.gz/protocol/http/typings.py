import typing as t
from os import _Environ

T_Version = t.Union[
    str,
    bytes
]
T_URL = t.Union[
    str,
    bytes
]

T_STATUS = t.Union[
    str, 
    bytes
]

T_STATUS_NUM = t.Union[
    str,
    bytes,
    int
]

T_Header = t.Union[
    None,
    t.Iterable[str],
    t.Mapping[str|bytes, str|bytes]
]

T_Separator = t.Union[
    str,
    bytes,
    t.Iterable[str|bytes],
]

T_FileReader = t.Union[
    t.TextIO,
    t.BinaryIO
]

T_RECV = t.Union[
    str,
    bytes,
    t.Iterable[str|bytes]
]

T_ENV = t.TypeVar('T_ENV', bound=_Environ[str])

T_NUM_SERIES = t.Union[
    int, 
    str
]

# For response
T_ResponseValue = t.Union[
    str,
    T_Header,
    bytes
]

#For request:
T_Payload = t.Union[
    str,
    bytes,
    t.Mapping[str|bytes, str|bytes]
]

T_RequestValue = t.Union[
    str,
    T_Header,
    T_Payload
]