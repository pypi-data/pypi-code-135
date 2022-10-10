#!/usr/bin/env python3
# -*- coding:utf-8; mode:python; -*-
#
# Copyright 2021 Pradyumna Paranjape
# This file is part of pyprojstencil.
#
# pyprojstencil is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyprojstencil is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pyprojstencil.  If not, see <https://www.gnu.org/licenses/>.
#
"""
Read yaml configuration
"""

import os
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional

import xdgpspconf

CONFIG_DISC = xdgpspconf.ConfDisc('ppstencil')


@dataclass
class PyConfig():
    """
    Configuration for Python project stencil.
    Values for commonly declared variables in python projects.
    The author must add the rest by hand.

    Attributes:
        project: project name
        version: project version
        description: project description
        years: copyright years
        license: project license [LGPLv3]
        license_header: project license header [LGPLv3]
        pyversion: compatible python version
        author: author's displayed name
        uname: author's user name
        email: author's email
        githost: host [remote] website for git
        branch: git's initial branch [default: `pagan`]
        url: project's url
        keys: all class key names
    """
    project: Path
    license: Path
    license_header: str = ('#\n' +
                           '# Contact the author(s) for License terms\n' +
                           '#\n')
    version: str = '0.0dev1'
    description: str = 'project - description'
    years: str = str(datetime.now().year)
    pyversion: str = "3"
    author: str = os.environ.get('USER', 'AUTHOR')
    email: Optional[str] = None
    url: Optional[str] = None
    uname: str = author.lower().replace(" ", "_")
    githost: str = "gitlab"
    branch: str = "pagan"

    def __repr__(self) -> str:
        """
        Representation of object
        """
        output = ['']
        for key, value in self.__dict__.items():
            output.append(f"{key}: {value}")
        output.append('')
        return '\n    '.join(output)


def read_config(project: Path, **kwargs) -> PyConfig:
    """
    Read standard configuration for project
    """
    project_args = list(
        CONFIG_DISC.read_config(flatten=True,
                                custom=kwargs.get('config')).values())[0]

    kwargs['config'] = None

    # remove unsupplied values
    kwargs = {key: val for key, val in kwargs.items() if val is not None}

    project_args.update(**kwargs)
    config = PyConfig(project=project, **project_args)
    return config
