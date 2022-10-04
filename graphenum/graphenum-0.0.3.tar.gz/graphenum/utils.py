"""Utils.

Theses functions are meant to have no dependencies on the graphintrospect package.
"""

import json
from enum import EnumMeta
from typing import Any, Dict, Type


# pylint: disable=no-value-for-parameter
class MetaEnum(EnumMeta):

    """Meta class for Enum."""

    def __contains__(
        cls: Type[Any],
        obj: object,
    ) -> bool:
        """Check if the object is in the enum using `in` keyword."""

        try:
            cls(obj)
        except ValueError:
            return False
        return True


class SetEncoder(json.JSONEncoder):

    """Encode sets as lists."""

    def default(self, o: Any) -> Any:
        """Encode sets as lists."""
        if isinstance(o, set):
            return list(o)
        return json.JSONEncoder.default(self, o)


def json_encode_schema(schema: Any) -> Dict:
    """Serialize the schema to a proper json encoding."""
    return json.loads(json.dumps(schema, indent=2, cls=SetEncoder))


def dump_schema(path: str, schema: Any) -> None:
    """Dump the schema to a file."""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(schema, indent=2, cls=SetEncoder))
