# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pysuit', 'pysuit.modules']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pysuit',
    'version': '1.0.0',
    'description': 'This package will resolve all small intigrities of python data structures(List,Tuple,Dictionary,Set) which are not provided by-default.',
    'long_description': '# PySuit\n\n[![Read the Docs](https://readthedocs.org/projects/py-suit/badge/?version=latest)](py-suit.rtfd.io/en/latest/) [![codecov](https://codecov.io/github/deep-tw/py-suit/branch/release/graph/badge.svg?token=WR57HD3UTR)](https://codecov.io/github/deep-tw/py-suit)\n[![PyPI version](https://badge.fury.io/py/pysuit.svg)](https://badge.fury.io/py/pysuit)\n\nA unified collection of python functions  eg dictsort,nested_iterator etc\n\n#### Purpose of the Package\n+ The purpose of the package is to provide a collection of fuction and module indices in one unified libary\n\n#### Documentation\n+ The official documentation is hosted on readthedocs.io: https://py-suit.readthedocs.io/en/latest/\n\n\n\n### Features\n+  Collection of PySuit\n   -  DictCollection\n   -  NestedCollections\n   -  ExcludeRandom\n   -  DataTypeCollection\n+  Collection of DictCollection\n   -  dictsort\n   -  etc\n+  Collection of NestedCollections\n   -  nested_iterator\n   -  etc\n+  Collection of ExcludeRandom\n   -  exclude_random\n   -  etc\n+  Collection of DataTypeCollection\n   -  fake_random_datatype\n   -  etc\n### Getting Started\nThe package can be found on pypi hence you can install it using pip\n\n#### Installation\n```bash\npip install pysuit\n```\n### Usage\nUsing the short forms or abbreviated forms of indices\n\n### DictCollection\n```python\nfrom pysuit import DictCollections\n\ndict_collection = DictCollections()\n\ndict_collection.dict_sort(dictionary , flag)\n\n```\n\n#### Examples of DictCollections\n```python\nfrom pysuit import DictCollections\n```\n```python\ndict_collection = DictCollections()\n```\n```python\ndict_collection.dict_sort({"b": 3, "a": 34, 67: "c", 1: 64} , keys)\n```\n```python\nSorted Dictionary is => {1: 64, \'a\': 34, \'b\': 3, 67: \'c\'}\n```\n### NestedCollections\n```python\nfrom pysuit import NestedCollections\n\nnested_collection = NestedCollections()\n\nnested_collection.nested_iterator(nested_list)\n\n```\n#### Examples of NestedCollections\n```python\nfrom pysuit import NestedCollections\n```\n```python\n\nnested_collection = NestedCollections()\n```\n```python\nnested_collection.nested_iterator([[0, 4], [2, 3, 4], [0, 1, 2], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]])\n```\n```python\nConverted list is => [0, 4, 2, 3, 4, 0, 1, 2, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]\n```\n### ExcludeRandom\n```python\nfrom pysuit import ExcludeRandom\n\nexclude_random = ExcludeRandom()\n\nexclude_random.exclude_random(start, stop, [exclude numbers])\n\n```\n#### Examples of ExcludeRandom\n```python\nfrom pysuit import ExcludeRandom\n```\n```python\nexclude_random = ExcludeRandom()\n```\n```python\nexclude_random.exclude_random(1, 10, [4, 5, 9])\n```\n```python\nRandom number is => 8\n```\n### DataTypeCollection\n```python\nfrom pysuit import DataTypeCollection\n\ndata_collection = DataTypeCollection()\n\ndata_collection.fake_random_datatype(datatype, length of datatype)\n\n```\n#### Examples of DataTypeCollection\n```python\nfrom pysuit import DataTypeCollection\n```\n```python\ndata_collection = DataTypeCollection()\n```\n```python\ndata_collection.fake_random_datatype(list, 10)\n```\n```python\nFake random data is => [93, 91, 9163, -1967.88203, 3, \'thousand\', -197247.03, 913, 983, \'thousand\']\n```\n\n### Contribution\nContributions are welcome\nNotice a bug let us know. Thanks\n\n\n### Author\n+ Main Maintainer: Deepak Patidar / Nitesh Yadav\n+ Team Thoughtwin\n\n### License\n+ MIT\n',
    'author': 'Deepak Patidar',
    'author_email': 'deepakp@thoughtwin.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/deep-tw/py-suit.git',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7.0',
}


setup(**setup_kwargs)
