from os import _Environ
from .typings import *
from .payload import Payload
from ._http_header import T_HTTPHeader

class HTTPRequest(Payload):
    def __init__(self, 
            requests: t.Optional[T_RECV],
            fd : t.Optional[T_FileReader] = None, 
            environ : t.Optional[T_ENV] = None,
        ):
        # request converted from bytes to str
        if type(requests) is bytes:
            self.__requests__ : T_RECV= requests.decode()

        self.__requests__ = self.__requests__.split("\r\n")
        #Get method, URL - route, Version
        self.__method__, self.__url__, self.__version__= self.__requests__[0].split(' ')

        #Get header
        self.__header__ = T_HTTPHeader(self.__requests__[1:])

        if self.__method__ in ['POST', 'PUT', "DELETE"] :
            super().__init__(self.__header__, fd=fd, environ=environ)

    @property
    def method(self) -> str:
        return self.__method__
    
    @property
    def url(self) -> str:
        return self.__url__
    
    @property
    def version(self) -> str:
        return self.__version__
    
    @property
    def header(self) -> dict:
        return self.__header__

    @property
    def payload(self) -> dict:
        return super().__payload__