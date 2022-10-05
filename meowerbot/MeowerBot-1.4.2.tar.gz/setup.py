# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['MeowerBot']

package_data = \
{'': ['*']}

install_requires = \
['cloudlink>=0.1.7,<0.2.0', 'requests>=2.28.0,<3.0.0']

setup_kwargs = {
    'name': 'meowerbot',
    'version': '1.4.2',
    'description': 'A meower bot lib for py',
    'long_description': '# MeowerBot.py\n\nA bot lib for Meower\n\n## How to use\n\n```py\n\nfrom MeowerBot import Client\n\nc = Client("Username","password",False) \n\ndef on_raw_msg(msg:dict, listener:dict):\n\n        print(f\'msg: {msg["u"]}: {msg["p"]}\')\n        if not msg["u"] == c.username:\n            if msg["u"] == "Discord":\n                msg["u"] = msg["p"].split(":")[0]\n                msg["p"] = msg["p"].split(":")[1].strip() \n            if msg["p"].startswith(f\'@{c.username}\'):   \n                c.send_msg(f\'Hello, {msg["u"]}!\')\n\ndef on_close(exiting:bool):\n    ...\n\ndef on_error(error):\n    ...\n\ndef on_login():\n    ...\n\ndef handle_pvar(pvar:dict, origin:str, var, lisserner):\n    ...\n\ndef handle_pmsg(msg:dict, origin:str, lissiner):\n    ...\n\ndef on_status_change(status, isserner):\n    c.satuscodee = status\n\ndef on_raw_packet(packet:dict, lissener)\n    ...\n\nc.callback(handle_pmsg)\nc.callback(handle_pvar)\nc.callback(on_login)\nc.callback(on_close)\nc.callback(on_error)\nc.callback(on_raw_msg)\nc.callback(on_status_change)\nc.callback(on_raw_packet)\n\nc.start()\n``` \n',
    'author': 'showierdata9978',
    'author_email': '68120127+showierdata9978@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/showierdata9978/MeowerBot',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
