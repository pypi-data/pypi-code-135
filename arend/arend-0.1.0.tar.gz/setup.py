# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['arend', 'arend.backends', 'arend.brokers', 'arend.settings', 'arend.worker']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'pandas>=1.4.3,<2.0.0',
 'pydantic>=1.9.1,<2.0.0',
 'pymongo>=4.2.0,<5.0.0',
 'pystalkd>=1.3.0,<2.0.0',
 'redis>=4.3.4,<5.0.0']

setup_kwargs = {
    'name': 'arend',
    'version': '0.1.0',
    'description': 'A simple producer consumer library for Beanstalkd.',
    'long_description': 'Arend\n========\n\nA simple producer-consumer library for the Beanstalkd queue.\n\nInstallation\n--------------\nHit the command:\n```shell\npip install arend\n```\n\nBasic Usage\n--------------\n\nIn your code:\n ```python\nfrom arend import arend_task\nfrom arend.backends.mongo import MongoSettings\nfrom arend.brokers import BeanstalkdSettings\nfrom arend.settings import ArendSettings\nfrom arend.worker import consumer\n\nsettings = ArendSettings(\n    beanstalkd=BeanstalkdSettings(host="beanstalkd", port=11300),\n    backend=MongoSettings(\n        mongo_connection="mongodb://user:pass@mongo:27017",\n        mongo_db="db",\n        mongo_collection="Tasks"\n    ),\n)\n\n@arend_task(queue="my_queue", settings=settings)\ndef double(num: int):\n    return 2 * num\n\ndouble(2)  # returns 4\ntask = double.apply_async(args=(4,))  # It is sent to the queue\n\nconsumer(queue="my_queue", settings=settings)  # consume tasks from the queue\n\nTask = settings.get_backend()  # you can check your backend for the result\ntask = Task.get(uuid=task.uuid)\nassert task.result == 4\n```\n\nBackends\n-------------------\nThe available backends to store logs are **Mongo** and **Redis**.\nPlease read the [docs](https://arend.readthedocs.io/en/latest/) \nfor further information.\n\nSetting your backend with environment variables\n--------------------------------------------------\nYou can set your backend by defining env vars.\nThe `AREND__` prefix indicates that it belongs to the Arend.\n```shell\n# Redis\nAREND__REDIS_HOST=\'redis\'\nAREND__REDIS_DB=\'1\'\nAREND__REDIS_PASSWORD=\'pass\'\n...\n\n# Mongo\nAREND__MONGO_CONNECTION=\'mongodb://user:pass@mongo:27017\'\nAREND__MONGO_DB=\'db\'\nAREND__MONGO_COLLECTION=\'logs\'\n...\n```\n\nIn your code:\n ```python\nfrom arend import arend_task\nfrom arend.worker import consumer\n\n\n@arend_task(queue="my_queue")\ndef double(num: int):\n    return 2 * num\n\ndouble.apply_async(args=(4,))  # It is sent to the queue\n\nconsumer(queue="my_queue")\n```\n\nDocumentation\n--------------\n\nPlease visit this [link](https://arend.readthedocs.io/en/latest/) for documentation.\n',
    'author': 'Jose Vazquez',
    'author_email': 'josevazjim88@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pyprogrammerblog/arend',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
