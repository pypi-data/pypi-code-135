import os
from pathlib import PurePath
from typing import Any

from aioworkers.core.formatter import FormattedEntity
from aioworkers.storage.base import AbstractStorage
from aioworkers.storage.filesystem import flat

from aioworkers_boto.core import Connector


class Storage(AbstractStorage, FormattedEntity, Connector):
    def __init__(self, *args, **kwargs):
        kwargs["service_name"] = "s3"
        self._path = kwargs.get("path", ".")
        self._bucket = kwargs.get("bucket", "")
        super().__init__(*args, **kwargs)

    def set_config(self, config) -> None:
        super().set_config(config)
        self._path = self.config.get("path", self._path)
        self._bucket = self.config.get("bucket", self._bucket)

    def raw_key(self, *key) -> PurePath:
        path = os.path.join(self._path, *flat(key))
        result = PurePath(os.path.normpath(path))
        result.relative_to(self._path)
        return result

    async def get(self, key: str, *, bucket: str = "") -> Any:
        kwargs = {"Key": str(self.raw_key(key))}
        bucket = bucket or self._bucket
        if bucket:
            kwargs["Bucket"] = bucket
        else:
            raise RuntimeError("Not allowed empty bucket")
        response = await self.client.get_object(**kwargs)
        async with response["Body"] as stream:
            return self.decode(await stream.read())

    async def set(self, key: str, value: Any, *, bucket: str = ""):
        kwargs = {"Key": str(self.raw_key(key))}
        bucket = bucket or self._bucket
        if bucket:
            kwargs["Bucket"] = bucket
        else:
            raise RuntimeError("Not allowed empty bucket")
        if value is None:
            await self.client.delete_object(**kwargs)
        else:
            kwargs["Body"] = self.encode(value)
            await self.client.put_object(**kwargs)
