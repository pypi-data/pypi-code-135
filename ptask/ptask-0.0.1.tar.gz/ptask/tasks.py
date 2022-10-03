"""Task setups system."""

import os

from pathlib import Path
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

from ptask.const import OS
from ptask.utils import assert_condition


class FileTask(object):
    """
    File task define how to build the project.

    Usually it's a '.projecttask' or a 'tasks.ini' file to determine which
    command line will be called to build the project.

    File tasks.ini example:

        [win32]
        init='mkdir build && cd build && cmake .. -G "MinGW Makefiles"'
        build='cmake --build build'
        clean='rmdir build'
        test=...

        [macos]
        init='mkdir build && cmake -H. -B build'
        build='cmake --build build'
        clean='rm build'

        [linux]
        init='mkdir build && cmake -H. -B build'
        build='cmake --build build'
        clean='rm build'
    """

    DEFAULT_FILE = ['.projecttask', 'tasks.ini', '.config/tasks.ini']

    def __init__(self, file_task: str, project_path: str):
        """Setp the file task."""
        self.cmds = dict()

        self.project_path = Path(project_path)
        assert_condition(self.project_path.is_dir(), 'Project path is expected to be a directory!!')

        if file_task != '':
            self.file_task = Path(os.path.join(project_path, file_task))
            assert_condition(self.file_task.is_file(), 'File task is expected to be a file!!')
        else:
            for file_name in self.DEFAULT_FILE:
                path = os.path.join(self.project_path, file_name)
                if os.path.isfile(path):
                    self.file_task = Path(path)
                    break
            assert_condition(self.file_task.is_file(), 'File task cannot be found!!')

        self.__process_tasks()

    def get_build_args(self, build_type: str) -> list:
        """
        Get build args based on the input build type.

        Parameter:
            build_type (str) : The command build type user want to get.
        """
        assert_condition(build_type in self.cmds, 'Cannot find command in task file !!')
        return self.cmds[build_type]

    def __process_tasks(self):
        self.cmds.clear()

        config = ConfigParser()
        config.read(self.file_task)
        for section in config.sections():
            if section != OS:
                continue
            for option, cmd in config.items(section):
                self.cmds[option] = cmd

        assert_condition(self.cmds, 'Cannot find the corresponding OS command !!')
