import datetime
import enum
import io

from nacl import encoding, public, signing

from .validators import *


class Field(abc.ABC):
    def __init__(self, *, validators: typing.List[Validator] = None):
        self.validators = validators or []

    @staticmethod
    def read_varint(buf, limit=4):
        result = 0

        for shift in range(0, 7 * limit, 7):
            bytes = buf.read(1)

            if len(bytes) != 1:
                raise CordExhaustedBufferError(field_type="cord header")

            byte = bytes[0]
            digit = byte & 0x7F
            result |= digit << shift

            if digit == byte:
                if shift > 0 and digit == 0:
                    raise CordValueError("Non-canonical ULEB128 number detected")

                return result

        raise CordValueError(f"ULEB128 traversal exceeded '{limit}' octets")

    @staticmethod
    def write_varint(buf, number):
        while True:
            acc = number & 0x7F
            number >>= 7

            if number:
                buf.write((acc | 0x80).to_bytes(1, byteorder="big"))
                continue

            buf.write(acc.to_bytes(1, byteorder="big"))
            break

    def _validate(self, obj):
        for validator in self.validators:
            obj = validator(obj)

    @abc.abstractmethod
    def _load(self, obj):
        ...

    def load(self, obj):
        result = self._load(obj)
        self._validate(obj)
        return result

    @abc.abstractmethod
    def encode(self, buf: io.BytesIO, obj: typing.Any) -> None:
        ...

    @abc.abstractmethod
    def decode(self, buf: io.BytesIO) -> typing.Any:
        ...


class NullField(Field):
    def _load(self, obj):
        if obj is not None:
            raise CordTypeError(expectation="null", received=obj)

        return obj

    def encode(self, buf: io.BytesIO, obj: None) -> None:
        return None

    def decode(self, buf: io.BytesIO) -> None:
        return None


class BooleanField(Field):
    def _load(self, obj):
        if not isinstance(obj, bool):
            raise CordTypeError(expectation="boolean", received=obj)

        return obj

    def encode(self, buf: io.BytesIO, obj: bool) -> None:
        buf.write(b"\x00" if obj is False else b"\x01")

    def decode(self, buf: io.BytesIO) -> bool:
        bytes = buf.read(1)

        if not bytes:
            raise CordExhaustedBufferError(field_type="boolean")

        byte = bytes[0]

        if byte == 0:
            return False

        if byte == 1:
            return True

        raise CordValueError(f"Received invalid byte {byte} while parsing boolean")


class UnsignedIntegerField(Field):
    def _load(self, obj):
        if not isinstance(obj, int):
            raise CordTypeError(expectation="unsigned integer", received=obj)

        if obj < 0:
            raise CordValueError(f"Expected unsigned integer, received invalid integer {obj}")

        return obj

    def encode(self, buf: io.BytesIO, obj: int) -> None:
        if obj < 0 or obj > 2**63:
            raise CordValueError(f"Expected positive integer in the range 0 to 2^63, received {obj}")

        self.write_varint(buf, obj)

    def decode(self, buf: io.BytesIO) -> int:
        return self.read_varint(buf, 9)


class SignedIntegerField(UnsignedIntegerField):
    def _load(self, obj):
        if not isinstance(obj, int):
            raise CordTypeError(expectation="signed integer", received=obj)

        return obj

    def encode(self, buf: io.BytesIO, obj: int) -> None:
        value = (obj << 1) ^ (obj >> 63)
        return super().encode(buf, value)

    def decode(self, buf: io.BytesIO) -> int:
        value = super().decode(buf)
        return (value >> 1) ^ -(value & 1)


class BytesField(Field):
    def _load(self, obj):
        if not isinstance(obj, bytes):
            raise CordTypeError(expectation="bytes", received=obj)

        return obj

    def encode(self, buf: io.BytesIO, obj: bytes) -> None:
        self.write_varint(buf, len(obj))
        buf.write(obj)

    def decode(self, buf: io.BytesIO) -> bytes:
        length = self.read_varint(buf, 9)
        result = buf.read(length)

        if len(result) != length:
            raise CordExhaustedBufferError(field_type="bytes")

        return result


