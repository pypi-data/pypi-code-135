"""
TODO:
 - dump / load
 - rocksns (namespace version?)
 - tests: shelve, zarr, orjson serde
"""

from collections.abc import MutableMapping
from collections import deque
from typing import (
    Optional, Literal, Union, Any,
    List, NamedTuple, Dict,
    Iterator, Tuple, Callable,
)
from functools import partialmethod
from itertools import count
import struct
from warnings import warn
from copy import copy

import rocksdb

def iterlen(it):
    # from https://stackoverflow.com/a/15112059/955854
    counter = count()
    deque(zip(it, counter), maxlen=0)
    return next(counter)

# from https://github.com/benjaminp/six/blob/master/six.py#L650
int2byte = struct.Struct(">B").pack

def inc_last_byte(buf: bytes) -> bytes:
    final = buf[-1]
    if final == 255:
        return buf + b'\x00'
    return buf[:-1] + int2byte(buf[-1] + 1)

REQUIRED = object()
DROP = object()
FIRST = 0
LAST = -1

class ExistsResult(NamedTuple):
    exists: bool
    value: Optional[bytes]

class RocksMap(MutableMapping):
    # defaults from https://python-rocksdb.readthedocs.io/en/latest/api/options.html#options-object
    DEFAULTS = {
        "create_if_missing": False,
        "error_if_exists": False,
        "paranoid_checks": True,
        "write_buffer_size": 4_194_304,
        "max_open_files": 5_000,
        "compression": rocksdb.CompressionType.snappy_compression,
        "num_levels": 7,
        "use_fsync": False,
        "db_log_dir": "",
        "wal_dir": "",
        "disable_auto_compactions": False,
    }
    def __init__(
        self,
        path: str,
        prefix: bytes=b"",
        #snapshot: Optional[rocksdb.Snapshot]=None,
        snapshot=None,
        read_only=False,
        **opts,
    ):
        self.path = path
        opt_values = RocksMap.DEFAULTS.copy()
        opt_values.update(opts)
        self.opts = rocksdb.Options(**opt_values)
        self.db = rocksdb.DB(path, opts=self.opts, read_only=read_only)
        self.prefix = prefix
        self._snapshot = snapshot

    def __repr__(self):
        cls = type(self).__name__
        return f"<{cls}({self.path!r})>"

    def prefixed(self, prefix: bytes):
        new_map = copy(self)
        new_map.prefix = self.prefix + prefix
        return new_map

    def snapshot(self):
        if self._snapshot is not None:
            return self
        new_map = copy(self)
        new_map._snapshot = self.db.snapshot()
        return new_map

    def _ensure_encoded(self, s: Union[str, bytes]) -> bytes:
        if isinstance(s, str):
            result = s.encode()
        else:
            result = s
        if self.prefix:
            result = self.prefix + result
        return result

    def put(
        self,
        key: Union[bytes, str],
        value: bytes,
        sync: bool=False,
        disable_wal: bool=False,
    ):
        self.db.put(
            self._ensure_encoded(key),
            value,
            sync,
            disable_wal,
        )
    __setitem__ = put

    def delete(
        self,
        key: Union[bytes, str],
        sync: bool=False,
        disable_wal: bool=False,
    ):
        self.db.delete(
            self._ensure_encoded(key),
            sync,
            disable_wal,
        )
    __delitem__ = delete

    def merge(
        self,
        key: Union[bytes, str],
        value: bytes,
        sync: bool=False,
        disable_wal: bool=False,
    ):
        self.db.merge(
            self._ensure_encoded(key),
            value,
            sync,
            disable_wal,
        )

    def get(
        self,
        key: Union[bytes, str],
        default: Union[Literal[REQUIRED, None], bytes]=None, 
        verify_checksums: bool=False,
        fill_cache: bool=True,
        read_tier: Literal["all", "cache"]="all",
    ) -> Optional[bytes]:
        result = self.db.get(
            self._ensure_encoded(key),
            verify_checksums=verify_checksums,
            fill_cache=fill_cache,
            #snapshot=self._snapshot,
            read_tier=read_tier,
        )
        if result is None:
            if default is REQUIRED:
                raise KeyError(f"Key {key} not present in db")
            return default
        return result

    def multi_get(
        self,
        keys: List[Union[bytes, str]],
        default: Union[Literal[DROP, REQUIRED, None], bytes]=DROP,
        verify_checksums: bool=False,
        fill_cache: bool=True,
        read_tier: Literal["all", "cache"]="all",
    ) -> Dict[bytes, Optional[bytes]]:
        req_keys = [self._ensure_encoded(k) for k in keys]
        result = self.db.multi_get(
            req_keys,
            verify_checksums=verify_checksums,
            fill_cache=fill_cache,
            snapshot=self._snapshot,
            read_tier=read_tier,
        )
        if default is REQUIRED:
            missing = set(req_keys) - set(result.keys())
            if missing:
                raise KeyError(f"Keys {missing} not present in db")
        final_result = {}
        for orig_key, req_key in zip(keys, req_keys):
            if req_key in result:
                final_result[orig_key] = req_key
            elif default is not DROP:
                final_result[orig_key] = default
        return final_result

    def __getitem__(
        self,
        key_or_keys: Union[bytes, str, List[Union[bytes, str]]],
    ) -> Union[bytes, Dict[bytes, Optional[bytes]]]:
        if isinstance(key_or_keys, (str, bytes)):
            return self.get(key_or_keys, default=REQUIRED)
        return self.multi_get(key_or_keys, default=REQUIRED)

    def key_may_exist(
        self,
        key: Union[bytes, str],
        fetch: bool=False,
        verify_checksums: bool=False,
        fill_cache: bool=True,
        read_tier: Literal["all", "cache"]="all",
    ) -> ExistsResult:
        return ExistsResult(*self.db.key_may_exist(
            self._ensure_encoded(key),
            fetch=fetch,
            verify_checksums=verify_checksums,
            fill_cache=fill_cache,
            snapshot=self._snapshot,
            read_tier=read_tier,
        ))

    def __contains__(self, key: Union[bytes, str]) -> bool:
        return self.key_may_exist(key).exists

    def close(self):
        self.db.close()
    __del__ = close

    def __len__(self):
        return iterlen(self.keys())

    def _iterator(
        self,
        kind: Literal["keys", "values", "items"],
        seek: Union[Literal[FIRST, LAST], str, bytes]=FIRST,
        verify_checksums: bool=False,
        fill_cache: bool=True,
        read_tier: Literal["all", "cache"]="all",
    ): # -> rocksdb.BaseIterator:
        method = getattr(self.db, f"iter{kind}")
        it = method(
            verify_checksums=verify_checksums,
            fill_cache=fill_cache,
            snapshot=self._snapshot,
            read_tier=read_tier,
        )
        if self.prefix:
            if seek == FIRST:
                it.seek(self.prefix)
            elif seek == LAST:
                it.seek(inc_last_byte(self.prefix))
            else:
                it.seek(self._ensure_encode(seek))
        else:
            if seek == FIRST:
                it.seek_to_first()
            elif seek == LAST:
                it.seek_to_last()
            else:
                it.seek(seek)
        return it

    def keys(
        self,
        seek: Union[Literal[FIRST, LAST], str, bytes]=FIRST,
        verify_checksums: bool=False,
        fill_cache: bool=True,
        read_tier: Literal["all", "cache"]="all",
    ) -> Iterator[bytes]:
        it = self._iterator("keys", seek, 
            verify_checksums=verify_checksums,
            fill_cache=fill_cache,
            read_tier=read_tier,
        )
        if self.prefix:
            for key in it:
                if not key.startswith(self.prefix):
                    break
                yield key
        else:
            yield from it
    __iter__ = keys

    def items(
        self,
        seek: Union[Literal[FIRST, LAST], str, bytes]=FIRST,
        verify_checksums: bool=False,
        fill_cache: bool=True,
        read_tier: Literal["all", "cache"]="all",
    ) -> Iterator[Tuple[bytes, bytes]]:
        it = self._iterator("items", seek, 
            verify_checksums=verify_checksums,
            fill_cache=fill_cache,
            read_tier=read_tier,
        )
        if self.prefix:
            for key, val in it:
                if not key.startswith(self.prefix):
                    break
                yield key, val
        else:
            yield from it

    def values(
        self,
        seek: Union[Literal[FIRST, LAST], str, bytes]=FIRST,
        verify_checksums: bool=False,
        fill_cache: bool=True,
        read_tier: Literal["all", "cache"]="all",
    ) -> Iterator[bytes]:
        if self.prefix:
            it = self._iterator("items", seek, 
                verify_checksums=verify_checksums,
                fill_cache=fill_cache,
                read_tier=read_tier,
            )
            for key, val in it:
                if not key.startswith(self.prefix):
                    break
                yield val
        else:
            it = self._iterator("values", seek, 
                verify_checksums=verify_checksums,
                fill_cache=fill_cache,
                read_tier=read_tier,
            )
            yield from it

