from io import open
from setuptools import setup

version = '1.0.2'

with open('./README.md', encoding = 'utf-8') as readme:
    long_description = readme.read()

setup(
    name = 'canvas_markup',
    version = version,

    author = 'Xpos587',
    author_email = 'x30827pos@gmail.com',

    description = 'Canvas-markup generates images',

    long_description = long_description,
    long_description_content_type = 'text/markdown',

    url = 'https://github.com/Xpos587/Canvas-markup-py',
    download_url = f'https://github.com/Xpos587/Canvas-markup-py/tree/master/releases/v{version}.zip',

    license = 'MIT License, Copyright (c) 2022 Xpos587, see LICENSE file.',
    packages = ['canvas_markup'],

    requires = ['os', 'pyppeteer', 'jinja2', 'asyncio']
)