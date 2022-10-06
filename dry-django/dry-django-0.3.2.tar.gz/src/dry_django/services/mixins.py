from functools import cached_property
from typing import Generic, TypeVar, Any

from django.db.models import Model
from dry_core import operation
from dry_core.services import ServiceInstanceMixin


__all__ = ["ServiceModelInstanceMixin", "CreateServiceMixin", "UpdateServiceMixin", "DestroyServiceMixin"]


_DjangoModelTypeVar = TypeVar("_DjangoModelTypeVar", bound=Model)


class ServiceModelInstanceMixin(ServiceInstanceMixin[_DjangoModelTypeVar], Generic[_DjangoModelTypeVar]):
    def __init__(self, *args, **kwargs):
        super(ServiceModelInstanceMixin, self).__init__(*args, **kwargs)

    @cached_property
    def _model_field_names(self) -> set[str]:
        return {field.name for field in self.model._meta.get_fields()}

    def _filter_kwargs_by_model_fields(self, kwargs: dict[str, Any]):
        return {key: value for key, value in kwargs.items() if key in self._model_field_names}

    def save(self, commit: bool = True) -> None:
        if self.instance is None:
            return
        if not commit:
            return
        self.instance.save()


class CreateServiceMixin(ServiceModelInstanceMixin[_DjangoModelTypeVar], Generic[_DjangoModelTypeVar]):
    @operation
    def create(self, *, commit: bool = True, **kwargs) -> _DjangoModelTypeVar:
        self.instance: _DjangoModelTypeVar = self.model(**self._filter_kwargs_by_model_fields(kwargs))
        self.save(commit=commit)
        return self.instance

    @operation
    async def acreate(self, *, commit: bool = True, **kwargs) -> _DjangoModelTypeVar:
        if commit:
            self.instance: _DjangoModelTypeVar = await self.model.objects.acreate(
                **self._filter_kwargs_by_model_fields(kwargs)
            )
        else:
            self.instance: _DjangoModelTypeVar = self.model(**self._filter_kwargs_by_model_fields(kwargs))
        return self.instance


class UpdateServiceMixin(ServiceModelInstanceMixin[_DjangoModelTypeVar], Generic[_DjangoModelTypeVar]):
    @operation
    def update(self, *, commit: bool = True, **kwargs) -> _DjangoModelTypeVar:
        self.validate_instance_filled()
        for attr, value in self._filter_kwargs_by_model_fields(kwargs).items():
            setattr(self.instance, attr, value)
        self.save(commit=commit)
        return self.instance

    @operation
    async def aupdate(self, *, commit: bool = True, **kwargs) -> _DjangoModelTypeVar:
        self.validate_instance_filled()
        for attr, value in self._filter_kwargs_by_model_fields(kwargs).items():
            setattr(self.instance, attr, value)
        self.save(commit=commit)
        return self.instance


class DestroyServiceMixin(ServiceModelInstanceMixin[_DjangoModelTypeVar], Generic[_DjangoModelTypeVar]):
    @operation
    def destroy(self) -> _DjangoModelTypeVar:
        self.validate_instance_filled()
        destroyed_instance: _DjangoModelTypeVar = self.instance
        self.instance.delete()
        self.instance = None
        return destroyed_instance

    @operation
    async def adestroy(self) -> _DjangoModelTypeVar:
        self.validate_instance_filled()
        destroyed_instance: _DjangoModelTypeVar = self.instance
        self.instance.delete()
        self.instance = None
        return destroyed_instance
