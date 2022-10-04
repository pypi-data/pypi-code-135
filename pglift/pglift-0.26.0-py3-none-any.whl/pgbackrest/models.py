from typing import Optional

from pydantic import Field, SecretStr

from .. import types


class RestoreManifest(types.Manifest):
    stanza: str = Field(
        description="pgBackRest stanza of the primary instance to restore from."
    )


class ServiceManifest(types.ServiceManifest, service_name="pgbackrest"):

    password: Optional[SecretStr] = Field(
        default=None,
        description="Password of PostgreSQL role for pgBackRest.",
        exclude=True,
    )
    restore: Optional[RestoreManifest] = Field(default=None, readOnly=True)
