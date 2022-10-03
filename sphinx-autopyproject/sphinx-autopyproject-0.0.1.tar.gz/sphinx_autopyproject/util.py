import os
from contextlib import contextmanager


@contextmanager
def restore_cwd():
    cwd = os.getcwd()
    try:
        yield
    finally:
        os.chdir(cwd)
