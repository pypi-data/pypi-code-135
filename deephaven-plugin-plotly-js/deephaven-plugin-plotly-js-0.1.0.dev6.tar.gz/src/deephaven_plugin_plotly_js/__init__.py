import pathlib

from deephaven.plugin import Registration
from deephaven.plugin.js import JsPlugin

from importlib.resources import files, as_file
from contextlib import contextmanager
from typing import Generator

from .__info__ import (
    __plugin_name__,
    __plugin_version__,
    __plugin_main__,
    __plugin_dist__,
)


class PlotlyJs(JsPlugin):
    @contextmanager
    def distribution_path(self) -> Generator[pathlib.Path, None, None]:
        with as_file(files(__package__)) as package:
            yield package / __plugin_dist__

    @property
    def name(self) -> str:
        return __plugin_name__

    @property
    def version(self) -> str:
        return __plugin_version__

    @property
    def main(self) -> str:
        return __plugin_main__


class PlotlyJsRegistration(Registration):
    @classmethod
    def register_into(cls, callback: Registration.Callback) -> None:
        callback.register(PlotlyJs)
