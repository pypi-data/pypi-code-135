from typing import Any, Dict

from marshmallow import Schema, fields


class Template(Schema):

    name = fields.String()
    path_prefix = fields.String(dump_default="{}-{}-{}")
    path_patterns = fields.List(fields.String())
