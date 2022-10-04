# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytest_jinja']

package_data = \
{'': ['*'], 'pytest_jinja': ['templates/bootstrap/*', 'templates/default/*']}

install_requires = \
['jinja2', 'pytest-metadata', 'pytest>=6.2.5,<7.0.0']

entry_points = \
{'pytest11': ['pytest-jinja = pytest_jinja.pytest_jinja']}

setup_kwargs = {
    'name': 'pytest-jinja',
    'version': '0.1.3',
    'description': 'A plugin to generate customizable jinja-based HTML reports in pytest',
    'long_description': '===================\npytest-jinja\n===================\n\npytest-jinja is a plugin to generate customizable jinja-based HTML reports in pytest.\nIt\'s based on pytest-html, but changes its inner working completely by separating the results data collection and the report generation, allowing easy developent of custom HTML reports that can include any javascript or css.\n\n\n.. image:: https://img.shields.io/badge/license-MPL%202.0-blue.svg\n   :target: https://github.com/magmax/pytest-jinja/blob/master/LICENSE\n   :alt: License\n\n.. image:: https://img.shields.io/pypi/pyversions/pytest-jinja.svg\n    :target: https://pypi.org/project/pytest-jinja\n    :alt: Python versions\n\n.. image:: https://img.shields.io/github/issues-raw/magmax/pytest-jinja.svg\n    :target: https://github.com/magmax/pytest-jinja/issues\n    :alt: Issues\n\nThis version is a fork from [g-bon\'s pytest-jinja](https://github.com/g-bon/pytest-jinja).\n\n----\n\n\nRequirements\n------------\n\nYou will need the following prerequisites in order to use pytest-html:\n\n* Python 3.10\n\n\nInstallation\n------------\n\nYou can install "pytest-jinja" via `pip`_ from `PyPI`_::\n\n    $ pip install pytest-jinja\n\nUsage\n-----\n- if no template is specified a default template is used. The default template looks almost identical to pytest-html::\n\n    $ pytest testcase --report=test_report.html\n\n- or you can pass your own template, pytest-jinja will render your template passing in the report data as jinja variables::\n\n    $ pytest testcase --report=test_report.html --template=my_template.html\n\nCreating a custom template\n--------------------------\nYou can create your own template by simply creating any template. The report data is "passed" to the page as a single object called `report`. The attributes of this object contain all the necessary report data.\n\nTemplate Example\n----------------\n.. code-block:: django\n\n    <html lang="en">\n    <head>\n        <meta charset="UTF-8">\n        <title>Test Report - {{ report.time_report_generation }}</title>\n    </head>\n    <body>\n    <h1>Test Report - {{ report.time_report_generation }} </h1>\n\n    <h2>Environment</h2>\n    <table id="environment">\n        {% for name,value in report.environment.items() %}\n        <tr>\n            <td>{{ name }}</td>\n            <td>{{ value }}</td>\n        </tr>\n        {% endfor %}\n    </table>\n\n    <h2>Summary</h2>\n    <p>{{ report.tests_count }} tests ran in {{ report.duration | round(2)}} seconds. </p>\n\n    <h2>Results</h2>\n    <table>\n        {% for r in report.results %}\n        <tr>\n            <td>{{ r.test_id }}</td>\n            <td>{{ r.outcome }}</td>\n            <td><strong>{{ r.time|round(5) }}s</strong></td>\n        </tr>\n        {% endfor %}\n    </table>\n\n    </body>\n    </html>\n\nAnother Template Example\n------------------------\n.. code-block::\n\n    {{ report | json }}\n\nAvailable Report Data\n---------------------\n\n`report.tests_count` : the total number of tests executed (int)\n\n`report.errors` : the number of errors (int)\n\n`report.failed` : the number of failed tests (int)\n\n`report.passed` : the number of passed tests (int)\n\n`report.skipped` : the number of skipped tests (int)\n\n`report.xfailed` : the number of expected failures (int)\n\n`report.xpassed`: the number of unexpected passes (int)\n\n`report.rerun`: the number of reruns (int)\n\n`report.duration` : the test session duration in seconds (float)\n\n`report.time_report_generation` : date and time of report generation (str)\n\n`report.environment`: metadata on tests execution (dict)\n\n`report.results`: the test results data (Object with attributes test_id, time, outcome, stacktrace, config)\n\n`report.report_path`: report path passed via command line (pathlib.Path)\n\n`report.template_path`: template path passed via command line (pathlib.Path)\n\n\n\nContributing\n------------\nContributions are very welcome. Tests can be run with `tox`_.\n\n\nLicense\n-------\nDistributed under Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this\nfile, You can obtain one at http://mozilla.org/MPL/2.0/. "pytest-jinja" is free and open source software\n\n\nIssues\n------\n\nIf you encounter any problems, please `file an issue`_ along with a detailed description.\n\nThis `pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_\'s `cookiecutter-pytest-plugin`_ template.\n\n\n.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter\n.. _`@hackebrot`: https://github.com/hackebrot\n.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin\n.. _`file an issue`: https://github.com/magmax/pytest-jinja/issues\n.. _`pytest`: https://github.com/pytest-dev/pytest\n.. _`tox`: https://tox.readthedocs.io/en/latest/\n.. _`pip`: https://pypi.org/project/pip/\n.. _`PyPI`: https://pypi.org/project\n',
    'author': 'Gabriele Bonetti',
    'author_email': 'gabriele.bonetti@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/g-bon/pytest-jinja',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
