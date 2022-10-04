"""Internal GraphEnum entities."""
from enum import Enum


class Callbacks(Enum):

    """The callbacks that can be used."""

    PRE_SERIALIZE = 'pre_serialize'
    POST_SERIALIZE = 'post_serialize'
    PRE_SCHEMA_GENERATION = 'pre_schema_generation'
    POST_SCHEMA_GENERATION = 'post_schema_generation'
