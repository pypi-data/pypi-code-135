"""The main build process function."""

import os
import logging
import platform
import subprocess

from ptask.const import ARCH
from ptask.tasks import FileTask
from ptask.utils import assert_condition


def __print_dependencies() -> None:
    logging.info(
        '''Checking dependencies...

    ----------------------------------------------------------------------------
    Detect current platform information:
        - OS: %s
        - Arch: %s
        - Python: %s
    ----------------------------------------------------------------------------
    ''', platform.system(), ARCH, platform.python_version())


def build(build_type: str, custom_file: str, custom_path: str, print_info: bool) -> None:
    """
    Get all the input args and process the build.

    Parameters:
        build_type (str) : check whether the user want to init, compile or run.
        custom_file (str) : build the project using custom file task config.
        custom_path (str) : build the project using custom path.
        print_info (bool) : check if the user want to print build information.
    """
    if print_info:
        __print_dependencies()

    file_task = FileTask(custom_file, custom_path if custom_path != '' else os.getcwd())

    args = file_task.get_build_args(build_type)
    with subprocess.Popen(args, shell=True) as build_cmd:
        build_cmd.wait()
        assert_condition(build_cmd.returncode == 0, 'Build failed !!')

    logging.info('Project build finished !!')
