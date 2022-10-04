import os.path
import shutil
import stat


def ensure_can_be_deleted(path: str):
    os.chmod(path, stat.S_IWRITE)
    if os.path.isdir(path):
        for child in os.listdir(path):
            ensure_can_be_deleted(os.path.join(path, child))


def delete(path: str):
    ensure_can_be_deleted(path)
    shutil.rmtree(path)
