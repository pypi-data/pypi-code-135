# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_ocr', 'nonebot_plugin_ocr.bot', 'nonebot_plugin_ocr.ocr']

package_data = \
{'': ['*']}

install_requires = \
['diskcache>=5.4.0,<6.0.0',
 'httpx>=0.23.0,<0.24.0',
 'nonebot-adapter-onebot>=2.1.3,<3.0.0',
 'nonebot2>=2.0.0-beta.5,<3.0.0',
 'tomli>=2.0.1,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-ocr',
    'version': '0.3.2',
    'description': 'OCR plugin for nonebot2',
    'long_description': '<div align="center">\n\n# nonebot-plugin-ocr\n\n基于 [NoneBot2](https://v2.nonebot.dev/) 的文字识别插件\n\n![](https://img.shields.io/badge/license-MIT-yellow)\n[![Python Compatability](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)\n[![PyPI version](https://badge.fury.io/py/nonebot-plugin-ocr.svg)](https://pypi.org/project/nonebot-plugin-ocr/)\n[![GitHub version](https://badge.fury.io/gh/NewYearPrism%2Fnonebot-plugin-ocr.svg)](https://github.com/NewYearPrism/nonebot-plugin-ocr)\n\n</div>\n\n## NoneBot 适配器支持\n + [OneBot V11](https://onebot.adapters.nonebot.dev/)\n\n## OCR 应用支持\n + [百度智能云](https://cloud.baidu.com/product/ocr)（Web应用，内置）\n\n\n## 部署指南\n### 一. 安装插件\n+ 方式一：使用 pip\n  > 1.安装 nonebot-plugin-ocr\n  > ```\n  > pip install nonebot-plugin-ocr\n  > ```\n  > 2.使用 nonebot 加载插件 "nonebot_plugin_ocr" （[参考：加载插件](https://v2.nonebot.dev/docs/tutorial/plugin/load-plugin)）\n+ 方式二：手动安装\n  > 1.克隆本仓库\n  > ```\n  > git clone https://github.com/NewYearPrism/nonebot-plugin-ocr\n  > ```\n  > 2.安装依赖 requirements.txt\n  > ```\n  > pip install -r requirements.txt\n  > ```\n  > 3.复制插件本体到 Nonebot 环境中\n  > ```\n  > cp path/to/repo/nonebot-plugin-ocr/nonebot_plugin_ocr path/to/nonebot_plugins -r\n  > ```\n  > 4.使用 nonebot 加载插件（同上）\n### 二. 创建配置文件\n+ 需要手动创建配置文件，配置文件默认路径 ".ocr/config.toml" (相对当前工作目录)， 你可以在 NoneBot .env配置中使用变量OCR_CONFIG_PATH指定之：\n  > <span># .env</span><br/>\n  > HOST=0.0.0.0<br/>\n  > PORT=8080<br/>\n  > SUPERUSERS=["123456789", "987654321"]<br/>\n  > <span># ...</span><br/>\n  > OCR_CONFIG_PATH="path/to/config/ocr.toml"<br/>\n    ```\n    mkdir -p path/to/config\n    vim path/to/config/ocr.toml \n    ```\n+ 具体参考：[配置模板](config.template.toml)和[配置文档](docs/config.md)\n\n\n# 使用方法\n+ [使用演示](docs/usage.md)\n\n\n# 特别感谢\n+ [cq-picsearcher-bot](https://github.com/Tsuk1ko/cq-picsearcher-bot)\n+ [baidu-aip](https://pypi.org/project/baidu-aip/)\n',
    'author': 'NewYearPrism',
    'author_email': 'None',
    'maintainer': 'NewYearPrism',
    'maintainer_email': 'None',
    'url': 'https://github.com/NewYearPrism/nonebot-plugin-ocr',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
