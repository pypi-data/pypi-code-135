import re
from typing import Any, Type
from rest_framework import generics
from rest_framework.serializers import BaseSerializer
from .exceptions import InvalidAPIVersion


class GenericAPIView(generics.GenericAPIView):
    """
    Extends GenericAPIView to add support for resolving serializer class based on the requested API version.
    """

    VERSION_FORMAT = re.compile("\d+\.\d+")

    def get_serializer_class(self, *args: Any, **kwargs: Any) -> Type[BaseSerializer]:
        assert (
            self.serializer_class is not None
        ), "serializer_class attribute is required to support version-less requests."

        version_serializer_attr = self._get_version_serializer_attr()
        if version_serializer_attr and hasattr(self, version_serializer_attr):
            return getattr(self, version_serializer_attr)

        return self.serializer_class

    def _get_version_serializer_attr(self) -> "str | None":
        formatted_version = self._get_formatted_version()

        if formatted_version is None:
            return None

        return "serializer_class_v{}".format(formatted_version)

    def _get_formatted_version(self) -> "str | None":
        if self.request.version is None:
            return None

        if self.VERSION_FORMAT.match(self.request.version) is None:
            raise InvalidAPIVersion()

        return self.request.version.replace(".", "_")
