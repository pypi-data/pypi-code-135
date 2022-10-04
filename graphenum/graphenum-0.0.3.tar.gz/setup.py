# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['graphenum', 'graphenum.entities', 'graphenum.entities.graphql']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0']

entry_points = \
{'console_scripts': ['graphenum = graphenum:cli']}

setup_kwargs = {
    'name': 'graphenum',
    'version': '0.0.3',
    'description': 'GraphQL introspection and path enumeration.',
    'long_description': '# graphenum ![PyPI](https://img.shields.io/pypi/v/graphenum) [![CI](https://github.com/Escape-Technologies/graphenum/actions/workflows/ci.yaml/badge.svg)](https://github.com/Escape-Technologies/graphenum/actions/workflows/ci.yaml) [![CD](https://github.com/Escape-Technologies/graphenum/actions/workflows/cd.yaml/badge.svg)](https://github.com/Escape-Technologies/graphenum/actions/workflows/cd.yaml)\n\nIntrospect a GraphQL endpoint and generate his specification schema with path enumeration.\n\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/graphenum)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/graphenum)\n\n## Getting Started\n\nIt takes only two simple steps to introspect an endpoint using graphenum.\n\n```bash\npip install graphenum\ngraphenum -u https://example.com/graphql -o schema.json\n```\n\n## Options\n\nGraphEnum supports the following options:\n\n```bash\ngraphenum \\\n# url of the GraphQL endpoint\n-u/--url https://example.com/graphql \\\n# input schema file (raw GraphQL schema)\n-s/--schema-path schema.json \\\n# output file name\n-o/--output-schema schema.json \\\n# verbose output\n-v/--verbose\n```\n\n## Environment Variables\n\n**Logger** - *No effect if you pass your own logger*\n| Name | Values  | Default| Behavior|\n|------|--------|--------|--------|\n| `LOG_FORMAT` | `console`, `json` | `console` | Change the log format accordingly |\n| `DEBUG` | `True`, `False` | `False` | Enable debug logging |\n\n## Integration\n\n```python\nimport logging\n\nfrom typing import Callable, Dict, Optional, List, Tuple\nfrom graphenum import IntrospectionSchema\nfrom graphenum.entities.internal import Callbacks\n\nasync def async_introspect( / def introspect(\n    url: str,\n    logger: Optional[logging.Logger] = None,\n    headers: Optional[Dict[str, str]] = None,\n    verbose_mode: bool = False,\n    schema_path: Optional[str] = None,\n    callbacks: Optional[Dict[Callbacks, List[Callable]]] = None,\n    json_encode: bool = False\n) -> Tuple[IntrospectionSchema, aiohttp.ClientResponse]:\n    ...\n```\n\n## Local installation\n\n```bash\ngit clone git@github.com:Escape-Technologies/graphenum.git\ncd graphenum\nchmod +x ./install-dev.sh\n./install-dev.sh\n```\n\n## Contributing\n\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n\nPlease make sure to update tests as appropriate.\n\n## License ![PyPI - License](https://img.shields.io/pypi/l/GraphDNA)\n\n[MIT](https://choosealicense.com/licenses/mit/)',
    'author': 'Escape Technologies SAS',
    'author_email': 'ping@escape.tech',
    'maintainer': 'Swan',
    'maintainer_email': 'swan@escape.tech',
    'url': 'https://escape.tech/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<=3.11',
}


setup(**setup_kwargs)
