from inject import Binder

from ns.di.dto import Dependency


class ContainerMeta(type):

    def container_function(cls, binder: Binder): ...

    def __new__(mcs, bases, *args, **kwargs):
        cls = super().__new__(mcs, bases, *args, **kwargs)
        annotations = cls.__annotations__
        print('annotations', annotations)
        dependencies = []
        for name, interface in annotations.items():
            if not hasattr(cls, name) or not isinstance(interface, type):
                continue
            impl = getattr(cls, name)
            dependency = Dependency(name=name, interface=interface, impl=impl)
            dependencies.append(dependency)
        cls.__dependencies__ = dependencies
        print('DEPS', cls.__dependencies__)
        return cls