class StringField(BytesField):
    def _load(self, obj):
        if not isinstance(obj, str):
            raise CordTypeError(expectation="string", received=obj)

        return obj

    def encode(self, buf: io.BytesIO, obj: str) -> None:
        return super().encode(buf, obj.encode("utf8"))

    def decode(self, buf: io.BytesIO) -> str:
        result = super().decode(buf)

        try:
            return result.decode("utf8")
        except UnicodeDecodeError as e:
            raise CordValueError("Expected string to be UTF-8 encoded") from e


class DateTimeField(UnsignedIntegerField):
    EPOCH = datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)

    def _load(self, obj):
        if not isinstance(obj, datetime.datetime):
            raise CordTypeError(expectation="datetime", received=obj)

        return obj

    def encode(self, buf: io.BytesIO, obj: datetime.datetime) -> None:
        time_dt = obj.astimezone(tz=datetime.timezone.utc) - self.EPOCH
        milliseconds = time_dt.days * 86400000 + time_dt.seconds * 1000 + time_dt.microseconds // 1000
        self.write_varint(buf, milliseconds)

    def decode(self, buf: io.BytesIO) -> datetime.datetime:
        milliseconds = self.read_varint(buf, 9)
        days, milliseconds = divmod(milliseconds, 86400000)
        seconds, milliseconds = divmod(milliseconds, 1000)

        try:
            return self.EPOCH + datetime.timedelta(days=days, seconds=seconds, milliseconds=milliseconds)
        except OverflowError as e:
            raise CordValueError("Datetime overflow") from e


