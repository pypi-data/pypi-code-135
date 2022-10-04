from enum import Enum


class WorkspacePermission(Enum):
    MANAGE_WORKSPACE = 0x00
    MANAGE_KEYSPACE = 0x01


class KeyspacePermission(Enum):
    READ = 0x00
    CREATE = 0x01
    UPDATE = 0x02
    DELETE = 0x03
