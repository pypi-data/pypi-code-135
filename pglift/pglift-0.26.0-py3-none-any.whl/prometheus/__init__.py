import logging
from typing import TYPE_CHECKING, Optional, Type

from .. import hookimpl, systemd, util
from ..models import interface
from . import impl, models
from .impl import apply as apply
from .impl import available as available
from .impl import start as start
from .impl import stop as stop
from .models import PostgresExporter as PostgresExporter
from .models import ServiceManifest

if TYPE_CHECKING:
    import click
    from pgtoolkit.conf import Configuration

    from ..ctx import BaseContext
    from ..models import system
    from ..settings import Settings, SystemdSettings

__all__ = ["PostgresExporter", "apply", "available", "start", "stop"]

logger = logging.getLogger(__name__)


def register_if(settings: "Settings") -> bool:
    return available(settings) is not None


@hookimpl  # type: ignore[misc]
def system_lookup(
    ctx: "BaseContext", instance: "system.PostgreSQLInstance"
) -> Optional[models.Service]:
    settings = available(ctx.settings)
    assert settings is not None
    return impl.system_lookup(ctx, instance.qualname, settings)


@hookimpl  # type: ignore[misc]
def interface_model() -> Type[models.ServiceManifest]:
    return models.ServiceManifest


@hookimpl  # type: ignore[misc]
def get(
    ctx: "BaseContext", instance: "system.Instance"
) -> Optional[models.ServiceManifest]:
    try:
        s = instance.service(models.Service)
    except ValueError:
        return None
    else:
        return models.ServiceManifest(port=s.port)


SYSTEMD_SERVICE_NAME = "pglift-postgres_exporter@.service"


@hookimpl  # type: ignore[misc]
def install_systemd_unit_template(
    ctx: "BaseContext", systemd_settings: "SystemdSettings", header: str = ""
) -> None:
    logger.info("installing systemd template unit for Prometheus postgres_exporter")
    settings = available(ctx.settings)
    assert settings is not None
    configpath = str(settings.configpath).replace("{name}", "%i")
    content = systemd.template(SYSTEMD_SERVICE_NAME).format(
        executeas=systemd.executeas(ctx.settings),
        configpath=configpath,
        execpath=settings.execpath,
    )
    systemd.install(
        SYSTEMD_SERVICE_NAME,
        util.with_header(content, header),
        systemd_settings.unit_path,
        logger=logger,
    )


@hookimpl  # type: ignore[misc]
def uninstall_systemd_unit_template(
    ctx: "BaseContext", systemd_settings: "SystemdSettings"
) -> None:
    logger.info("uninstalling systemd template unit for Prometheus postgres_exporter")
    systemd.uninstall(SYSTEMD_SERVICE_NAME, systemd_settings.unit_path, logger=logger)


@hookimpl  # type: ignore[misc]
def instance_configure(
    ctx: "BaseContext", manifest: "interface.Instance", config: "Configuration"
) -> None:
    """Install postgres_exporter for an instance when it gets configured."""
    settings = available(ctx.settings)
    if not settings:
        logger.warning(
            "Prometheus postgres_exporter not available, skipping monitoring configuration"
        )
        return
    impl.setup_local(ctx, manifest, settings, config)


@hookimpl  # type: ignore[misc]
def instance_start(ctx: "BaseContext", instance: "system.Instance") -> None:
    """Start postgres_exporter service."""
    try:
        service = instance.service(models.Service)
    except ValueError:
        return
    impl.start(ctx, service)


@hookimpl  # type: ignore[misc]
def instance_stop(ctx: "BaseContext", instance: "system.Instance") -> None:
    """Stop postgres_exporter service."""
    try:
        service = instance.service(models.Service)
    except ValueError:
        return
    impl.stop(ctx, service)


@hookimpl  # type: ignore[misc]
def instance_drop(ctx: "BaseContext", instance: "system.Instance") -> None:
    """Uninstall postgres_exporter from an instance being dropped."""
    settings = available(ctx.settings)
    if not settings:
        return
    impl.revert_setup(ctx, instance.qualname, settings)


@hookimpl  # type: ignore[misc]
def role(
    settings: "Settings", manifest: "interface.Instance"
) -> Optional[interface.Role]:
    service_manifest = manifest.service_manifest(ServiceManifest)
    if service_manifest is None:
        return None
    password = None
    if service_manifest.password:
        password = service_manifest.password.get_secret_value()
    assert settings.prometheus is not None
    return interface.Role(
        name=settings.prometheus.role,
        password=password,
        login=True,
        in_roles=["pg_monitor"],
    )


@hookimpl  # type: ignore[misc]
def cli() -> "click.Group":
    from .cli import postgres_exporter

    return postgres_exporter
