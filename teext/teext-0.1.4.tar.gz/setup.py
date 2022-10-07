# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['teext']

package_data = \
{'': ['*']}

install_requires = \
['typing-extensions>=4.4.0,<5.0.0']

setup_kwargs = {
    'name': 'teext',
    'version': '0.1.4',
    'description': 'Typing extensions extensions',
    'long_description': '# teext – typing extensions extensions\n\nPackage which provides useful types.\n\n### [Documentation](https://wearepal.github.io/teext/)\n\n## Examples\n\n### Value-constraint types without runtime overhead\n\nThese types are most useful in conjunction with static type checkers like mypy.\n\n```python\nimport teext as tx\n\ndef f(x: tx.PositiveInt) -> None:\n    print(x)\n\na = 5\nassert tx.is_positive_int(a)\nf(a)  # OK\nf(7)  # works at runtime but mypy gives error\n\nassert tx.is_positive_int(-3)  # AssertionError\n```\n',
    'author': 'Thomas MK',
    'author_email': 'tmke@posteo.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
