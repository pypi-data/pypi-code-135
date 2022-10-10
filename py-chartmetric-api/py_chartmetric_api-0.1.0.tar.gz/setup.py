# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['py_chartmetric_api']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'py-chartmetric-api',
    'version': '0.1.0',
    'description': 'simple Python library for retrieving data from chartmetric.com',
    'long_description': '# py_chartmetric_api\n\npy_chartmetric_api is a simple Python library for retrieving data from [chartmetrics.com](https://chartmetric.com/).\n\n## Requirements\n- Python 3.9 or later\n\n## Installation\n\n```bash\n$ pip install py_chartmetric_api\n```\n\n## Usage\n\n```python\nimport py_chartmetric_api\n\n# returns first 100 artists that had a first relaase 30 days ago or less\npy_chartmetric_api.artist.get_artists_with_filters(0, 100, {"firstReleaseDaysAgo": "30"})\n\n# returns 300 artists that have between 1000 and 100000 spotify followers\npy_chartmetric_api.artist.get_artists_by_stats("sp_followers", 1000, 100000, 300)\n\n```\nRefer to examply.py for a more in-depth example\n\n## Contributing\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n\nPlease make sure to update tests as appropriate.\n\n## License\n[MIT](https://choosealicense.com/licenses/mit/)',
    'author': 'Felix Perron-Brault',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
