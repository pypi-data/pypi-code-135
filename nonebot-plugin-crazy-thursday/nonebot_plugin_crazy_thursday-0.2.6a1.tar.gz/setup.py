# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_crazy_thursday']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.0,<0.24.0',
 'nonebot-adapter-onebot>=2.1.1,<3.0.0',
 'nonebot2>=2.0.0rc1,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-crazy-thursday',
    'version': '0.2.6a1',
    'description': 'Send KFC crazy thursday articles randomly!',
    'long_description': '<div align="center">\n\n# Crazy Thursday\n\n<!-- prettier-ignore-start -->\n<!-- markdownlint-disable-next-line MD036 -->\n_🍗 疯狂星期四 🍗_\n<!-- prettier-ignore-end -->\n\n</div>\n\n<p align="center">\n  \n  <a href="https://github.com/MinatoAquaCrews/nonebot_plugin_crazy_thursday/blob/beta/LICENSE">\n    <img src="https://img.shields.io/github/license/MinatoAquaCrews/nonebot_plugin_crazy_thursday?color=blue">\n  </a>\n  \n  <a href="https://github.com/nonebot/nonebot2">\n    <img src="https://img.shields.io/badge/nonebot2-2.0.0rc1+-green">\n  </a>\n  \n  <a href="https://github.com/MinatoAquaCrews/nonebot_plugin_crazy_thursday/releases/tag/v0.2.6a1">\n    <img src="https://img.shields.io/github/v/release/MinatoAquaCrews/nonebot_plugin_crazy_thursday?color=orange">\n  </a>\n\n  <a href="https://www.codefactor.io/repository/github/MinatoAquaCrews/nonebot_plugin_crazy_thursday">\n    <img src="https://img.shields.io/codefactor/grade/github/MinatoAquaCrews/nonebot_plugin_crazy_thursday/beta?color=red">\n  </a>\n  \n</p>\n\n## 版本\n\nv0.2.6a1\n\n⚠ 适配nonebot2-2.0.0rc1+\n\n[更新日志](https://github.com/MinatoAquaCrews/nonebot_plugin_crazy_thursday/releases/tag/v0.2.6a1)\n\n## 安装\n\n1. 通过`pip`或`nb`安装；\n\n2. 读取文案的默认路径位于**插件同级目录**下；可在`.env`下设置：\n\n    ```python\n    CRAZY_PATH="your-path-to-post.json"   # For example: "./my_data/crazy_thursday"，在此文件夹下放置"post.json"\n    ```\n\n## 功能\n\n天天疯狂！随机输出KFC疯狂星期四文案。\n\n⚠ 每次启动插件会自动尝试从repo中下载最新的文案资源\n\n## 命令\n\n1. 天天疯狂，疯狂星期[一|二|三|四|五|六|日|天]，输入**疯狂星期八**等不合法时间将提示；\n\n2. 支持日文触发：狂乱[月|火|水|木|金|土|日]曜日；\n\n## 本插件改自\n\n[HoshinoBot-fucking_crazy_thursday](https://github.com/Nicr0n/fucking_crazy_thursday)',
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
