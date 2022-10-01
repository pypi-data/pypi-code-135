from .typings import *
import os
import sys
from .exceptions import NoneVariableException
from .exceptions import FoundKeyNameException

class Payload:
    def __init__(
        self,
        header : t.Optional[T_Header] = None,
        separator: t.Optional[T_Separator] = None,
        fd : t.Optional[T_FileReader] = None,
        environ: t.Optional[T_ENV] = None) -> None:
        
        def __load_payload__(
            value_payload : t.Optional[T_RECV], 
            separator : t.Optional[t.Iterable[str]] = ['&', '=']
        ) -> T_Payload:
            if value_payload:
                if separator[0] in value_payload:
                    value_payload = value_payload.split(separator[0])
                else:
                    value_payload=[value_payload]
                target : T_Payload = {}
                for i in value_payload:
                    __tmp__ = i.split(separator)
                    target[__tmp__[0]] = __tmp__[1]
                return target
            return {}
        
        if not header:
            raise NoneVariableException('header is None, check it now!')

        if not fd:
            fd = sys.stdin
        if not environ:
            environ = os.environ
        if not separator:
            separator : T_Separator = ['&', '=']
        
        #Get lenght payload:
        if 'Content-Length' in header:
            self.__length_payload__ : int= header['Content-Length']
        elif "CONTENT_LENGTH" in environ:
            self.__length_payload__ : int= environ["CONTENT_LENGTH"] 
        else:
            self.__length_payload__ : int= 0
        
        #Check against Content-Type. Is it application/x-www-form-urlencoded?
        try:
            self.__payload__ : T_Payload = fd.read(self.__length_payload__).decode()
        except:
            if "QUERY_STRING" in environ:
                self.__payload__: T_Payload= environ['QUERY_STRING']
            else:
                self.__payload__: T_Payload = ""
        self.__payload__ = __load_payload__(self.__payload__, separator=separator)
    
    
    @property
    def pld(self) -> str:
        return self.__payload__
    
    @property
    def len_pld(self) -> int:
        return self.__length_payload__
    
    def getValue(self, name : str) -> str:
        if name in self.__payload__:
            return self.__payload__[name]
        else:
            raise FoundKeyNameException(f'{name}')