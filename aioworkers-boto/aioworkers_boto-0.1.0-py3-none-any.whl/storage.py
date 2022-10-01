from typing import Any

from aioworkers.core.formatter import FormattedEntity
from aioworkers.storage.base import AbstractStorage

from aioworkers_boto.core import Connector


class Storage(AbstractStorage, FormattedEntity, Connector):
    _SEP = "/"

    def __init__(self, *args, **kwargs):
        kwargs["service_name"] = "s3"
        self._path = self._prepare_path(kwargs.get("path", ""))
        self._bucket = kwargs.get("bucket", "")
        super().__init__(*args, **kwargs)

    def _prepare_path(self, path: str) -> str:
        if path and not path.endswith(self._SEP):
            path += self._SEP
        return path

    def set_config(self, config) -> None:
        super().set_config(config)
        self._path = self._prepare_path(self.config.get("path", self._path))
        self._bucket = self.config.get("bucket", self._bucket)

    def raw_key(self, key: str) -> str:
        if ".." in key:
            raise ValueError("Access denied: %s" % key)
        elif key.startswith(self._SEP):
            key = key.lstrip(self._SEP)
        return self._path + key

    async def get(self, key: str, *, bucket: str = "") -> Any:
        kwargs = {"Key": self.raw_key(key)}
        bucket = bucket or self._bucket
        if bucket:
            kwargs["Bucket"] = bucket
        else:
            raise RuntimeError("Not allowed empty bucket")
        response = await self.client.get_object(**kwargs)
        async with response["Body"] as stream:
            return self.decode(await stream.read())

    async def set(self, key: str, value: Any, *, bucket: str = ""):
        kwargs = {"Key": self.raw_key(key)}
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
