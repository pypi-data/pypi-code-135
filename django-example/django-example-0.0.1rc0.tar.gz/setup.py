# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_example',
 'django_example.management',
 'django_example.management.commands',
 'django_example.settings',
 'django_example.tests']

package_data = \
{'': ['*'], 'django_example': ['templates/example_project/*']}

install_requires = \
['django-tools', 'django_yunohost_integration>=0.5.0rc1']

entry_points = \
{'console_scripts': ['publish = django_example.publish:publish']}

setup_kwargs = {
    'name': 'django-example',
    'version': '0.0.1rc0',
    'description': 'Demo YunoHost Application to demonstrate the integration of a Django project under YunoHost.',
    'long_description': '# django-example\nExample Django Project for: https://github.com/YunoHost-Apps/django_example_ynh\n',
    'author': 'JensDiemer',
    'author_email': 'git@jensdiemer.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/jedie/django-example',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0.0',
}


setup(**setup_kwargs)
