#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='hhl_game',
    version='1.0.1',
    description=(
        'a game engine made by pygame'
    ),
    long_description=open('README.rst').read(),
    author='sjh',
    author_email='1607837367@qq.com',
    maintainer='sjh',
    maintainer_email='1607837367@qq.com',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/apammaaaa/fast_game',
    install_requires = ["pygame"]          #这个项目需要的第三方库
)