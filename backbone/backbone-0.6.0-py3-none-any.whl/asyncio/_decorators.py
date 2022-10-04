import functools
import typing

from backbone.common import cord


def endpoint(
    action: str,
    ingress: typing.Optional[typing.Type[cord.Record]] = None,
    egress: typing.Optional[typing.Type[cord.Record]] = None,
):
    def endpoint_(method):
        @functools.wraps(method)
        def endpoint__(self, *args, **kwargs):
            if action not in self._origin:
                self._origin.add_reactor(action, ingress, egress)

            return method(self, *args, **kwargs)

        return endpoint__

    return endpoint_
