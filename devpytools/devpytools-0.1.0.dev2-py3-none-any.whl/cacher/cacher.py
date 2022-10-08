import inspect
from os import PathLike
import sys
from typing import Any, Callable, Optional, Dict, OrderedDict, TypeVar, Union, cast, overload
from functools import wraps

from .general import _NoValue
from .cache_provider import CacheProvider, FileCacheProvider, InMemoryCacheProvider

if sys.version_info < (3, 7):
    from typing_extensions import Protocol
else:
    from typing import Protocol


class UniqueKeyTypeProto(Protocol):
    def __call__(self, *args: Any, **kwargs: Any) -> str:
        ...


UniqueKeyType = Union[Callable[[OrderedDict[str, Any]], str], UniqueKeyTypeProto]

FuncType = TypeVar('FuncType', bound=Callable[..., Any])

CACHER_MAP: Dict[Optional[str], "Cacher"] = {}


class Cacher:
    def __init__(self, *, name: Optional[str] = None, tmpDirPath: Optional[Union[str, PathLike]] = None,
                 isExpired: Optional[Callable[[int, Any], bool]] = None, isLocal=False,
                 uniqueKey: Optional[UniqueKeyType] = None, isEnable: bool = True,
                 cacheProvider: Optional[CacheProvider] = None,
                 isSavable: Optional[Callable[[Any], bool]] = lambda x: bool(x),
                 version=1,
                 **kwargs) -> None:
        if not isLocal:
            if CACHER_MAP.get(name):
                raise ValueError('name should be unique across process')
            CACHER_MAP[name] = self
        self.name = name
        self.tmpDirPath = tmpDirPath
        self.isExpired = isExpired
        self.isLocal = isLocal
        self.isEnable = isEnable
        self.uniqueKey = uniqueKey
        self.isSavable = isSavable
        self.version = str(version)
        self.cacheProvider = cacheProvider or (FileCacheProvider(tmpDirPath=tmpDirPath, isExpired=isExpired)
                                               if tmpDirPath else InMemoryCacheProvider(isExpired=isExpired))

    def _getUniqueKey(self, arguments) -> str:
        res = []
        for k, v in arguments.items():
            if k == 'self':
                continue
            if isinstance(v, (str, int, float)):
                res.append((k, v))
                continue
            try:
                v = tuple(v)
                hash(v)
            except:  # noqa
                res.append((k, "None"))
        return str(hash(tuple(res)))

    @overload
    def cache(self, func: FuncType, *, tmpDirPath: Optional[Union[str, PathLike]] = None,
              isExpired: Optional[Callable[[int, Any], bool]] = None,
              uniqueKey: Optional[UniqueKeyType] = None, isEnable: bool = True,
              cacheProvider: Optional[CacheProvider] = None,
              isSavable: Optional[Callable[[Any], bool]] = None,) -> FuncType:
        ...

    @overload
    def cache(self, func=None, *, tmpDirPath: Optional[Union[str, PathLike]] = None,
              isExpired: Optional[Callable[[int, Any], bool]] = None,
              uniqueKey: Optional[UniqueKeyType] = None, isEnable: bool = True,
              cacheProvider: Optional[CacheProvider] = None,
              isSavable: Optional[Callable[[Any], bool]] = None,) -> Callable[[FuncType], FuncType]:
        ...

    def cache(self, func: Optional[FuncType] = None, *, tmpDirPath: Optional[Union[str, PathLike]] = None,
              isExpired: Optional[Callable[[int, Any], bool]] = None,
              uniqueKey: Optional[UniqueKeyType] = None, isEnable: bool = True,
              cacheProvider: Optional[CacheProvider] = None,
              isSavable: Optional[Callable[[Any], bool]] = None,):
        if not func:
            signature = inspect.signature(self.cache)
            kwargs = {k: v for k, v in locals().items() if k in signature.parameters}
            newself = Cacher(**{**self.__dict__, **kwargs, 'isLocal': True})

            def dec(func):
                return self._getDecorated(func, newself)
            return dec
        return self._getDecorated(func, self)

    @staticmethod
    def _getDecorated(func: FuncType, self: 'Cacher') -> FuncType:
        if not self.isEnable:
            return func
        signature = inspect.signature(func)

        @wraps(func)
        def decorated(*args, **kwargs):
            kw = signature.bind(*args, **kwargs)
            if self.uniqueKey:
                hsh = self.uniqueKey(kw.arguments)
            else:
                hsh = self._getUniqueKey(kw.arguments)
            res = self.cacheProvider.getData(hsh, self.version, func, kw.arguments)
            if res is not _NoValue:
                return res
            res = func(*args, **kwargs)
            if not self.isSavable or self.isSavable(res):
                self.cacheProvider.setData(hsh, self.version, func, res, kw.arguments)
            return res
        return cast(FuncType, decorated)



CACHER_MAP[None] = Cacher()


def getCacher(name: Optional[str] = None):
    return CACHER_MAP.get(name, CACHER_MAP[None])
