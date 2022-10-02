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
 'pynotionclient.schema.database.request',
 'pynotionclient.schema.database.response',
 'pynotionclient.utils']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'pynotionclient',
    'version': '0.0.8',
    'description': 'Python wrapper for Notion API',
    'long_description': '# PyNotion\n\n<img src="assets/notion.png" alt="Notion Logo" height="64" width="64">\n<br>\n\n[![PyPI version](https://badge.fury.io/py/PyNotionclient.svg)](https://badge.fury.io/py/PyNotionclient)\n[![Top Language](https://img.shields.io/github/languages/top/pythonhubdev/PyNotion)](https://img.shields.io/github/languages/top/pythonhubdev/PyNotion)\n![GitHub last commit](https://img.shields.io/github/last-commit/pythonhubdev/PyNotion)\n![PyPI - License](https://img.shields.io/pypi/l/pynotionclient)\n![GitHub Repo stars](https://img.shields.io/github/stars/pythonhubdev/PyNotion?style=social)\n[![Downloads](https://static.pepy.tech/personalized-badge/pynotionclient?period=month&units=international_system&left_color=black&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/pynotionclient)\n\n### A Notion API wrapper for Python (In Development)\n\nSimple to use and easy to understand API wrapper for Notion.so Curently in development and \nsupports the following features:\n1. Create a new database (Work in progress can create datbase passing payload as a dictionary)\n2. Get a database\n\n## Installation\n`poetry add pynotionclient`\n\n`pip install pynotionclient`\n\n## Usage\n```python\nfrom pynotionclient import PyNotion\nfrom examples.config import base_config\nfrom pynotionclient.schema.database import RichTextFilter, PropertyFilter, Filter, NotionDatabaseResponseSchema\n\npy_notion_client = PyNotion(token=base_config.notion_secret_token)\n\n# Create necessary properties as dictionary\nfilter_dict = {"page_size": 100, "filter": {"property": "Name", "rich_text": {"contains": "Home"}}}\n\n# Create necessary filter objects from Pydantic models and use them to query the database.\n\nrich_text_filter = RichTextFilter(contains="Game")\nproperty_filter = PropertyFilter(property="Name", rich_text=rich_text_filter)\nfilter_object = Filter(page_size=100, filter=property_filter)\n\nresponse_dict_payload: NotionDatabaseResponseSchema = py_notion_client.database.query_database(\n        database_id=base_config.database_id, payload=filter_dict\n        )\nresponse_filter_payload: NotionDatabaseResponseSchema = py_notion_client.database.query_database(\n        database_id=base_config.database_id, payload=filter_object\n        )\n```\n\n## Querying a Database\n\n#### 1. Querying a database using a dictionary\n\n```python\nfrom pynotionclient import PyNotion\nfrom examples.config import base_config\nfrom pynotionclient.schema.database import NotionDatabaseResponseSchema\n\npy_notion_client = PyNotion(token=base_config.notion_secret_token)\n\n# Create necessary properties as dictionary\nfilter_dict = {"page_size": 100, "filter": {"property": "Name", "rich_text": {"contains": "Home"}}}\nresponse_dict_payload: NotionDatabaseResponseSchema = py_notion_client.database.query_database(\n        database_id=base_config.database_id, payload=filter_dict\n        )\n```\n\n#### 2. Querying a database using a Pydantic model\n\n```python\nfrom pynotionclient import PyNotion\nfrom examples.config import base_config\nfrom pynotionclient.schema.database import RichTextFilter, PropertyFilter, Filter, NotionDatabaseResponseSchema\n\npy_notion_client = PyNotion(token=base_config.notion_secret_token)\n\n# Create necessary filter objects from Pydantic models and use them to query the database.\n\nrich_text_filter = RichTextFilter(contains="Game")\nproperty_filter = PropertyFilter(property="Name", rich_text=rich_text_filter)\nfilter_object = Filter(page_size=100, filter=property_filter)\n\nresponse_filter_payload: NotionDatabaseResponseSchema = py_notion_client.database.query_database(\n        database_id=base_config.database_id, payload=filter_object)\n```\n\n#### Response for querying a database\n\n> Pynotionclient gives you the response as a Pydantic model. You can access the response as a dictionary or as a\n> Pydantic model. The response is a NotionDatabaseResponseSchema model which has the following\n> properties: https://developers.notion.com/reference/database\n\n#### 3. Creating a database\n```python\nfrom dotenv import load_dotenv\n\nfrom examples.config import base_config\nfrom pynotionclient import PyNotion\nfrom pynotionclient.schema.database import (\n    ParentConfiguration,\n    IconConfiguration,\n    TextConfiguration,\n    ExternalConfiguration,\n    CoverConfiguration,\n    SelectOptionsConfiguration,\n    SelecOptionsListConfig,\n    TitleConfiguration,\n    RichTextConfiguration,\n    CheckboxConfiguration,\n    SelectConfiguration,\n    ContentConfiguration,\n    MultiSelectConfiguration,\n    NumberConfiguration,\n    NumberFormats,\n    NumberFormatConfiguration,\n    DatabasePropertyConfiguration,\n)\n\nload_dotenv()\npy_notion_client = PyNotion(token=base_config.notion_secret_token)\n\n# # Create database payload\nparent_payload = ParentConfiguration(\n    type="page_id", page_id=base_config.page_id\n)  # The parent is the page where the database will be created.\nicon_payload = IconConfiguration(\n    type="emoji", emoji="🎮"\n)  # The icon is the icon that will be displayed on the database.\ntext = TextConfiguration(\n    content="Game"\n)  # The text is the text that will be displayed as the title of the database.\ncontent = ContentConfiguration(\n    type="text", plain_text="Game", href="https://www.google.com", text=text\n)  # The content has other info\'s of the title.\n\n# Cover schema\ncover = CoverConfiguration(\n    type="external", external=ExternalConfiguration(url="https://www.google.com")\n)\n\n# # Forming select options schema\nproperties = {\n    "Name": TitleConfiguration().dict(),\n    "Description": RichTextConfiguration().dict(),\n    "In stock": CheckboxConfiguration().dict(),\n    "Food Group": SelectConfiguration(\n        select=SelecOptionsListConfig(\n            options=[\n                SelectOptionsConfiguration(color="green", name="Code"),\n                SelectOptionsConfiguration(color="red", name="Game"),\n            ],\n        )\n    ).dict(),\n    "Cusines": MultiSelectConfiguration(\n        multi_select=SelecOptionsListConfig(\n            options=[\n                SelectOptionsConfiguration(color="green", name="Code"),\n                SelectOptionsConfiguration(color="red", name="Game"),\n            ],\n        )\n    ).dict(),\n    "Price": NumberConfiguration(\n        number=NumberFormatConfiguration(\n            format=NumberFormats.NUMBER_WITH_COMMAS,\n        ),\n    ).dict(),\n}\nprint(properties)\ncreate_database_payload = DatabasePropertyConfiguration(\n    title=[content],\n    cover=cover,\n    parent=parent_payload,\n    icon=icon_payload,\n    properties=properties,\n)\n\nresponse = py_notion_client.database.create_database(\n    payload=create_database_payload,\n)\n\nprint(response.json())\n```\n\n## Contributing\n\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.',
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
