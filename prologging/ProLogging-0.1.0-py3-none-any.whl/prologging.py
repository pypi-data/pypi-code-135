import os
import sys

class PrettyLog:
    def __init__(self, handler = None, output = None) -> None:
        self.handler = handler
        self.output = output

    def ERROR(self, msg: str) -> None:
        __type = "ERROR"
        self.handler(msg=msg, type=__type)
        if self.output:
            self.output(msg=msg, type=__type)

    def INFO(self, msg: str) -> None:
        __type = "INFO"
        self.handler(msg=msg, type=__type)
        if self.output:
            self.output(msg=msg, type=__type)

    def WARNING(self, msg: str) -> None:
        __type = "WARNING"
        self.handler(msg=msg, type=__type)
        if self.output:
            self.output(msg=msg, type=__type)

    def DEBUG(self, msg: str) -> None:
        __type = "DEBUG"
        self.handler(msg=msg, type=__type)
        if self.output:
            self.output(msg=msg, type=__type)