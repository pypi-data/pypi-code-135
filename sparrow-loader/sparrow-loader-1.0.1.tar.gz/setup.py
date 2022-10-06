# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sparrow', 'sparrow.loader']

package_data = \
{'': ['*']}

install_requires = \
['GeoAlchemy2>=0.9.4,<0.10.0',
 'SQLAlchemy>=1.4.41,<2.0.0',
 'macrostrat.database>=1.0.2,<2.0.0',
 'marshmallow-jsonschema>=0.10.0,<0.11.0',
 'marshmallow-sqlalchemy>=0.24.2,<0.25.0',
 'marshmallow>=3.11.1,<4.0.0',
 'stringcase>=1.2.0,<2.0.0']

setup_kwargs = {
    'name': 'sparrow-loader',
    'version': '1.0.1',
    'description': 'Utilities for loading data into Sparrow',
    'long_description': "# sparrow.loader\n\nThe `sparrow.loader` module helps you prepare data for loading\ninto the Sparrow geochemistry database system.\n\nWhen disconnected from a database, it can be used to check that\ndata is ready to be imported into a standard installation of\nSparrow.\n\nIf connected to a Sparrow installation's PostgreSQL database,\nthe module can be used to insert data into the appropriate tables.\n\n## Key functions\n\n- `validate_data(schema_name: str, data: dict)`  \n  Checks data against a loader schema\n- `show_loader_schemas(schema_name: str,  ..., nest_depth=0)`  \n  Show the fields for one or several loader schemas.\n\n## Installation\n\n`pip install sparrow-loader`\n\nRequires Python `>=3.9`",
    'author': 'Daven Quinn',
    'author_email': 'dev@davenquinn.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
