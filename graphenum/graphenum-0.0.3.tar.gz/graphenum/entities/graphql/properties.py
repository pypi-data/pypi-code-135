"""Define GraphQL properties."""

import sys
from enum import Enum, unique
from typing import List, NewType, Tuple, Union

from graphenum.utils import MetaEnum

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

Operation: TypeAlias = Literal['query', 'mutation', 'subscription']
SupportedOperations: Tuple[Operation, Operation] = ('query', 'mutation')
GraphValue = Union[int, str, float, bool, List['GraphValue']]  # type: ignore[misc]
SpecKey = Literal['query', 'mutation', 'subscription', 'unions', 'objects', 'interfaces', 'inputObjects']
ObjectType = Literal['unions', 'objects', 'interfaces']

ArgName = NewType('ArgName', str)
FieldName = NewType('FieldName', str)
ObjectName = NewType('ObjectName', str)
InputObjectName = NewType('InputObjectName', str)
UnionName = NewType('UnionName', str)
InterfaceName = NewType('InterfaceName', str)
EnumName = NewType('EnumName', str)
CustomScalarName = NewType('CustomScalarName', str)

GraphObjectType = Union[ObjectName, UnionName, InterfaceName]
GraphPath = Tuple[Tuple[FieldName, GraphObjectType], ...]


@unique
class GraphPrimitive(str, Enum, metaclass=MetaEnum):

    """The default GraphQL Scalar types."""

    ID = 'ID'
    INT = 'Int'
    STRING = 'String'
    BOOLEAN = 'Boolean'
    FLOAT = 'Float'


GraphTypeName = Union[ObjectName, InputObjectName, UnionName, InterfaceName, CustomScalarName, EnumName]


@unique
class GraphKind(str, Enum):

    """GraphQL Kind.

    Source:
        https://spec.graphql.org/draft/#sec-Schema-Introspection.Schema-Introspection-Schema
        -> __TypeKind
    """

    SCALAR = 'SCALAR'
    OBJECT = 'OBJECT'
    INTERFACE = 'INTERFACE'
    UNION = 'UNION'
    ENUM = 'ENUM'
    INPUT_OBJECT = 'INPUT_OBJECT'
    # LIST
    # NON_NULL
