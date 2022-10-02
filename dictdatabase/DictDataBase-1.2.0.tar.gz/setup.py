# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dictdatabase']

package_data = \
{'': ['*']}

install_requires = \
['Brotli>=1.0.9,<2.0.0', 'path-dict>=1.0.4,<2.0.0']

setup_kwargs = {
    'name': 'dictdatabase',
    'version': '1.2.0',
    'description': 'Easy-to-use database using dicts',
    'long_description': '# DictDataBase\n\n[![Downloads](https://pepy.tech/badge/dictdatabase)](https://pepy.tech/project/dictdatabase)\n[![Downloads](https://pepy.tech/badge/dictdatabase/month)](https://pepy.tech/project/dictdatabase)\n[![Downloads](https://pepy.tech/badge/dictdatabase/week)](https://pepy.tech/project/dictdatabase)\n\nDictDataBase is a simple but fast and secure database for handling dicts (or PathDicts for more advanced features), that uses json files as the underlying storage mechanism.\nIt is also multiprocessind and multithreading safe, due to the employed locking mechanisms.\n\n## Import\n\n```python\nimport DictDataBase as DDB\n```\n\n\n## Configuration\n\nThere are 3 configuration options.\nSet storage_directory to the path of the directory that will contain your database files:\n\n```python\nDDB.config.storage_directory = "./ddb_storage" # Default value\n```\n\nIf you want to use compressed files, set use_compression to True.\nThis will make the db files significantly smaller and might improve performance if your disk is slow.\nHowever, the files will not be human readable.\n```python\nDDB.config.use_compression = False # Default value\n```\n\nIf you set pretty_json_files to True, the json db files will be indented and the keys will be sorted.\nIt won\'t affect compressed files, since the are not human-readable anyways.\n```python\nDDB.config.pretty_json_files = True # Default value\n```\n\n\nYou can specify your own json encoder and decoder if you need to.\nThe standard library json module is sufficient most of the time.\nHowever, alternatives like orjson might be more performant for your use case.\nThe encoder function should take a dict and return a str or bytes.\nThe decoder function should take a string and return a dict.\n```python\nDDB.config.custom_json_encoder = None # Default value\nDDB.config.custom_json_decoder = None # Default value\n```\n\n\n\n\n## Create dicts\nBefore you can access dicts, you need to explicitly create them.\n\nDo create ones that already exist, this would raise an exception.\nAlso do not access ones that do not exist, this will also raise an exception.\n\n```python\nuser_data_dict = {\n\t"users": {\n\t\t"Ben": {\n\t\t\t"age": 30,\n\t\t\t"job": "Software Engineer"\n\t\t},\n\t\t"Sue": {\n\t\t\t"age": 21:\n\t\t\t"job": "Student"\n\t\t},\n\t\t"Joe": {\n\t\t\t"age": 50,\n\t\t\t"job": "Influencer"\n\t\t}\n\t},\n\t"follows": [["Ben", "Sue"], ["Joe", "Ben"]]\n})\nDDB.create("user_data", db=user_data_dict)\n# There is now a file called user_data.json (or user_data.ddb if you use compression)\n# in your specified storage directory.\n```\n\n\n## Read dicts\n```python\nd = DDB.read("user_data")\n# You now have a copy of the dict named "user_data"\nprint(d == user_data_dict) # True\n```\n\n## Write dicts\n\n```python\nimport DictDataBase as DDB\nwith DDB.session("user_data") as (session, user_data):\n\t# You now have a handle on the dict named "user_data"\n\t# Inside the with statement, the file of user_data will be locked, and no other\n\t# processes will be able to interfere.\n\tuser_data["follows"].append(["Sue", "Ben"])\n\tsession.write()\n\t# Now the changes to d are written to the database\n\nprint(DDB.read("user_data")["follows"])\n# -> [["Ben", "Sue"], ["Joe", "Ben"], ["Sue", "Ben"]]\n```\n\nIf you do not call session.write(), the database file will not be modified.\n',
    'author': 'Marcel Kröker',
    'author_email': 'kroeker.marcel@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mkrd/DictDataBase',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
