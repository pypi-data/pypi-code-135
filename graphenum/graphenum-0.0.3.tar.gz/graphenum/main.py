"""Manage module flow."""

import asyncio
import logging
from typing import Callable, Dict, List, Optional, Tuple

import aiohttp

from graphenum.entities.errors import IntrospectionError
from graphenum.entities.graphql import IntrospectionSchema
from graphenum.entities.internal import Callbacks
from graphenum.logger import LOG, setup_logger  # pylint: disable=unused-import # noqa
from graphenum.paths import generate_objects_paths
from graphenum.serdes import flatten_types, lists_to_dicts, serialize_schema
from graphenum.sources import fetch_schema, load_schema
from graphenum.utils import json_encode_schema


async def async_introspect(
    url: str,
    logger: Optional[logging.Logger] = None,
    headers: Optional[Dict[str, str]] = None,
    verbose_mode: bool = False,
    schema_path: Optional[str] = None,
    callbacks: Optional[Dict[Callbacks, List[Callable]]] = None,
    json_encode: bool = False,
) -> Tuple[IntrospectionSchema, aiohttp.ClientResponse]:
    """Run the introspection.

    Args:
        url: The URL of the GraphQL endpoint.
        logger: The logger to use.
        headers: The headers to send with the fetch_schema request.
        verbose_mode: Infer logging level.
        schema_path: The path to the provided GraphQL schema.

    Returns:
        The introspected schema.
    """

    callbacks = callbacks or {}

    global LOG  # pylint: disable=global-statement
    LOG = logger or setup_logger(verbose_mode)

    gql_schema, response = await fetch_schema(url, headers)
    if not gql_schema and schema_path:
        gql_schema = load_schema(schema_path)

    assert gql_schema, IntrospectionError(f'Could not retrieve schema from {url}')

    if callbacks.get(Callbacks.PRE_SERIALIZE):
        for callback in callbacks[Callbacks.PRE_SERIALIZE]:
            raw_schema = callback(gql_schema)

    raw_schema = serialize_schema(gql_schema)
    raw_schema = flatten_types(raw_schema)
    if callbacks.get(Callbacks.POST_SERIALIZE):
        for callback in callbacks[Callbacks.POST_SERIALIZE]:
            raw_schema = callback(gql_schema)

    schema = lists_to_dicts(raw_schema)
    if callbacks.get(Callbacks.PRE_SCHEMA_GENERATION):
        for callback in callbacks[Callbacks.PRE_SCHEMA_GENERATION]:
            schema = callback(schema)

    schema = generate_objects_paths(schema)
    if callbacks.get(Callbacks.POST_SCHEMA_GENERATION):
        for callback in callbacks[Callbacks.POST_SCHEMA_GENERATION]:
            schema = callback(schema)

    schema = json_encode_schema(schema) if json_encode else schema
    if verbose_mode:
        LOG.debug(schema)

    return schema, response


def introspect(
    url: str,
    logger: Optional[logging.Logger] = None,
    headers: Optional[Dict[str, str]] = None,
    verbose_mode: bool = False,
    schema_path: Optional[str] = None,
    callbacks: Optional[Dict[Callbacks, List[Callable]]] = None,
    json_encode: bool = False,
) -> Tuple[IntrospectionSchema, aiohttp.ClientResponse]:
    """Create a new asyncronous task to run the introspection."""

    return asyncio.run(
        async_introspect(
            url=url,
            logger=logger,
            headers=headers,
            verbose_mode=verbose_mode,
            schema_path=schema_path,
            callbacks=callbacks,
            json_encode=json_encode,
        )
    )
