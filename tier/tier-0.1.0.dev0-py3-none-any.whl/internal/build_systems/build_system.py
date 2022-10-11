# std
from __future__ import annotations
from typing import Optional as Opt

# internal
from tier.internal.errors import TierException


def get(build_backend: str, dirpath: Opt[str] = None) -> 'AbstractBuildSystem':
    from tier.internal.build_systems.poetry import Poetry
    if build_backend == Poetry.build_backend():
        return Poetry(dirpath)
    else:
        raise TierException('Could not determine build system')
