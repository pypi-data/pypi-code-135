# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['command_mk2']

package_data = \
{'': ['*']}

install_requires = \
['aiogram==3.0.0b5']

setup_kwargs = {
    'name': 'command-mk2',
    'version': '0.1.1',
    'description': 'Custom version of Command filter for aiogram 3',
    'long_description': "### Filter CommandMk2 Aiogram 3\n\n![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)\n\n---\n\nImproved command filter\n\n```python\nclass RestrictModel(BaseModel):\n    period: date\n    reason: Optional[str]\n\n\n@router.message(CommandMk2('ban {period} {reason}', response_model=RestrictModel, response_model_name='vars'))\nasync def ban_user(message: Message, period: date, reason: Optional[str]):\n    ...\n```\n\nDiff:\n\n- Command arguments parsing, not just leaving single string like built-in aiogram filter\n- Command arguments separation and validation using Pydantic model.\n",
    'author': 'Aleksandr Antonov',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/AbstractiveNord/CommandMk2',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
