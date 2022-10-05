# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_magicadmin', 'django_magicadmin.migrations', 'django_magicadmin.tests']

package_data = \
{'': ['*'],
 'django_magicadmin': ['static/magicadmin/css/*',
                       'templates/*',
                       'templates/emails/*']}

install_requires = \
['Django>=4.1.2,<5.0.0']

setup_kwargs = {
    'name': 'django-magicadmin',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Django Magic Admin\n\nThis is a plugin to facilitate django-admin login through magic links.\n\n## Requirements\n\n - Django 4.X or higher\n - An E-mail service provider such as SMTP, Sendgrid or others configured on settings.py\n\n## Installation\n\n - `pip install django-django_magicadmin` on your system\n - Add the following URL and include it in your main `urls.py`\n\n```\npath("", include("django_magicadmin.urls")),\n```\n - Add the app to your INSTALLED_APPS\n```\nINSTALLED_APPS = [\n    "django_magicadmin",\n    ...\n]\n```\n - If you want custom settings about Sender address, Domain, etc, use the following fields and add them to your settings.py:\n\n```\nMAGICADMIN_DEFAULT_EXPIRATION = 10800 # default\nMAGICADMIN_DEFAULT_MAGIC_LINK_SUBJECT = "Here is your magic link to login!" # default\nMAGICADMIN_CURRENT_WEBSITE = localhost\nMAGICADMIN_DEFAULT_SENDER_EMAIL = magiclink@localhost\n```\n\n### Pro tips:\n\nHere are some tips that will enable a better experience for you\n\n#### Pro tip #1:\nIf you want to develop using the magic link functionality, I recommend you\nthe Django Terminal E-mail Backend, which enables you to see all of the messages sent through the system.\n\nJust add this one-liner to your settings.py:\n\n```\nEMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"\n```\n\n\n#### Pro tip #2:\nTo override with custom e-mail templates, override the files: `emails/magiclogin.html` and `emails/magiclogin.txt`',
    'author': 'Vinicius Mesel',
    'author_email': 'me@vmesel.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
