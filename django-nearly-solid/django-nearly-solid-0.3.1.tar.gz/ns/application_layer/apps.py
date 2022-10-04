from abc import ABC
from typing import Callable

from django.apps import AppConfig

from ns.application_layer import registry
from ns.di.abc import Container
from ns.di.meta import ContainerMeta
from ns.di.utils import configure_dependencies_in_django
from ns.application_layer.entities.application import ApplicationData
from ns.application_layer.serialization.application import serialize_application
from ns.application_layer.typings import EntityMeta
from ns.utils import to_snake_case, is_pydantic_model, is_django_model, is_dataclass, is_enum, \
    import_classes_from_module


class NSAppConfig(ABC, AppConfig):
    # Настройки сущностей
    entities_apps = []  # В наследнике нужно переопределить
    entities_file_names = ['models', 'entities', 'enums']

    # Настройки сервисов
    services_apps = []  # В наследнике нужно переопределить
    services_files_names = ['services', 'service']

    # Настройки контейнеров
    containers_apps = []  # В наследнике нужно переопределить
    containers_file_names = ['containers', 'container']

    # Данные приложения
    application_data: ApplicationData
    containers: list[Callable] = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def ready(self):
        self.configure_dependencies()
        self.configure_application()

    def configure_dependencies(self):
        containers = self._import_containers()
        configure_dependencies_in_django(containers)

    def configure_application(self):
        services = self._import_services()
        registry.SERVICES.update(services)

        entities = self._import_entities()
        registry.ENTITIES += entities

        self.application_data = serialize_application(services, entities)

    def _import_containers(self) -> list[ContainerMeta]:
        result = []
        for app_module_name in [self.name, *self.containers_apps]:
            for container_module_name in self.containers_file_names:
                module_name = f'{app_module_name}.{container_module_name}'
                for cls in import_classes_from_module(module_name):
                    if issubclass(cls, Container):
                        result.append(cls)
        return result

    def _import_services(self) -> dict[str, type]:
        result = {}
        for app_module_name in [self.name, *self.services_apps]:
            for service_module_name in self.services_files_names:
                module_name = f'{app_module_name}.{service_module_name}'
                for cls in import_classes_from_module(module_name):
                    if cls.__name__.lower().endswith('service'):
                        service_name = self._get_service_name(cls.__name__)
                        result[service_name] = cls
        return result

    def _get_service_name(self, service_cls_name: str):
        snake_cls_name = to_snake_case(service_cls_name)
        if snake_cls_name.endswith('_service'):
            snake_cls_name = snake_cls_name.replace('_service', '')
        return snake_cls_name

    def _import_entities(self) -> list[EntityMeta]:
        models = []
        for app_module_name in [self.name, *self.entities_apps]:
            for entity_module_name in self.entities_file_names:
                module_name = f'{app_module_name}.{entity_module_name}'
                for cls in import_classes_from_module(module_name):
                    if is_pydantic_model(cls) or is_django_model(cls) or is_dataclass(cls) or is_enum(cls):
                        cls: EntityMeta
                        models.append(cls)
        return models
