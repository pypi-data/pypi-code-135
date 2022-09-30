import asyncio
import logging
import socket
from typing import Any

from cashews.backends.interface import CacheBackendInteractionException

try:
    from redis.asyncio import Redis as _Redis
    from redis.exceptions import RedisError as RedisConnectionError
except ImportError:
    from aioredis import Redis as _Redis
    from aioredis import RedisError as RedisConnectionError


logger = logging.getLogger(__name__)


class Redis(_Redis):
    async def execute_command(self, command, *args: Any, **kwargs: Any):
        try:
            return await super().execute_command(command, *args, **kwargs)
        except (RedisConnectionError, socket.gaierror, OSError, asyncio.TimeoutError) as exp:
            raise CacheBackendInteractionException() from exp


class SafeRedis(_Redis):
    async def execute_command(self, command, *args: Any, **kwargs: Any):
        try:
            return await super().execute_command(command, *args, **kwargs)
        except (RedisConnectionError, socket.gaierror, OSError, asyncio.TimeoutError) as exp:
            if command.lower() == "ping":
                raise CacheBackendInteractionException() from exp
            logger.error("redis: can not execute command: %s", command, exc_info=True)
            if command.lower() in ["unlink", "del", "memory", "ttl"]:
                return 0
            if command.lower() == "scan":
                return [0, []]
            return None

    async def initialize(self):
        try:
            return await super().initialize()
        except (RedisConnectionError, socket.gaierror, OSError, asyncio.TimeoutError):
            logger.error("redis: can not initialize cache", exc_info=True)
            return self

    __aenter__ = initialize
