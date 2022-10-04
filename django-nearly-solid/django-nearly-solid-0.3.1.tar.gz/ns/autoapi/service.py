from ns.autoapi.entities import Request
from ns.autoapi.errors import AutoapiError, ErrorCodes
from ns.application_layer import registry
from ns.application_layer.entities.application import ApplicationData
from ns.application_layer.serialization.application import serialize_application
from ns.application_layer.typings import EntityMeta


class AutoapiService:
    services: dict[str, object] = ...

    @property
    def declared_services(self) -> dict[str, type]:
        return registry.SERVICES

    @property
    def declared_models(self) -> list[EntityMeta]:
        return registry.ENTITIES

    def get_application_data(self) -> ApplicationData:
        return serialize_application(self.declared_services, self.declared_models)

    def execute_method(self, request: Request) -> any:
        """
        Все-таки вьюха
        """
        service_name = request.service_name
        method_name = request.method_name
        args = request.args

        if service_name not in self.services:
            raise AutoapiError(ErrorCodes.UNKNOWN_SERVICE, service_name=service_name)
        service = self.services[service_name]
        if method_name not in dir(service):
            raise AutoapiError(ErrorCodes.UNKNOWN_SERVICE_METHOD, service_name=service_name, method_name=method_name)
        method = getattr(service, method_name)
        if not callable(method):
            raise AutoapiError(ErrorCodes.NOT_A_METHOD, service_name=service_name, method_name=method_name)
        if isinstance(args, list):
            return method(*args)
        elif isinstance(args, dict):
            return method(**args)
        else:
            raise AutoapiError(ErrorCodes.INVALID_ARGUMENTS, service_name=service_name,
                               method_name=method_name, args=args)
