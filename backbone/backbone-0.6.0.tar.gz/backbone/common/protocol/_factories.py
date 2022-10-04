import typing

from backbone.common import cord

T = typing.TypeVar("T", bound=cord.Record)


class WorkspaceBound(cord.Record):
    workspace_name: str = cord.StringField()
    data: typing.Optional[T] = cord.OptionalField(cord.RecordField(T))

    def __init__(self, workspace_name: str, data: typing.Optional[T] = None):
        super().__init__(workspace_name=workspace_name, data=data)


class StreamBound(cord.Record):
    stream_name: str = cord.StringField()
    data: typing.Optional[T] = cord.OptionalField(cord.RecordField(T))

    def __init__(self, stream_name: str, data=None):
        super().__init__(stream_name=stream_name, data=data)
