from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar, Callable, Union

T = TypeVar("T")


class Designed(Generic[T], ABC):
    """
    an abstraction of a value to be created with DI with overriding Design.
    """

    @property
    @abstractmethod
    def design(self) -> "Design":
        pass

    @property
    @abstractmethod
    def internal_injected(self) -> "Injected":
        pass

    @staticmethod
    def from_data(design: "Design", injected: "Injected"):
        return PureDesigned(design, injected)

    @staticmethod
    def bind(target: Union["Injected"]):
        from pinject_design import Injected
        from pinject_design.di.util import EmptyDesign
        if isinstance(target, Callable):
            return Designed.bind(Injected.bind(target))
        if isinstance(target, Injected):
            return PureDesigned(EmptyDesign, target)
        else:
            raise TypeError("target must be a subclass of Injected")

    def override(self, design: "Design"):
        return PureDesigned(self.design + design, self.internal_injected)


@dataclass
class PureDesigned(Designed):
    _design: "Design"
    _internal_injected: "Injected"

    @property
    def design(self) -> "Design":
        return self._design

    @property
    def internal_injected(self) -> "Injected":
        return self._internal_injected
