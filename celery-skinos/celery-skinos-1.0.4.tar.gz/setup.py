# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['skinos']

package_data = \
{'': ['*']}

install_requires = \
['celery>=4.2.0', 'sentry-sdk>=0.8']

setup_kwargs = {
    'name': 'celery-skinos',
    'version': '1.0.4',
    'description': 'Custom consumer for celery integration',
    'long_description': '# Celery Skinos\n\n\nCustom consumer for celery integration.\n\n## Usage\n\n```PYTHON\nfrom skinos.custom_consumer import CustomConsumer\n```\n\n### Define a new exchange\n\ndefined a new exchange with a name and a binding key (always a topic).\nThe exchange name must be unique.\n\n```PYTHON\n# add_exchange(str, str) -> Exchange\nCustomConsumer.add_exchange(\'test\', "test.*.*")\n```\n\n\n### Define a new task\n\nDefine a new message handler \n\ndecoration take 3 arguments:\n\n- exchange name (must be defined)\n- queue name (must be defined)\n- queue binding key\n\n\nFunction but have this prototype: `(str, Message) -> Any`\n- `body` is the payload \n- `msg` is the message object (kombu.transport.myamqp.Message)\n\n\n```PYTHON\n# consumer(str, str, str) -> Callable[[str, Message], Any]\n@CustomConsumer.consumer(\'test\', \'test.test\', \'test.test.*\')\ndef coucou(body, msg):\n    print(\'payload content : {}\'.format(body))\n    print(\'message object content : {}\'.format(msg))\n```\n\n### Build consumers for Celery integration\n\nBuild consumers itself. all previous methods are just a pre-configuration for this build.\nIt take one argument, which is the Celery app.\n```PYTHON\n# build(Celery) -> None\nCustomConsumer.build(app)\n```\n\n### Add Sentry handler\n\nYou must init Sentry normally for a Celery project.\nThen Skinos is able to catch exception and send it sentry.\n\nset sentry to True and set raise to False (i.e: if error occur, error is not re-raise, but ignored)\nif you don\'t use it, default values are False and False\n\n```\n# with_sentry(bool, bool) -> Tuple(bool, bool)\nCustomConsumer.with_sentry(False, False)\n```\n\n### Run celery\n\nRun celery normally\n\n\n\n',
    'author': 'DIP - Université de Strasbourg',
    'author_email': 'dnum-dip@unistra.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
