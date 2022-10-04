from .fields import *


class VariantMeta(abc.ABCMeta):
    def __new__(cls, name: str, bases: typing.Tuple[type], attrs: typing.Dict[str, typing.Any]):
        is_root = any(base is tuple for base in bases)
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
                if not issubclass(base, Variant):
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
        result.entry_point = VariantField(result)

        return result


class Variant(tuple, abc.ABC, metaclass=VariantMeta):
    fields: typing.Dict[str, Field]
    ordered_keys: typing.List[str]
    entry_point: VariantField

    def __new__(cls, value):
        value = cls.entry_point.load(value)
        return super().__new__(cls, value)

    @classmethod
    def load_unsafe(cls, obj):
        return tuple.__new__(cls, obj)

    @classmethod
    def decode(cls, obj: bytes):
        buf = io.BytesIO(obj)
        return cls.entry_point.decode(buf)

    def encode(self) -> bytes:
        buf = io.BytesIO()
        self.entry_point.encode(buf, self)
        return buf.getvalue()
