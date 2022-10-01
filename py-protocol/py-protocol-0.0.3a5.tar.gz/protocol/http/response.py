import typing as t
import socket
import ssl
from ._http_code import HTTPCode
from ._http_header import T_Element
from ._http_header import T_HTTPHeader
from ._http_ver import HTTPVersion
from ._http_default import EMPTY_STRING
from ._http_default import DefaultHTTPHeader as DF_HTTPHeaders

T_HTTPCODE = t.Optional[
    HTTPCode.ClientErrorResponses | 
    HTTPCode.InfomationResponses | 
    HTTPCode.RedirectionResponses | 
    HTTPCode.ServerErrorResponses |
    HTTPCode.SuccessfullResponses
]

T_HTTPVERSION = t.TypeVar('T_HTTPVERSION', bound=str)

class HEADERSNAME:
    __sercure__ = lambda x : x
    ACCEPT = __sercure__("Accept")
    ACCEPT_CH = __sercure__("Accept-CH")
    ACCEPT_CH_LIFETIME = __sercure__("Accept-CH-Lifetime")
    ACCEPT_CHARSET = __sercure__("Accept-Charset")
    ACCEPT_ENCODING = __sercure__("Accept-Encoding")
    ACCEPT_LANGUAGE = __sercure__("Accept-Language")
    ACCEPT_PATCH = __sercure__("Accept-Patch")
    ACCEPT_POST = __sercure__("Accept-Post")
    ACCEPT_RANGES = __sercure__("Accept-Ranges")
    ACCESS_CONTROL_ALLOW_CREDENTIALS = __sercure__("Access-Control-Allow-Credentials")
    ACCESS_CONTROL_ALLOW_HEADERS = __sercure__("Access-Control-Allow-Headers")
    ACCESS_CONTROL_ALLOW_METHODS = __sercure__("Access-Control-Allow-Methods")
    ACCESS_CONTROL_ALLOW_ORIGIN = __sercure__("Access-Control-Allow-Origin")
    ACCESS_CONTROL_EXPOSE_HEADERS = __sercure__("Access-Control-Expose-Headers")
    ACCESS_CONTROL_MAX_AGE = __sercure__("Access-Control-Max-Age")
    ACCESS_CONTROL_REQUEST_HEADERS = __sercure__("Access-Control-Request-Headers")
    ACCESS_CONTROL_REQUEST_METHOD = __sercure__("Access-Control-Request-Method")
    AGE = __sercure__("Age")
    ALLOW = __sercure__("Allow")
    ALT_SVC = __sercure__("Alt-Svc")
    AUTHORIZATION = __sercure__("Authorization")
    CACHE_CONTROL = __sercure__("Cache-Control")
    CLEAR_SITE_DATA = __sercure__("Clear-Site-Data")
    CONNECTION = __sercure__("Connection")
    CONTENT_DISPOSITION = __sercure__("Content-Disposition")
    CONTENT_DPR = __sercure__("Content-DPR")
    CONTENT_ENCODING = __sercure__("Content-Encoding")
    CONTENT_LANGUAGE = __sercure__("Content-Language")
    CONTENT_LENGTH = __sercure__("Content-Length")
    CONTENT_LOCATION = __sercure__("Content-Location")
    CONTENT_RANGE = __sercure__("Content-Range")
    CONTENT_SECURITY_POLICY = __sercure__("Content-Security-Policy")
    CONTENT_SECURITY_POLICY_REPORT_ONLY = __sercure__("Content-Security-Policy-Report-Only")
    CONTENT_TYPE = __sercure__("Content-Type")
    COOKIE = __sercure__("Cookie")
    CROSS_ORIGIN_EMBEDDER_POLICY = __sercure__("Cross-Origin-Embedder-Policy")
    CROSS_ORIGIN_OPENER_POLICY = __sercure__("Cross-Origin-Opener-Policy")
    CROSS_ORIGIN_RESOURCE_POLICY = __sercure__("Cross-Origin-Resource-Policy")
    DATE = __sercure__("Date")
    DEVICE_MEMORY = __sercure__("Device-Memory")
    DIGEST = __sercure__("Digest")
    DNT = __sercure__("DNT")
    DOWNLINK = __sercure__("Downlink")
    DPR = __sercure__("DPR")
    EARLY_DATA = __sercure__("Early-Data")
    ECT = __sercure__("ECT")
    ETAG = __sercure__("ETag")
    EXPECT = __sercure__("Expect")
    EXPECT_CT = __sercure__("Expect-CT")
    EXPIRES = __sercure__("Expires")
    FEATURE_POLICY = __sercure__("Feature-Policy")
    FORWARDED = __sercure__("Forwarded")
    FROM = __sercure__("From")
    HOST = __sercure__("Host")
    IF_MATCH = __sercure__("If-Match")
    IF_MODIFIED_SINCE = __sercure__("If-Modified-Since")
    IF_NONE_MATCH = __sercure__("If-None-Match")
    IF_RANGE = __sercure__("If-Range")
    IF_UNMODIFIED_SINCE = __sercure__("If-Unmodified-Since")
    KEEP_ALIVE = __sercure__("Keep-Alive")
    LARGE_ALLOCATION = __sercure__("Large-Allocation")
    LAST_MODIFIED = __sercure__("Last-Modified")
    LINK = __sercure__("Link")
    LOCATION = __sercure__("Location")
    MAX_FORWARDS = __sercure__("Max-Forwards")
    NEL = __sercure__("NEL")
    ORIGIN = __sercure__("Origin")
    PRAGMA = __sercure__("Pragma")
    PROXY_AUTHENTICATE = __sercure__("Proxy-Authenticate")
    PROXY_AUTHORIZATION = __sercure__("Proxy-Authorization")
    RANGE = __sercure__("Range")
    REFERER = __sercure__("Referer")
    REFERRER_POLICY = __sercure__("Referrer-Policy")
    RETRY_AFTER = __sercure__("Retry-After")
    RTT = __sercure__("RTT")
    SAVE_DATA = __sercure__("Save-Data")
    SEC_CH_UA = __sercure__("Sec-CH-UA")
    SEC_CH_UA_ARCH = __sercure__("Sec-CH-UA-Arch")
    SEC_CH_UA_BITNESS = __sercure__("Sec-CH-UA-Bitness")
    SEC_CH_UA_FULL_VERSION = __sercure__("Sec-CH-UA-Full-Version")
    SEC_CH_UA_FULL_VERSION_LIST = __sercure__("Sec-CH-UA-Full-Version-List")
    SEC_CH_UA_MOBILE = __sercure__("Sec-CH-UA-Mobile")
    SEC_CH_UA_MODEL = __sercure__("Sec-CH-UA-Model")
    SEC_CH_UA_PLATFORM = __sercure__("Sec-CH-UA-Platform")
    SEC_CH_UA_PLATFORM_VERSION = __sercure__("Sec-CH-UA-Platform-Version")
    SEC_FETCH_DEST = __sercure__("Sec-Fetch-Dest")
    SEC_FETCH_MODE = __sercure__("Sec-Fetch-Mode")
    SEC_FETCH_SITE = __sercure__("Sec-Fetch-Site")
    SEC_FETCH_USER = __sercure__("Sec-Fetch-User")
    SEC_GPC    = __sercure__("Sec-GPC")
    SEC_WEBSOCKET_ACCEPT = __sercure__("Sec-WebSocket-Accept")
    SERVER = __sercure__("Server")
    SERVER_TIMING = __sercure__("Server-Timing")
    SERVICE_WORKER_NAVIGATION_PRELOAD = __sercure__("Service-Worker-Navigation-Preload")
    SET_COOKIE = __sercure__("Set-Cookie")
    SOURCEMAP = __sercure__("SourceMap")
    STRICT_TRANSPORT_SECURITY = __sercure__("Strict-Transport-Security")
    TE = __sercure__("TE")
    TIMING_ALLOW_ORIGIN = __sercure__("Timing-Allow-Origin")
    TK = __sercure__("TK")
    TRAILER = __sercure__("Trailer")
    TRANSFER_ENCODING = __sercure__("Transfer-Encoding")
    UPGRADE_INSECURE_REQUESTS = __sercure__("Upgrade-Insecure-Requests")
    USER_AGENT = __sercure__("User-Agent")
    VARY = __sercure__("Vary")
    VIA = __sercure__("Via")
    VIEWPORT_WIDTH = __sercure__("Viewport-Width")
    WANT_DIGEST = __sercure__("Want-Digest")
    WARNING = __sercure__("Warning")
    WIDTH = __sercure__("Width")
    WWW_AUTHENTICATE = __sercure__("WWW-Authenticate")
    X_CONTENT_TYPE_OPTIONS = __sercure__("X-Content-Type-Options")
    X_DNS_PREFETCH_CONTROL = __sercure__("X-DNS-Prefetch-Control")
    X_FORWARDED_FOR = __sercure__("X-Forwarded-For")
    X_FORWARDED_HOST = __sercure__("X-Forwarded-Host")
    X_FORWARDED_PROTO = __sercure__("X-Forwarded-Proto")
    X_FRAME_OPTIONS = __sercure__("X-Frame-Options")
    X_XSS_PROTECTION = __sercure__("X-XSS-Protection")

