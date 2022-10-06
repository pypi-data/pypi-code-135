# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyuploadcare',
 'pyuploadcare.api',
 'pyuploadcare.dj',
 'pyuploadcare.resources',
 'pyuploadcare.transformations',
 'pyuploadcare.ucare_cli',
 'pyuploadcare.ucare_cli.commands']

package_data = \
{'': ['*'], 'pyuploadcare.dj': ['static/uploadcare/*']}

install_requires = \
['httpx>=0.18.2,<0.19.0',
 'pydantic[email]>=1.8.2,<2.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'pytz>=2022.4,<2023.0']

extras_require = \
{':python_version >= "3.6" and python_version < "3.7"': ['typing-extensions>=3.10.0,<4.0.0'],
 ':python_version >= "3.7" and python_version < "4.0"': ['typing-extensions>=4.3.0,<5.0.0'],
 'django': ['Django>=1.11']}

entry_points = \
{'console_scripts': ['ucare = pyuploadcare.ucare_cli.main:main']}

setup_kwargs = {
    'name': 'pyuploadcare',
    'version': '3.0.1',
    'description': 'Python library for Uploadcare.com',
    'long_description': '.. image:: https://ucarecdn.com/2f4864b7-ed0e-4411-965b-8148623aa680/-/inline/yes/uploadcare-logo-mark.svg\n   :target: https://uploadcare.com/?utm_source=github&utm_campaign=pyuploadcare\n   :height: 64 px\n   :width: 64 px\n   :align: left\n\n=============================================\nPyUploadcare: a Python library for Uploadcare\n=============================================\n\n.. image:: https://badge.fury.io/py/pyuploadcare.svg\n   :target: https://badge.fury.io/py/pyuploadcare\n.. image:: https://github.com/uploadcare/pyuploadcare/actions/workflows/test.yml/badge.svg\n   :target: https://github.com/uploadcare/pyuploadcare/actions/workflows/test.yml\n   :alt: Build Status\n.. image:: https://readthedocs.org/projects/pyuploadcare/badge/?version=latest\n   :target: https://readthedocs.org/projects/pyuploadcare/?badge=latest\n   :alt: Documentation Status\n.. image:: https://coveralls.io/repos/github/uploadcare/pyuploadcare/badge.svg?branch=master\n   :target: https://coveralls.io/github/uploadcare/pyuploadcare?branch=master\n   :alt: Coverage\n.. image:: https://img.shields.io/badge/tech-stack-0690fa.svg?style=flat\n   :target: https://stackshare.io/uploadcare/stacks/\n   :alt: Uploadcare tech stack\n\nUploadcare Python & Django integrations handle uploads and further operations\nwith files by wrapping Upload and REST APIs.\n\nSimple file uploads for the web are of most importance for us. Today, everyone\nis used to the routine of allowing users to upload their pics or attach resumes.\nThe routine covers it all: installing image processing libraries, adjusting\npermissions, ensuring servers never go down, and enabling CDN.\n\nThis library consists of the Uploadcare API interface and a couple of Django\ngoodies.\n\nSimple as that, Uploadcare ``ImageField`` can be added to an\nexisting Django project in just a couple of `simple steps`_.\nThis will enable your users to see the upload progress, pick files\nfrom Google Drive or Instagram, and edit a form while files are\nbeing uploaded asynchronously.\n\nYou can find an example project `here <https://github.com/uploadcare/pyuploadcare-example>`_.\n\n.. code-block:: python\n\n    from django import forms\n    from django.db import models\n\n    from pyuploadcare.dj.models import ImageField\n    from pyuploadcare.dj.forms import FileWidget, ImageField as ImageFormField\n\n\n    class Candidate(models.Model):\n        photo = ImageField(blank=True, manual_crop="")\n\n\n    # optional. provide advanced widget options: https://uploadcare.com/docs/uploads/widget/config/#options\n    class CandidateForm(forms.Form):\n        photo = ImageFormField(widget=FileWidget(attrs={\n            \'data-cdn-base\': \'https://cdn.super-candidates.com\',\n            \'data-image-shrink\': \'1024x1024\',\n        }))\n\n.. image:: https://ucarecdn.com/dbb4021e-b20e-40fa-907b-3da0a4f8ed70/-/resize/800/manual_crop.png\n\nDocumentation\n=============\n\nDetailed documentation is available `on RTD <https://pyuploadcare.readthedocs.io/en/latest/>`_.\n\nFeedback\n========\n\nIssues and PRs are welcome. You can provide your feedback or drop us a support\nrequest at `hello@uploadcare.com`_.\n\n.. _hello@uploadcare.com: mailto:hello@uploadcare.com\n.. _Uploadcare: https://uploadcare.com/?utm_source=github&utm_campaign=pyuploadcare\n.. _simple steps: https://pyuploadcare.readthedocs.org/en/latest/quickstart.html\n.. _bugbounty@uploadcare.com: mailto:bugbounty@uploadcare.com\n',
    'author': 'Uploadcare Inc',
    'author_email': 'hello@uploadcare.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://uploadcare.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
