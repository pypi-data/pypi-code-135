from datetime import timedelta

from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject
from dropland.util import default_value, invoke_async
from pytimeparse.timeparse import timeparse

from .engine import EngineConfig, RedisStorageBackend
from .session import SessionManager


class RedisStorage(containers.DeclarativeContainer):
    __self__ = providers.Self()
    engine_factory = providers.Singleton(RedisStorageBackend)
    manager = providers.Singleton(SessionManager, engine_factory)
    default_ttl = providers.Object(timedelta(seconds=timeparse('1 min')))

    def _create_engine(self, *args, **kwargs):
        return self.engine_factory().create_engine(*args, **kwargs)

    async def _init_async_session(self):
        async with self.manager().init_async_engines():
            yield self.manager()

    create_engine = providers.Factory(_create_engine, __self__)
    session_context = providers.Resource(_init_async_session, __self__)
    get_session = providers.Factory(manager.provided.get_session.call())

    wiring_config = containers.WiringConfiguration(
        modules=['.model', __name__]
    )


class SingleRedisStorage(RedisStorage):
    __self__ = providers.Self()
    config = providers.Configuration()
    # noinspection PyArgumentList
    default_ttl = providers.Object(timedelta(
        seconds=timeparse(config.get('default_cache_ttl', required=False) or '1 min')))

    def _create_engine(self):
        if isinstance(self.config.engine_config(), EngineConfig):
            engine_config = self.config.engine_config()
        else:
            engine_config = EngineConfig(
                url=self.config.engine_config.url(),
                max_connections=self.config.engine_config.
                    max_connections.as_(default_value(int))(default=4),
                pool_timeout_seconds=self.config.engine_config.
                    pool_timeout_seconds.as_(default_value(int))(default=5)
            )
        return RedisStorage._create_engine(self, self.config.name(), engine_config, self.default_ttl())

    create_engine = providers.Factory(_create_engine, __self__)
    session_context = providers.Resource(RedisStorage._init_async_session, __self__)
    get_session = providers.Factory(RedisStorage.get_session, config.name)

    wiring_config = containers.WiringConfiguration(
        modules=['.model', __name__]
    )


class MultipleRedisStorage(RedisStorage):
    __self__ = providers.Self()
    config = providers.Configuration()

    def _create_engine(self, name: str):
        if conf := self.config.get(name):
            if isinstance(conf['engine_config'], EngineConfig):
                engine_config = conf['engine_config']
            else:
                engine_config = EngineConfig(
                    url=conf['engine_config']['url'],
                    max_connections=int(conf['engine_config'].get('max_connections', 4)),
                    pool_timeout_seconds=int(conf['engine_config'].get('pool_timeout_seconds', 5))
                )
            return RedisStorage._create_engine(
                self, name, engine_config,
                timedelta(seconds=timeparse(conf.get('default_cache_ttl', '1 min'))))
        return None

    def _get_session(self, name: str):
        return self.manager().get_session(name)

    create_engine = providers.Factory(_create_engine, __self__)
    session_context = providers.Resource(RedisStorage._init_async_session, __self__)
    get_session = providers.Factory(_get_session, __self__)

    wiring_config = containers.WiringConfiguration(
        modules=['.model', __name__]
    )


default_redis_storage = RedisStorage()


@inject
async def async_resource_session(func, resource: RedisStorage = Provide['<container>'], *args, **kwargs):
    if not isinstance(resource, (RedisStorage, containers.DynamicContainer)):
        return await invoke_async(func)

    try:
        await resource.session_context.init()
        return await invoke_async(func)
    finally:
        await resource.session_context.shutdown()