class BufferedRocksMap(RocksMap):
    def __init__(self, *args, autoflush: Optional[int]=None, **kwargs):
        # auto-flush buffer size?
        super().__init__(*args, **kwargs)
        self.buffer = rocksdb.WriteBatch()
        self.autoflush = autoflush

    def flush(self, sync=False, disable_wal=False):
        self.db.write(
            self.buffer,
            sync=sync,
            disable_wal=disable_wal,
        )
        self.buffer.clear()

    def put(
        self,
        key: Union[bytes, str],
        value: bytes,
        sync: bool=False,
        disable_wal: bool=False,
        flush: Optional[bool]=None,
    ):
        self.buffer.put(self._ensure_encoded(key), value)
        if flush:
            self.flush()
        elif flush is None and self.autoflush is not None:
            if self.buffer.count() >= self.autoflush:
                self.flush(sync=sync, disable_wal=disable_wal)
    __setitem__ = put

    def delete(
        self,
        key: Union[bytes, str],
        sync: bool=False,
        disable_wal: bool=False,
        flush: Optional[bool]=None,
    ):
        self.buffer.delete(self._ensure_encoded(key))
        if flush:
            self.flush()
        elif flush is None and self.autoflush is not None:
            if self.buffer.count() >= self.autoflush:
                self.flush(sync=sync, disable_wal=disable_wal)
    __delitem__ = delete

    def merge(
        self,
        key: Union[bytes, str],
        value: bytes,
        sync: bool=False,
        disable_wal: bool=False,
        flush: Optional[bool]=None,
    ):
        self.buffer.merge(self._ensure_encoded(key), value)
        if flush:
            self.flush()
        elif flush is None and self.autoflush is not None:
            if self.buffer.count() >= self.autoflush:
                self.flush(sync=sync, disable_wal=disable_wal)

    # ?? don't allow iter if not flushed ??

    def close(self):
        self.flush()
        super().close()
    __del__ = close

    def _iterator(self, *args, **kwargs): # -> rocksdb.BaseIterator:
        if self.buffer.count():
            warn("Iterating on unflushed buffer", RuntimeWarning)
        return super()._iterator(*args, **kwargs)

