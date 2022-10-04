import abc
import contextlib
import enum
import typing

import halo
import typer

from backbone.common import models


class Format(str, enum.Enum):
    PLAIN = "plain"
    DECORATED = "decorated"


class Formatter(abc.ABC):
    @abc.abstractmethod
    @contextlib.contextmanager
    def begin(self, message: str):
        """Begin an operation"""
        ...

    @abc.abstractmethod
    def success(self, message: str):
        """Succeed an operation"""
        ...

    @abc.abstractmethod
    def failure(self, message: str):
        """Fail an operation"""
        ...

    @abc.abstractmethod
    def info(self, message: str):
        """Provide information pertaining to an operation"""
        ...

    @abc.abstractmethod
    def result(self, obj: typing.Any):
        """Display the result of an operation"""
        ...

    @staticmethod
    def raw(message: str):
        """Display raw text"""
        typer.echo(message)

    def display_grant(self, grant):
        permissions = grant.permissions
        recipient_type, identity = grant.recipient

        if isinstance(identity, (models.UserIdentity, models.WorkspaceIdentity)):
            identifier = identity.name
        elif isinstance(identity, models.NamespaceIdentity):
            identifier = identity.path
        else:
            self.failure(f"Unknown recipient type: {recipient_type}")
            raise typer.Exit()

        self.info(f"[{recipient_type}] {identifier}: {sorted(list(permission.name for permission in permissions))}")


class PlainFormatter(Formatter):
    @contextlib.contextmanager
    def begin(self, message: str):
        yield

    def success(self, message: str):
        self.raw(message)

    def failure(self, message: str):
        typer.echo(message, err=True)

    def info(self, message: str):
        self.raw(message)

    def result(self, obj: typing.Any):
        pass


class DecoratedFormatter(Formatter):
    def __init__(self):
        self._halo = None

    @property
    def halo(self):
        if not self._halo:
            self._halo = halo.Halo()
        return self._halo

    @contextlib.contextmanager
    def begin(self, message: str):
        self._halo = halo.Halo(message)
        self.halo.start()
        yield
        self.halo.stop()

    def success(self, message: str):
        self.halo.succeed(message)

    def failure(self, message: str):
        self.halo.fail(message)

    def info(self, message: str):
        self.halo.info(message)

    def result(self, obj: typing.Any):
        pass
