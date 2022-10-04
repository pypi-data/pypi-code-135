from ns.application_layer.entities.application import ApplicationData
from ns.application_layer.serialization.entities import serialize_entities
from ns.application_layer.serialization.services import serialize_services
from ns.application_layer.typings import EntityMeta


def serialize_application(services: dict[str, type], entities: list[EntityMeta]) -> ApplicationData:
    return ApplicationData(
        services=serialize_services(**services),
        entities=serialize_entities(*entities),
    )

