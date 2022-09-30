from __future__ import annotations

import psutil
import os

from typing import Any, MutableMapping, Mapping, Iterable, Iterator, Sequence

def checkIfProcessRunning(processName: str) -> bool:
    '''
    Check if there is any running process that contains the given name
        processName.
    '''
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (
                psutil.NoSuchProcess, psutil.AccessDenied,
                psutil.ZombieProcess):
            pass
    return False

def make_dir(path: os.PathLike[str]) -> None:
    """"
    Create folder if folder does not exist and check permissions for the 
    created folder.
    """
    curr_dir = os.getcwd()
    try:
        temp_file = 'temp.txt'
        if not os.path.exists(path):
            os.makedirs(path)
        os.chdir(path)
        with open(temp_file,'w') as temp:
            pass
    except PermissionError:
        raise PermissionError(f'Please check permission for {path} folder')
    except:
        raise RuntimeError(f'Unknown error occurred when accessing {path} folder')
    finally:
        os.remove(temp_file) if os.path.exists(temp_file) else None
        os.chdir(curr_dir)


def merge_dicts(dest: MutableMapping[str, Any], other: Mapping[str, Any]) -> MutableMapping[str, Any]:
    for k, v in other.items():
        if k in dest and isinstance(dest[k], MutableMapping) and isinstance(v, Mapping):
            merge_dicts(dest[k], v)
        else:
            dest[k] = v
    return dest


class TableIterator(Iterator):
    def __init__(self, data: Iterable, fields: Sequence[str]) -> None:
        self._data = data
        self._fields = fields

    def __get_field(self, _o: Any, _f, _d: Any = None) -> Any:
        if isinstance(_f, str):
            return getattr(_o, _f, _d)
        elif isinstance(_f, Sequence):
            if len(_f) == 2:
                return _f[1](getattr(_o, _f[0], _d))
            elif len(_f) == 3:
                return _f[1](getattr(_o, _f[0], _f[2]))

    def __iter__(self) -> TableIterator:
        self._iter = iter(self._data)
        return self

    def __next__(self) -> Sequence[Any]:
        obj = next(self._iter)
        return [self.__get_field(obj, f) for f in self._fields]


__all__ = ['checkIfProcessRunning', 'make_dir', 'merge_dicts', 'TableIterator']
