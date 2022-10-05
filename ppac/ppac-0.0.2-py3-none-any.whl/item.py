from dataclasses import dataclass
import dataclasses
from datetime import datetime, date
from typing import List
from .utils import datetime_to_str, str_to_datetime

import json


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (date, datetime)):
            return datetime_to_str(obj)


def decode_date(value_dict):
    for k, v in value_dict.items():
        if k.endswith('_date') and v:
            value_dict[k] = str_to_datetime(v)
    return value_dict


@dataclass
class Item:
    id: str
    due_date: datetime = None
    start_date: datetime = None
    end_date: datetime = None
    labels: List[str] = dataclasses.field(default_factory=list)

    @property
    def name(self):
        return self.id.split('/')[-1]

    def to_dict(self):
        return dataclasses.asdict(self)

    def to_json_str(self, indent=0):
        return json.dumps(self.to_dict(), indent=indent, cls=DateTimeEncoder)

    @classmethod
    def from_dict(cls, value):
        return Item(**value)

    @classmethod
    def from_json_str(cls, value):
        return Item.from_dict(json.loads(value, object_hook=decode_date))
