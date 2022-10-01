# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['benchling_sdk',
 'benchling_sdk.apps',
 'benchling_sdk.apps.config',
 'benchling_sdk.apps.helpers',
 'benchling_sdk.auth',
 'benchling_sdk.docs',
 'benchling_sdk.helpers',
 'benchling_sdk.models',
 'benchling_sdk.services',
 'benchling_sdk.services.v2',
 'benchling_sdk.services.v2.alpha',
 'benchling_sdk.services.v2.beta',
 'benchling_sdk.services.v2.stable']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'attrs>=20.1.0,<22.0',
 'backoff>=1.10.0,<2.0.0',
 'benchling-api-client==2.0.41',
 'dataclasses-json>=0.5.2,<0.6.0',
 'httpx>=0.23.0',
 'python-dateutil>=2.8.0,<3.0.0',
 'typing-extensions>=3.7.4,<5.0']

setup_kwargs = {
    'name': 'benchling-sdk',
    'version': '1.5.0a1',
    'description': 'SDK for interacting with the Benchling Platform.',
    'long_description': '# Benchling SDK\n\nA Python 3.7+ SDK for the [Benchling](https://www.benchling.com/) platform designed to provide typed, fluent\ninteractions with [Benchling APIs](https://docs.benchling.com/reference).\n\n## Installation\n\nInstall the dependency via [Poetry](https://python-poetry.org/) (if applicable):\n\n```bash\npoetry add benchling-sdk\n```\n \nOr [Pip](https://pypi.org/project/pip/):\n \n```bash\npip install benchling-sdk\n```\n\n## Documentation\n\nDocumentation for the SDK is kept up-to-date at [docs.benchling.com](https://docs.benchling.com), and you can get started with\nit using this guide:\n[https://docs.benchling.com/docs/getting-started-with-the-sdk](https://docs.benchling.com/docs/getting-started-with-the-sdk).\n\n## Support\n\nTo report issues with using the SDK, contact [support@benchling.com](mailto:support@benchling.com).\n',
    'author': 'Benchling Support',
    'author_email': 'support@benchling.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
