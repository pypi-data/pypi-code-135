from inspect import isfunction

from ns.application_layer.entities.services import ServiceData
from ns.application_layer.serialization.methods import serialize_method


def serialize_services(**services: type) -> list[ServiceData]:
    return [serialize_service(service_name, service) for service_name, service in services.items()]


def serialize_service(service_name, service: type) -> ServiceData:
    prop_names = dir(service)
    methods = []
    for prop_name in prop_names:
        if prop_name.startswith('_'):
            continue
        prop = getattr(service, prop_name)
        if not isfunction(prop) or hasattr(prop, '__task__'):
            continue
        method = prop
        method_data = serialize_method(method)
        methods.append(method_data)
    return ServiceData(
        name=service_name,
        methods=methods,
    )
