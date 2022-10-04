from ns.application_layer.entities.props import PropData
from ns.application_layer.serialization.types import serialize_type


def serialize_prop(name: str, type_: type, required: bool, default: any) -> PropData:
    return PropData(
        name=name,
        type=serialize_type(type_),
        required=required,
        default_value=default,
    )
