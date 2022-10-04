"""
Each sub-section below defines the expected fields of __Type given each possible value of the __TypeKind enum:
source: https://spec.graphql.org/draft/#sec-The-__Type-Type

    x "SCALAR"
    ✓ "OBJECT"
    ✓ "INTERFACE"
    ✓ "UNION"
    ✓ "ENUM"
    ✓ "INPUT_OBJECT"
    x "LIST"
    x "NON_NULL"
"""

import sys
from typing import Dict, List, Optional, Set, Tuple

from graphenum.entities.graphql.properties import ArgName, EnumName, FieldName, GraphKind, GraphObjectType, GraphPath, GraphTypeName, GraphValue
from graphenum.entities.graphql.properties import InputObjectName, InterfaceName, ObjectName, Operation, UnionName

if sys.version_info >= (3, 8):
    from typing import TypedDict  # pylint: disable=no-name-in-module
else:
    from typing_extensions import TypedDict


class MinimalGraphType(TypedDict):

    """Minimal GraphQL Type."""

    name: GraphTypeName
    nullable: List[bool]
    depth: int  # depth = 1 <=> it's a list | depth >= 2 <=> it is a list of lists
    kind: GraphKind


class GraphType(MinimalGraphType, total=False):

    """GraphQL Type."""


class MinimalGraphField(TypedDict):

    """Minimal GraphQL Field."""

    name: FieldName
    description: str
    args: Dict[ArgName, 'GraphArg']
    type: GraphType
    isDeprecated: bool
    deprecationReason: str


class GraphField(MinimalGraphField, total=False):

    """GraphQL Field."""


class GraphObject(TypedDict):

    """GraphQL Object.

    Source:
        https://spec.graphql.org/draft/#sec-The-__Type-Type.Object
    """

    kind: GraphKind
    name: ObjectName
    description: Optional[str]
    fields: Dict[FieldName, GraphField]
    interfaces: Dict[InterfaceName, 'GraphInterface']  # type: ignore[misc]
    enumValues: Dict[str, 'GraphEnum']
    paths: Dict[Operation, Set[GraphPath]]  # GraphPath that end on the object


class GraphInterface(TypedDict):

    """GraphQL Interface.

    Source:
        https://spec.graphql.org/draft/#sec-The-__Type-Type.Interface
    """

    kind: GraphKind
    name: InterfaceName
    description: Optional[str]
    fields: Dict[FieldName, GraphField]
    interfaces: Dict[InterfaceName, 'GraphInterface']  # type: ignore[misc]
    possibleTypes: Dict[GraphObjectType, GraphType]
    paths: Dict[Operation, Set[GraphPath]]  # GraphPath that end on the object


class GraphUnion(TypedDict):

    """GraphQL Union.

    Source:
        https://spec.graphql.org/draft/#sec-The-__Type-Type.Union
    """

    kind: GraphKind
    name: UnionName
    description: Optional[str]
    possibleTypes: Dict[GraphObjectType, GraphType]
    paths: Dict[Operation, Set[GraphPath]]  # GraphPath that end on the object


class GraphArg(TypedDict):

    """Minimal GraphQL Argument."""

    name: ArgName
    description: str
    defaultValue: GraphValue
    type: GraphType
    sources: List[Tuple[ObjectName, FieldName]]


class EnumValue(TypedDict):

    """Type for enum values."""

    name: str
    description: Optional[str]
    isDeprecated: bool
    deprecationReason: Optional[str]


class GraphEnum(TypedDict):

    """GraphQL Input.

    Source:
        https://spec.graphql.org/draft/#sec-The-__Type-Type.Enum
    """

    kind: GraphKind
    name: EnumName
    description: Optional[str]
    enumValues: Dict[str, EnumValue]


class GraphInputObject(TypedDict):

    """GraphQL Input Object.

    Source:
        https://spec.graphql.org/draft/#sec-The-__Type-Type.Input-Object
    """

    kind: GraphKind
    name: InputObjectName
    description: Optional[str]
    inputFields: Dict[ArgName, GraphArg]
