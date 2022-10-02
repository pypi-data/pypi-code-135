# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pynotionclient',
 'pynotionclient.config',
 'pynotionclient.exceptions',
 'pynotionclient.schema',
 'pynotionclient.schema.common',
 'pynotionclient.schema.database',
 'pynotionclient.utils']

package_data = \
{'': ['*']}

install_requires = \
['black[d]>=22.8.0,<23.0.0',
 'mypy>=0.981,<0.982',
 'pre-commit>=2.20.0,<3.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'pylint-quotes>=0.2.3,<0.3.0',
 'pylint>=2.15.3,<3.0.0',
 'pytest-cov>=4.0.0,<5.0.0',
 'pytest>=7.1.3,<8.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'pynotionclient',
    'version': '0.0.4',
    'description': 'Python wrapper for Notion API',
    'long_description': '# PyNotion\n\n<img src="assets/notion.png" alt="Notion Logo" height="64" width="64">\n<br>\n\n### A Notion API wrapper for Python (In Development)\n\n> Simple to use and easy to understand API wrapper for Notion.so\n>\n>Curently in development and supports the following features:\n> 1. Create a new database (Work in progress can create datbase passing payload as a dictionary)\n> 2. Get a database\n\n## Installation\n\n`poetry add pynotionclient`\n\n`pip install pynotionclient`\n\n## Usage\n\n```python\nfrom pynotionclient import PyNotion\nfrom examples.config import base_config\nfrom pynotionclient.schema.database import RichTextFilter, PropertyFilter, Filter, NotionDatabaseResponseSchema\n\npy_notion_client = PyNotion(token=base_config.notion_secret_token)\n\n# Create necessary properties as dictionary\nfilter_dict = {"page_size": 100, "filter": {"property": "Name", "rich_text": {"contains": "Home"}}}\n\n# Create necessary filter objects from Pydantic models and use them to query the database.\n\nrich_text_filter = RichTextFilter(contains="Game")\nproperty_filter = PropertyFilter(property="Name", rich_text=rich_text_filter)\nfilter_object = Filter(page_size=100, filter=property_filter)\n\nresponse_dict_payload: NotionDatabaseResponseSchema = py_notion_client.database.query_database(\n        database_id=base_config.database_id, payload=filter_dict\n        )\nresponse_filter_payload: NotionDatabaseResponseSchema = py_notion_client.database.query_database(\n        database_id=base_config.database_id, payload=filter_object\n        )\n```\n\n## Querying a Database\n\n#### 1. Querying a database using a dictionary\n\n```python\nfrom pynotionclient import PyNotion\nfrom examples.config import base_config\nfrom pynotionclient.schema.database import NotionDatabaseResponseSchema\npy_notion_client = PyNotion(token=base_config.notion_secret_token)\n\n# Create necessary properties as dictionary\nfilter_dict = {"page_size": 100, "filter": {"property": "Name", "rich_text": {"contains": "Home"}}}\nresponse_dict_payload: NotionDatabaseResponseSchema = py_notion_client.database.query_database(\n        database_id=base_config.database_id, payload=filter_dict\n        )\n```\n\n#### 2. Querying a database using a Pydantic model\n\n```python\nfrom pynotionclient import PyNotion\nfrom examples.config import base_config\nfrom pynotionclient.schema.database import RichTextFilter, PropertyFilter, Filter, NotionDatabaseResponseSchema\npy_notion_client = PyNotion(token=base_config.notion_secret_token)\n\n# Create necessary filter objects from Pydantic models and use them to query the database.\n\nrich_text_filter = RichTextFilter(contains="Game")\nproperty_filter = PropertyFilter(property="Name", rich_text=rich_text_filter)\nfilter_object = Filter(page_size=100, filter=property_filter)\n\nresponse_filter_payload: NotionDatabaseResponseSchema = py_notion_client.database.query_database(\n        database_id=base_config.database_id, payload=filter_object)\n```\n\n#### Response for querying a database\n\n> Pynotionclient gives you the response as a Pydantic model. You can access the response as a dictionary or as a\n> Pydantic model. The response is a NotionDatabaseResponseSchema model which has the following\n> properties: https://developers.notion.com/reference/database\n\n## Contributing\n\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.',
    'author': 'Vetrichelvan',
    'author_email': 'pythonhub.py@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pythonhubpy/PyNotion',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
