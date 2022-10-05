import os
import sys

class Logger:
    def __init__(self, handler = None, output = None, copy_path: str = None) -> None:
        self.handler = handler
        self.output = output
        self.copy = copy_path

    def ERROR(self, msg: str, peer: str = None) -> None:
        __type = "ERROR"
        if peer:
            msg = f"{peer} → {msg}"
        self.handler(msg=msg, type=__type, copy_path=self.copy)
        if self.output:
            self.output(msg=msg, type=__type)

    def INFO(self, msg: str, peer: str = None) -> None:
        __type = "INFO"
        if peer:
            msg = f"{peer} → {msg}"
        self.handler(msg=msg, type=__type, copy_path=self.copy)
        if self.output:
            self.output(msg=msg, type=__type)

    def WARNING(self, msg: str, peer: str = None) -> None:
        __type = "WARNING"
        if peer:
            msg = f"{peer} → {msg}"
        self.handler(msg=msg, type=__type, copy_path=self.copy)
        if self.output:
            self.output(msg=msg, type=__type)

    def DEBUG(self, msg: str, peer: str = None) -> None:
        __type = "DEBUG"
        if peer:
            msg = f"{peer} → {msg}"
        self.handler(msg=msg, type=__type, copy_path=self.copy)
        if self.output:
            self.output(msg=msg, type=__type)