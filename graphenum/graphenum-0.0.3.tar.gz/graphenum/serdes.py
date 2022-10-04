"""Manage serialization/deserialization of the schema."""

from typing import Any, Dict, List, Optional, Set, cast

from graphenum.entities.graphql import GraphType, Operation, RawSchema, SpecKey
from graphenum.logger import LOG

RESERVED_KEYWORDS = ['__Schema', '__Type', '__Field', '__InputValue', '__EnumValue', '__Directive']


def _init_fields(dct: dict) -> dict:
    """Initialize a field in the schema."""

    for field in dct['fields']:

        field['pii'] = []

        for arg in field['args']:
            arg['sources'] = []

    return dct


# pylint: disable=too-many-branches
def serialize_schema(gql_schema: Dict) -> RawSchema:
    """Serialize a GraphQL schema to a RawSchema."""

    raw_schema = RawSchema({
        'query': None,
        'mutation': None,
        'subscription': None,
        'directives': {},
        'objects': {},
        'inputObjects': {},
        'unions': {},
        'interfaces': {},
        'others': {},
        'scalars': {},
        'enums': {}
    })

    document_types: Dict[Operation, Set[str]] = {
        'query': set(),
        'mutation': set(),
        'subscription': set(),
    }

    for operation, operation_names in document_types.items():
        operation_type = f'{operation}Type'
        if gql_schema.get(operation_type):
            operation_names.add(gql_schema[operation_type].get('name', '').lower())
        else:
            LOG.info(f'No {operation_type} detected')

    for typ in gql_schema['types']:

        if typ['kind'] == 'OBJECT':

            if typ['name'].lower().startswith('__'):  # For the moment we don't want to deal with reserved keywords
                continue

            # We want to save sent arguments in each field of queries, mutations, and subcriptions…
            is_operation = False
            for operation, operation_names in document_types.items():
                if typ['name'].lower() in operation_names:
                    raw_schema[operation] = _init_fields(typ)
                    is_operation = True
                    break

            # … but also normal objects.
            # In addition, we want to save the returned values of objects when querrying them.
            if not is_operation:
                raw_schema['objects'][typ['name']] = _init_fields(typ)
                raw_schema['objects'][typ['name']]['returnedExamples'] = {}
                raw_schema['objects'][typ['name']]['paths'] = {'query': {}, 'mutation': {}}

        # Input objects have no fields but directly arguments.
        # They cannont be used as a return type.
        elif typ['kind'] == 'INPUT_OBJECT':
            for input_field in typ['inputFields']:
                input_field['sources'] = []
            raw_schema['inputObjects'][typ['name']] = typ

        elif typ['kind'] == 'UNION':
            raw_schema['unions'][typ['name']] = typ
            typ['possibleTypes'] = {possible_type['name']: possible_type for possible_type in typ['possibleTypes']}
            raw_schema['unions'][typ['name']]['paths'] = {'query': {}, 'mutation': {}}

        elif typ['kind'] == 'SCALAR':
            raw_schema['scalars'][typ['name']] = {'name': typ['name'], 'description': typ['description'], 'returnedExamples': []}

        elif typ['kind'] == 'INTERFACE':
            raw_schema['interfaces'][typ['name']] = typ
            typ['possibleTypes'] = {possible_type['name']: possible_type for possible_type in typ['possibleTypes']}
            raw_schema['interfaces'][typ['name']]['paths'] = {'query': {}, 'mutation': {}}

        elif typ['kind'] == 'ENUM':
            raw_schema['enums'][typ['name']] = {'name': typ['name'], 'description': typ['description'], 'enumValues': typ['enumValues']}

        # We do not want to save anything for other values so far.
        else:
            raw_schema['others'][typ['name']] = typ

    return raw_schema


def _process_raw_type(graph_type: dict) -> Optional[GraphType]:
    """Recursively flatten types.
    Note: at the beginning of this function, the "graph_type" is still not a valid graph_type.

    TODO: Might need to find a better solution for complex types (accession…)
    """
    if graph_type['kind'] in ['OBJECT', 'SCALAR', 'ENUM', 'INTERFACE', 'INPUT_OBJECT', 'UNION']:
        return GraphType(name=graph_type['name'], nullable=[True], depth=0, kind=graph_type['kind'])

    if graph_type['kind'] == 'LIST':
        of_type = _process_raw_type(graph_type['ofType'])
        of_type = cast(GraphType, of_type)
        of_type['depth'] += 1
        of_type['nullable'] = [True] + of_type['nullable']
        return of_type

    if graph_type['kind'] == 'NON_NULL':
        of_type = _process_raw_type(graph_type['ofType'])
        of_type = cast(GraphType, of_type)
        of_type['nullable'][0] = False
        return of_type

    # If this raises, check if we forgot to support one type
    LOG.warning(f'graphenum [TODO]: Unsupported field : {graph_type}')
    return None


def flatten_types(specification: RawSchema) -> RawSchema:  #pylint: disable=too-many-branches
    """Flatten types everywhere in the spec.
    Note: at the beginning of this function, the "specification" is still not a valid specification.

    # TODO: Factorize this
    """

    LOG.info('Recursively flattening schema types to custom GraphTypes')
    for key in specification:

        key = cast(SpecKey, key)

        # We don't want fields that return graphql special type like fields in RESERVED_KEYWORDS
        # We first get the index of element to remove then we remove it.
        if specification[key]:
            index_to_suppress = (index for index, field in enumerate(specification[key].get('fields', [])) if field['type']['name'] in RESERVED_KEYWORDS)
            for index in index_to_suppress:
                specification[key]['fields'].pop(index)

            if key == 'objects':
                for obj in specification['objects'].values():
                    for field in obj['fields']:
                        field['type'] = _process_raw_type(field['type'])
                        for arg in field['args']:
                            arg['type'] = _process_raw_type(arg['type'])

            elif key == 'inputObjects':
                for obj in specification['inputObjects'].values():
                    for input_field in obj['inputFields']:
                        input_field['type'] = _process_raw_type(input_field['type'])

            elif key == 'unions':
                for obj in specification['unions'].values():
                    for possible_type in obj['possibleTypes'].values():
                        obj['possibleTypes'][possible_type['name']] = _process_raw_type(possible_type)

            elif key == 'interfaces':
                for obj in specification['interfaces'].values():
                    for field in obj['fields']:
                        field['type'] = _process_raw_type(field['type'])
                        for arg in field['args']:
                            arg['type'] = _process_raw_type(arg['type'])
                    for possible_type in obj['possibleTypes'].values():
                        obj['possibleTypes'][possible_type['name']] = _process_raw_type(possible_type)

            else:

                for index, field in enumerate(specification[key].get('fields', [])):
                    field['type'] = _process_raw_type(field['type'])
                    for arg in field['args']:
                        arg['type'] = _process_raw_type(arg['type'])

    return specification


def lists_to_dicts(obj: Any) -> Any:
    """Convert lists of dicts to dicts (by duplicating the "name" to use it as a key) for the keys 'fields' and 'args'."""

    if isinstance(obj, List):
        return list(map(lists_to_dicts, obj))

    if isinstance(obj, Dict):

        for key in ['fields', 'inputFields', 'args', 'enumValues', 'interfaces']:
            if key in obj and isinstance(obj[key], List):
                obj[key] = {el['name']: el for el in obj[key]}

        return {k: lists_to_dicts(v) for k, v in obj.items()}

    return obj
