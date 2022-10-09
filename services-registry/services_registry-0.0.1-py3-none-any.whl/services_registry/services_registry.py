from typing import Dict


class Service:
    """Services base class."""
    pass


class ServicesRegistry:
    """A class implementing a registry to manage services in a Python application."""
    def __init__(self):
        self._services: Dict[type, Service] = {}

    @property
    def services(self):
        raise AttributeError("Direct access to services attribute is forbidden")

    def register_service(self, service: Service):
        """Register a service in registry. A service of some type can be registered only once.
        Raises a :class:`ValueError` on attempt to register a service of some type the second time.
        :param service: a service to register."""

        if service.__class__ in self._services:
            raise ValueError(f"A service of type {service.__class__} has been registered already")
        self._services[service.__class__] = service
        print(f"{service} has been added to registry")

    def get_service(self, service_type: type) -> Service:
        """Get a service by its type from registry. If it is not in the registry, initialize it and add to registry.
        :param service_type: type of the service.
        :return: service."""

        if service_type not in self._services:
            print(f"The {service_type} service has not been registered yet. Initializing it")
            self.register_service(service_type())
        return self._services[service_type]


services_registry = ServicesRegistry()
