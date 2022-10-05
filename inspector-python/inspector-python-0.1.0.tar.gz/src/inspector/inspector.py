from __future__ import annotations
from . import Configuration
from src.inspector.models.enums import TransportType


# import http.client
# import multiprocessing


class Inspector:
    # Agent configuration.
    # type: Configuration
    _configuration: Configuration = None

    # Transport strategy.
    # type:
    _transport = None

    # Current transaction.
    # type:
    _transaction = None

    # Runa callback before flushing data to the remote platform.
    # type:
    _beforeCallbacks = []

    def __init__(self, configuration: Configuration):
        if configuration.get_transport() == TransportType.ASYNC:
            # self._transport = AsyncTransport(configuration)
            pass
        else:
            # self._transport = CurlTransport(configuration)
            pass

    def set_transport(self, resolver):
        pass

    def start_transaction(self, name):
        pass

    # Get current transaction instance.
    # return null|Transaction
    def current_transaction(self):
        return self._transport

    # Determine if an active transaction exists.
    # return: bool
    def has_transaction(self) -> bool:
        return True if self._transaction else False

    # Determine if the current cycle hasn't started its transaction yet.
    # return: bool
    def need_transaction(self) -> bool:
        return self.is_recording() and not self.has_transaction()

    # Determine if a new segment can be added.
    # return: bool
    def can_add_segments(self) -> bool:
        return self.is_recording() and self.has_transaction()

    # Check if the monitoring is enabled.
    # return: bool
    def is_recording(self) -> bool:
        return self._configuration.is_enabled()

    # Enable recording.
    # return: Inspector
    def start_recording(self) -> Inspector:
        self._configuration.set_enabled(True)
        return self

    # Disable recording.
    # return: Inspector
    def stop_recording(self) -> Inspector:
        self._configuration.set_enabled(False)
        return self

    def start_segment(self, type, label=None):
        pass

    def add_segment(self, callback, type, label=None, throw=False):
        pass

    def report_exception(self, exception, handled=True):
        pass

    def add_entries(self, entries):
        pass

    @staticmethod
    def before_flush(self, callback):
        pass

    def flush(self):
        pass
