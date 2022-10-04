import logging
from typing import TYPE_CHECKING, Dict, Literal, Optional, Type

import pgtoolkit.conf as pgconf

from .. import exceptions, hookimpl
from ..models import interface, system
from ..postgresql import Standby
from ..settings import PostgreSQLVersion
from . import impl, models
from .impl import available as available
from .impl import backup as backup
from .impl import expire as expire
from .impl import iter_backups as iter_backups
from .impl import restore as restore
from .models import ServiceManifest

if TYPE_CHECKING:
    import click

    from ..ctx import BaseContext
    from ..settings import Settings

__all__ = ["available", "backup", "expire", "iter_backups", "restore"]

logger = logging.getLogger(__name__)


def register_if(settings: "Settings") -> bool:
    return available(settings) is not None


@hookimpl  # type: ignore[misc]
def instance_configuration(
    ctx: "BaseContext", manifest: "interface.Instance"
) -> pgconf.Configuration:
    settings = available(ctx.settings)
    if not settings:
        return pgconf.Configuration()
    service_manifest = manifest.service_manifest(ServiceManifest)
    if service_manifest is None:
        return pgconf.Configuration()
    instance = system.BaseInstance.get(manifest.name, manifest.version, ctx)
    return impl.postgresql_configuration(instance.qualname, settings)


@hookimpl  # type: ignore[misc]
def interface_model() -> Type[models.ServiceManifest]:
    return models.ServiceManifest


@hookimpl  # type: ignore[misc]
def instance_configure(
    ctx: "BaseContext",
    manifest: "interface.Instance",
    config: pgconf.Configuration,
    creating: bool,
) -> None:
    """Install pgBackRest for an instance when it gets configured."""
    settings = available(ctx.settings)
    if not settings:
        logger.warning("pgbackrest not available, skipping backup configuration")
        return
    service_manifest = manifest.service_manifest(ServiceManifest)
    if service_manifest is None:
        return
    instance = system.PostgreSQLInstance.system_lookup(
        ctx, (manifest.name, manifest.version)
    )
    if instance.standby:
        return

    if creating and impl.enabled(instance.qualname, settings):
        if not ctx.confirm(
            f"Old pgbackrest repository exists for instance {instance}, continue by overwriting it?",
            False,
        ):
            raise exceptions.Cancelled("Pgbackrest repository already exists")
        impl.revert_init(ctx, instance, settings)
        impl.revert_setup(ctx, instance.qualname, settings, config, instance.datadir)

    impl.setup(ctx, instance.qualname, settings, config, instance.datadir)

    info = impl.backup_info(ctx, instance.qualname, settings)
    # Only initialize if the stanza does not already exist.
    if not info or info[0]["status"]["code"] == 1:
        password = None
        backup_role = role(ctx.settings, manifest)
        assert backup_role is not None
        if not backup_role.pgpass and backup_role.password is not None:
            password = backup_role.password.get_secret_value()
        impl.init(ctx, instance, settings, password)


@hookimpl  # type: ignore[misc]
def initdb(
    ctx: "BaseContext", manifest: "interface.Instance", instance: system.BaseInstance
) -> Optional[Literal[True]]:
    service_manifest = manifest.service_manifest(ServiceManifest)
    if service_manifest is None or service_manifest.restore is None:
        return None
    settings = available(ctx.settings)
    assert settings
    logger.info("creating instance from pgbackrest backup")
    cmd = [
        str(settings.execpath),
        "--log-level-file=off",
        "--log-level-stderr=info",
        "--config-path",
        str(settings.configpath),
        "--stanza",
        service_manifest.restore.stanza,
        "--pg1-path",
        str(instance.datadir),
    ]
    if manifest._standby():
        cmd.append("--type=standby")
    cmd.append("restore")
    ctx.run(cmd, check=True)
    return True


@hookimpl  # type: ignore[misc]
def instance_init_replication(
    ctx: "BaseContext",
    instance: system.BaseInstance,
    manifest: "interface.Instance",
    standby: Standby,
) -> Optional[bool]:
    service_manifest = manifest.service_manifest(ServiceManifest)
    if service_manifest is None or service_manifest.restore is None:
        return None
    if instance.version == PostgreSQLVersion.v11:
        path = instance.datadir / "recovery.conf"
    else:
        path = instance.datadir / "postgresql.auto.conf"
    config = pgconf.parse(str(path))
    logger.info("configure standby from pgbackrest backup")
    with config.edit() as entries:
        entries.add("primary_conninfo", standby.primary_conninfo)
        if standby.slot:
            entries.add("primary_slot_name", standby.slot)
    config.save()
    return True


@hookimpl  # type: ignore[misc]
def instance_drop(ctx: "BaseContext", instance: system.Instance) -> None:
    """Uninstall pgBackRest from an instance being dropped."""
    settings = available(ctx.settings)
    if not settings:
        return
    if not impl.enabled(instance.qualname, settings):
        return

    nb_backups = len(impl.backup_info(ctx, instance.qualname, settings)[0]["backup"])

    if not nb_backups or ctx.confirm(
        f"Confirm deletion of {nb_backups} backup(s) for instance {instance}?",
        True,
    ):
        impl.revert_init(ctx, instance, settings)
        impl.revert_setup(
            ctx, instance.qualname, settings, instance.config(), instance.datadir
        )


@hookimpl  # type: ignore[misc]
def instance_env(ctx: "BaseContext", instance: "system.Instance") -> Dict[str, str]:
    pgbackrest_settings = impl.available(ctx.settings)
    if not pgbackrest_settings:
        return {}
    return impl.env_for(instance, pgbackrest_settings)


@hookimpl  # type: ignore[misc]
def rolename(settings: "Settings") -> str:
    return settings.postgresql.backuprole.name


@hookimpl  # type: ignore[misc]
def role(
    settings: "Settings", manifest: "interface.Instance"
) -> Optional["interface.Role"]:
    name = rolename(settings)
    service_manifest = manifest.service_manifest(ServiceManifest)
    if service_manifest is None:
        return None
    password = None
    if service_manifest.password:
        password = service_manifest.password.get_secret_value()
    pgpass = settings.postgresql.backuprole.pgpass
    return interface.Role(
        name=name,
        password=password,
        login=True,
        superuser=True,
        pgpass=pgpass,
    )


@hookimpl  # type: ignore[misc]
def cli() -> "click.Command":
    from .cli import pgbackrest

    return pgbackrest


@hookimpl  # type: ignore[misc]
def instance_cli(group: "click.Group") -> None:
    from .cli import instance_backup, instance_backups, instance_restore

    group.add_command(instance_backup)
    group.add_command(instance_backups)
    group.add_command(instance_restore)
