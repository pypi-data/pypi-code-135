from inject import Binder

from ns.di.dto import Dependency
from ns.di.meta import ContainerMeta


class Container(metaclass=ContainerMeta):
    __dependencies__: list[Dependency]

    @classmethod
    def container_function(cls, binder: Binder):
        for dependency in cls.__dependencies__:
            binder.bind(dependency.interface, dependency.impl)
            binder.bind(dependency.name, dependency.impl)
