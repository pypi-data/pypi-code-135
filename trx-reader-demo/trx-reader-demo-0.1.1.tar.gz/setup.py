# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['src']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'trx-reader-demo',
    'version': '0.1.1',
    'description': 'This app reads a .csv file that contains trx information, send a formatted email with this content and load the information into a Mongodb cluster',
    'long_description': '# Trx_reader\n\n# Download docker container from DockerHub:\nhttps://hub.docker.com/repository/docker/romibareiro/stori01\n\nOr\n\n# Clone repository and install:\n<text>pip3 install -r requirements.txt</text>\n\n# Load env variables:\nCreate an .env file with this content:\n\n<code>\nCSV_PATH=CSV_PATH\nSENDER_EMAIL=SENDER_EMAIL\nDEST_EMAIL=DEST_EMAIL\nEMAIL_PWD=EMAIL_PWD\nUSER_NAME=USER_NAME\nMONGODB_CONNSTRING=MONGODB_CONNSTRING\n</code>\n\n# And then run:\n<code>python3  main.py\n</code>\n\n\nNote: if your email sender is a gmal account, you must get app password from gmail settings.\nIf you want to build the docker image, you need to change the flags values in .env ( PATH_TO_CSV, EMAIL_SENDER, EMAIL_DESTINATION,EMAIL_SENDER_PWD,USER_NAME)\n\n# You will receive an email like this: \n\n\n![index](https://user-images.githubusercontent.com/100946603/189212924-1cd51e00-cfa7-4c53-8ebd-18bd6328c7e8.jpeg)\n',
    'author': 'Romina Bareiro',
    'author_email': '100946603+RomiBareiro@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
