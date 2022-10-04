"""Manage paths generation."""

import random
from typing import Counter, Dict, List, Optional, Set, Tuple, Union, cast

from graphenum import settings
from graphenum.entities.graphql import FieldName, GraphInterface, GraphObjectType, GraphPath, GraphUnion, InterfaceName, IntrospectionSchema, ObjectName
from graphenum.entities.graphql import ObjectType, Operation, SupportedOperations, UnionName
from graphenum.logger import LOG


def _generate_reverse_objects_dict(schema: IntrospectionSchema) -> Dict[GraphObjectType, List[Tuple[FieldName, GraphObjectType]]]:
    """Generate a Dictionary that associate the name of an object to all the objects that include this object in their fields.

    <object_name> str: List[Tuple[str, str]] [(<field_name_A>, <parent_object_name_A>), (<field_name_B>, <parent_object_name_B>)]
    """

    reverse_dict: Dict[GraphObjectType, List[Tuple[FieldName, GraphObjectType]]] = {}

    for parent_name, obj in schema['objects'].items():

        for field_name, field in obj['fields'].items():
            child_name = field['type']['name']

            if field['type']['kind'] in ['OBJECT', 'UNION', 'INTERFACE']:
                child_name = cast(GraphObjectType, child_name)
                reverse_dict[child_name] = reverse_dict.get(child_name, []) + [(field_name, parent_name)]

            # For unions and interfaces we add a step to select all possible types
            if field['type']['kind'] == 'UNION':
                child_name = cast(UnionName, child_name)
                graph_union: GraphUnion = schema['unions'][child_name]
                for possible_type in graph_union['possibleTypes']:
                    reverse_dict[possible_type] = reverse_dict.get(possible_type, []) + [(FieldName(f'... on {possible_type}'), child_name)]

                # Limit maximum of possible union types to avoid too much recursion.
                # This is mandatory on big applications.
                if settings.MAX_POSSIBLE_TYPES_PER_UNIONS > 0:
                    reverse_dict = {k: reverse_dict[k] for k in list(reverse_dict.keys())[:settings.MAX_POSSIBLE_TYPES_PER_UNIONS]}

            if field['type']['kind'] == 'INTERFACE':
                child_name = cast(InterfaceName, child_name)
                graph_interface: GraphInterface = schema['interfaces'][child_name]
                for possible_type in graph_interface['possibleTypes']:
                    reverse_dict[possible_type] = reverse_dict.get(possible_type, []) + [(FieldName(f'... on {possible_type}'), child_name)]

    return reverse_dict


def _generate_reverse_doc_type_dict(
    schema: IntrospectionSchema,
    operation: Operation,
) -> Dict[GraphObjectType, List[FieldName]]:
    """Generate a dictionary of the queries/mutations that return an object.

    <object_name> str: List[str] [<query_A>, <query_B>, ...]
    """

    reverse_dict: Dict[GraphObjectType, List[FieldName]] = {}

    operation_field = schema[operation]
    if operation_field:
        for field_name, field in operation_field['fields'].items():

            if field['type']['kind'] in ['OBJECT', 'UNION', 'INTERFACE']:
                type_name = cast(GraphObjectType, field['type']['name'])
                reverse_dict[type_name] = reverse_dict.get(type_name, []) + [field_name]

    if not reverse_dict:
        LOG.error(f'It seems there is no paths coming from a "{operation}"')

    return reverse_dict


def _get_leading_paths_object(
    root_parents: List[FieldName],
    object_name: GraphObjectType,
) -> Set[GraphPath]:
    """Get List of the paths that lead to an object."""

    return {((root_parent, object_name), ) for root_parent in root_parents}


def _get_parent_object_type(
    schema: IntrospectionSchema,
    object_parent: Tuple[FieldName, GraphObjectType],
) -> Optional[ObjectType]:
    """Determinate parent object type."""

    if object_parent[1] in schema['objects'].keys():
        return 'objects'
    if object_parent[1] in schema['unions'].keys():
        return 'unions'
    if object_parent[1] in schema['interfaces'].keys():
        return 'interfaces'

    LOG.warning(f'Escape[TODO]: We do not support this type for creating the path: {schema["others"][object_parent[1]]["kind"]}')
    return None


