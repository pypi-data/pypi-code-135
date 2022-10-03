from typing import Any, Dict

from marshmallow import Schema, fields

PATH_PREFIX_DEFAULT = "{}_{}_{}"


class Template(Schema):

    name = fields.String()
    path_prefix = fields.String(dump_default=PATH_PREFIX_DEFAULT)
    path_patterns = fields.List(fields.String())
