# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['finance_tracker',
 'finance_tracker.aggregators',
 'finance_tracker.categories',
 'finance_tracker.entries',
 'finance_tracker.readers']

package_data = \
{'': ['*']}

install_requires = \
['inquirer>=2.10.0,<3.0.0', 'pandas>=1.5.0,<2.0.0']

setup_kwargs = {
    'name': 'finance-tracker',
    'version': '0.0.0a1',
    'description': 'Python tool to track finances over a year',
    'long_description': '# finance-tracker\n\nPython tool to track finances over a year\n\n## Installation\n\n### PyPi package\n\nTBD\n\n## Usage\n\n1. Clone the repo\n2. Install poetry\n3. Run `make install`\n4. Load the categories and categories to filter as incomes wanted in a file called `categories.json`\n    in `./load/categories/`. Such as:\n    \n    ```json\n    {\n      "CATEGORIES": {\n        "CATEGORY_ONE": [\n          "TITLE TO CATEGORIZE"\n        ],\n        "CATEGORY_TWO": [\n          "TITLE 2 TO CATEGORIZE"\n        ]\n      },\n      "POSITIVE_CATEGORIES": [\n        "CATEGORY_TWO"\n      ]\n    }\n    ```\n\n5. Load the CSV files in the folder `./load/entries_files/`. Those files have 3 _headers_ (2 with text and 1 with column\ntitles) and the following columns:\n\n    ```csv\n    HEADER1;;;;;\n    HEADER2;;;;;\n    DATE;DATE TWO;TITLE;OTHER DATA;QUANTITY;OTHER\n    01/01/1999;01/01/1999;PAYCHECK;PAYCHECK FROM COMPANY 1;1.000;1.000\n    ```\n\n6. Run `make run`\n\n## Contributing\n\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n\nPlease make sure to update tests as appropriate.\n\n## License\n\n[MIT](https://choosealicense.com/licenses/mit/)\n',
    'author': 'w0rmr1d3r',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/w0rmr1d3r/finance-tracker',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
