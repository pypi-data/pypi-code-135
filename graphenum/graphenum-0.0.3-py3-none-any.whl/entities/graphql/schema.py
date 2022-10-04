"""Define GraphQL schema."""

import sys
from typing import Any, Dict, Optional

from graphenum.entities.graphql.properties import InputObjectName, InterfaceName, ObjectName, UnionName
from graphenum.entities.graphql.types import GraphEnum, GraphInputObject, GraphInterface, GraphObject, GraphUnion

if sys.version_info >= (3, 8):
    from typing import TypedDict  # pylint: disable=no-name-in-module
else:
    from typing_extensions import TypedDict


class IntrospectionSchema(TypedDict):

    """Define a GraphQL Introspection Schema.

    Source:
        https://spec.graphql.org/draft/#sec-Schema-Introspection.Schema-Introspection-Schema
    """

    query: Optional[GraphObject]
    mutation: Optional[GraphObject]
    subscription: Optional[GraphObject]
    directives: Dict
    objects: Dict[ObjectName, GraphObject]
    inputObjects: Dict[InputObjectName, GraphInputObject]
    unions: Dict[UnionName, GraphUnion]
    interfaces: Dict[InterfaceName, GraphInterface]
    enums: Dict[str, GraphEnum]
    others: Dict


class RawSchema(TypedDict):

    """Define a GraphQL Raw Schema."""

    query: Any
    mutation: Any
    subscription: Any
    directives: Any
    objects: Any
    inputObjects: Any
    others: Any
    unions: Any
    interfaces: Any
    scalars: Any
    enums: Any
