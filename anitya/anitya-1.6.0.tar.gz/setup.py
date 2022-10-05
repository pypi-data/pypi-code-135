# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['anitya',
 'anitya.db',
 'anitya.db.migrations',
 'anitya.db.migrations.versions',
 'anitya.lib',
 'anitya.lib.backends',
 'anitya.lib.ecosystems',
 'anitya.lib.versions',
 'anitya.templates']

package_data = \
{'': ['*'],
 'anitya': ['static/*',
            'static/bootstrap-3.3.4-fedora/css/*',
            'static/bootstrap-3.3.4-fedora/fonts/*',
            'static/bootstrap-3.3.4-fedora/js/*',
            'static/css/*',
            'static/css/fonts/*',
            'static/css/images/*',
            'static/docs/*',
            'static/docs/_images/*',
            'static/docs/_modules/*',
            'static/docs/_modules/anitya/db/*',
            'static/docs/_modules/anitya/lib/*',
            'static/docs/_modules/anitya/lib/versions/*',
            'static/docs/_modules/sqlalchemy/ext/declarative/*',
            'static/docs/_modules/sqlalchemy/orm/*',
            'static/docs/_modules/sqlalchemy/sql/*',
            'static/docs/_sources/*',
            'static/docs/_sources/docblocks/*',
            'static/docs/_static/*',
            'static/docs/docblocks/*',
            'static/ico/*',
            'static/img/*',
            'static/js/*']}

install_requires = \
['Flask-Login>=0.6.2,<0.7.0',
 'Flask-WTF>=1.0.1,<2.0.0',
 'Flask>=2.1.2,<3.0.0',
 'Jinja2<3.1.3',
 'SQLAlchemy>=1.4.41,<2.0.0',
 'WTForms>=3.0.1,<4.0.0',
 'Werkzeug==2.1.2',
 'alembic>=1.8.1,<2.0.0',
 'anitya-schema>=2.0.1,<3.0.0',
 'arrow>=1.2.3,<2.0.0',
 'beautifulsoup4>=4.11.1,<5.0.0',
 'defusedxml>=0.7.1,<0.8.0',
 'fedora-messaging>=3.1.0,<4.0.0',
 'ordered-set>=4.1.0,<5.0.0',
 'packaging>=21.3,<22.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'semver>=2.13.0,<3.0.0',
 'social-auth-app-flask-sqlalchemy>=1.0.1,<2.0.0',
 'social-auth-app-flask>=1.0.0,<2.0.0',
 'sseclient>=0.0.27,<0.0.28',
 'straight.plugin>=1.5.0,<2.0.0',
 'toml>=0.10.2,<0.11.0',
 'webargs>=8.2.0,<9.0.0']

entry_points = \
{'console_scripts': ['check_service = anitya.check_service:main',
                     'librariesio_consumer = anitya.librariesio_consumer:main',
                     'sar = anitya.sar:main']}

setup_kwargs = {
    'name': 'anitya',
    'version': '1.6.0',
    'description': 'A cross-distribution upstream release monitoring project',
    'long_description': '\n.. image:: https://img.shields.io/pypi/v/anitya.svg\n  :target: https://pypi.org/project/anitya/\n\n.. image:: https://img.shields.io/pypi/pyversions/anitya.svg\n  :target: https://pypi.org/project/anitya/\n\n.. image:: https://readthedocs.org/projects/anitya/badge/?version=latest\n  :alt: Documentation Status\n  :target: https://anitya.readthedocs.io/en/latest/?badge=latest\n\n.. image:: https://img.shields.io/lgtm/alerts/g/fedora-infra/anitya.svg?logo=lgtm&logoWidth=18\n  :target: https://lgtm.com/projects/g/fedora-infra/anitya/alerts/\n\n.. image:: https://img.shields.io/lgtm/grade/javascript/g/fedora-infra/anitya.svg?logo=lgtm&logoWidth=18\n  :target: https://lgtm.com/projects/g/fedora-infra/anitya/context:javascript\n  \n.. image:: https://img.shields.io/lgtm/grade/python/g/fedora-infra/anitya.svg?logo=lgtm&logoWidth=18\n  :target: https://lgtm.com/projects/g/fedora-infra/anitya/context:python\n  \n\n======\nAnitya\n======\n\nAnitya is a release monitoring project. It provides a user-friendly interface\nto add, edit, or browse projects. A cron job can be configured to regularly\nscan for new releases of projects. When Anitya discovers a new release for a\nproject, it publishes a RabbitMQ messages via `fedora messaging`_.\nThis makes it easy to integrate with Anitya and perform actions when a new\nrelease is created for a project. For example, the Fedora project runs a service\ncalled `the-new-hotness <https://github.com/fedora-infra/the-new-hotness/>`_\nwhich files a Bugzilla bug against a package when the upstream project makes a\nnew release.\n\nFor more information, check out the `documentation`_!\n\n\nDevelopment\n===========\n\nFor details on how to contribute, check out the `contribution guide`_.\n\n\n.. _documentation: https://anitya.readthedocs.io/\n.. _contribution guide: https://anitya.readthedocs.io/en/latest/contributing.html\n.. _fedora messaging: https://fedora-messaging.readthedocs.io/en/latest\n',
    'author': 'Pierre-Yves Chibon',
    'author_email': 'pingou@pingoured.fr',
    'maintainer': 'Michal Konecny',
    'maintainer_email': 'mkonecny@redhat.com',
    'url': 'https://release-monitoring.org',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