def _generate_parents_object_paths(
    schema: IntrospectionSchema,
    operation: Operation,
    object_parent: Tuple[FieldName, GraphObjectType],
    object_name: GraphObjectType,
    reverse_objects_dict: Dict[GraphObjectType, List[Tuple[FieldName, GraphObjectType]]],
    reverse_doc_type_dict: Dict[GraphObjectType, List[FieldName]],
    already_seen: Counter[GraphObjectType],
) -> Set[GraphPath]:
    """Generate parents paths for an object."""

    parent_node = (object_parent[0], object_name)
    parent_object_type: Optional[ObjectType] = _get_parent_object_type(schema, object_parent)
    if not parent_object_type:
        return set()

    # Get the paths of the parent object, compute them if they don't exist yet
    parent_paths: Set[GraphPath] = schema[parent_object_type][object_parent[1]]['paths'][operation]  # type: ignore[index]
    if not parent_paths:
        _generate_nested_object_paths(
            schema,
            operation,
            object_parent[1],
            parent_object_type,
            reverse_objects_dict,
            reverse_doc_type_dict,
            already_seen.copy(),
        )
        parent_paths = schema[parent_object_type][object_parent[1]]['paths'][operation]  # type: ignore[index]

    paths: Set[GraphPath] = set()
    for parent_path in parent_paths:
        if object_name in [parent_name for _, parent_name in parent_path]:
            continue
        paths.add(parent_path + (parent_node, ))

    return paths


def _generate_nested_object_paths(
    schema: IntrospectionSchema,
    operation: Operation,
    object_name: Union[ObjectName, UnionName, InterfaceName],
    object_type: ObjectType,
    reverse_objects_dict: Dict[Union[ObjectName, UnionName, InterfaceName], List[Tuple[FieldName, Union[ObjectName, UnionName, InterfaceName]]]],
    reverse_doc_type_dict: Dict[Union[ObjectName, UnionName, InterfaceName], List[FieldName]],
    already_seen: Counter[Union[ObjectName, UnionName, InterfaceName]] = None,
) -> IntrospectionSchema:
    """Recursively save the paths that lead to one object."""

    # If the parent object has already been treated, we skip it to avoid endless loops
    already_seen = already_seen or Counter()
    if already_seen[object_name] > 0:
        return schema
    already_seen[object_name] += 1

    root_parents = reverse_doc_type_dict.get(object_name, [])  # List of the queries/mutations that return this object
    object_parents = reverse_objects_dict.get(object_name, [])  # List of the objects that contain this object in their fields
    paths: Set[GraphPath] = _get_leading_paths_object(root_parents, object_name)

    # Then look for the "parent" objects that contain this object in their fields
    for object_parent in object_parents:

        parent_paths: Set[GraphPath] = _generate_parents_object_paths(
            schema,
            operation,
            object_parent,
            object_name,
            reverse_objects_dict,
            reverse_doc_type_dict,
            already_seen,
        )

        paths = paths.union(parent_paths)

    if settings.MAX_PATHS_PER_OBJECT > 0:
        paths = set(random.sample(paths, settings.MAX_PATHS_PER_OBJECT))

    schema[object_type][object_name]['paths'][operation] = paths  # type: ignore[index]

    return schema


def generate_objects_paths_for_operation(
    schema: IntrospectionSchema,
    operation: Operation,
) -> IntrospectionSchema:
    """Save the paths to one object in the specification."""

    if schema[operation]:
        reverse_objects_dict = _generate_reverse_objects_dict(schema)
        reverse_doc_type_dict = _generate_reverse_doc_type_dict(schema, operation)

        for object_name in schema['objects']:
            schema = _generate_nested_object_paths(
                schema,
                operation,
                object_name,
                'objects',
                reverse_objects_dict,
                reverse_doc_type_dict,
            )

        for union_name in schema['unions']:
            schema = _generate_nested_object_paths(
                schema,
                operation,
                union_name,
                'unions',
                reverse_objects_dict,
                reverse_doc_type_dict,
            )

    return schema


def generate_objects_paths(schema: IntrospectionSchema) -> IntrospectionSchema:
    """Iterate over all the operations and save the paths to one object in the specification."""

    for operation in SupportedOperations:
        schema = generate_objects_paths_for_operation(schema, operation)

    return schema
