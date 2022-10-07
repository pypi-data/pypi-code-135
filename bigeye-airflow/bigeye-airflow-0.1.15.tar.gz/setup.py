# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bigeye_airflow',
 'bigeye_airflow.airflow_ext',
 'bigeye_airflow.aws',
 'bigeye_airflow.bigeye_requests',
 'bigeye_airflow.functions',
 'bigeye_airflow.models',
 'bigeye_airflow.operators']

package_data = \
{'': ['*']}

install_requires = \
['Flask-OpenID==1.3.0', 'apache-airflow==2.2.2', 'bigeye-sdk>=0.4.35,<0.5.0']

entry_points = \
{'console_scripts': ['bigeye = bigeye_cli.__main__:app']}

setup_kwargs = {
    'name': 'bigeye-airflow',
    'version': '0.1.15',
    'description': 'Bigeye Airflow Library supports Airflow 2.2.2 and offers custom operators for interacting with your your bigeye workspace.',
    'long_description': 'None',
    'author': 'Bigeye',
    'author_email': 'support@bigeye.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://docs.bigeye.com/docs',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
