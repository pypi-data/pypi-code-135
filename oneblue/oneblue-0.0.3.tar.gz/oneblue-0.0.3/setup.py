#!/usr/bin/env Python
# -*- coding: utf-8 -*-
# (Script for Setting-up) Oneblue
# ===
# GNU General Public License v3.0, This file is part of Oneblue.
#             Copyright (C) 2022 凪坤 (GitHub ID: sandyzikun)
# -*-
# Oneblue is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# -*-
# Oneblue is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# -*-
# You should have received a copy of the GNU General Public License
# along with Oneblue. If not, see <https://www.gnu.org/licenses/>.
# -*-
import setuptools
setuptools.setup(
    name = "oneblue",
    version = "0.0.3",
    description = "A Simple Colormap for Matplotlib",
    long_description = open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/sandyzikun/oneblue.git",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        ],
    packages = setuptools.find_packages(),
    install_requires = ["numpy>=1.14.3", "matplotlib>=2.2.2"],
    )