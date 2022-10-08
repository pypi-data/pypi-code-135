# pylint: disable=no-member
import io
import os
import shutil
from pathlib import Path
from typing import Dict, Optional

import docutils.io  # pylint: disable=import-error

from .mock import mock

base_path = os.getcwd()
virtual_files: Dict[str, str] = {}


def startstrip(search: str, pattern: str) -> Optional[str]:
    search, pattern = str(search), str(pattern)
    if search.startswith(pattern):
        return search[len(pattern) :]
    return None


def find_virtual(path: str) -> Optional[str]:
    match = startstrip(path, base_path)
    if match is not None and match[1:] in virtual_files:
        return virtual_files[match[1:]]
    return None


@mock(os.walk, module=os)
def os_walk(*args, **kwargs):
    for path, dirs, files in os.walk.original(*args, **kwargs):
        if path == base_path:
            files += [
                virtual_file_name.split(os.path.sep)[-1]
                for virtual_file_name in virtual_files
            ]
        yield path, dirs, files


@mock(os.access, module=os)
def os_access(*args, **kwargs):
    if find_virtual(args[0]):
        return True

    return os.access.original(*args, **kwargs)


@mock(os.stat, module=os)
def os_stat(*args, **kwargs):
    if find_virtual(args[0]):
        return os.stat_result([0] * 10)

    return os.stat.original(*args, **kwargs)


@mock(open, module=docutils.io)
def docutils_io_opem(*args, **kwargs):
    file_match = find_virtual(args[0])

    if file_match:
        return io.TextIOWrapper(io.BytesIO(file_match.encode('utf-8')))

    return docutils.io.open.original(*args, **kwargs)


@mock(shutil.copyfile, module=shutil)
def shutil_copyfile(*args, **kwargs):
    file_match = find_virtual(args[0])
    if file_match:
        Path(args[1]).write_text(file_match, encoding="utf-8")
        return True
    return shutil.copyfile.original(*args, **kwargs)
