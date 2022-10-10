import glob
import os


def clear_directory(path: str):
    target = os.path.join(path, '*')
    for path in glob.glob(target):
        os.remove(path)


def get_real_path(path: str) -> str:
    for f in [
        os.path.expandvars,
        os.path.expanduser,
        os.path.realpath,
    ]:
        path = f(path)
    return path


def get_filename(path: str) -> str:
    return os.path.basename(path)


def get_filename_without_file_extension(path: str) -> str:
    filename = get_filename(path)
    return os.path.splitext(filename)[0]
