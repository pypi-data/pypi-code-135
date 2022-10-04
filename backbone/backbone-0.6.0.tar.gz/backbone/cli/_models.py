from dataclasses import dataclass
from enum import Enum
from typing import Optional

from backbone import sync as backbone
from backbone.cli._config import LocalConfiguration
from backbone.cli._format import Formatter


@dataclass
class Context:
    config: Optional[LocalConfiguration]
    client: Optional[backbone.Client]
    workspace_name: Optional[str]
    fmt: Formatter


class WorkspacePermission(Enum):
    MANAGE_WORKSPACE = "MANAGE_WORKSPACE"
    MANAGE_KEYSPACE = "MANAGE_KEYSPACE"


class KeyspacePermission(Enum):
    READ = "READ"
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
