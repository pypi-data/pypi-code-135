# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['notes_compiler', 'notes_compiler.resources']

package_data = \
{'': ['*']}

install_requires = \
['Markdown>=3.4.1,<4.0.0',
 'Pygments>=2.13.0,<3.0.0',
 'markdown-katex>=202112.1034,<202113.0',
 'pymdown-extensions>=9.5,<10.0',
 'python3-markdown-extension-graphviz>=0.1.0,<0.2.0']

entry_points = \
{'console_scripts': ['notes = notes_compiler.main:main']}

setup_kwargs = {
    'name': 'notes-compiler',
    'version': '0.3.2',
    'description': '',
    'long_description': '# notes-compiler\n\n## Usage\n\n```bash\nnotes <input_path> <output_path>\n```\n\nFor example:\n\n```bash\nnotes ./src ./public\n```\n\n## Installation\n\n### Release version\n\nInstall using pip (or your choice of PyPI package manager):\n\n```bash\npip install notes-compiler\n```\n\n### Installing latest master from source\n\nWhile on the root of this repository:\n\n```bash\npoetry install\npoetry build\ncd dist\npip install notes_compiler-<VERSION>-py3-none-any.whl --force-reinstal\n```\n\nreplacing `<VERSION>` with the actual version number.\n',
    'author': 'Manuel Brea',
    'author_email': 'm.brea.carreras@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
