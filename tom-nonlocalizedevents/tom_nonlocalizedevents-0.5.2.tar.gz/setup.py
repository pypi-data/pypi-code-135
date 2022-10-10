# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tom_nonlocalizedevents',
 'tom_nonlocalizedevents.migrations',
 'tom_nonlocalizedevents.superevent_clients',
 'tom_nonlocalizedevents.templatetags',
 'tom_nonlocalizedevents.tests']

package_data = \
{'': ['*'],
 'tom_nonlocalizedevents': ['static/tom_nonlocalizedevents/css/*',
                            'static/tom_nonlocalizedevents/vue/*',
                            'static/tom_nonlocalizedevents/vue/css/*',
                            'static/tom_nonlocalizedevents/vue/js/*',
                            'templates/tom_nonlocalizedevents/*',
                            'templates/tom_nonlocalizedevents/partials/*',
                            'templates/tom_nonlocalizedevents/superevent_detail/*']}

install_requires = \
['django-webpack-loader==1.6.0',
 'gracedb-sdk>=0.1,<0.2',
 'python-dateutil>=2.8,<3.0',
 'tomtoolkit>=2.10,<3.0',
 'voevent-parse>=1.0,<2.0']

setup_kwargs = {
    'name': 'tom-nonlocalizedevents',
    'version': '0.5.2',
    'description': 'Reusable TOMToolkit app to support gravitational wave superevent and other nonlocalized event EM follow-up observations.',
    'long_description': "[![pypi](https://img.shields.io/pypi/v/tom-superevents.svg)](https://pypi.python.org/pypi/tom-superevents)\n[![run-tests](https://github.com/TOMToolkit/tom_nonlocalizedevents/actions/workflows/run-tests.yml/badge.svg)](https://github.com/TOMToolkit/tom_nonlocalizedevents/actions/workflows/run-tests.yml)\n[![Codacy Badge](https://app.codacy.com/project/badge/Grade/cbcf7ce565d8450f86fff863ef061ff9)](https://www.codacy.com/gh/TOMToolkit/tom_nonlocalizedevents/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=TOMToolkit/tom_nonlocalizedevents&amp;utm_campaign=Badge_Grade)\n[![Coverage Status](https://coveralls.io/repos/github/TOMToolkit/tom_nonlocalizedevents/badge.svg?branch=main)](https://coveralls.io/github/TOMToolkit/tom_nonlocalizedevents?branch=main)\n\n# GW Superevent (or GRB, Neutrino) EM follow-up\n\nThis reusable TOM Toolkit app provides support for gravitational wave (GW) superevent\nand other non-localized event electromagnetic (EM) follow up observations.  \n\n## Installation\n\n1. Install the package into your TOM environment:\n    ```bash\n    pip install tom-nonlocalizedevents\n   ```\n\n2. In your project `settings.py`, add `tom_nonlocalizedevents` to your `INSTALLED_APPS` setting:\n\n    ```python\n    INSTALLED_APPS = [\n        ...\n        'tom_nonlocalizedevents',\n    ]\n    ```\n    \n    Also include the following Django-Webpack-Loader settings in your settings.py:\n\n    ```python\n    VUE_FRONTEND_DIR_TOM_NONLOCAL = os.path.join(STATIC_ROOT, 'tom_nonlocalizedevents/vue')\n    WEBPACK_LOADER = {\n        'TOM_NONLOCALIZEDEVENTS': {\n            'CACHE': not DEBUG,\n            'BUNDLE_DIR_NAME': 'tom_nonlocalizedevents/vue/',  # must end with slash\n            'STATS_FILE': os.path.join(VUE_FRONTEND_DIR_TOM_NONLOCAL, 'webpack-stats.json'),\n            'POLL_INTERVAL': 0.1,\n            'TIMEOUT': None,\n            'IGNORE': [r'.+\\.hot-update.js', r'.+\\.map']\n        }\n    }\n    ```\n\n    If `WEBPACK_LOADER` is already defined in your settings, then integrate these values in to it.\n\n3. Include the tom_nonlocalizedevent URLconf in your project `urls.py`:\n   ```python\n   urlpatterns = [\n        ...\n        path('nonlocalizedevents/', include('tom_nonlocalizedevents.urls')),\n   ]\n   ```\n\n4. Copy ``tom_nonlocalizedevents/templates/tom_common/base.html`` into your project root's ``templates/tom_common/base.html``.\n\n5. Run ``python manage.py migrate`` to create the tom_nonlocalizedevents models.\n\n\n## Development\n\nWhen any changes are made to this library, the vue files will need to be build and bundled and committed into the repo so that they can be bundled and deployed with the django package. This means that after making any vue changes, you must run `npm run build` within the `tom_nonlocalizedevents_vue` directory once, which will install the built files into `tom_nonlocalizedevents/static/`, and then those built files will need to be committed into the repo. This allows django projects using this library to get those files when running `python manage.py collectstatic`.\n\n## Running the tests\n\nIn order to run the tests, run the following in your virtualenv:\n\n`python manage.py test`\n\n",
    'author': 'TOM Toolkit Project',
    'author_email': 'tomtoolkit@lco.global',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/TOMToolkit/tom_nonlocalizedevents',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