class EnumField(UnsignedIntegerField):
    def __init__(self, enum, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.enum = enum

    def _load(self, obj):
        if not isinstance(obj, self.enum):
            raise CordTypeError(expectation="enumeration", received=obj)

        return obj

    def encode(self, buf: io.BytesIO, obj: enum.IntEnum) -> None:
        self.write_varint(buf, obj.value)

    def decode(self, buf: io.BytesIO) -> datetime.datetime:
        result = self.read_varint(buf, 9)

        try:
            return self.enum(result)
        except ValueError:
            raise CordValueError(f"Invalid enumeration index")


class ListField(Field):
    def __init__(self, item_field, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.item_field = item_field

    def _load(self, obj):
        if not isinstance(obj, list):
            raise CordTypeError(expectation="list", received=obj)

        return [self.item_field.load(item) for item in obj]

    def encode(self, buf: io.BytesIO, obj: list) -> None:
        self.write_varint(buf, len(obj))

        for item in obj:
            self.item_field.encode(buf, item)

    def decode(self, buf: io.BytesIO) -> list:
        length = self.read_varint(buf)
        result = []

        for i in range(length):
            result.append(self.item_field.decode(buf))

        return result


class SetField(Field):
    def __init__(self, item_field, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.item_field = item_field

    def _load(self, obj):
        if isinstance(obj, list):
            obj = set(obj)

        if not isinstance(obj, set):
            raise CordTypeError(expectation="set", received=obj)

        return {self.item_field.load(item) for item in obj}

    def encode(self, buf: io.BytesIO, obj: set) -> None:
        items = []

        for item in obj:
            item_buf = io.BytesIO()
            self.item_field.encode(item_buf, item)
            items.append(item_buf.getvalue())

        items = sorted(items)
        self.write_varint(buf, len(items))

        for item in items:
            buf.write(item)

    def decode(self, buf: io.BytesIO) -> set:
        length = self.read_varint(buf)
        result = set()
        encodings = []

        for i in range(length):
            start_position = buf.tell()
            result.add(self.item_field.decode(buf))

            seek_delta = start_position - buf.tell()
            buf.seek(seek_delta, io.SEEK_CUR)

            encodings.append(buf.read(-seek_delta))

        if sorted(encodings) != encodings:
            raise CordValueError("Expected sorted set")

        return result


class OptionalField(Field):
    def __init__(self, item_field, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.item_field = item_field

    def _load(self, obj):
        if obj is None:
            return None

        return self.item_field.load(obj)

    def encode(self, buf: io.BytesIO, obj: typing.Any) -> None:
        if obj is None:
            self.write_varint(buf, 0)
        else:
            self.write_varint(buf, 1)
            self.item_field.encode(buf, obj)

    def decode(self, buf: io.BytesIO) -> typing.Any:
        field_index = self.read_varint(buf, 9)

        if field_index == 0:
            return None

        if field_index != 1:
            raise CordValueError("Expected optional, encountered invalid index")

        return self.item_field.decode(buf)


class RecordField(Field):
    def __init__(self, schema, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.schema = schema

    def _load(self, obj):
        if not isinstance(obj, dict):
            raise CordTypeError(expectation="record", received=obj)

        missing_fields = set(self.schema.ordered_keys).symmetric_difference(set(obj.keys()))
        if missing_fields:
            raise CordValueError(f"Record missing fields: {', '.join(missing_fields)}")

        return self.schema.load_unsafe({key: self.schema.fields[key].load(value) for key, value in obj.items()})

    def encode(self, buf: io.BytesIO, obj: typing.Any) -> None:
        for key in self.schema.ordered_keys:
            field_obj = self.schema.fields[key]
            field_obj.encode(buf, obj[key])

    def decode(self, buf: io.BytesIO) -> typing.Any:
        result = {}

        for key in self.schema.ordered_keys:
            field_obj = self.schema.fields[key]

            try:
                result[key] = field_obj.decode(buf)
            except CordException as e:
                raise CordValueError(f"Failed while decoding record field '{key}'") from e

        return self.schema(**result)


class VariantField(Field):
    def __init__(self, union, **kwargs):
        super().__init__(**kwargs)
        self.union = union

    def _load(self, obj):
        if not isinstance(obj, tuple) or len(obj) != 2:
            raise CordTypeError(expectation="variant tuple", received=obj)

        field_key, value = obj
        field: Field = dict.get(self.union.fields, field_key)

        if field is None:
            raise CordValueError(f"'{field_key}' does not correspond to any recognized union field")

        return self.union.load_unsafe((field_key, field.load(value)))

    def encode(self, buf: io.BytesIO, obj: typing.Tuple[str, typing.Any]) -> None:
        field_key, value = obj
        field: Field = dict.get(self.union.fields, field_key)

        if field is None:
            raise CordValueError(f"'{field_key}' does not correspond to any recognized union field")

        field_index = self.union.ordered_keys.index(field_key)
        self.write_varint(buf, field_index)
        field.encode(buf, value)

    def decode(self, buf: io.BytesIO) -> typing.Tuple[str, typing.Any]:
        field_index = self.read_varint(buf, 9)

        try:
            field_key = self.union.ordered_keys[field_index]
            field: Field = self.union.fields[field_key]
        except IndexError as e:
            raise CordValueError(f"Unknown variant {field_index} in {self.union.__name__}") from e

        value = field.decode(buf)
        return field_key, value


class CryptographicKeyField(BytesField, abc.ABC):
    __key_cls__ = None
    __key_length__ = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _load(self, obj):
        if not isinstance(obj, self.__key_cls__):
            raise CordTypeError(expectation=self.__key_cls__.__name__, received=obj)

        return obj

    def encode(self, buf: io.BytesIO, obj: typing.Any) -> None:
        obj = self.__key_cls__.encode(obj, encoder=encoding.RawEncoder)
        return super().encode(buf, obj)

    def decode(self, buf: io.BytesIO) -> typing.Any:
        value = super().decode(buf)

        if len(value) != self.__key_length__:
            raise CordValueError(
                f"Expected {self.__key_length__} bytes to instantiate {self.__key_cls__.__name__}, received"
                f" {len(value)} bytes"
            )

        return self.__key_cls__(value, encoder=encoding.RawEncoder)


class PrivateKeyField(CryptographicKeyField):
    __key_cls__ = public.PrivateKey
    __key_length__ = 32


class PublicKeyField(CryptographicKeyField):
    __key_cls__ = public.PublicKey
    __key_length__ = 32


class SigningKeyField(CryptographicKeyField):
    __key_cls__ = signing.SigningKey
    __key_length__ = 32


class VerifyKeyField(CryptographicKeyField):
    __key_cls__ = signing.VerifyKey
    __key_length__ = 32


class EncryptedField(BytesField):
    def __init__(self, record_cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.record_cls = record_cls
