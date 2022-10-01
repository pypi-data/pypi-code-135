import os
import sys
import platform
from pathlib import Path
from configparser import ConfigParser

OS_PLATFORM = platform.system()


def colorize(text, color="HEADER"):
    class bcolors:
        HEADER = '\033[95m'
        BLUE = '\033[94m'
        CYAN = '\033[96m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    return f"{getattr(bcolors, color)}{text}\33[0m"


def get_firefox_profile_dir_path():
    mozilla_profile_ini = os.path.join(
        get_firefox_path(), r'profiles.ini')

    parser = ConfigParser()
    parser.read(mozilla_profile_ini)

    default_profile_path = os.path.normpath(os.path.join(
        get_firefox_path(), parser.get('Profile0', 'Path')))

    return default_profile_path


def get_resources_path():
    return os.path.join(os.path.dirname(
        __file__), 'resources')


def get_mozilla_path():
    linux_path = [Path.home(), ".mozilla"]
    win_path = [os.getenv("APPDATA"), "Mozilla"]

    return os.path.join(*plateform_switch(linux_path, win_path))


def get_firefox_path():
    linux_path = [get_mozilla_path(), "firefox"]
    win_path = [get_mozilla_path(), "Firefox"]

    return os.path.join(*plateform_switch(linux_path, win_path))


def plateform_switch(linux_cb, windows_cb, linux_args=(), windows_args=()):
    if OS_PLATFORM == "Linux":
        if(isinstance(linux_cb, str) or isinstance(linux_cb, list)):
            return linux_cb

        if(linux_args):
            return linux_cb(linux_args)

        return linux_cb()

    elif OS_PLATFORM == "Windows":
        if(isinstance(windows_cb, str) or isinstance(linux_cb, list)):
            return windows_cb

        if(windows_args):
            return windows_cb(windows_args)

        return windows_cb()
    else:
        return sys.exit("Unrecognized platform")
