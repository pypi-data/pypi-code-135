# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['StarkChat']

package_data = \
{'': ['*'], 'StarkChat': ['aiml_data/alice/*', 'aiml_data/custom/*']}

install_requires = \
['python-aiml==0.9.3']

setup_kwargs = {
    'name': 'starkchat',
    'version': '0.0.1beta0',
    'description': 'Stark chatbot client based on AIML',
    'long_description': '# StarkChat\nStark chatbot client based on AIML\n\n# Installation\n\n```sh\npip3 install starkchat\n```\n\n# Example\n\n```py\nfrom StarkChat import starkchat\n\nchatbot = starkchat.StarkChat()\n\nwhile True:\n    question = input("You: ")\n    answer = chatbot.chat(question)\n    print("Bot:", answer)\n```\n\n## Created and maintained by Sathishzus ❄️\n',
    'author': 'Sathishzus',
    'author_email': 'sourechebala19470@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/StarkIndustriesTG',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
