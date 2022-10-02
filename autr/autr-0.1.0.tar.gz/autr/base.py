import typing

import os
import pathlib

ALLOW_MULTIPLE_READERS = True


class Reader:
    _REGISTRY = {}

    @staticmethod
    def _validate_extensions(
        cls, extensions: typing.Union[typing.Tuple[str], typing.List[str]]
    ):
        if not extensions or not isinstance(extensions, (list, tuple)):
            raise TypeError(f"Invalid type for extensions in {cls}")

        return tuple(extensions) if isinstance(extensions, list) else extensions

    def __init_subclass__(
        cls,
        extensions: typing.Union[typing.Tuple[str], typing.List[str]],
        *args,
        **kwargs,
    ):
        super().__init_subclass__(*args, **kwargs)
        extensions = Reader._validate_extensions(cls, extensions)
        for extension in extensions:
            if extension in cls._REGISTRY:
                if ALLOW_MULTIPLE_READERS:
                    if not isinstance(cls._REGISTRY[extension], list):
                        cls._REGISTRY[extension] = [cls._REGISTRY[extension]]

                    cls._REGISTRY[extension].append(cls)
                else:
                    raise TypeError(
                        f"Another class for the extension {extension} already exists: {cls._REGISTRY[extension]}"
                    )
            else:
                cls._REGISTRY[extension] = cls

        cls.__extensions = extensions

    def __new__(cls, filename: str, *args, **kwargs):
        extension = pathlib.Path(filename).suffix

        if extension not in cls._REGISTRY:
            raise ValueError("Invalid extension")

        cls_return = cls._REGISTRY[extension]

        if isinstance(cls._REGISTRY[extension], list):
            cls_return = cls_return[0]

        return object.__new__(cls_return)

    def _read(self, filename: str, *args, **kwargs) -> typing.Any:
        raise NotImplementedError

    def _write(self, filename: str, *args, **kwargs):
        raise NotImplementedError

    @property
    def extensions(self) -> typing.Tuple[str]:
        return self.__extensions

    __extensions: typing.Union[typing.Tuple[str], typing.List[str]]

    def __init__(
        self,
        filename: str,
        check_exists: bool = True,
        data: typing.Any = None,
        *args,
        **kwargs,
    ):
        if (check_exists and not os.path.exists(filename)) and data is None:
            raise FileNotFoundError(f"File was not found: {filename}")

        if not filename.endswith(self.extensions):
            raise ValueError(f"Unsupported extension. Valid values: {self.extensions}")

        if data:
            self._data = data
            self._write(filename, *args, **kwargs)
        else:
            self._data = self._read(filename, *args, **kwargs)

    @property
    def data(self) -> typing.Any:
        return self._data


def read(filename: str, *args, **kwargs) -> typing.Any:
    return Reader(filename, *args, **kwargs).data


def write(data: typing.Any, filename: str, *args, **kwargs):
    Reader(filename, *args, data=data, **kwargs)