class HTTPResponse:
    FORMAT_RESPONSES = '{VERSION} {STATUS}\r\n{HEADER}\r\n{CONTENT}'
    FORMAT_RESPONSES_NO_CONTENT = '{VERSION} {STATUS}\r\n{HEADER}'
    FORMAT_RESPONSES_NO_CONTENT_HEADER = '{VERSION} {STATUS}'
    FORMAT_RESPONSES_NO_HEADER = '{VERSION} {STATUS}\r\n{CONTENT}'
    def __init__(
            self,
            version : T_HTTPVERSION = HTTPVersion.HTTP1_1,
            code : T_HTTPCODE = HTTPCode.SuccessfullResponses.OK,
            headers : T_HTTPHeader = T_HTTPHeader(),
            content : t.Optional[str | bytes] = None
            ) -> None:
        self.__cd__ = code
        self.__ver__ = version
        self.__hd__ = headers
        if type(content) is bytes:
            self.__ct__ = content.decode()
        elif content is None:
            self.__ct__ = ""
        else:
            self.__ct__ = content
    
    def __str__(self) -> str:
        if self.__ct__ and self.__hd__:
            return HTTPResponse.FORMAT_RESPONSES.format(
                VERSION = self.__ver__, 
                STATUS=self.__cd__, 
                HEADER = self.__hd__,
                CONTENT = self.__ct__)
        elif self.__ct__:
            return HTTPResponse.FORMAT_RESPONSES_NO_HEADER.format(
                VERSION = self.__ver__, 
                STATUS=self.__cd__, 
                CONTENT = self.__ct__
            )
        elif self.__hd__:
            return HTTPResponse.FORMAT_RESPONSES_NO_CONTENT.format(
                VERSION = self.__ver__, 
                STATUS=self.__cd__, 
                HEADER = self.__hd__,)
        else:
            return HTTPResponse.FORMAT_RESPONSES_NO_CONTENT_HEADER.format(
                VERSION = self.__ver__, 
                STATUS=self.__cd__)

    @property
    def code(self) -> str:
        return self.__cd__
    @code.setter
    def code(self, _vl) -> None:
        self.__cd__ = _vl
    
    @property
    def version(self) -> str:
        return self.__ver__
    @version.setter
    def version(self, _v : T_HTTPVERSION) -> None:
        self.__ver__ = _v
    
    @property
    def headers(self) -> T_HTTPHeader:
        return self.__hd__
    @headers.setter
    def headers(self, _v: T_HTTPHeader) -> None:
        self.__hd__ = _v
    def addHeader(self, _n : str | bytes, _v : str|bytes)-> None:
        self.__hd__.changeInfo(_n, _v)


    @property
    def content(self) -> str:
        return self.__ct__
    @content.setter
    def content(self, _v) -> None:
        self.__ct__ = _v

    def get(
            self,
            _sock : t.Optional[socket.socket|ssl.SSLSocket] = None,
            _content: t.Optional[str | bytes] = None
        ) -> bool:
        try:
            def _send_(
                _s : t.Optional[socket.socket | ssl.SSLSocket] = None, 
                _responseInfo: t.Optional[str|bytes] = None) -> None:
                if _s:
                    if _responseInfo:
                        if type(_responseInfo) is str:
                            _responseInfo = _responseInfo.encode()
                        _s.send(_responseInfo)
                    else:
                        raise
                else:
                    raise
            
            if _content:
                if type(_content) is bytes:
                    _content = _content.decode()
                self.__ct__ = _content

            if self.__ct__:
                self.__hd__.content_length = len(self.__ct__)
            else:
                self.__hd__.content_length = 0

            if _sock:
                _send_(_sock, self.__str__())
            else:
                return True
        except:
            return False