from nacl import hash

from .fields import *


class RecordMeta(abc.ABCMeta):
    def __new__(cls, name: str, bases: typing.Tuple[type], attrs: typing.Dict[str, typing.Any]):
        is_root = any(base is dict for base in bases)
        fields: typing.Dict[str, Field] = {}

        if not is_root:
            for key, value in list(attrs.items()):
                if not isinstance(value, Field):
                    continue

                value = attrs.pop(key)

                if value is None:
                    continue

                fields[key] = value

            for base in reversed(bases):
                if not issubclass(base, Record):
                    continue

                for key, field in dict.items(base.fields):
                    if key in fields:
                        continue

                    if field is None:
                        continue

                    fields[key] = field

        attrs["fields"] = fields
        attrs["ordered_keys"] = list(dict.keys(fields))
        attrs["entry_point"] = None

        result = super().__new__(cls, name, bases, attrs)
        result.entry_point = RecordField(result)  # type: ignore

        return result


class Record(dict, abc.ABC, metaclass=RecordMeta):
    fields: typing.Dict[str, Field]
    ordered_keys: typing.List[str]
    entry_point: RecordField

    def __init__(self, **kwargs):
        value = self.entry_point.load(kwargs)
        super().__init__(value)

    def __getattr__(self, key):
        return self.__getitem__(key)

    def __setattr__(self, key, value):
        return self.__setitem__(key, value)

    def __setitem__(self, key, value):
        field = self.fields[key]
        super().__setitem__(key, field.load(value))

    def digest(self):
        return hash.sha256(hash.sha256(self.encode()))

    def __hash__(self):
        return self.digest().__hash__()

    @classmethod
    def load_unsafe(cls, obj):
        self = cls.__new__(cls)
        super(Record, self).__init__(obj)
        return self

    @classmethod
    def decode(cls, obj: bytes):
        buf = io.BytesIO(obj)
        return cls.entry_point.decode(buf)

    def encode(self) -> bytes:
        buf = io.BytesIO()
        self.entry_point.encode(buf, self)
        return buf.getvalue()
