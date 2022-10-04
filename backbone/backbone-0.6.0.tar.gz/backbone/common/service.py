import dataclasses
import typing

from backbone.common import cord, protocol


@dataclasses.dataclass(frozen=True)
class Endpoint:
    action: str
    reactor: typing.Callable
    view: str = dataclasses.field(default="default")
    version: str = dataclasses.field(default="latest")
    ingress: typing.Optional[cord.Record] = dataclasses.field(default=None)
    egress: typing.Optional[cord.Record] = dataclasses.field(default=None)


@dataclasses.dataclass(frozen=True)
class Error(Exception):
    code: str
    message: str

    def __str__(self):
        return f"{self.code}: {self.message}"

    @classmethod
    def load(cls, obj: protocol.ServiceError):
        return cls(code=obj.code, message=obj.message)

    def dump(self):
        return protocol.ServiceError(code=self.code, message=self.message)