class SerdeRocksMap(RocksMap):
    def __init__(self, path: str,
        dump: Callable[[Any], bytes],
        load: Callable[[bytes], Any],
        *args, **kwargs,
    ):
        super().__init__(path, *args, **kwargs)
        self.dump = dump
        self.load = load

    def merge(
        self,
        key: Union[bytes, str],
        value: bytes,
        **kwargs,
    ):
        raise NotImplementedError("Cannot merge and serialize")

    def get(
        self,
        key: Union[bytes, str],
        default: Any=None,
        **kwargs,
    ) -> Any:
        try:
            result = super().get(
                key,
                default=REQUIRED,
                **kwargs,
            )
        except KeyError:
            if default is REQUIRED:
                raise
            return default
        else:
            return self.load(result)

    def multi_get(
        self,
        keys: List[Union[bytes, str]],
        default: Any=DROP, 
        **kwargs,
    ) -> Dict[bytes, Any]:
        super_default = REQUIRED if default is REQUIRED else DROP
        result = super().multi_get(keys, default=super_default)
        loaded_result = {k: self.load(v) for k, v in result.items()}
        if default is not DROP:
            missing = set(keys) - set(result.keys())
            for key in missing:
                loaded_result[key] = default
        return loaded_result

    def __getitem__(
        self,
        key_or_keys: Union[bytes, str, List[Union[bytes, str]]],
    ) -> Any:
        if isinstance(key_or_keys, (str, bytes)):
            return self.get(key_or_keys, default=REQUIRED)
        return self.multi_get(key_or_keys, default=REQUIRED)

    def put(
        self,
        key: Union[bytes, str],
        value: Any,
        **kwargs,
    ):
        dump_value = self.dump(value)
        super().put(key, dump_value, **kwargs)
    __setitem__ = put

    def items(self, *args, **kwargs) -> Iterator[Tuple[bytes, Any]]:
        it = super().items(*args, **kwargs)
        for k, v in it:
            v_loaded = self.load(v)
            yield k, v

    def values(self, *args, **kwargs) -> Iterator[Tuple[bytes, Any]]:
        it = super().values(*args, **kwargs)
        yield from map(self.load, it)

class ProxiedNamespace:
    def __init__(self, mapping: MutableMapping):
        self._mapping = mapping

    def __dir__(self):
        yield from super().__dir__()
        # !! bytes keys would yield bytes ... ?
        # ? need an ensure str
        yield from self._mapping

    def __getattr__(self, attr):
        try:
            return self._mapping[attr]
        except KeyError as e:
            raise AttributeError(f"No attribute {attr}") from e

    def __setattr__(self, attr, value):
        self._mapping[attr] = value

    def __len__(self):
        return len(self._mapping)
