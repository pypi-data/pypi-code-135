# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_roll']

package_data = \
{'': ['*']}

install_requires = \
['nonebot-adapter-onebot>=2.1.1,<3.0.0', 'nonebot2>=2.0.0b3,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-roll',
    'version': '0.2.2a1',
    'description': 'Roll a dice!',
    'long_description': '<div align="center">\n\n# Roll\n\n<!-- prettier-ignore-start -->\n<!-- markdownlint-disable-next-line MD036 -->\n_🎲 掷骰子 🎲_\n<!-- prettier-ignore-end -->\n\n</div>\n\n<p align="center">\n  \n  <a href="https://github.com/KafCoppelia/nonebot_plugin_roll/blob/beta/LICENSE">\n    <img src="https://img.shields.io/badge/license-MIT-informational">\n  </a>\n  \n  <a href="https://github.com/nonebot/nonebot2">\n    <img src="https://img.shields.io/badge/nonebot2-2.0.0b3+-green">\n  </a>\n\n  <a href="https://github.com/MinatoAquaCrews/nonebot_plugin_roll/releases/tag/v0.2.2a1">\n    <img src="https://img.shields.io/github/v/release/MinatoAquaCrews/nonebot_plugin_roll?color=orange">\n  </a>\n  \n  <a href="https://www.codefactor.io/repository/github/MinatoAquaCrews/nonebot_plugin_roll">\n    <img src="https://img.shields.io/codefactor/grade/github/MinatoAquaCrews/nonebot_plugin_roll/beta?color=red">\n  </a>\n  \n</p>\n\n## 版本\n\nv0.2.2a1\n\n⚠ 适配nonebot2-2.0.0b3+\n\n## 安装\n\n通过`pip`或`nb`安装。\n\n## 功能\n\n掷骰！扔出指定个数的多面骰子；支持群聊与私聊。\n\n## 命令\n\n掷骰子：[rd/roll/掷骰] [x]d[y]，掷出x个y面的骰子，并返回点数。\n\n## 本插件改自\n\n[Omega Miya-roll](https://github.com/Ailitonia/omega-miya)',
    'author': 'KafCoppelia',
    'author_email': 'k740677208@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
