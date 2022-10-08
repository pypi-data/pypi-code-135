# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot', 'nonebot.adapters.kook']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'deprecated>=1.2.13,<2.0.0',
 'nonebot2>=2.0.0-beta.1,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-adapter-kook',
    'version': '0.0.8',
    'description': 'Kook adapter for nonebot2',
    'long_description': '<p align="center">\n  <a"><img src="docs/logo2.png" width="500" alt="logo"></a>\n</p>\n\n<div align="center">\n\n# NoneBot-Adapter-Kook\n\n_✨ Kook协议适配 ✨_\n\n</div>\n\n## 个人工作繁忙时间不多， 欢迎有想法的各位共同维护仓库\n\n## Manual\n\n[使用指南](./MANUAL.md)\n',
    'author': 'Krysztal',
    'author_email': 'suibing112233@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/SUIBING112233/nonebot-adapter-kook',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.3,<4.0.0',
}


setup(**setup_kwargs)
