from inject import Binder, configure_once

from ns.di.meta import ContainerMeta


def configure_dependencies_in_django(containers: list[ContainerMeta]):
    def full_container(binder: Binder):
        for container in containers:
            binder.install(container.container_function)
    configure_once(full_container)

