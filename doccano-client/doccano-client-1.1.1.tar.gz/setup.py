# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['doccano_client',
 'doccano_client.beta',
 'doccano_client.beta.controllers',
 'doccano_client.beta.models',
 'doccano_client.beta.tests',
 'doccano_client.beta.tests.controllers',
 'doccano_client.beta.tests.controllers.mock_api_responses',
 'doccano_client.beta.tests.utils',
 'doccano_client.beta.utils',
 'doccano_client.cli']

package_data = \
{'': ['*']}

install_requires = \
['dataclasses-json>=0.5.7,<0.6.0', 'requests>=2.28.1,<3.0.0']

extras_require = \
{'spacy': ['spacy>=3.4.1,<4.0.0',
           'spacy-partial-tagger>=0.9.1,<0.10.0',
           'tqdm>=4.64.1,<5.0.0']}

entry_points = \
{'console_scripts': ['docli = doccano_client.cli.commands:main']}

setup_kwargs = {
    'name': 'doccano-client',
    'version': '1.1.1',
    'description': 'A simple client for doccano API.',
    'long_description': "# Doccano API Client\n\nA simple client wrapper for the doccano API.\n\n- [Doccano API Client](#doccano-api-client)\n  - [Installation](#installation)\n  - [Usage](#usage)\n  - [Completion](#completion)\n  - [To-Do](#to-do)\n- [Doccano API BETA Client](#doccano-api-beta-client)\n\n## Installation\n\nTo install `doccano-client`, simply run:\n\n```bash\npip install doccano-client\n```\n\n## Usage\n\n- Object instantiation takes care of session authorization.\n- All methods return a `requests.models.Response` object.\n\n```python\nfrom doccano_client import DoccanoClient\n\n# instantiate a client and log in to a Doccano instance\ndoccano_client = DoccanoClient(\n  'http://doccano.example.com',\n  'username',\n  'password'\n)\n\n# get basic information about the authorized user\nr_me = doccano_client.get_me()\n\n# print the details from the above query\nprint(r_me)\n\n# get the label text from project 1, label 3\nlabel_text = doccano_client.get_label_detail(1, 3)['text']\n\n# upload a json file to project 1. If file is in current directory, file_path is omittable\nr_json_upload = doccano_client.post_doc_upload(1, 'json', 'file.json', '/path/to/file/without/filename/')\n```\n\nInfo: Uploading documents has been reported as broken, but it works with the beta-client (see below)\n- [#16](https://github.com/doccano/doccano-client/issues/16)\n- [#13](https://github.com/doccano/doccano-client/issues/13)\n- [#50](https://github.com/doccano/doccano-client/issues/50)\n\n## Completion\n\nThis wrapper's methods are based on doccano url [paths](https://github.com/chakki-works/doccano/blob/master/app/api/urls.py).\n\nKey:\n\n- ✔️ implemented\n- ❌ not implemented\n- ⚠️ currently broken or improperly implemented\n\nEndpoint Names:\n\n- ✔️ `auth-token`\n- ✔️ `me`\n- ✔️ `user_list`\n- ✔️ `roles`\n- ✔️ `features`\n- ✔️ `project_list`\n- ✔️ `project_detail`\n- ✔️ `statistics`\n- ✔️ `label_list`\n- ✔️ `label_detail`\n- ❌ `label_upload`\n- ✔️ `doc_list`\n- ✔️ `doc_detail`\n- ✔️ `doc_uploader`\n- ❌ `cloud_uploader`\n- ✔️ `approve_labels`\n- ✔️ `annotation_list`\n- ⚠️ `annotation_detail`\n- ✔️ `doc_downloader`\n- ✔️ `rolemapping_list`\n- ⚠️ `rolemapping_detail`\n\n## To-Do\n\n- investigate more secure alternatives to plaintext login\n- improve docstrings\n\n# Doccano API BETA Client\n\nWe're introducing a newly revamped Doccano API Client that features more Pythonic interaction as well as more testing and documentation. It also adds more regulated compatibility with specific Doccano release versions.\n\nYou can find the documentation on usage of the beta client [here](doccano_client/beta/README.md).\n",
    'author': 'Hironsan',
    'author_email': 'hiroki.nakayama.py@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/doccano/doccano-client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
